import logging
import xml.etree.ElementTree as ET

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def find_incoming_by_group_number(file_path, target_number):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for group in root.findall("group"):
            number = group.find("number")
            incoming = group.find("timingExbytes/incoming")

            if number is not None and incoming is not None:
                if number.text == target_number:
                    logger.info(f"Found! Number: {target_number}, incoming = {incoming.text}")
                    return

        logger.info(f"Nothing found for group/number = {target_number}")

    except Exception as e:
        logger.error(f"Error: {e}")


find_incoming_by_group_number("ideas_for_test/work_with_xml/groups.xml", "4")