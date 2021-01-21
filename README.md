# SecureLoginSystem
An MVC example. Uses encryption and salts to make your account data secure.

When I make two accounts with the same password, they will have a different salt, and therefore a different hash.

In this gif, I show three usage examples.

1. I try to create an account that already exists (it doesn't let me).
2. I make an account "James2" with password "James"
3. I make an account "James3" with password "James"

We see at the end the different hashes for the password for James2 and James3, even though it is the same password.

![Example](https://i.imgur.com/AjBTCGi.gif)

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
