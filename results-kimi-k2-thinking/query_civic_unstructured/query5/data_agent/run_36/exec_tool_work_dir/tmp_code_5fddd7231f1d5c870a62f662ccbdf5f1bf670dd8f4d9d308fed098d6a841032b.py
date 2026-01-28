code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print("Funding records loaded:", len(funding_data))

# Count amounts and convert to integers
total_funding = 0
funding_by_project = {}
for record in funding_data:
    amount = int(record['Amount'])
    total_funding += amount
    funding_by_project[record['Project_Name']] = amount

print("Total funding sum:", total_funding)

# Identify disaster-related projects from funding data (by name)
disaster_project_names = []
for record in funding_data:
    project_name = record['Project_Name'].lower()
    # Look for disaster indicators in project name
    if any(keyword in project_name for keyword in ['fema', 'caloes', 'caljpia', 'fire', 'disaster']):
        disaster_project_names.append(record['Project_Name'])

print("Disaster-related projects found in funding data:", len(disaster_project_names))

# Check if any have "2022" in the name
disaster_2022_projects = []
for name in disaster_project_names:
    if '2022' in name:
        disaster_2022_projects.append(name)

print("Disaster projects with 2022 in name:", len(disaster_2022_projects))

# Find all FEMA/disaster projects in funding data
all_disaster_funding = {}
for record in funding_data:
    project_name = record['Project_Name']
    if any(keyword in project_name.lower() for keyword in ['fema', 'caloes', 'caljpia', 'fire']):
        all_disaster_funding[project_name] = int(record['Amount'])

print("All disaster projects in funding:", len(all_disaster_funding))

# Output the data
print("__RESULT__:")
print(json.dumps({
    "total_funding_records": len(funding_data),
    "total_funding_amount": total_funding,
    "disaster_projects_count": len(all_disaster_funding),
    "disaster_projects": list(all_disaster_funding.items())[:20]  # Top 20
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_records': 500, 'sample_records': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:12': {'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
