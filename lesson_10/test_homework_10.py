from lesson_10.homework_10 import log_event

import pytest

def test_log_success():
    username = "Oksana"
    status = "success"
    log_event(username=username, status=status)
    with open("login_system.log", "r") as file:
        log_contents = file.read()

    assert f"Login event - Username: {username}, Status: {status}" in log_contents


def test_log_expired():
    username = "Oksana"
    status = "expired"
    log_event(username=username, status=status)
    with open("login_system.log", "r") as file:
        log_contents = file.read()

    assert f"Login event - Username: {username}, Status: {status}" in log_contents

def test_log_failed():
    username = "Oksana"
    status = "failed"
    log_event(username=username, status=status)
    with open("login_system.log", "r") as file:
        log_contents = file.read()

    assert f"Login event - Username: {username}, Status: {status}" in log_contents