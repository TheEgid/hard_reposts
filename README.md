# hard_reposts!

input = content_number


### Как установить

Скачиваем файлы в папку hard_reposts. В этой же папке создаем .env файл. Ваш .env должен содержать строки:

```
LOGIN_INST=ваш_инстаграм_логин
PASSWORD_INST=ваш_инстаграм_пароль
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Использование
В папке "content_folder" сохраняем .txt и .jpg файлы с контентом, где название - порядковый номер поста.
например -
```
12.jpg
12.txt
```
Используем консольный ввод. Аргументом передаем порядковый номер поста.
```
python3 main.py 12
```
Программа выводит в консоль лог своей работы. Пример лога

 ```
INFO:root:download & saved images/space1.jpg
2019-01-02 00:51:41,505 - INFO - Photo 'images\space1.jpg' is uploaded.
INFO:root:timeout= 21
```

!
```
INFO:root:download & saved images/space1.jpg
2019-01-02 00:51:41,505 - INFO - Photo 'images\space1.jpg' is uploaded.
INFO:root:timeout= 21
```
После этого сообщения посты размещены.
