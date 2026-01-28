code = """import json

with open(locals()['var_function-call-15070344879824368496'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-15070344879824368069'], 'r') as f:
    civic_docs = json.load(f)

text = civic_docs[0]['text']
lines = text.split(chr(10))

parsed_names = []
current_project_name = None
last_non_empty_line = ""

for line in lines:
    line = line.strip()
    if not line: continue
    
    is_bullet = line.startswith("(cid:190)") or line.startswith(chr(190))
    if is_bullet:
        is_start = False
        if "Project Description:" in line: is_start = True
        elif "Updates:" in line and "Project Updates" not in line: is_start = True
        
        if is_start:
             if "Page" not in last_non_empty_line and "Agenda Item" not in last_non_empty_line:
                parsed_names.append(last_non_empty_line)
    else:
        last_non_empty_line = line

# Check for keywords in parsed names
fema_parsed = [n for n in parsed_names if "FEMA" in n or "Emergency" in n or "Warning" in n]

# Check for keywords in funding names
fema_funding = [n['Project_Name'] for n in funding_data if "FEMA" in n['Project_Name'] or "Emergency" in n['Project_Name'] or "Warning" in n['Project_Name']]

print("__RESULT__:")
print(json.dumps({
    "parsed_fema_related": fema_parsed,
    "funding_fema_related": fema_funding[:10]
}))"""

env_args = {'var_function-call-18371054564754366390': 'file_storage/function-call-18371054564754366390.json', 'var_function-call-18371054564754362375': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_function-call-15070344879824368496': 'file_storage/function-call-15070344879824368496.json', 'var_function-call-15070344879824368069': 'file_storage/function-call-15070344879824368069.json', 'var_function-call-2633647079085397024': [], 'var_function-call-8767218630817718124': {'parsed_count': 45, 'sample_parsed': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'project and will submit to the County for review.', 'PCH Median Improvements Project', 'or phasing out the project', 'Westward Beach Road Repair Project'], 'funding_count': 500, 'sample_funding': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Annual Street Maintenance', 'Birdview Avenue Improvements']}, 'var_function-call-9458519939930987624': []}

exec(code, env_args)
