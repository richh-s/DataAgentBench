code = """import json

# Load funding data (it's stored as a string path)
funding_path = var_functions.query_db_0
if isinstance(funding_path, str):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db_0

# Load civic docs data (it's stored as a string path)  
civic_docs_path = var_functions.query_db_2
if isinstance(civic_docs_path, str):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db_2

# Find disaster-related project names from funding data
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'emergency', 'warning', 'siren']
disaster_funding_records = []

for record in funding_data:
    project_name = record.get('Project_Name', '')
    if any(keyword.lower() in project_name.lower() for keyword in disaster_keywords):
        disaster_funding_records.append(record)

disaster_projects_list = [record['Project_Name'] for record in disaster_funding_records]

print("__RESULT__:")
print(json.dumps({
    "disaster_records_count": len(disaster_funding_records),
    "disaster_projects": disaster_projects_list,
    "total_disaster_funding": sum(int(record.get('Amount', 0)) for record in disaster_funding_records)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': 'file_storage/functions.execute_python:4.json'}

exec(code, env_args)
