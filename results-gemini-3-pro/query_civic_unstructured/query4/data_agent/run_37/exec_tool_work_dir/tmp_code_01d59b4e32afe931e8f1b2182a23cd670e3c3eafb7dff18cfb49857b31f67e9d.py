code = """import json

# Load data
with open(locals()['var_function-call-7227617260641500172'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-7188498576282706077'], 'r') as f:
    civic_docs = json.load(f)

project_names = [item['Project_Name'] for item in funding_data]
project_names.sort(key=len, reverse=True)

target_tokens = ['spring 2022', '2022-spring', 'march 2022', 'april 2022', 'may 2022', 'spring, 2022']

found_details = {}

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    current_project = None
    
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue
            
        for pname in project_names:
            if pname in line_stripped and len(line_stripped) < len(pname) + 20:
                current_project = pname
                break
        
        if current_project:
            lower_line = line_stripped.lower()
            if 'begin construction' in lower_line or 'start' in lower_line:
                for token in target_tokens:
                    if token in lower_line:
                        found_details[current_project] = line_stripped

print('__RESULT__:')
print(json.dumps(found_details))"""

env_args = {'var_function-call-17279470663678048780': 'file_storage/function-call-17279470663678048780.json', 'var_function-call-7227617260641500172': 'file_storage/function-call-7227617260641500172.json', 'var_function-call-7188498576282706077': 'file_storage/function-call-7188498576282706077.json', 'var_function-call-9111514807247843541': {'count': 10, 'total_funding': 549000, 'projects': ['Marie Canyon Green Streets', 'Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Civic Center Water Treatment Facility Phase 2', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)']}}

exec(code, env_args)
