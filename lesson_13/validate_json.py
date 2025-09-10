import json
import logging

log_file = "json_Doskoch.log"

logging.basicConfig(filename=log_file, level=logging.ERROR)

files = [
    "ideas_for_test/work_with_json/localizations_en.json",
    "ideas_for_test/work_with_json/localizations_ru.json",
    "ideas_for_test/work_with_json/login.json",
    "ideas_for_test/work_with_json/swagger.json",
]
for file_path in files:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            json.load(f)
    except json.JSONDecodeError:
        logging.error(f"File invalid!, file_path: {file_path}")