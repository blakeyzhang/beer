# -*- encoding: utf-8 -*-
"""
@File    :   test_beer.py
@Time    :   2023/03/10 16:30:51
@Author  :   blakeyzhang
@Version :   1.0
@Desc    :   None
"""

import pytest
from beer import Beer


def test_beer_test_client_can_send_requests(app, client):
    RESPONSE_TEXT = "THIS IS COOL"

    @app.route("/hey")
    def cool(req, resp):
        resp.text = RESPONSE_TEXT

    assert client.get("http://testserver/hey").text == RESPONSE_TEXT


def test_parameterized_route(app, client):
    @app.route("/{name}")
    def hello(req, resp, name):
        resp.text = f"hey, {name}"

    assert client.get("http://testserver/matthew").text == "hey, matthew"
    assert client.get("http://testserver/ashley").text == "hey, ashley"


def test_default_404_response(client):
    response = client.get("http://testserver/doesnotexist")

    assert response.status_code == 404
    assert response.text == "Not Found"


def test_alternative_route(app, client):
    response_text = "Alternative way to add a route"

    def home(req, resp):
        resp.text = response_text

    app.add_route("/alternative", home)

    assert client.get("http://testserver/alternative").text == response_text
