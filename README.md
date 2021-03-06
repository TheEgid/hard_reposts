# hard_reposts!

Проект предназначен для автоматизированного постинга текста и изображений в группы социальных сетей - телеграм, фейсбук, вконтакте.

### Как установить

Скачиваем файлы в папку hard_reposts. В этой же папке создаем .env файл. Ваш .env должен содержать строки:

```
LOGIN_VK = ваш_логин_в_контакте
PASSWORD_VK = ваш_пароль_в_контакте
TOKEN_VK = токен_вашего приложения_в_контакте
GROUP_ID_VK = id_группы_в_контакте
GROUP_ID_ALBUM_VK = id_альбома_в_контакте
TOKEN_TG = токен_вашего_бота_телеграм
CHANNEL_TG = название_канала_телеграм
TOKEN_FB = токен_вашего_приложения_в_фейсбуке
GROUP_ID_FB = id_вашей_группы_в_фейсбуке
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Использование
В папке "content_folder" сохраняем .txt и .jpg файлы с контентом, где название - цифра - порядковый номер поста.
например -
```
12.jpg
12.txt
```
Используем консольный ввод. Аргументом передаем порядковый номер поста.
```
python3 main.py 12
```
Программа выводит в консоль лог своей работы. 

```
INFO:root: Success publish: facebook post was published
```
После этого сообщения пост размещен.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
