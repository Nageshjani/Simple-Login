```bash
login/
├── login/
│   ├── settings.py
│   ├── urls.py
|
├── myapp/
│   └── views.py
|
├── templates/
│       ├── myapp/
│            ├── base.html
│            ├── login.html
│            ├── home.html
└── manage.py

```


```bash
django-admin startproject login
```
```bash
cd login
```
```bash
python manage.py startapp myapp
```

```bash
mkdir templates
cd templates
```
```bash
mkdir myapp
cd myapp
type nul > base.html
type nul > login.html
type nul > home.html

```
## settings.py
```python 
import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        
    },
]

```
# templates/myapp/ 

## base.html
```html


<head>

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

</head>

<body>

    {% block content %}
    {% endblock %}
    
</body>

```

## Note: {% extends 'myapp/base.html' %}
```bash
myapp/base.html , dont forget to update accordingly to your templates structure, I have added accordingly to mine
````


## login.html
```html


{% extends 'myapp/base.html' %}

{% block content %}
  <h2>Login</h2>
  
  {% if messages %}
    {% for message in messages %}
      <div class="alert alert-danger" role="alert">
        {{ message }}
      </div>
    {% endfor %}
  {% endif %}
  
  <form method="post">
    {% csrf_token %}
    <div class="form-group">
      <label for="username">Username:</label>
      <input type="text" name="username" id="username" class="form-control">
    </div>
    <div class="form-group">
      <label for="password">Password:</label>
      <input type="password" name="password" id="password" class="form-control">
    </div>
    <button type="submit" class="btn btn-primary">Login</button>
  </form>
{% endblock %}


```

## home.html
```html
{% extends 'myapp/base.html' %}

{% block content %}
  <h2>Welcome {{ request.user.username }}!</h2>
  <p>This is the home page for authenticated users.</p>
{% endblock %}


```

#

## myapp/views
```python
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def loginView(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is None:
            messages.error(request,'Invalid Credentials')
        else:
            login(request,user)
            return redirect('home')
    else:
        return render(request,'myapp/login.html')
            



@login_required
def home(request):
    return render(request,'myapp/home.html')
```

#
## login/urls.py
```python
from django.contrib import admin
from django.urls import path
from myapp.views import loginView,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',loginView,name='login'),
    path('home/',home,name='home')
    
    
]

```

```bash
python manage.py migrate
```
```bash
python manage.py createsuperuser
```
```bash
python manage.py runserver
```

## Let's Do Fun
```bash
'Go To below Home Link, You wont be able to go to home page since we added login_required'
```
[Home](http://localhost:8000/home)

```bash
'Dont, worry Now  just Go To Login Page, After giving right credentials you will redirect to Home page'
```
[Login](http://localhost:8000/login)

```bash
'Now You will be able to visit home page as many times as you want to since already logged in'
```
[Home](http://localhost:8000/home)

```bash
'You can check below admin panel to see your user details'
```

[Admin](http://localhost:8000/admin)


```bash
'Home pages not accessed without loggin in'
```
![Home Page](https://user-images.githubusercontent.com/34247973/228174380-07bf8a92-6b99-4fb4-a5c5-4edcbbe413ad.png)

```bash
'Now Loggin in'
```
![Login](https://user-images.githubusercontent.com/34247973/228174845-6699873f-652f-4ddf-8acf-ab072c570360.png)

```bash
'Finally Home Page'
```
![Home Page](https://user-images.githubusercontent.com/34247973/228174959-83e89e4d-45b0-409b-90a8-a4d5d6118c75.png)


