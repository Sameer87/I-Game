# ESP Game


Let’s suppose we have Player A and Player B. There are 15 questions in the system (i.e. 15 primary images). Each time Player A starts the game, he/she is shown 5 random primary images and secondary images corresponding to the primary image. 

- Player A selects the matching secondary images for the primary image
- Player B is shown the same 5 question (i.e same 5 primary image). Player B selects his/her answers.
- If the answer for Player A and Player B match, both of them get a point else none of them gets the point.

### Installation

##### 1. Virtualenv
You should already know what is virtualenv at this stage. So, simply create it for your own project, where projectname is the name of your project:
```sh
$ virtualenv projectname
```
##### 2.Download
Now, you need ESP Game project files in your workspace,So you can clone it easily

```sh
git clone https://github.com/Sameer87/I-Game.git
```

##### 3.Requirements
You can find all requirements in requirements.txt file and easily install them with 
```sh
$ pip install -r requirements.txt
```
##### 4.Initialize the database
First set the database engine (PostgreSQL, MySQL, etc..) in your settings files; Of course, remember to install necessary database driver for your engine. Then define your credentials as well. Time to finish it up:

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```
##### 5.Ready and Go!
Apply the following command to run the local server and check localhost(http://127.0.0.1:8000/ ) now.

```sh
$ python manage.py runserver
```
