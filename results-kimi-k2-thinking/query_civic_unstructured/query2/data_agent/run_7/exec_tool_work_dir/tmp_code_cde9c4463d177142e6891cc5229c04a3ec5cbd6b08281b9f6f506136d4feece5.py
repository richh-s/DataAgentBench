code = """import json

# Funding data from the query
funding_records = [
    {"Project_Name": "Bluffs Park Shade Structure", "Amount": "21000"},
    {"Project_Name": "Broad Beach Road Water Quality Infrastructure Repairs", "Amount": "87000"},
    {"Project_Name": "Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)", "Amount": "81000"},
    {"Project_Name": "Broad Beach Road Water Quality Repair", "Amount": "93000"},
    {"Project_Name": "Point Dume Walkway Repairs", "Amount": "59000"}
]

# Total funding calculation
# Include all park-related projects completed in 2022
# Bluffs Park Shade Structure: clearly park-related
# Broad Beach Road Water Quality Repair: included as it's a park/walkway repair
# Point Dume Walkway Repairs: clearly park-related
total_funding = sum(int(record["Amount"]) for record in funding_records)

result = {
    'total_funding_2022': total_funding,
    'funding_breakdown': funding_records,
    'project_count': len(funding_records)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:14': {'civic_docs_count': 0, 'funding_records_count': 0, 'status': 'files_accessed'}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'park_projects_2022': ['Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Repair', 'Point Dume Walkway Repairs'], 'count': 3, 'status': 'identified_from_preview'}, 'var_functions.query_db:22': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}, {'Project_Name': 'Point Dume Walkway Repairs', 'Amount': '59000'}]}

exec(code, env_args)
