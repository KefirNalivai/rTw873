Инструкция по развертыванию проеекта:
<h5>
  1. Устанавливаем приложение git командой sudo apt get git
  
  2. Создаём папку для хранения приложения mkdir Project и переходим в этот каталог командой cd/Project
  
  3. Последовательно вводим команды git init (Первоначальная наcтройка локального репазитория), git remote add origin https://github.com/KefirNalivai/rTwz873 (Установление подключения к репазиторию), git pull https://github.com/KefirNalivai/rTwz873 (установка проекта в папку)
  
      P.S. Изначально должен быть установлен и минимально настроен postresql, но я не буду углубляться в его установку и буду отталкиваться от того, что он установлен.
  
  4. Переходим в проект в консоли через cd Project. Далее вводим команду sudo gedit testProject/settings.py для открытия файла настроек проеекта. Этот файл нам нужен для того, чтоб настроить подключение к базе данных. Переходим на строки как на скриншоте ниже.
  
  ![image](https://user-images.githubusercontent.com/98163662/213194464-65b0f30d-d763-4711-9ef7-e9f0bb6c8f58.png)
  
   Нам нужно поменять лишь значения NAME (имя базы данных), USER (имя пользователя для поключения), PASSWORD (пароль пользователя), HOST (адресс на поключения к базе).
   Далее вводим команды: ./manage.py makemigrations и ./manage.py migrate для установки в БД таблицы для хранения значеницй инпутов.
        
      Если команда ./manage.py выдаёт ошибку permision denied, тогда нужно добавлять команду python3. Пример: pyrhon3 manage.py migrate
      
  5. Запускаем сервер командой ./manage.py runserver.
    </h5>


Настройка статичных файлов.
  1. В корне проекта создаём новые папки mkdir static и mkdir media
  2. Далее идем в файл settings.py (Смотрите пункт 4 инструкции по развертыванию) и вписываем туда новые строки STATIC_ROOT = 'static' и MEDIA_ROOT = 'media'. Также можем изменить доменный хост в строке ALLOWED_HOSTS = [ 'www.example.com' ], если нужно.
  3. Возращаемся в корень cd .. и прописываем ./manage.py collectstatic

Настройка uwsgi
<h5>
  1. Идем в дерикторию /etc/uwsgi/apps-enabled и создаем там файл my_app.ini с содержимым:
 <i><pre>
        [uwsgi]
        chdir = git/Project
        env = DJANGO_SETTINGS_MODULE=project.settings.production
        wsgi-file = testProject/wsgi.py
        workers = 1max-requests=5000
        plugins=python3
        processes = 5
        threads = 2
        master = true
        die-on-term = true
        socket = sedova.sock
        chmod-socket = 660
        vacuum = true
        uid = www-data
        gui = www-data
        </pre>
  </i>
       
  2. Пишем команду service uwsgi restart
</h5>

Настройка Nginx
<h5>
  1. Идем в дерикторию /etc/nginx/conf.d и создаем там файл my_app.conf с содержимым:
  <i>
    <pre>
    server {
      listen 80;
      server_tokens off;
      server_name my_app my_app.domain.local;

      location / {
          include uwsgi_params;
          uwsgi_pass unix:///run/uwsgi/app/sedova/socket;
      }

      location /static/ {
          alias /var/www/my_app/static/;
      }

      location /media/ {
          alias /var/www/my_app/media/;
    }
}
    </pre>
  </i>
 </h5>

  2. Пишем команду systemctl restart nginx
