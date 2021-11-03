# CS162_Kanban_Board
A kanban board web app built on Flask

to set up venv:

> py -3 -m venv <name_of_environment>
> <name_of_environment>\Scripts\activate

to run:

> pip install -e .
> set FLASK_APP=KanbanFlask
> set FLASK_ENV=development
> flask init-db
> flask run

to test:

> pip install pytest coverage
> set FLASK_APP=KanbanFlask
> set FLASK_ENV=development
> flask init-db
> flask run
