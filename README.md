# Project 2 Milestone 1
## Chatter-chat application

## Cloning repository 

- Add a new folder under your userhome directory 
- Run the below command 
    - ``` git clone https://github.com/NJIT-CS490/project2-m1-aaa332```
    
   
  ## Installation
  ### Run the following commands
  - ```  npm install  ```
  - ```  pip install flask-socketio ```
  -  ``` pip install eventlet ``` 
  - ``` npm install -g webpack ```
  - ``` npm install --save-dev webpack ```
  - ``` npm install socket.io-client --save ```
  - If you encouncer any errors, use ``` sudo pip/npm ``` , or use the full path of pip using ``` which pip ```
  ### Setting up PSQL with Python
  - ``` sudo yum update ``` (Updating yum)
  - ``` sudo /usr/local/bin/pip install --upgrade pip ``` (Upgrading pip) 
  - ``` sudo /usr/local/bin/pip install psycopg2-binary ``` (Installing psycopg2)
  - ``` sudo /usr/local/bin/pip install Flask-SQLAlchemy==2.1 ``` (Installing FlaskSQLAlchemy)
  
  - Install PostgreSQL ``` sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs ```
  - Initialize PSQL database ``` sudo service postgresql initdb ```
  - Start PSQL ``` sudo service postgresql start ```
  - Make a new superuser ```sudo -u postgres createuser --superuser $USER ``` (ignore the error message)
  - Make a new database ``` sudo -u postgres createdb $USER ``` (ignore the error message)
  - Create a password ``` create user [some_username_here] superuser password '[some_unique_new_password_here]'; ```
  - Make a new file called ``` sql.env ``` and insert ``` SQL_USER=<UserNameHere> ``` and ``` SQL_PASSWORD=<PasswordHere> ```
  - Make another variable called ``` DATABASE_URL ```  and insert ``` postgresql://<usernamehere>:<passwordhere>@localhost/<nameofdatabasehere> ```
  
