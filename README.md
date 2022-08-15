# Daily Cat Facts Project


## Requirements
Python version: 3.10.5, 
API framework: FastAPI


## Instructions to run the project


#### 1. Clone gitHub project
https://github.com/enriqueparrac/daily_cat_facts.git

cd /daily_cat_facts


#### 2. Create a virtual environment in python
python -m venv environmentName


#### 3. Download the project libraries
pip install -r requirements.txt


### 4. Run the server with
uvicorn main:app --reload


### 5. Type the following URL in the browser
http://127.0.0.1:8000/cat-facts/3


### 6. The API will return a JSON, example:
[
   {
      "status":{
         "verified":null,
         "sentCount":0
      },
      "_id":"624c880e6674929831649f28",
      "user":"624c87b46674929831649f05",
      "text":"Testing.",
      "type":"cat",
      "deleted":false,
      "createdAt":"2022-04-05T18:18:54.640Z",
      "updatedAt":"2022-04-05T18:18:54.640Z",
      "__v":0
   },
   {
      "status":{
         "verified":null,
         "sentCount":0
      },
      "_id":"626c9bad41f4aa428ac223fb",
      "user":"6263383cf782346dbf665fb1",
      "text":"Любой текст.",
      "type":"cat",
      "deleted":false,
      "createdAt":"2022-04-30T02:15:09.229Z",
      "updatedAt":"2022-04-30T02:15:09.229Z",
      "__v":0
   },
   {
      "status":{
         "verified":null,
         "sentCount":0
      },
      "_id":"626ed12e922f2d4faf10a32b",
      "user":"626c19be41f4aa428ac1a540",
      "text":"I.",
      "type":"cat",
      "deleted":false,
      "createdAt":"2022-05-01T18:27:58.882Z",
      "updatedAt":"2022-05-01T18:27:58.882Z",
      "__v":0
   },
   {
      "status":{
         "verified":null,
         "sentCount":0
      },
      "_id":"62ea72469646e4ec1ee93f43",
      "user":"61b8566766b26cede617b4ef",
      "text":"Cat is so weird.",
      "type":"cat",
      "deleted":false,
      "createdAt":"2022-08-03T13:04:06.763Z",
      "updatedAt":"2022-08-03T13:04:06.763Z",
      "__v":0
   }
]


### 7. Run the tests with
pytest


### 8. Run the tests with
The diagram.pptx file explains the developed API
