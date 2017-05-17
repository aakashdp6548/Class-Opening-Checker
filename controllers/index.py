from flask import render_template, request
from app import app
from schedule_api import *
from datetime import datetime
import time
import os
import logging
from apscheduler.schedulers.background import BackgroundScheduler

section_info = {    "term_code": "2160",
                    "school_code": "ENG",
                    "subject_code": "EECS",
                    "catalog_num": "280",
                    "section_type": "LAB"
                }

def get_open_seats(section_list, section_type):
    open_classes = []

    for section in section_list:
        if section["SectionType"] == section_info["section_type"]:
            if section["AvailableSeats"] > 0:
                open_classes.append("Section " + section["SectionNumber"] + ": " + str(section["AvailableSeats"]))


    return open_classes

# def print_open_sections():
#
#     sections = get_sections("2160", "ENG", "EECS", "280")
#     open_sections = get_open_seats(sections, section_info["section_type"])
#
#     if len(open_sections) != 0:
#         print time.strftime("%H:%M:%S")
#         for section in open_sections:
#             print "Section " + str(section) + ": " + str(open_sections[section])
#     else:
#         print time.strftime("%H:%M:%S"), "No open sections found"S

@app.route('/')
def index():

    data = {}

    sections = get_sections(section_info["term_code"], section_info["school_code"], section_info["subject_code"], section_info["catalog_num"])
    open_sections = get_open_seats(sections, section_info["section_type"])
    if len(open_sections) == 0:
        open_sections = ["No open sections found"]

    data["section_info"] = section_info
    data["open_sections"] = open_sections

    return render_template('index.html', **data)
