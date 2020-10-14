# Project 2 Milestone 1
## Chatter-chat application

## Cloning repository 

- Add a new folder under your userhome directory 
- Run the below command 
    - ``` git clone https://github.com/NJIT-CS490/project2-m1-aaa332```
    
   
  ## Installation
  ### Run the following commands
  - ``` nvm install 7  ``` 
  - ```  npm install  ```
  - ```  pip install flask-socketio ```
  -  ``` pip install eventlet ``` 
  - ``` npm install -g webpack ```
  - ``` npm install --save-dev webpack ```
  - ``` npm install --save-dev style-loader ``` 
  - ``` npm install --save-dev css-loader ```
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
  
  ### Enabling Read/Write from SQLAlchemy
  - run ``` sudo vim /var/lib/pgsql9/data/pg_hba.conf ``` and type the command ``` :%s/ident/md5/g ``` in vim
  - Restart the server with ``` sudo service postgresql restart ``` 
  
  ### Deploying to Heroku
  - Sign up for heroku at heroku.com 
  - Install heroku by running ``` npm install -g heroku ```
  - Make two files ``` requirements.txt ``` and ``` Procfile ``` named exactly as shown.
  - Run ``` pip freeze > requirements.txt ``` and insert ``` web: python app.py ``` in the Procfile
  Run the following commands:
    - ``` nvm i v8 ```
    - ``` heroku login -i ```
    -  ``` heroku create ```
    -  ``` git push heroku master ```

  ### Known Issues
  - There is currently no option for authentication/login and no usernames are displayed dynamically. Future support for this feature will be to allow login 
  to distinguish users from each other
  - The backend server is currently sendings the entire copy of the table in the database everytime the site is refresed. Future support for this to incrementally
  send message by message, or via caching the messages in the client side.
  - Number of active users sometimes lags due to socketio issues when opening new tabs/different browsers. Sometimes this issue is fixed by refreshing the page.
  
  ### Technical Issues
  - Had an issue with some messages not being rendered in the client side. Fixed it by correctly setting a react useState hook alongside a useEffect hook
  which will update the page everytime a new message arrives.
  - Had an issue with how to style useState arrays, i fixed this by mapping all the values using map() function and pass a className/css attribute to appropriately
  style the elements.
  - Had an issue with displaying CSS in general . This was fixed by    running 
  ``` npm install --save-dev css-loader ``` and ``` npm install --save-dev style-loader ``` 
  and  adding 
  ``` loaders: [  { test: /\.css$/, loader: "style-loader!css-loader" }]  ``` to the webpack.config.js
  - 
  
