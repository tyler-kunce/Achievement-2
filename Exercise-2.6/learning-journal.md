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