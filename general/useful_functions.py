from datetime import datetime


def print_time_to_miliseconds():
    print(datetime.utcnow().strftime("%Y%m%d-%H:%M:%S.%f"))


def create_dir_and_save_img(dir_name, image):
    from datetime import datetime
    import cv2
    import os

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    cv2.imwrite(
        f"{dir_name}/{datetime.now().strftime('%Y-%m-%d-%H:%M:%S.%f')[:-3]}.jpg", image
    )


def list_contents_in_dir(dir_name):
    """
    usage:
    file_list, non_file_list = list_contents_in_dir("/")
    print(f"file_list: {file_list}")
    print(f"non_file_list: {non_file_list}")
    :param dir_name: absolute path to a directory
    :return (file_list, non_file_list): list of absolute path of file and non_file in the given directory
    """
    from os import listdir
    from os.path import join, isfile

    file_list = []
    non_file_list = []
    content_list = listdir(dir_name)
    for content in content_list:
        content_path = join(dir_name, content)
        if isfile(content_path):
            file_list.append(content_path)
        else:
            non_file_list.append(content_path)
    return file_list, non_file_list
