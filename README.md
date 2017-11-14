# Installation

Install python packages in virtualenv:

    ```
    cd gqlclans
    mkvritualenv gqlclans --python=python3
    pip install -r requirements
    ```


# Usage

To run http server command:

    ```
    python start_app.py
    ```

Now you can visit [http://localhost:8567](http://localhost:8567) and play with GraphQL queries in GraphiQL console


# Frontend

To run React-Apollo example follow steps in frontend [section](./frontend/README.md)

# Docker

To run backend container from docker:

    ```
    docker create --name=gqlclans -t -i -p 8567:8567 sudoaptget/gqlclans:latest
    docker start -i gqlclans
    ```

To run frontend container from docker:

    ```
    docker create --name=gqlclans-fe -t -i -p 8010:8010 sudoaptget/gqlclans-fe:latest
    docker start -i gqlclans-fe
    ```

To run project from docker for development use docker-compose:

    ```
    docker-compose -p gqlclans up
    ```

Frontend service will be available via [http://0.0.0.0:8010](http://0.0.0.0:8010)
and backend via [http://0.0.0.0:8567](http://0.0.0.0:8567) as well

