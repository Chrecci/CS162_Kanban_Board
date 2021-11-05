# CS162_Kanban_Board
A kanban board web app built on Flask

Welcome to Chrecci & Co. Kanban Board! Simple Kanban board where you can list tasks, declare their status, and attribute to someone else on your team.

## Key Features

### Auth
Users are allowed to create their own accounts and passwords. Once logged in, users gain access to numerous more features! All users can be referenced to within the app, and each username must be unique. There are currently no limits set on passwords, but usernames are limited to 10 characters. Auth is handled by Flask. Users can log out by hovering over their username on the top right corner of the app.

### Kanban Blog (index)
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
*If you're reading from direct README.md file, don't forget to ignore '<br />' tags*

> py -3 -m venv <name_of_environment> <br />
> <name_of_environment>\Scripts\activate <br />
> pip install -r requirements.txt <br />

### Running application
> pip install -e . <br />
> set FLASK_APP=KanbanFlask <br />
> set FLASK_ENV=development <br />
> flask init-db <br />
> flask run <br />

### Testing

> pip install pytest coverage <br />
> pytest <br />
> pytest -v (verbose) <br />
>coverage run -m pytest <br />

*if working from venv, may have to reinstall numpy globally from anaconda*

## HC & LO's

### LO

webstandards - Flask's strengths are captured through this project. Its minimalism, Blueprints, code blocks, and url routing are all taken advantage of to make the code simpler, easier to follow, and more efficient (I'd argue this is even a good application of #abstraction). Furthermore, a breadth of languages (Python, CSS, HTML, Javascript) are all effectively utilized to construct a seamless well-functioning web application. A lot of these decisions are justified above, but for example using Javascript scripts to handle functions and avoid convoluting our HTML code. This made sure that I could easily integrate more-complex logic without having to squeeze it all in a few lines, making it hard for readers to follow. This also makes it such that I can easily edit the logic, recycle it elsewhere, add on to it etc (#agile). JS is very well integrated with HTML so this decision was a natural one, and resorting to python would have simply complicated things; also, because JS paired with HTML is the industry standards, using python could needlessly confuse other developers.

#testing - refer to section testing above. Not only does the code pass all the tests, the tests are well-designed, insightful, and genuinely purposeful. The tests help me while I'm coding to make sure I didn't look something over, and each component is working as desired. Tests are well justified and comprehensive, strong application.

#communication - while this was not a team project, this README.md file is thorough in providing potential user's a high level overview of what the app is doing. For a simple web app as this one, I preferred this over over-commenting the code itself. For anyone with any minimal experience in coding, following any file is not hard (its mostly html and css...), but understanding how it all ties together, what the functionalities are etc. are not always immediately obvious. Thus, this write up exists to explain what users should look for and how things work. Furthermore, installation instructions are simple, direct, and easy to follow. Comments are placed where appropriate.

### HC's

constraints - a web-app had to be built in a short time-frame. The first constraint I had to identify was the obvious one of time. Given my constraint, I prioritized which aspects of the project were most important. Considering this is software development, I chose functionality over aesthetics, simplicity and modularity over complications. Thus, I spent just the necessary time on CSS and styling to show adequacy, but spent more time on getting the big features and functionalities across. This application of constraint led to a better and completed project. Furthermore, there were internal constraints. The technology of Flask meant it was unreasonable to resort to other convenient tools in this time. For example, using react.js to handle the front end. Thus, careful time was spent instead on maximizing Flask's features, such as code block, to create a similarly functional frontend. By assessing and breaking down constraints, and choosing to work within those constraints effectively, the whole and quality product could be delivered. 