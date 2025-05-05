from lesson_10.homework_10 import log_event

import pytest

class TestLogEvent:
    def parse_last_log_line(self):
        with open("login_system.log", "r") as file:
            last_line = file.readlines()[-1]

        message_part = last_line.split(" - ")[-1]
        parts = message_part.strip().split(", ")
        username = parts[0].split(": ")[-1]
        status = parts[1].split(": ")[-1]
        return username, status


    def test_log_success(self):
        username = "Oksana"
        status = "success"
        log_event(username=username, status=status)

        actual_username, actual_status = self.parse_last_log_line()

        assert actual_username == username
        assert actual_status == status


    def test_log_expired(self):
        username = "Oksana"
        status = "expired"
        log_event(username=username, status=status)

        actual_username, actual_status = self.parse_last_log_line()

        assert actual_username == username
        assert actual_status == status


    def test_log_failed(self):
        username = "Oksana"
        status = "failed"
        log_event(username=username, status=status)

        actual_username, actual_status = self.parse_last_log_line()

        assert actual_username == username
        assert actual_status == status