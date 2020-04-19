import requests
import os
import sys
import pandas as pd
import json

def get_csv(url: str):
    try:
        df = pd.read_csv(url)
        df = df.fillna(0)
        return df
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

def df_to_json(df):
    output = {}

    for unique_key in df.location.unique():
        
        sub_df = df.loc[df['location'] == unique_key]
        output[unique_key] = sub_df.to_dict('records')

    return json.dumps(output)


def post_json(json_data):
    try:
        url = "http://"+os.getenv("API_HOST")+"/api/v1/"+os.getenv("POST_PATH")
        requests.post(url, json=json_data)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    
    df = get_csv(os.getenv("SOURCE"))
    json_data = df_to_json(df)
    post_json(json_data)