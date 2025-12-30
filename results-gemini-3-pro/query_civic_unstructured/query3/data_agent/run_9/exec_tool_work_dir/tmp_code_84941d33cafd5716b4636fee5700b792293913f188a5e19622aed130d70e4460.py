code = """import json

try:
    with open(locals()['var_function-call-2491706478099471168'], 'r') as f:
        civic_docs = json.load(f)
except:
    civic_docs = []

text = civic_docs[0]['text']
lines = [l.strip() for l in text.splitlines()]

debug_projects = []
current_status = "Unknown"
i = 0
while i < len(lines):
    line = lines[i]
    if "Capital Improvement Projects (Design)" in line:
        current_status = "Design"
    elif "Capital Improvement Projects (Construction)" in line:
        current_status = "Construction"
    elif "Capital Improvement Projects (Not Started)" in line:
        current_status = "Not Started"
    
    is_project = False
    if i + 1 < len(lines):
        next_line = lines[i+1]
        # Check leniently
        if "Updates:" in next_line:
            is_project = True
    
    if is_project and line:
        debug_projects.append({"name": line, "status": current_status, "next_line": lines[i+1]})
        i += 1
    else:
        i += 1

print("__RESULT__:")
print(json.dumps(debug_projects))"""

env_args = {'var_function-call-247840188859049492': ['civic_docs'], 'var_function-call-247840188859048797': ['Funding'], 'var_function-call-5543153819745217051': 'file_storage/function-call-5543153819745217051.json', 'var_function-call-5543153819745218422': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-2491706478099471168': 'file_storage/function-call-2491706478099471168.json', 'var_function-call-148111800493069151': 'file_storage/function-call-148111800493069151.json', 'var_function-call-9464340337520931465': [{'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000', 'Status': 'not started'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000', 'Status': 'not started'}], 'var_function-call-144355590160047694': []}

exec(code, env_args)
