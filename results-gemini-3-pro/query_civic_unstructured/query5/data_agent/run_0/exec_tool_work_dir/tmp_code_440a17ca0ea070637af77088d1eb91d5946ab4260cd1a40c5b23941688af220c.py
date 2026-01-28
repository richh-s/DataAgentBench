code = """import json
import pandas as pd

f1_path = locals()['var_function-call-1023604252681241279']
with open(f1_path, 'r') as f:
    funding_list = json.load(f)

f2_path = locals()['var_function-call-1023604252681243206']
with open(f2_path, 'r') as f:
    civic_docs = json.load(f)

funding_df = pd.DataFrame(funding_list)
project_funding = {}
for i, row in funding_df.iterrows():
    project_funding[row['Project_Name']] = row['Amount']

known_projects = list(project_funding.keys())

project_details = {}
current_project = None
current_type_context = 'capital'

for doc in civic_docs:
    lines = doc['text'].splitlines()
    for line in lines:
        clean_line = line.strip()
        if not clean_line:
            continue

        if "Disaster Recovery Projects" in clean_line:
            current_type_context = 'disaster'
        elif "Capital Improvement Projects" in clean_line:
            current_type_context = 'capital'
        
        if clean_line in known_projects:
            current_project = clean_line
            p_type = current_type_context
            lower_name = clean_line.lower()
            if "fema" in lower_name or "caloes" in lower_name or "caljpia" in lower_name or "woolsey" in lower_name:
                p_type = 'disaster'
            
            if current_project not in project_details:
                project_details[current_project] = {'type': p_type, 'st': None}
            else:
                if p_type == 'disaster':
                    project_details[current_project]['type'] = 'disaster'
            continue
            
        if current_project:
            lower_line = clean_line.lower()
            if "begin construction" in lower_line or "construction start" in lower_line or "start date" in lower_line:
                found_year = None
                if "2022" in lower_line:
                    found_year = "2022"
                elif "2023" in lower_line:
                    found_year = "2023"
                elif "2021" in lower_line:
                    found_year = "2021"
                
                if found_year:
                    old_st = project_details[current_project]['st']
                    if "begin construction" in lower_line:
                        project_details[current_project]['st'] = found_year
                    elif old_st is None:
                        project_details[current_project]['st'] = found_year

total = 0
matches = []
for p in project_details:
    info = project_details[p]
    if info['type'] == 'disaster' and info['st'] == '2022':
        amt = int(project_funding.get(p, 0))
        total += amt
        matches.append(p)

print("__RESULT__:")
print(json.dumps({"total": total, "matches": matches}))"""

env_args = {'var_function-call-1023604252681241279': 'file_storage/function-call-1023604252681241279.json', 'var_function-call-1023604252681243206': 'file_storage/function-call-1023604252681243206.json'}

exec(code, env_args)
