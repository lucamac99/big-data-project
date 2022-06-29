# Big Data Project – UniTn, 2021/22

<!-- ABOUT THE PROJECT -->
## About The Project

The goal of the project is to implement a big data system to support a real estate investor who is considering buying property for short-term rentals in Europe, and direct him or her to choose the area where he or she can buy.

### Built With

The technologies used in the implementation of the project are listed below.

* Plugin per Scraping di cui non ricordo il nome
* [Python](https://nextjs.org/)
* [Docker](https://www.docker.com/)
* [Redis](https://redis.io/)
* [FastAPI](https://fastapi.tiangolo.com/)

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

In order to start the system, you have to first install the dependencies, which are listed below. Then, start the various scripts in the order to follow.

You should always pay attention to the directory inside which you are executing terminal commands.

All dependencies needed to start the project are listed in the requirements.txt file, so simply run the terminal command

```sh
pip install requirements.txt 
```

### Diagram

Da inserire il diagramma del sistema

<!-- USAGE  -->

## Starting the system

First you have to start the Docker yml in order to have a working Redis instance.

```sh
cd redis
docker compose up
```

APIs have been made through FastAPI to make Redis database endpoints available in localhost. Therefore, one would need to start the Uvicorn server to make the endpoints work.

```sh
uvicorn main:app --reload
```

At this point all the elements needed to have the system running are running.
## Usage

For the purposes of this project, the data were collected manually by web scraping and are already collected inside the *scraped.json* file. However, it is possible to implement a data stream processing system, since the Data Storage and Data Preparation scripts are already set up for this.

### Importing data into the database

Make sure you are in the 'redis' folder. Then run the command:

```sh
python3 import_to_redis.py
```

This script imports all the Real Estates records obtained in the scraped.json file into the Redis database.

### Getting the data from the database

Return to root. Then run the command to start the getData script, which performs a retrieve from the database and merges all the JSON records into a CSV file.

```sh
cd ..
python3 getData.py
```

### Data Preparation and Data Cleaning

Two separate scripts perform data preparation and cleaning.

```sh
python3 dataPreparation.py
python3 dataCleaning.py
```
### Data Visualization

The final script performs the generation of the various plots aimed at directing the operator in the choice of purchase.

```sh
python3 dataVisualisation.py
```

<!-- ROADMAP -->
## Roadmap

- [x] Scraping
- [x] Data Collection
- [x] Implementing Redis DB
- [x] Dockerize DB
- [x] Implementing FastAPI and various endpoints
- [x] Implementing Redis UI
- [x] Realizing importing to Redis script
- [x] Script to retrieve data from Redis and converting JSON to CSV
- [x] Implementing data cleaning and preparation scripts
- [x] Implementing data visualization script
- [ ] Web App

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Luca Maccacaro - luca.maccacaro@studenti.unitn.it

Simone Bellavia – simone.bellavia@studenti.unitn.it

Project Link: [https://github.com/lucamac99/big-data-project](https://github.com/lucamac99/big-data-project)

<p align="right">(<a href="#top">back to top</a>)</p>