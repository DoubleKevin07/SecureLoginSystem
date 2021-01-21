# SecureLoginSystem
An MVC example. Uses encryption and salts to make your account data secure.

## Which file is which?

### Model
The model for my MVC is in *model.py*. This file stores the model for accounts.

What the website will do is, it will interact with a database that uses this model for each Account.

### View
The "View" component is mixed between Application.py, and every file in "templates."

The files in "templates" are the individual HTML files that will be rendered 

The application.py will render the individual HTML files.

### Controller
The controller is "Application.py". It will tell the webpage to render, and will fetch objects from the database.
This is where most of the user interaction takes place.

# How to run

- NOTE: You will need your own SQL database URL and Key.

1. Fill in `<DATABASE URL HERE>` in start.bat, and `<DATABASE KEY HERE>` in application.py.
2. Run start.bat and go to http://127.0.0.1:5000/ in a web browser.
