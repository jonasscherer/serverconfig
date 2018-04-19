import requests
import re
import urllib
import os
import uuid
import shutil
from urlparse import urljoin


def download_file_list(to_do, uid):
    basic_url = os.environ['BASICURL']
    print("BASICURL: %s" % basic_url)

    source_path = os.environ['SOURCEPATH']

    if not os.path.exists(source_path):
        os.makedirs(source_path)

    for img_file in to_do:
        print("Download File: %s" % img_file.title)
        server_url = urljoin(basic_url, img_file.path)
        file_target = os.path.join(source_path, img_file.title)
        print("server_url: %s" % server_url)
        print("file_target: %s" % file_target)
        urllib.urlretrieve(server_url, file_target)
        print("File downloaded: %s" % img_file)

    print("All files downloaded!")


def upload_results(uuid, function_name):
    basic_url = os.environ['BASICURL']
    target_path = os.environ['TARGETPATH']

    post_url = urljoin(basic_url, 'post')
    print("Post-url: %s" % post_url)

    headers = {'uuid': uuid, 'function_name': function_name}

    for path in os.listdir(target_path):
        full_path = os.path.join(target_path, path)
        if os.path.isfile(full_path):
            file_name = os.path.basename(full_path)
            print("upload file: %s" % full_path)
            with open(full_path, 'rb') as f:
                r = requests.post(post_url, files={file_name: f}, headers=headers)
                print(r.text)
            print("File %s uploaded!" % file_name)


def remove_tmp(uid):
    shutil.rmtree("/tmp/%s/" % uid)

# if __name__ == "__main__":
#     os.environ['SOURCEPATH'] = '/home/jonas/data/source/'
#     os.environ['TARGETPATH'] = '/home/jonas/data/target'
#     os.environ['BASICURL'] = 'http://192.168.99.100:30142/'
#     # os.environ['BASICURL'] = 'http://localhost:8000/'
#
#     uid = uuid.uuid4().hex
#     # os.environ['BASICURL'] = 'http://192.168.99.100:30142/'
#
#     # os.environ['EXTENSIONS'] = '.py'
#     os.environ['EXTENSIONS'] = '.dcm,.nii,.nrrd,.tar.gz,.txt'
#
#     download_file_list(["image_data/test/text.txt"],uid)
#
#     for filename in os.listdir(os.environ['SOURCEPATH']):
#         upload_file(os.environ['SOURCEPATH'] + filename, uid)
