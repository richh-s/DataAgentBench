code = """import json
import re

# Load data
with open(locals()['var_function-call-7842478251555825910'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-7842478251555825611'], 'r') as f:
    funding_data = json.load(f)

funding_names = set(item['Project_Name'] for item in funding_data)

full_text = "\\n".join([d['text'] for d in civic_docs])

lines = full_text.split('\\n')
current_project = None
project_texts = {}

# Identify project sections
for line in lines:
    clean_line = line.strip()
    if clean_line in funding_names:
        current_project = clean_line
        if current_project not in project_texts:
            project_texts[current_project] = ""
    elif current_project:
        project_texts[current_project] += "\\n" + clean_line

disaster_projects_2022 = []

for pname, text in project_texts.items():
    # Check start date
    # Regex needs double escaping for JSON: \\s -> \\\\s
    start_matches = re.findall(r"Begin Construction[:\\s]+([A-Za-z0-9\\s]+)", text, re.IGNORECASE)
    
    started_2022 = False
    for date_str in start_matches:
        if "2022" in date_str:
            started_2022 = True
            break
            
    if not started_2022:
        start_matches_2 = re.findall(r"Start(?:ed|s|ing)?[:\\s]+([A-Za-z0-9\\s]+)", text, re.IGNORECASE)
        for date_str in start_matches_2:
            if "2022" in date_str:
                started_2022 = True
                break
    
    # Check disaster
    is_disaster = False
    if any(x in pname for x in ["FEMA", "CalOES", "CalJPIA", "Disaster", "Recovery"]):
        is_disaster = True
    if not is_disaster:
        if re.search(r"(FEMA|CalOES|CalJPIA|Woolsey|Disaster|Recovery|Emergency)", text, re.IGNORECASE):
            is_disaster = True
            
    if started_2022 and is_disaster:
        disaster_projects_2022.append(pname)

# Sum funding
processed_funding_ids = set()
final_funding_amount = 0
matched_records = []

for target_pname in disaster_projects_2022:
    for record in funding_data:
        r_pname = record['Project_Name']
        match = False
        if r_pname == target_pname:
            match = True
        elif r_pname.startswith(target_pname + " ("):
            match = True
            
        if match:
            if record['Funding_ID'] not in processed_funding_ids:
                final_funding_amount += int(record['Amount'])
                processed_funding_ids.add(record['Funding_ID'])
                matched_records.append(r_pname)

print("__RESULT__:")
print(json.dumps({"total_funding": final_funding_amount, "projects": disaster_projects_2022, "records": matched_records}))"""

env_args = {'var_function-call-7842478251555825910': 'file_storage/function-call-7842478251555825910.json', 'var_function-call-7842478251555825611': 'file_storage/function-call-7842478251555825611.json'}

exec(code, env_args)
