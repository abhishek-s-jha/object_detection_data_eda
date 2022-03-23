import os
import json


def logs(timestamp, function_name, task):
    """
    This is a custom function which generates logs in this format: timestamp --> function_name --> task --> status
    All the logs are displayed on the screen and is also saved in files for later uses.
    :param timestamp: current date and time
    :param function_name: name of the function which is presently executing
    :param task: status of the task
    :return: None
    """
    from datetime import date
    today_date = date.today()
    today_date = today_date.strftime("%d-%b-%Y")
    log_data = log_structure.format(timestamp, function_name, task.upper())
    print(log_data)
    log_file = os.path.join(sub_dir['dir_logs'], today_date + ".log")
    with open(log_file, 'a+') as fp:
        fp.write(log_data + '\n')

def json_reader(file_loc):
    """
    Simple json reader as we need this all the time
    :param file_loc: location of the file
    :return: file data in dictionary format
    """
    with open(file_loc) as fp:
        data = json.load(fp)
    return data

def json_writer(data, file_loc):
    """
    Simple json writer to write the directory in file
    :param data: data in dictionary format
    :param file_loc: location to store the file on disk
    :return: None
    """
    with open(file_loc, 'w') as fp:
        json.dump(data, fp)


# root directory location on disk
base = "E:/1_python_project"
main_dir = os.path.join(base, 'eda_odd')

# structure of directory for this project
sub_dir = {
    "dir_test": os.path.join(main_dir, 'test'),
    "dir_data": os.path.join(main_dir, 'data'),
    "dir_code": os.path.join(main_dir, 'code'),
    "dir_logs": os.path.join(main_dir, 'logs'),
    "dir_docs": os.path.join(main_dir, 'docs'),
    "dir_docs_research": os.path.join(main_dir, 'docs', 'research_paper')
}

# format for logs and timestamp
log_structure = "{0} -> [{1}] -> {2}"
timestamp_format = "%d-%m-%Y %H:%M:%S.%f"


# name of dataset and their urls
dataset_url = {
    "coco": ["http://images.cocodataset.org/zips/train2017.zip",
             "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"],

    "imagenet": ["https://image-net.org/data/imagenet21k_resized.tar.gz"],

    "stanford_dogs": ["http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar",
                      "http://vision.stanford.edu/aditya86/ImageNetDogs/annotation.tar"],

    "bdd100k": ["http://dl.yf.io/bdd100k/bdd100k_videos.zip"],

    "oxford_pet": [
        "https://storage.googleapis.com/kaggle-data-sets/112480/268736/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-"
        "SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20211124%2Fauto%2Fstorage%2Fgoog4_"
        "request&X-Goog-Date=20211124T193143Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=8192e40b00d93dea"
        "ba7deb4bf80f3ee1802541bd14801c2fb41d7dc6348e6cd0ae0189680ed53bce1fd201044212393d0adf3f57d7c72edf6e5eb252c563304c8c12f467d"
        "9d34ad621efa171cbcc8bf923d5f05a69a77b423b2e1be041687331df515c34bd85465d0c3b754c4d98fdb9561827b61463984de87835c0034a16f222c0a"
        "ae1019a202dd96d3ead9a0ac6c65dd4e47f2766e1aea70580b3f77c241e517b4639dda89a39f5bf959de85720d3e209ab880ad456a9b1812320388f19137a"
        "7a9ee1577bc38420550ccc4bf217ea2f0ca508b3a64a5d6f07379f66807f64da5de7ab642513949382a5dfcb4f6c643c52a354ed808d7fa0b9fcaefafe85c8"],

    "pothole_detection": [
        "https://storage.googleapis.com/kaggle-data-sets/877652/1494662/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-"
        "SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20211124%2Fauto%2Fstorage%2Fgoog4_"
        "request&X-Goog-Date=20211124T193916Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=0ea191244c26a3e"
        "e3b92cfbef7d1cdc072b2ad03b44dc67afbc81f582f78f43792fc2a9a5d9e9d446a76eb642446e1fcdc83a52d8bf08560957e589e7f3261cbaa63a"
        "7b020946a1b368eebb239b4ccb331f75fba33f926bb28d2c812157f00d129609c8748f78e730fe32955d7a71408b021b85c9b1f3f19fadec9e79622"
        "33eb7d64e67e9ae151f081f1103d09eca3a160bdb3b5a1057e4756653053564e6b927c87cb5b0b9f81150ca972462b88a28db5f4a5bcb0a53b44edd4"
        "2c66dcb2ee86565c79b72dae01b260b6d616ef0cc21e1643d64224a38ec4d215f240a3bc6ae403d83c7e1cd513372f584acc5e955c05c18c16f4bccdb09fe87eb7c86e170d7a"],

    "logo_detection": ["http://123.57.42.89/Dataset_ict/LogoDet-3K.zip"]
}
