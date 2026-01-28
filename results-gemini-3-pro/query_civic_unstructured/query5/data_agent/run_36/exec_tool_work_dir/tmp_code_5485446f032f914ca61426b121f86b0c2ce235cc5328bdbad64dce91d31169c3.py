code = """import json
import re

funding_file_path = locals()['var_function-call-7345581642634636200']
civic_docs_file_path = locals()['var_function-call-13795452578231862592']

with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_file_path, 'r') as f:
    civic_docs = json.load(f)

funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}
project_names = list(funding_map.keys())

date_pattern = re.compile(r'(Begin Construction|Advertise|Start Date|Construction started)[:\s]+([A-Za-z0-9,\s]+)', re.IGNORECASE)

potential_misses = []

for doc in civic_docs:
    text = doc['text']
    for proj_name in project_names:
        if proj_name in text:
            idx = text.find(proj_name)
            segment = text[idx:idx+3000]
            
            # Check Start Date 2022
            started_2022 = False
            dates = date_pattern.findall(segment)
            for action, date_str in dates:
                if "2022" in date_str:
                    if any(x in action.lower() for x in ["begin construction", "advertise", "start date", "construction started"]):
                        started_2022 = True
                        break
            
            if started_2022:
                # Check if it was ALREADY classified as disaster
                is_disaster_suffix = any(suffix in proj_name for suffix in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)', '(CalJPIA/FEMA Project)', '(FEMA/CalOES Project)', '(FEMA)'])
                
                if not is_disaster_suffix:
                    potential_misses.append(proj_name)

print("__RESULT__:")
print(json.dumps(list(set(potential_misses))))"""

env_args = {'var_function-call-7345581642634636200': 'file_storage/function-call-7345581642634636200.json', 'var_function-call-13795452578231862592': 'file_storage/function-call-13795452578231862592.json', 'var_function-call-10640987408951217709': {'matched_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Guardrail Replacement Citywide (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Malibu Road Slope Repairs (CalOES Project)', 'Storm Drain Master Plan (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)'], 'total_funding': 1175000}}

exec(code, env_args)
