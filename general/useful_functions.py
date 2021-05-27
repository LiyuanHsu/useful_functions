from datetime import datetime


def print_time_to_miliseconds():
    print(datetime.utcnow().strftime("%Y%m%d-%H:%M:%S.%f"))
    
    
def create_dir_and_save_img(dir_name, image):
    from datetime import datetime
    import cv2
    import os
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    cv2.imwrite(f"{dir_name}/{datetime.now().strftime('%Y-%m-%d-%H:%M:%S.%f')[:-3]}.jpg", image)
