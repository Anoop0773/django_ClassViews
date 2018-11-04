Required Configuration-
Python==3.5
Django==2.1.3

Summary-
In this small project you have to create user usign your django-admin panel.Admin can create project and can create tasks.Admin can assign task to other usrers.I have used django generic views for making this project.

Create DB-
python manage.py makemigrations
python manage.py migrate


Create Superuser-
python manage.py createsuperuser
username : admin
email : admin@gmail.com
pass : pass@123
confirm-pass : pass@123

Create Admin and Members-
1) python manage.py runserver
2) Goto - http://127.0.0.1:8000/admin
3) Give super-username and super-password.eg: username : admin,password:pass@123
4) Click on 'users'
5) click on 'ADD USER+'
6) We will Create 5 users 2 will be staff(Admin) and 3 will be member
    a) for staff repeat same following process two times with different credentials- 
        After clicking 'ADD USER+'
            -username : admin01
            -password : pass@123
            -password-confirmatiom : pass@123
            click on 'sava and continue editing'

            Personal info
                -First Name : admin
                -Last Name : 01
                -Email : admin01@gmail.com
            Permissions
                -Active : check
                -Staff Status : check
                -Superuser status : uncheck
            
        Click on 'Save'

    b) for member repeat same following process three times with different credentials- 
        After clicking 'ADD USER+'
            -username : user01
            -password : pass@123
            -password-confirmatiom : pass@123
            click on 'sava and continue editing'

            Personal info
                -First Name : user
                -Last Name : 01
                -Email : user01@gmail.com
            Permissions
                -Active : check
                -Staff Status : uncheck
                -Superuser status : uncheck

            Click on 'Save'

After the above command you'll be able to see html page by running following url in browser:
http://127.0.0.1:8000/

