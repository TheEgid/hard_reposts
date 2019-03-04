import os
import sys
import logging
import requests
import argparse
from dotenv import load_dotenv
import vk_api
import telegram
from services import get_content_from_file_system
from services import check_existence_content_pickle


def post_facebook(token, fb_group, content_text, content_img_file_pathname):
    url = 'https://graph.facebook.com/{}/photos'.format(fb_group)
    params = {'access_token': token, 'message': content_text}
    with open(content_img_file_pathname, 'rb') as img_file:
        response = requests.post(url=url, params=params, files={'file': img_file})
        response.raise_for_status()


def post_telegram(token, tg_channel, content_text, content_img_file_pathname):
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=tg_channel, text=content_text)
    with open(content_img_file_pathname, 'rb') as img_file:
        bot.send_photo(chat_id=tg_channel, photo=img_file)


def post_vkontakte(login, password, token, vk_group, vk_group_album,
            content_text, content_img_file_pathname):
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth(token_only=True)
    vk = vk_session.get_api()
    upload = vk_api.VkUpload(vk_session)
    img = upload.photo(photos=content_img_file_pathname,
                       album_id=vk_group_album,
                       group_id=vk_group)
    attach = 'photo{}_{}'.format(img[0]['owner_id'], img[0]['id'])
    vk_group = int(vk_group) * -1  # with "-" (vk.com/dev/wall.post#owner_id)
    vk.wall.post(message=content_text,
                 access_token=token,
                 owner_id=vk_group,
                 attachments=attach)
    wallpostsdict = vk.wall.get(count=1, owner_id=vk_group)['items'][0]
    if wallpostsdict['text'] != content_text:
        raise Exception('error with: '+content_text)


def get_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int,
                        help='digit only: number of the post')
    return parser


def post_all(content_number):
    load_dotenv()

    LOGIN_VK = os.getenv("LOGIN_VK")
    PASSWORD_VK = os.getenv("PASSWORD_VK")
    TOKEN_VK = os.getenv("TOKEN_VK")
    GROUP_ID_VK = os.getenv("GROUP_ID_VK")
    GROUP_ID_ALBUM_VK = os.getenv("GROUP_ID_ALBUM_VK")
    TOKEN_TG = os.getenv("TOKEN_TG")
    CHANNEL_TG = os.getenv("CHANNEL_TG")
    TOKEN_FB = os.getenv("TOKEN_FB")
    GROUP_ID_FB = os.getenv("GROUP_ID_FB")

    content_number = check_existence_content_pickle(content_number)

    if content_number is None:
        logging.info(' No success publish: already published')
    else:
        text, img_file_pathname = get_content_from_file_system(content_number)

        post_vkontakte(login=LOGIN_VK,
                password=PASSWORD_VK,
                token=TOKEN_VK,
                vk_group=GROUP_ID_VK,
                vk_group_album=GROUP_ID_ALBUM_VK,
                content_text=text,
                content_img_file_pathname=img_file_pathname)
        logging.info(' Success publish: vkontakte post was published')

        post_telegram(token=TOKEN_TG,
                tg_channel=CHANNEL_TG,
                content_text=text,
                content_img_file_pathname=img_file_pathname)
        logging.info(' Success publish: telegram post was published')

        post_facebook(token=TOKEN_FB,
                  fb_group =GROUP_ID_FB,
                  content_text=text,
                  content_img_file_pathname=img_file_pathname)
        logging.info(' Success publish: facebook post was published')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, os.path.split(dir_path)[0])
    arg_parser = get_args_parser()
    args = arg_parser.parse_args()
    post_all(args.number)
