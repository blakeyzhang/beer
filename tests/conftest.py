# -*- encoding: utf-8 -*-
"""
@File    :   conftest.py
@Time    :   2023/03/10 17:04:54
@Author  :   blakeyzhang
@Version :   1.0
@Desc    :   None
"""
import pytest
from beer import Beer


@pytest.fixture
def app():
    return Beer()


@pytest.fixture
def client(app):
    return app.test_session()
