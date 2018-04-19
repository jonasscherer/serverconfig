import sys
import os
from order_management import Order, Image, get_json_from_object, get_object_from_json, process_order
import filehandler
import function


def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line
    return buf


if (__name__ == "__main__"):
    input = get_stdin()
    command=input.split(";")[0]
    order_json=input.split(";")[1]
    if "info" in command:
        function.info()
    else:
        order = get_object_from_json(order_json)
        with open("/tmp/input.txt", "a") as myfile:
            myfile.write(input + "\n")
        print(input)
        uuid = order.uuid
        function_name = order.function_name
        dimensions = order.dimensions
        target_file_format = order.target_file_format
        image_list = order.image_list
        img_count_function = order.img_count_function
        to_do = order.to_do

        os.environ['SOURCEPATH'] = "/tmp/%s/source/" % uuid
        os.environ['TARGETPATH'] = "/tmp/%s/target/" % uuid
        os.environ['BASICURL'] = 'http://fileserver-service:8000'

        print("UUID: %s" % uuid)
        print("Function-name: %s" % function_name)
        filehandler.download_file_list(to_do, uuid)

        print("All files downloaded - start function...")
        function.start(order)

        print("Function finished - start upload of results...")
        filehandler.upload_results(uuid, function_name)

        print("Upload finished - deleting tmp files...")
        filehandler.remove_tmp(uuid)
        print("End of function!")

