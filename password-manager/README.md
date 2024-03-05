# Password Manager

---

This tool allows you to manage your passwords by doing 3 things:
- Generating complex passwords that consist of a combination of random letters, symbols and numbers.
- Saving each password with its website name and email in a csv file.
- Allowing you to search for and retrieve the password you generated for a website by typing the name of that website.

![password_mngr_screenshot](https://github.com/Abdelrahman-Elsaudy/Password-Manager/assets/158151388/fa2d1f3f-5bc0-4ac1-8db6-de1524076c53)

---

## Applied Skills:

---
**1. GUI with Tkinter Module**

- Creating interactive user-interface with labels, entries and buttons.
- Using **messagebox** which provides the user with different feedbacks for each scenario:
    - [x] Confirming the entered data before adding them to the password keychain (saved data).
    - [x] Showing error if the user leaves a blank entry cell and wants to save a generated password.
    - [x] Showing error if the user presses _search_ and there were no saved data file.
    - [x] Showing error if the user searches for a website that was not saved before.


**2. Using Pandas Module**

- Writing the generated password alongside with the entered website and email in a row inside the data csv file.
- Reading the saved email and password when the user searches for a saved website.

**3. Exception Handling**

- To handle the error of not finding the _data.csv_ file when the user opens the app for the first time.


```
try:
    data = pandas.read_csv("data.csv")
except FileNotFoundError:
    web_list = []
    user_list = []
    passw_list = []
else:
    web_list = data.website.to_list()
    user_list = data.user.to_list()
    passw_list = data.password.to_list()
```

**4. Global Variables**

- To recall the data lists and add the entered data to them once the user confirms.


```
if confirm:
    global web_list, user_list, passw_list
    web_list.append(web)
    user_list.append(user)
    passw_list.append(passw)
```


---


## Note:

---

- There are several password generators online but having an offline tool like this one is a lot safer.
---

_Credits to: 100-Days of Code Course on Udemy._