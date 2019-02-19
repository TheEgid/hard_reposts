import logging
import os

def get_content_from_files_system(content_number)
    dir_name = 'content_folder'
    text_extension = '.jpg'
    img_extension = '.txt'
    if not os.path.exists(dir_name):
        except FileNotFoundError:
		logging.exception('folder error! check the content_folder')
		raise FileNotFoundError('folder error!')
    content_text_file_path_and_name = dir_name+'/'+str(content)+'/'+text_extension
    content_img_file_path_and_name = dir_name+'/'+str(content)+'/'+img_extension	
    if not os.path.isfile(content_text_file_path_and_name): 
        except FileNotFoundError:
		logging.exception('content_text file error! check the content_folder')
		raise FileNotFoundError('content_text error!')
    if not os.path.isfile(content_img_file_path_and_name):
        except FileNotFoundError:
		logging.exception('content_img file error! check the content_folder')
		raise FileNotFoundError('content_img error!')
    with open(content_text_file_path_and_name, 'r') as inp_file:
    	content_text = inp_file.read()
    return (content_text, content_img_file_path_and_name)


#pickle.dump(all_followers, f)


#all_followers = pickle.load(f)
