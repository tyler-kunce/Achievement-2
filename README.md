# Achievement 2

## Exercise 2.1: Getting Started with Django
### Learning Goals
- Explain MVT architecture and compare it with MVC
- Summarize Django's benefits and drawbacks
- Install and get started with Django

### Reflection Questions
1. Suppose you're a web developer in a company and need to decide if you'll use vanilla (plain) Python for a project, or a framework like Django instead. What are the advantages and drawbacks of each?

- 'Vanilla' Python offers the most flexibility as it is not constrained to the rules or restrictions of a framework (The Django Way). Unlike Django though, 'vanilla' Python doesn't have a lot of the tools and built-in/out-of-the-box functions and features that a framework offers. Lastly, one of many advantages of frameworks is that it is open-sourced with a vast community of developers while 'vanilla' requires the expertise and resourcefulness of the developer.

2. In your own words, what is the most significant advantage of Model View Template (MVT) architecture over Model View Controller (MVC) architecture?

- The biggest advantage of MVT over MVC is the simplicity in its interaction with the user, the database, the framework, and the business logic. It cuts out a lot of added steps in coding that's required of MVC.

3. Now that you've had an introduction to the Django framework, write down three goals you have for yourself and your learning process during this Achievement.

- Further my experience and expertise of Python
- Learn a Python-centric framework, Django
- Develop a more user-friendly Python-based app

## Exercise 2.2: Django Project Set Up
### Learning Goals
- Describe the basic structure of a Django project
- Summarize the difference between projects and apps
- Create a Django project and run it locally
- Create a superuser for a Django web application

### Reflection Questions
1.	Suppose you’re in an interview. The interviewer gives you their company’s website as an example, asking you to convert the website and its different parts into Django terms. How would you proceed? For this question, you can think about your dream company and look at their website for reference.

- With regards to Django, the entirety off the web application is considered a 'project'. Nestled under the project are 'apps' that each perform specific functions, such as 'login', 'admin', 'users', etc. Each app performs one function for the overall project (or other projects; they can be recycled).

2.	In your own words, describe the steps you would take to deploy a basic Django application locally on your system.

- After locating to the directory in which I want to create my application, I would first create a virtual environment then immediately install Django. Next, calling django-admin, I would use 'startproject' to create the project (application). From there, I can run `python manage.py migrate` to run migrations on the project/application, followed by `python manage.py runserver` to locally deploy or run the application.

3.	Do some research about the Django admin site and write down how you’d use it during your web application development.

- The Django admin site is a GUI interface for super users to perform CRUD (create, read, update, delete) operations on the project models.