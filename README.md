## Run the project


### Development

Uses the default Flask development server.

Build the images and run the containers:

    ```
    $ docker-compose up -d --build
    ```

Test it out at [http://localhost:5000](http://localhost:5000). The "web" folder is mounted into the container and your code changes apply automatically.

PgAdmin is available at [http://localhost:5555](http://localhost:5555). The default credentials are `

PGADMIN_DEFAULT_EMAIL: pgadmin4@pgadmin.org
PGADMIN_DEFAULT_PASSWORD: admin

Connect PgAdmin to the database:

    ```
    GENERAL
    Docker Localhost

    Host name/address: 172.19.0.2
    Port: 5432
    Maintenance database: hello_flask_dev
    Username: hello_flask
    Password: hello_flask
    ```

Error handling if connection fails: Track down the correct Ip address of the db container:

    ```
    $ docker ps
    ### Find and copy the container id of the container "postgres:13-alpine"
    $ docker inspect <container id of the container "postgres:13-alpine> | grep IPAddress  
    $ 
    ```

### Production

Uses gunicorn + nginx.

Build the images and run the containers:

    ```
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```
  Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.



