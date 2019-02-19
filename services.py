import logging
import os
import pickle

def get_content_from_file_system(content_number):
    dir_name = 'content_folder'
    img_ext = '.jpg'
    text_ext = '.txt'
    if not os.path.exists(dir_name):
        logging.exception('folder error! check the content_folder')
        raise FileNotFoundError('folder error!')

    content_text_file_pathname = dir_name + '/' +str(content_number) + text_ext
    content_img_file_pathname = dir_name + '/' +str(content_number) + img_ext

    if not os.path.isfile(content_text_file_pathname):
        logging.exception('content_text file error! check the content_folder')
        raise FileNotFoundError('content_text error!')

    if not os.path.isfile(content_img_file_pathname):
        logging.exception('content_img file error! check the content_folder')
        raise FileNotFoundError('content_img error!')

    with open(content_text_file_pathname, 'r') as imp_file:
        content_text = imp_file.read()

    return (content_text, content_img_file_pathname)


def check_existence_content_pickle(content_number):
    with open("content_list.pickle", "rb") as pickle_file:
         numbers_list = pickle.load(pickle_file)
    if content_number in numbers_list:
        return None
    else:
        numbers_list.append(content_number)
        with open("content_list.pickle", "wb") as pickle_file:
            pickle.dump(numbers_list, pickle_file)
        return content_number



if __name__ == '__main__':
    v = check_existence_content_pickle(66)
    print(v)


#all_followers = pickle.load(f)
