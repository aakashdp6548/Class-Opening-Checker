from schedule_api import *
from datetime import datetime
import time
import os
import logging
import sys
from termcolor import cprint, colored
from apscheduler.schedulers.background import BackgroundScheduler

section_info = {    "term_code": "2160",
                    "school_code": "ENG",
                    "subject_code": "EECS",
                    "catalog_num": "280",
                    "section_type": "a"
                }

def get_open_seats(section_list, section_type):
    open_classes = {}

    for section in section_list:
        if section_info["section_type"] == "a":
            if section["AvailableSeats"] > 0:
                open_classes[section["SectionNumber"]] = section["AvailableSeats"]

        elif section["SectionType"] == section_info["section_type"]:
            if section["AvailableSeats"] > 0:
                open_classes[section["SectionNumber"]] = section["AvailableSeats"]

    return open_classes

def print_open_sections():

    sections = get_sections("2160", "ENG", "EECS", "280")
    open_sections = get_open_seats(sections, section_info["section_type"])

    if len(open_sections) != 0:
        print time.strftime("%H:%M:%S")
        for section in open_sections:
            print "Section " + str(section) + ": " + str(open_sections[section])
    else:
        print time.strftime("%H:%M:%S"), "No open sections found"

if __name__ == '__main__':

    print "Checking openings for %s %s %s %s (%s)" % ( section_info["term_code"], section_info["school_code"], section_info["subject_code"], section_info["catalog_num"], section_info["section_type"] )
    logging.basicConfig()
    scheduler = BackgroundScheduler()
    scheduler.add_job(print_open_sections, 'interval', hours=2)
    scheduler.start()

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
