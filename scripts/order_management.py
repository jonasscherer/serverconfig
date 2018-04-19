import jsonpickle
from copy import copy
import requests

import sys

if sys.version_info >= (3, 0):
    from urllib.parse import urljoin
else:
    from urlparse import urljoin


class Image(object):
    def __init__(self, title, path, dir, file_format):
        self.title = title
        self.path = path
        self.dir = dir
        self.file_format = file_format


class Order(object):
    def __init__(self, uuid, function_name, dimensions, target_file_format, image_list, img_count_function):
        self.uuid = uuid
        self.function_name = function_name
        self.dimensions = dimensions
        self.target_file_format = target_file_format
        self.image_list = image_list
        self.img_count_function = img_count_function
        self.to_do = []

    def update_state(self):
        print("update")


def get_json_from_object(order_obj):
    return jsonpickle.encode(order_obj)


def get_object_from_json(json_str):
    return jsonpickle.decode(json_str)


def process_order(order, callback_url, faas_functions_url):
    count = order.img_count_function
    image_list = copy(order.image_list)
    headers = {'X-Callback-Url: %s' % callback_url}
    while len(image_list) > 0:
        todo = []
        for c in range(count):
            if len(image_list) > 0:
                img = image_list.pop()
                todo.append(img)
        order.to_do = todo
        payload = get_json_from_object(order)
        response = requests.post(urljoin(faas_functions_url, order.function_name), data=payload, timeout=30)
        print(response.text)

    return True
