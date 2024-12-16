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

## Exercise 2.3: Django Models
### Learning Goals
- Discuss Django models, the 'M' part of Django's MVT architecture
- Create apps and models representing different parts of your web application
- Write and run automated tests

### Reflection Questions
1.	Do some research on Django models. In your own words, write down how Django models work and what their benefits are.

- Django models are Python classes that define schema of the project database for a specific app. Their benefits include scalability, reusability, and efficiency/performance.

2.	In your own words, explain why it is crucial to write test cases from the beginning of a project. You can take an example project to explain your answer.

- Writing test cases from the beginning is crucial in order for the developer to ensure components and functions are working as designed/intended throughout the development cycle. Debugging and troubleshooting can take place in tandem with scaling up the project/application.

## Exercise 2.5: Django MVT Revisited
### Learning Goals
- Add images to the model and display them on the frontend of your application
- Create complex views with access to the model
- Display records with views and templates

### Reflection Questions
1.	In your own words, explain Django static files and how Django handles them.

- Django static files are those that don't change or they require processing by Django during application runtime (CSS, JavaScript, and images). With regards to handling, Django best practices direct developers to create dedicated 'Static' directories for them.

2. Look up the following two Django packages on Django's official documentation and/or other trusted sources. Write a brief description of each.

| Package    | Description                                               |
|------------|-----------------------------------------------------------|
| ListView   | A generic view in Django that displays a list of objects  |
| DetailView | A generic view in Django that displays details of objects |

3. You're now more than halfway through Achievement 2! Take a moment to reflect on your learnig in the course so far. How is it going? What's something you're proud of so far? Is there something you're struggling with? What do you need more practice with? You can use these notes to guide your next mentor call.

- I think things have been going really well. The concepts are relatively easy to grasp and work through, which I have enjoyed. I can't think of anything major that I'm struggling with. As said, the concepts are pretty straightforward and incorporating them into the project is made simpler.

## Exercise 2.6: User Authentication in Django
### Learning Goals
- Create authentication for your web application
- Use GET and POST methods
- Password-protect your web application's views

### Reflection Questions
1.	In your own words, write down the importance of incorporating authentication into an application. You can take an example application to explain your answer.

- Authentication plays an important role in security, especially if an application stores and displays sensitive data. In addition, it provides capabilities for catering functions and views uniquely to each individual user experience.

2.	In your own words, explain the steps you should take to create a login for your Django web application.

- First, one must create a view in which to import `authenticate`, `login`, and `AuthenticationForm` packages. Once imported, the functions of the packages can be incorporated into the CBV or FBV. Next, a template needs to be created to provide the login form to the user. Last, you need to register the URLs in the project's `urls.py` file.

3.	Look up the following three Django functions on Django's official documentation and/or other trusted sources and write a brief description of each.

| Function         | Description                                                      |
|------------------|------------------------------------------------------------------|
| authenticate()   | Verifies credentials as arguments to check against the database  |
| redirect()       | Redirects users to a specified URL                               |
| include()        | Used to add URLs from apps to the project level                  |

## Exercise 2.7: Data Analysis and Visualization in Django
### Learning Goals
- Work on elements of two-way communication like creating forms and buttons
- Implement search and visualization (reports/charts) features
- Use QuerySet API, DataFrames (with pandas), and plotting libraries (with matplotlib)

### Reflection Questions
1.	Consider your favorite website/application (you can also take CareerFoundry). Think about the various data that your favorite website/application collects. Write down how analyzing the collected data could help the website/application.

- I don't necessarily have a favorite website or application. However, if I use a social media site such as Twitter or Facebook, there are several areas in which data is collected and/or analyzed. One such example with Twitter is the `Trending` feature that takes either hashtags (`#`) or consistent keywords and provides those in a specific view or section on Twitter wherein users can see what things are currently being "discussed".

2.	Read the Django official documentation on QuerySet API. Note down the different ways in which you can evaluate a QuerySet.

- `.all()` - Retrieves all records from a specified object.
- `.filter()` - Narrows/filters results of a query from specified search criteria.
- `.exclude()` - Opposite of `filter`, omits results not matching specified criteria.

3.	In the Exercise, you converted your QuerySet to DataFrame. Now do some research on the advantages and disadvantages of QuerySet and DataFrame, and explain the ways in which DataFrame is better for data processing.

- QuerySets tends to be better suited for large data sets from databases as they don't require a lot of resources from systems (memory, processing, etc.). DataFrames provide agile functions for data manipulation, integration, and analysis.
