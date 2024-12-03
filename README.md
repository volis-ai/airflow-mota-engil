# Mota-Engil Airflow

This project contains data pipelines to be runned with Apache Airflow in the
Mota-Engil's server.

## Running Airflow

Follow these instructions to run Apache Airflow locally. If you feel stuck, take
a look at the [official documentation](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).

- Build the Docker image:

    ```sh
    docker build -t volis-airflow:custom . --no-cache
    ```

- Run `mkdir logs`.

- Create the config files, copying `.env.sample`, `configs/variables.yaml.sample`
and `configs/connections.yaml.sample` files and filling any field needed there.

- Set `AIRFLOW_UID` to the value returned from `id -u`.

- Copy any required credential files to `credentials/` folder.

  - To GCP credentials, you should save the service account credential file with
  the name `gcp.json`.

- Start the Airflow services:

    ```sh
    docker compose up
    ```

- Access the Airflow web interface:

    Open your browser and go to `http://localhost:8080`. Use the following credentials to log in:
    - **Username:** airflow
    - **Password:** airflow

### Stopping the Services

To stop the Airflow services, run:

```sh
docker compose down
```
