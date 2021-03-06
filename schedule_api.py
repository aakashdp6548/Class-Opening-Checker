import json
import time
import requests

class ScheduleApiError(Exception):
    pass

# The base API endpoint
base_url = 'http://umich-schedule-api.herokuapp.com/v4'

# the amount of time to wait for the schedule API
timeout_duration = 25

def get_data(relative_path):
    
    timeout_at = time.time() + timeout_duration

    while time.time() < timeout_at:
        r = requests.get(base_url + relative_path)
        if r.status_code == 200:
            return json.loads(r.text)
        if r.status_code == 400:
            break

    raise ScheduleApiError('error for url: {0} message: "{1}" code: {2}' \
        .format(relative_path, r.text, r.status_code))

def get_sections(TermCode, SchoolCode, SubjectCode, CatalogNumber):

    return get_data('/get_sections?term_code=' + TermCode + '&school=' + SchoolCode + '&subject='
     + SubjectCode + '&catalog_num=' + CatalogNumber)
