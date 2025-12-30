code = """import json

# Load data
with open(locals()['var_function-call-15070344879824368496'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-15070344879824368069'], 'r') as f:
    civic_docs = json.load(f)

text = civic_docs[0]['text']
lines = text.split(chr(10))

parsed_names = []
parsed_projects = {}
current_project_name = None
last_non_empty_line = ""
current_section_status = "design"

for line in lines:
    line = line.strip()
    if not line:
        continue

    # Headers check
    if "Capital Improvement Projects" in line:
        current_project_name = None
        continue
    
    is_bullet = line.startswith("(cid:190)") or line.startswith(chr(190))
    
    if is_bullet:
        if current_project_name != last_non_empty_line:
             if "Page" not in last_non_empty_line and "Agenda Item" not in last_non_empty_line:
                current_project_name = last_non_empty_line
                parsed_names.append(current_project_name)
    else:
        last_non_empty_line = line

print("__RESULT__:")
print(json.dumps({
    "parsed_count": len(parsed_names),
    "sample_parsed": parsed_names[:5],
    "funding_count": len(funding_data),
    "sample_funding": [f['Project_Name'] for f in funding_data[:5]]
}))"""

env_args = {'var_function-call-18371054564754366390': 'file_storage/function-call-18371054564754366390.json', 'var_function-call-18371054564754362375': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_function-call-15070344879824368496': 'file_storage/function-call-15070344879824368496.json', 'var_function-call-15070344879824368069': 'file_storage/function-call-15070344879824368069.json', 'var_function-call-2633647079085397024': []}

exec(code, env_args)
