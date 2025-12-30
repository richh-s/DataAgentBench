code = """import json
import re

civic_path = locals()['var_function-call-15640139870961922644']
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

def parse(text):
    lines = text.splitlines()
    found = []
    for line in lines:
        if "Construction" in line and "2022" in line:
            found.append(line)
    return found

res = []
for doc in civic_data:
    res.extend(parse(doc['text']))
    
print("__RESULT__:")
print(json.dumps(res[:20]))"""

env_args = {'var_function-call-15640139870961926103': 'file_storage/function-call-15640139870961926103.json', 'var_function-call-15640139870961922644': 'file_storage/function-call-15640139870961922644.json', 'var_function-call-4280233803932826645': {'total_funding': 91000.0, 'matched_projects': [{'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'amount': 91000.0}], 'missing_projects': []}, 'var_function-call-15849578272413360394': 'file_storage/function-call-15849578272413360394.json', 'var_function-call-2056573886096391775': [{'name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'mentions': [' It is anticipated that the final design will be complete by February 2022', ' The project will be advertised for construction bids with construction beginning in April 2022']}, {'name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'mentions': ['(cid:190) Updates: (cid:131) The project design will commence during the Spring 2022']}, {'name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'mentions': [' It is anticipated that the final design will be complete by July 2022', ' The project will be advertised for construction bids with construction beginning in Fall 2022', ' (cid:190) Estimated Schedule: (cid:131) Complete Design: July 2022']}, {'name': 'Storm Drain Master Plan (FEMA Project)', 'mentions': [' (cid:190) Estimated Schedule: (cid:131) Completion Date: Spring 2022 Page 6 of 6 Agenda Item # 4']}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'mentions': [' (cid:190) Project Schedule (cid:131) Complete Design: April 2022 (cid:131) Advertise: Spring 2022 (cid:131) Begin Construction: Spring 2022 Page 5 of 8 Agenda Item # 4']}, {'name': 'damaged by the Woolsey Fire.', 'mentions': [' It is anticipated that the final design will be complete by March 2022', ' project will be advertised for construction bids with construction beginning in Spring 2022']}, {'name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'mentions': ['(cid:190) Updates: (cid:131) The project design has begun and preliminary design should be completed by Spring 2022']}, {'name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'mentions': [' It is anticipated that the final design will be complete by July 2022', ' The project will be advertised for construction bids with construction beginning in Fall 2022', ' (cid:190) Estimated Schedule: (cid:131) Complete Design: July 2022']}, {'name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'mentions': [' (cid:131) The Kickoff meeting for the Steering Committee was held on March 17, 2022']}, {'name': 'Birdview Avenue Improvements (CalOES Project)', 'mentions': [' The project was accepted by the Council on January 24, 2022 in Page 8 of 8 Agenda Item # 4']}], 'var_function-call-2641073418365439178': {'total': 0, 'found_projects': [], 'not_found': []}}

exec(code, env_args)
