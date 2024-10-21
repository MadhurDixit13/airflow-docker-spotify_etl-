# Spotify ETL Pipeline with Apache Airflow

This project builds an ETL (Extract, Transform, Load) pipeline using Apache Airflow and Spotify's API. The pipeline fetches recently played tracks of a user from the Spotify API and stores them in a MySQL database.

## Table of Contents
- [Spotify ETL Pipeline with Apache Airflow](#spotify-etl-pipeline-with-apache-airflow)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Requirements](#requirements)
    - [Python Libraries](#python-libraries)
  - [Installation](#installation)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Set up Docker and Airflow](#2-set-up-docker-and-airflow)
    - [3. Set Up Airflow and MySQL with Docker](#3-set-up-airflow-and-mysql-with-docker)
    - [4. Add Spotify API Credentials in Airflow Variables](#4-add-spotify-api-credentials-in-airflow-variables)
    - [Set Up Database Connection in Airflow](#set-up-database-connection-in-airflow)
    - [6. Install Python Dependencies](#6-install-python-dependencies)
  - [DAG Schedule](#dag-schedule)
  - [Usage](#usage)
    - [Verifying Data in MySQL](#verifying-data-in-mysql)
  - [Contributing](#contributing)
  - [License](#license)
  - [References](#references)

## Project Overview
The Spotify ETL pipeline uses Airflow to periodically retrieve a user's recently played tracks and stores them in a MySQL database. It consists of three main tasks:
1. Exchanging the Spotify API authorization code for an access token.
2. Refreshing the access token using the refresh token.
3. Fetching recently played tracks and storing them in a MySQL table.

## Features
- **Spotify API Integration**: Automatically retrieves recently played songs.
- **ETL Pipeline**: Uses Airflow for task scheduling and managing data workflows.
- **MySQL Database**: Stores song data like track names, artists, and timestamps.
- **Automatic Token Refresh**: Refreshes the Spotify API access token using Airflow Variables.

## Requirements
The following software is required to run the project:
- Docker
- Docker Compose
- Apache Airflow
- MySQL
- Python 3.x
- Spotify API credentials

### Python Libraries
The required Python libraries are managed inside Airflow. Ensure the following are installed in your Airflow environment:
- `pandas`
- `sqlalchemy`
- `requests`
- `tabulate`
- `pytz`
- `mysql-connector-python`
- `apache-airflow`

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/spotify-etl.git
cd spotify-etl
```

### 2. Set up Docker and Airflow

Make sure Docker and Docker Compose are installed on your system.

### 3. Set Up Airflow and MySQL with Docker

Use the docker-compose.yml file to set up Apache Airflow and MySQL:

```bash
docker-compose up -d
```

### 4. Add Spotify API Credentials in Airflow Variables

In the Airflow web interface, go to Admin > Variables and add the following keys:

- **spotify_redirect_uri**: The Spotify redirect URI.
- **spotify_auth_code**: Your Spotify authorization code.
- **spotify_access_token**: (Leave empty; it will be set automatically).
- **spotify_refresh_token**: (Leave empty; it will be set automatically).

### Set Up Database Connection in Airflow

In the Airflow web interface, go to Admin > Connections and create a MySQL connection:
Conn ID: my_db
Conn Type: MySQL
Host: mysql
Schema: airflow
Login: airflow
Password: airflow
Port: 3306

### 6. Install Python Dependencies

Make sure all required Python libraries are installed in your Airflow environment.

Airflow DAG Overview
The DAG is defined in spotify_etl.py and consists of three tasks:

- Exchange Token (_exchange_token): Exchanges the authorization code for an access token.
- Refresh Token (_refresh_token): Refreshes the access token using the refresh token.
- Get Recently Played Tracks (_get_recently_played_tracks): Fetches the last 24 hours of recently played tracks from Spotify and loads them into a MySQL table.

## DAG Schedule

The DAG is scheduled to run every day at 12:10 AM (Eastern Time). You can modify the schedule using the schedule_interval parameter in the DAG definition.

## Usage

Running the DAG
Start the Airflow scheduler and web server:
```bash
docker-compose up -d
```

- Access the Airflow UI at http://localhost:8080.
- Trigger the spotify_dag from the UI.
### Verifying Data in MySQL

- To verify that the data is stored in the MySQL database, run the following query:

```bash
USE airflow;
SELECT * FROM my_played_tracks;
```
You should see the recently played tracks with details like song name, artist, and the timestamp when it was played.

## Contributing
Feel free to submit issues and pull requests for improvements. Follow these steps for contributing:

- Fork the project.
- Create a new feature branch (git checkout -b feature/your-feature).
- Commit your changes (git commit -am 'Add new feature').
- Push the branch (git push origin feature/your-feature).
- Create a new Pull Request.
  
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## References
- [Building an ETL Pipeline with Airflow & Spotify](https://medium.com/apache-airflow/building-etl-pipeline-with-airflow-spotify-d1bccb2f4d13)
- [How to Create a Spotify App and Generate Auth Keys and Tokens for API Consumption](https://medium.com/@mihirs202/how-to-create-a-spotify-app-and-generate-auth-keys-and-tokens-for-api-consumption-72078f4a8b83)
