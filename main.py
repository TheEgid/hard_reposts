import os
import sys
import logging
from dotenv import load_dotenv
import vk_api

class VKApiPostingError(Exception):
    """Declare special exception."""
    pass


def vk_post(login, password, token, vk_group, message, image=None):
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except:
        vk_api.AuthError()
    vk = vk_session.get_api()
    vk.wall.post(owner_id=vk_group, access_token=token, message=message)
    wallpostsdict = vk.wall.get(count=1, owner_id=vk_group)['items'][0]
    if wallpostsdict['text'] != message:
        raise VKApiPostingError()


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, os.path.split(dir_path)[0])

    load_dotenv()
    LOGIN_VK = os.getenv("LOGIN_VK")
    PASSWORD_VK = os.getenv("PASSWORD_VK")
    TOKEN_VK = os.getenv("TOKEN_VK")
    GROUP_ID_VK = os.getenv("GROUP_ID_VK")

    my_message = 'раздватри'
    vk_post(login=LOGIN_VK,
            password=PASSWORD_VK,
            token=TOKEN_VK,
            message=my_message,
            vk_group=GROUP_ID_VK,
            image=None)
    #logging.info('finished!')
