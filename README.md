# current_time_django_project
My First Python-Django project 
It Will display the current Date and Time of the server..
Steps to Do:(need to install django)
in cmd prmt type: django-admin startproject Current_time_django_project
it will create project with name as "Current_time_django_project"
now go to inside of the project: cd Current_time_django_project
now type in cmd: python manage.py startapp timeapp
it will create application with name as "timeapp".
create one folder as name "templates" at project level. In that template folder create folder with name "timeapptemp" and again in that subfolder create html file as "index.html"
so basically it will look like this.."templates/timeapptemp/index.html"
now go to settings.py(project level) file add line below BASE_DIR as TEMPLATES_DIR = os.path.join(BASE_DIR,'templates') and this variable TEMPLATES_DIR in TEMPLATES/DIRS(settings.py)
now go to the views.py file(application level) and here i am imported datetime to get current datetime and passed it to index.html file in the template tag file format.
now go to the index.html file. Here we are passing the template tag value from views.py file.r
now define the url,for that you need to go urls.py(project level) and write down as code.
to check the  output type cmd: python manage.py runserver
it will run on localhost with url as: "127.0.0.1:8000/date" or "localhost/date"
