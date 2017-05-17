from schedule_api import *

def get_open_seats(section_list, section_type):
    open_classes = {}

    for section in section_list:
        if section["SectionType"] == section_type:
            if section["AvailableSeats"] > 0:
                open_classes[section["SectionNumber"]] = section["AvailableSeats"]

    return open_classes

term_code = "2160"
school_code = "ENG"
subject_code = "EECS"
catalog_num = "280"

sections = get_sections(term_code, school_code, subject_code, catalog_num)
open_sections = get_open_seats(sections, "DIS")

for section in open_sections:
    print section, ": ", open_sections[section]
