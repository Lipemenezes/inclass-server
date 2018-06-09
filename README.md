# Dependencies

Install the dependencies using `pip install -r requirements.txt`.


If you are running on windows, you must install MySQL-python manually.

You can download it here:

https://pypi.org/project/MySQL-python/1.2.5/#files

# Run development server

After you have all the dependencies installed, you must create a database and set it's access information to `settings.py`.

Then, you can run the migrations with `python manage.py migrate`.

After that, you are ready to go, just type on the terminal `python manage.py runserver`.
