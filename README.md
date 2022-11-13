## Run the project


### Development

Uses the default Flask development server.

Build the images and run the containers:

    ```
    $ docker-compose up -d --build
    ```

Test it out at [http://localhost:5000](http://localhost:5000). The "web" folder is mounted into the container and your code changes apply automatically.



### Production

Uses gunicorn + nginx.

Build the images and run the containers:

    ```
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```
  Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.



Franchise.cloud

Terminal:
npx franchise-client@0.2.7