code = """import json
import re

# Load data
funding_path = locals()['var_function-call-15640139870961926103']
civic_path = locals()['var_function-call-15640139870961922644']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

projects_to_check = [
    "Clover Heights Storm Drain (FEMA Project)",
    "Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)",
    "Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)",
    "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)",
    "Westward Beach Road Shoulder Repairs (CalOES Project)",
    "Encinal Canyon Road Drainage Improvements (CalOES Project)"
]

def check_snippet(text, p_names):
    res = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        for name in p_names:
            if name in line:
                # Get next 10 lines
                snippet = " ".join(lines[i:i+15])
                res.append({'name': name, 'snippet': snippet})
    return res

results = []
for doc in civic_data:
    results.extend(check_snippet(doc['text'], projects_to_check))

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15640139870961926103': 'file_storage/function-call-15640139870961926103.json', 'var_function-call-15640139870961922644': 'file_storage/function-call-15640139870961922644.json', 'var_function-call-4280233803932826645': {'total_funding': 91000.0, 'matched_projects': [{'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'amount': 91000.0}], 'missing_projects': []}, 'var_function-call-15849578272413360394': 'file_storage/function-call-15849578272413360394.json', 'var_function-call-2056573886096391775': [{'name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'mentions': [' It is anticipated that the final design will be complete by February 2022', ' The project will be advertised for construction bids with construction beginning in April 2022']}, {'name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'mentions': ['(cid:190) Updates: (cid:131) The project design will commence during the Spring 2022']}, {'name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'mentions': [' It is anticipated that the final design will be complete by July 2022', ' The project will be advertised for construction bids with construction beginning in Fall 2022', ' (cid:190) Estimated Schedule: (cid:131) Complete Design: July 2022']}, {'name': 'Storm Drain Master Plan (FEMA Project)', 'mentions': [' (cid:190) Estimated Schedule: (cid:131) Completion Date: Spring 2022 Page 6 of 6 Agenda Item # 4']}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'mentions': [' (cid:190) Project Schedule (cid:131) Complete Design: April 2022 (cid:131) Advertise: Spring 2022 (cid:131) Begin Construction: Spring 2022 Page 5 of 8 Agenda Item # 4']}, {'name': 'damaged by the Woolsey Fire.', 'mentions': [' It is anticipated that the final design will be complete by March 2022', ' project will be advertised for construction bids with construction beginning in Spring 2022']}, {'name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'mentions': ['(cid:190) Updates: (cid:131) The project design has begun and preliminary design should be completed by Spring 2022']}, {'name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'mentions': [' It is anticipated that the final design will be complete by July 2022', ' The project will be advertised for construction bids with construction beginning in Fall 2022', ' (cid:190) Estimated Schedule: (cid:131) Complete Design: July 2022']}, {'name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'mentions': [' (cid:131) The Kickoff meeting for the Steering Committee was held on March 17, 2022']}, {'name': 'Birdview Avenue Improvements (CalOES Project)', 'mentions': [' The project was accepted by the Council on January 24, 2022 in Page 8 of 8 Agenda Item # 4']}], 'var_function-call-2641073418365439178': {'total': 0, 'found_projects': [], 'not_found': []}, 'var_function-call-3790710361129771328': ['(cid:190) Updates: Construction was completed November 2022. Notice of completion', '(cid:131) Construction was completed, November 2022', '(cid:131) Construction was completed, November 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring/Summer 2022', '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', '(cid:131) Begin Construction: Summer/Winter 2022', '(cid:131) Begin Construction: Fall 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: April 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: April 2022', '(cid:131) Begin Construction: Fall 2022', '(cid:131) Begin Construction: Fall 2022', '(cid:131) Begin Construction: March 2022', '(cid:131) Begin Construction: Summer 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022'], 'var_function-call-16088723962090965018': {'total': 87000.0, 'matched': ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)'], 'missing': ['facilities and roadway embankments that were damaged by the Woolsey Fire.', 'that was damaged by the Woolsey Fire.'], 'details': [{'name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'type': 'disaster', 'line': '(cid:131) Begin Construction: Summer 2022'}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'type': 'disaster', 'line': '(cid:131) Begin Construction: Summer 2022'}, {'name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'type': 'disaster', 'line': '(cid:131) The project design will commence during the Spring 2022.'}, {'name': 'that was damaged by the Woolsey Fire.', 'type': 'disaster', 'line': '(cid:131) Begin Construction: Spring 2022'}]}, 'var_function-call-11317362019623661218': {'total': 327000.0, 'matched': [{'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'amount': 91000.0}, {'name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'amount': 77000.0}, {'name': 'Clover Heights Storm Drain (FEMA Project)', 'amount': 21000.0}, {'name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'amount': 44000.0}, {'name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'amount': 94000.0}], 'missing': ['facilities and roadway embankments that were damaged by the Woolsey Fire.', 'damaged by the Woolsey Fire.']}}

exec(code, env_args)
