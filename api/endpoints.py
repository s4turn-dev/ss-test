"""
Due to the fact that both frontend and API utilize Flask, we may 'cheat' a little:
use one Flask() object in client/app.py for serving frontend and simply extend the 
routes list in here with the api endpointsin using the same object.

It is worth noting that in case frontend is written, let's say, using React, API
would need an app=Flask() object of its own. It would also take two different processes
for the frontend framework  and for the backend service to function, in opposition to
a single Python process in the current configuration.
"""
from flask import request as request
import json

from . import app

API_PREFIX = "/api"


@app.get(f"{API_PREFIX}/<user>/requisites/")
def read(user: str):
    return f"GET {user} REQUISITES"

@app.post(f"{API_PREFIX}/<user>/requisites/")
def create(user: str):
    data = json.loads(request.data if request.data else "{}")
    return f"CREATE {user} REQUISITE: {data}"

@app.get(f"{API_PREFIX}/<user>/requisites/edit")
def update(user: str):
    req_id = request.args.get('req_id')
    if req_id is None:
        return "HTTP 400"
    data = json.loads(request.data if request.data else "{}")
    return f"UPDATE {user} REQUISITE #{req_id}: {data}"

@app.get(f"{API_PREFIX}/<user>/requisites/delete")
def delete(user: str):
    req_id = request.args.get('req_id')
    if req_id is None:
        return "HTTP 400"
    return f"DELETE {user} REQUISITE #{req_id}"
