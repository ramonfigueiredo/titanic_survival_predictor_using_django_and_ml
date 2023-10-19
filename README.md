![Titanic-sinking](https://github.com/ramonfigueiredo/titanic_survival_predictor_using_django_and_ml/blob/main/images/titanic_image.png)

# Titanic Survival Predictor ML Model 
### Tells whether a passenger (with characteristics as your input) can survive the Titanic drowning or not!

The model and dataset can be found [here](https://github.com/ramonfigueiredo/titanic_survival_predictor_using_django_and_ml/tree/master/model_and_data).
Also check the competetion [Titanic: Machine learning from Disaster](https://www.kaggle.com/c/titanic) on kaggle.


## System Overview
![System overview](https://github.com/ramonfigueiredo/titanic_survival_predictor_using_django_and_ml/blob/main/images/system_overview.jpg)


## Running the system

- Install [Python3](https://www.python.org/downloads/) and [virtualenv](https://virtualenv.pypa.io/en/latest/)

- Create a virtual environment
```
virtualenv titanic_survival_predictor -p python3
```

- Activate the virtual environment
```
source titanic_survival_predictor/bin/activate
```

- Upgrade pip
```
pip install --upgrade pip
```

- Install Python requirements
```
source titanic_survival_predictor/bin/activate
```

- Make migrations

```
python manage.py migrate
```

- Create an admin user and password

```
python manage.py createsuperuser --email admin@example.com --username admin
```

- Run the system
```
cd titanic
python manage.py runserver
```

- Access the Titanic Survival Predictor system using the link below

[http://127.0.0.1:8000](http://127.0.0.1:8000)

Example using the system

- Predicted: Survive

![Titanic API using system - Example will_survive](https://github.com/ramonfigueiredo/titanic_survival_predictor_using_django_and_ml/blob/main/images/titanic_system_input_example_survived.png)

- Predicted: Could not survive

![Titanic API using system - Example could not survive](https://github.com/ramonfigueiredo/titanic_survival_predictor_using_django_and_ml/blob/main/images/titanic_system_input_example_could_not_survive.png)  


- Access the admin page using the link below:

[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

- Access the API to create users and groups using the link below

[http://127.0.0.1:8000/api](http://127.0.0.1:8000/api)

- Access the API to predict Titanic people survival using the link below

POST [http://127.0.0.1:8000/api/predict-titanic-survival](http://127.0.0.1:8000/api/predict-titanic-survival)
```
{
    "pclass": "",
    "sex": "",
    "age": "",
    "sibsp": "",
    "parch": "",
    "fare": "",
    "embC": "",
    "embQ": "",
    "embS": ""
}
```

Example using Postman

- Predicted: Survive

![Titanic API using Postman - Example will_survive](https://github.com/ramonfigueiredo/titanic_survival_predictor_using_django_and_ml/blob/main/images/titanic_api_using_postman_input_example_survived.png)

- Predicted: Could not survive

![Titanic API using Postman - Example could not survive](https://github.com/ramonfigueiredo/titanic_survival_predictor_using_django_and_ml/blob/main/images/titanic_api_using_postman_input_example_could_not_survive.png)  

Example using curl

- Predicted: Survive

```
curl -i -X POST -H "Content-Type: application/json" -d '{"pclass": "1", "sex": "0", "age": "80", "sibsp": "2", "parch": "1", "fare": "6", "embC": "1", "embQ": "0", "embS": "0"}' http://127.0.0.1:8000/api/predict-titanic-survival
```

Output:

``` 
HTTP/1.1 200 OK
Date: Thu, 19 Oct 2023 20:46:40 GMT
Server: WSGIServer/0.2 CPython/3.11.3
Content-Type: application/json
Vary: Accept, Cookie
Allow: POST, OPTIONS
X-Frame-Options: DENY
Content-Length: 79
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

{"error":"0","message":"Successfull","prediction":[0],"confidence_score":100.0}
```

- Predicted: Could not survive

```
curl -i -X POST -H "Content-Type: application/json" -d '{"pclass": "1", "sex": "0", "age": "80", "sibsp": "2", "parch": "1", "fare": "6", "embC": "1", "embQ": "0", "embS": "0"}' http://127.0.0.1:8000/api/predict-titanic-survival
```

Output:

``` 
HTTP/1.1 200 OK
Date: Thu, 19 Oct 2023 20:49:42 GMT
Server: WSGIServer/0.2 CPython/3.11.3
Content-Type: application/json
Vary: Accept, Cookie
Allow: POST, OPTIONS
X-Frame-Options: DENY
Content-Length: 79
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

{"error":"0","message":"Successfull","prediction":[0],"confidence_score":100.0
```

Example using httpie

- Predicted: Survive

```
http http://127.0.0.1:8000/api/predict-titanic-survival pclass=2 sex=1 age=40 sibsp=1 parch=1 fare=40 embC=1 embQ=0 embS=0
```

Output:

```
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 79
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Thu, 19 Oct 2023 22:11:52 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.11.3
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "confidence_score": 100.0,
    "error": "0",
    "message": "Successfull",
    "prediction": [
        1
    ]
}
```

- Predicted: Could not survive

```
http http://127.0.0.1:8000/api/predict-titanic-survival pclass=1 sex=0 age=80 sibsp=2 parch=1 fare=6 embC=1 embQ=0 embS=0
```

Output:

```
HTTP/1.1 405 Method Not Allowed
Allow: POST, OPTIONS
Content-Length: 40
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Thu, 19 Oct 2023 22:06:59 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.11.3
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "detail": "Method \"GET\" not allowed."
}


(titanic_survival_predictor) (base) ramon@Ramons-MacBook-Pro titanic_survival_predictor_using_django_and_ml %   clear
(titanic_survival_predictor) (base) ramon@Ramons-MacBook-Pro titanic_survival_predictor_using_django_and_ml % http http://127.0.0.1:8000/api/predict-titanic-survival pclass=1 sex=0 age=80 sibsp=2 parch=1 fare=6 embC=1 embQ=0 embS=0
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 79
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Thu, 19 Oct 2023 22:09:50 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.11.3
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "confidence_score": 100.0,
    "error": "0",
    "message": "Successfull",
    "prediction": [
        0
    ]
}
```