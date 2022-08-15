from fastapi import FastAPI
import requests
from datetime import (
    date,
    datetime,
)


app = FastAPI()


@app.get("/")
def read_root():
    return {"Coding Challenge Bankaya"}


@app.get("/cat-facts/{number_records}")
def read_api(number_records: int):
    if number_records in range(1, 501):
        url = "https://cat-fact.herokuapp.com"
        endpoint = "/facts/random"
        parameters = "?animal_type=cat"
        parameters += "&amount=%s" % number_records

        api_response = requests.get(url + endpoint + parameters)
        api_response_json = api_response.json()

        api_response_list = []
        if number_records == 1:
            api_response_list.append(api_response_json)
        else:
            api_response_list = api_response_json

        json_cats = []
        current_year = date.today().year
        for record in api_response_list:
            updated_date = record["updatedAt"]
            #updated_year = datetime.strptime(updated_date[:10], "%Y-%m-%d").date().year
            updated_year = int(updated_date[:4])
            if updated_year == current_year:
                json_cats.append(record)

        return json_cats
    else:
        message = {"Number_records must be between 1 and 500"}
        return message
