# Purbeurre

## What is PurBeurre ? 

Purbeurre is an application whose purpose is to give healthier alternative to the foods we eat every day.
Select a food and it will suggest you another one, healthier, from the same category

## How to use the program

### First, install the requirement.txt 

Type **pip install requirement.txt**

### Create a database  

Create a mysql database called Purbeurredb. 

### Rename the config_exemple.py file

Rename config_exemple.py to config.py.
Inside, replace:
- DB_HOST = _"localhost"_ with the SQL server adress;
- DB_USER = _"root"_ with your username;
- DB_PASSWD = _""_ with your password;

### How to load the database 

Execute:
**mysql -h server -u username -p purbeurredb>purbeurredb.sql**
(*replace server with your sql server, username with your username before launching*)

Then, execute **dbfiller.py**

### Launch

Execute **purbeurre.py**


