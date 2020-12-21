# Workshop system

The system for collecting information necessary to build a personal learning path

- Collects information on the current requirements of employers and the responsibilities of applicants
- Helps to find activities related to the current educational program

# Setup

1. Database is a PostgreSQL setup using docker

```shell
docker run -d --name workshop-system -p5432:5432 -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=workshop-system postgres
```

2. Selenium webdriver requires Google Chrome installation


