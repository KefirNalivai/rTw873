Инструкция по развертыванию проеекта:
  1. Устанавливаем приложение git командой sudo apt get git
  2. Создаём папку для хранения приложения mkdir Project и переходим в этот каталог командой cd/Project
  3. Последовательно вводим команды git init (Первоначальная натсрйокал  окального репазитория), git git remote add origin https://github.com/KefirNalivai/rTwz873 (Установление подключения к репазиторию), git pull https://github.com/KefirNalivai/rTwz873 (установка проекта в папку)
  
      P.S. Изначально должен быть установлен и минимально настроен postresql, но я не буду углубляться в его установку и буду отталкиваться от того, что он установлен.
  
  4. Переходим в проект в консоли через cd Project. Далее вводим команду sudo gedit testProject/settings.py для открытия файла настроек проеекта. Этот файл нам нужен для того, чтоб настроить подключение к базе данных. Переходим на строки как на скриншоте ниже.
  
  ![image](https://user-images.githubusercontent.com/98163662/213194464-65b0f30d-d763-4711-9ef7-e9f0bb6c8f58.png)
  
   Нам нужно поменять лишь значения NAME (имя базы данных), USER (имя пользователя для поключения), PASSWORD (пароль пользователя), HOST (адресс на поключения к базе).
   Далее вводим команды: ./manage.py makemigrations и ./manage.py migrate для установки в БД таблицы для хранения значеницй инпутов.
        
      Если команда ./manage.py выдаёт ошибку permision denied, тогда нужно добавлять команду python3. Пример: pyrhon3 manage.py migrate
      
  5. 
    
Сервер развернут.
