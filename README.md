# CS162_Kanban_Board
A kanban board web app built on Flask

Welcome to Chrecci & Co. Kanban Board! Simple Kanban board where you can list taskss, declare their status, and attribute to someone else on your team.

## Key Features

### Auth
Users are allowed to create their own accounts and passwords. Once logged in, users gain access to numerous more features! All users can be referenced to within the app, and each username must be unique. There are currently no limits set on passwords, but usernames are limited to 10 characters. Auth is handled by Flask. Users can log out by hovering over their username on the top right corner of the app.

### Kanban Blog
After every new issue is made, the change will be reflected in the Home page. This is essentially a blog from where you can see all the tasks that have been assigned, with the most recent ones at the top. Furthermore, all the posts can be clicked upon to expand the post, leading to its actual page. The benefit here is that the home blog can be kept concise, and if a user would like to see more info, they can click on the post title and go to the post page. 
Additionally, if a post was made by currently logged in user, they are also allowed, and only they are allowed, to edit the post. This is to preserve ownership of posts, and integrity within team members. More will be elaborated upon later under "tickts." Clicking on the main header also leads you back to this page, ensuring all navigation can be fully through the app alone.

### Main Board
Here is a traditional Kanban Board. All 7 task statuses are laid out with their respective tickets organized appropriately. The goal here is to provide an accurate, functional, and efficient overview of a project's or team's backlog. You can easily discern which sections are longer, which tasks are where, and which tasks still need to be completed. Unlike the blog, you must have an account to utilize this feature.

### Your Board
To make a user's life better and more practical, when a user hovers over their username in the top right corner, there is a drop down menu that pops up, allowing the user to see their unique board. All tasks assigned to them are in one column, and all tasks that they have assigned are in the other. There was an idea to make it such that only tasks that were not DONE showed up here, but users may want to see tasks that were done first then delete etc. so the option remains.

### Posts
Posts can be created whenever on the website, so long as user is logged in. All fields must be filled out to prevent spam. Furthermore, all tasks can be edited by the author of that task. This can be done either from the Home blog, or by clicking on a post, then "Edit." The great thing is that all posts can be viewed by everyone, but not edited. Furthermore, careful thought and deliberation went into the routing. If you are creating or updating a post, and then click either "cancel" or simply to another page, a pop-up notification will ask you to confirm so you don't accidentally lose your information. Clicking "cancel" automatically leads you back to the previous page.
Upon updating, an option to "Delete" also exists. Similarly, a confirm situation is presented just in case.

### Testing
26 individual tests are provided that cover each page of the app and most important functionalities. These tests are thorough and comprehensive. They exist to help prevent oftentimes forgotten errors, such as url editing to bypass access, SQL injection, missed links etc. See more below on how to run tests.

## Functionalites of Note (for grading)

Here is a list of subtle features that may not appear immediately obvious but I believe bolster the security, usability, practicality, and complexity of this project over what was simply demanded:

- Applied user auth (certain actions require sign in, others a specific user, this is all handled rather seamlessly within app and not clunkily. For example, if you're not the author of a post, the option to edit simply won't be there for you, instead of it leading to an error message)
- Hover menu (solid application of HTML and CSS, intuitive for users and allows us to furhter compartmentalize parts of our app. Less clutter. In the future, things such as "settings," "help" etc. will all live here)
- Javascript logic handling. A little bit of javascript is included to help with certain processes. For example, I really wanted to make sure that Cancel's led to previous page and not some hard-coded URL; that would feel weird. At the same time, I wanted to include a confirmation message. Thus, applying simple js to help handle that logic solves the issue. Again, its not much, but for future can include more complex logic, like autofill, recommending users to tag etc.)
- Custom font (Press Start 2p is used instead of default fonts. Its just more fun)
- Main Board
- Your Board (both took significant time and learning to build. Included creating another Flask blueprint and strong HTML logic)
- Pytest (a lot of tests are included that really do explore almost to entirety of the app. Every page and virtually every function)
- Post Creation (the post creation and deletion process are both very smooth, and implemented the usage of databases strongly)
- URL-routing

## Installation

### Virtual Environment

> py -3 -m venv <name_of_environment>
> <name_of_environment>\Scripts\activate
> pip install -r requirements.txt

### Running application
> pip install -e .
> set FLASK_APP=KanbanFlask
> set FLASK_ENV=development
> flask init-db
> flask run

### Testing

> pip install pytest coverage
> pytest
> pytest -v (verbose)
>coverage run -m pytest

*if working from venv, may have to reinstall nnumpy globally from anaconda*

next steps (11/03/2021):
- set up main kanban board page
- set up user tasks assigned to and from user
- fix more tests
- more secure auth
- create .gitignore file

next steps (11/04/2021):
- set up main kanban board page DONE
- Cleaned up UI DONE
- MENU BAR DONE
- Return back to previous page after canceling DONE
- set up user tasks assigned to and from user 
- fix more tests
- more secure auth
- create .gitignore file