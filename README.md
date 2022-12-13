# SE 05 Relational Databases: Code Base

## Run the project
This is a simple flask project with postgres database and an attached pgadmin4. The project is dockerized and can be run with docker-compose. 

The Database is fully functional and can be used to store data and retriev data via the pgadmin4 interface. 
The flask app does not yet succesfully joins data from the database.

<br>

## ER Model

![ER Model](/ER_Model.png "ER Model")

## Requirements
Docker Desktop

    - installed and running

<br>

## Setting up Database in Local Deployment

### 1. Build the images and run the containers:

    ```
    $ docker-compose up -d --build
    OR
    $ docker-compose -f docker-compose.yml up -d --build 
    ```

The flask app should be reachable at [http://localhost:5000](http://localhost:5000) and returns "hello world". 

<br>

### 2. Start PgAdmin
PgAdmin should be available at [http://localhost:5555](http://localhost:5555). It can take up to 30 seconds for the pgadmin service to be available.

The default credentials are:
 ```
PGADMIN_DEFAULT_EMAIL:      pgadmin4@pgadmin.org

PGADMIN_DEFAULT_PASSWORD:   admin
 ``` 
<br>

### 3. Connect PgAdmin to the database

Brows to "Add Server" and enter the following credentials:

    GENERAL
    Name: Docker Localhost

    CONNECTION
    Host name/address: <see beneith "Retrieving IP-Address of DB">
    Port: 5432
    Maintenance database: code-db
    Username: code
    Password: code


#### Retrieving IP-Address of DB 
 Track down the correct Ip address of the postgres container.
 Please typ in your terminal:

    $ docker ps
    ### Find the "container id" of the container "postgres:13-alpine" and insert the "container id" in the following command:
    $ docker inspect <container id of the container "postgres:13-alpine> | grep IPAddress  
    $ 

### 4. Fill the database with data
Now we are going to execute the sql scripts to fill the database with data. 

    1. Inside PGadmin browse in the left browser to: 
    "Servers/Docker Localhost/Databases/code-db/Schemas/public/tables"
    
    2. Right click on the table and select "Query Tool"

    3. From this code repository, browse to the folder /sql, and copy the content of the sql script "1_create_tables.sql" and paste it into PGAdmins query tool. Then press the "Execute" button.

    4. Repeat step 3 for the sql scripts "2_fill_tables.sql" and "3_create_index.sql"

    5. Now the database is filled with data and ready to be used. If the tables are not shown properly, please right click in PGAdmin inside the browser view on the "table" and select "Refresh".


### 5. Closing down the project
To close down the project, please type in your terminal:

    $ docker-compose down
    