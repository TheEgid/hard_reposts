import os
import sys
import logging
from dotenv import load_dotenv
import vk_api
from services import get_content_from_file_system
from services import check_existence_content_pickle

#https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/tTQRtFq8EeiRsxJFDm6TJA_3422191ca7e55751c7ab1ceb6244239e_single-copy.png?expiry=1550707200000&hmac=bMXWjG57F8OB93cQBBfQtb77QXTnwLh8pUuMSIs-BHg
class VKApiPostingError(Exception):
    """Declare special exception."""
    pass


def vk_post(login, password, token, vk_group, vk_group_album,
            content_text, content_img_file_pathname):
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.exceptions:
         vk_api.AuthError()
    vk = vk_session.get_api()
    upload = vk_api.VkUpload(vk_session)
    img = upload.photo(photos=content_img_file_pathname,
                       album_id=vk_group_album,
                       group_id=vk_group)
    attach = 'photo{}_{}'.format(img[0]['owner_id'], img[0]['id'])
    vk_group = int(vk_group) * -1
    vk.wall.post(message=content_text,
                 access_token=token,
                 owner_id=vk_group,
                 attachments=attach)

    wallpostsdict = vk.wall.get(count=1, owner_id=vk_group)['items'][0]
    if wallpostsdict['text'] != content_text:
        raise VKApiPostingError()


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, os.path.split(dir_path)[0])
    logging.basicConfig(level=logging.INFO)
    load_dotenv()

    LOGIN_VK = os.getenv("LOGIN_VK")
    PASSWORD_VK = os.getenv("PASSWORD_VK")
    TOKEN_VK = os.getenv("TOKEN_VK")
    GROUP_ID_VK = os.getenv("GROUP_ID_VK")
    GROUP_ID_ALBUM_VK = os.getenv("GROUP_ID_ALBUM_VK")

    content_check = 5

    content_check = check_existence_content_pickle(content_check)

    if content_check is None:
        logging.info(' No success publish: already posted')
    else:
        text, img_file_pathname = get_content_from_file_system(content_check)

        vk_post(login=LOGIN_VK,
                password=PASSWORD_VK,
                token=TOKEN_VK,
                vk_group=GROUP_ID_VK,
                vk_group_album=GROUP_ID_ALBUM_VK,
                content_text=text,
                content_img_file_pathname=img_file_pathname)
        logging.info(' Success publish: post was publised')


if __name__ == '__main__':
    main()
