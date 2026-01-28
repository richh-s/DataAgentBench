code = """import json, re

# Access the data from storage
funding_data = var_functions.query_db_5 if 'var_functions.query_db_5' in dir() else []
civic_docs_data = var_functions.query_db_2 if 'var_functions.query_db_2' in dir() else []

# Filter for park-related projects in civic docs
park_projects_2022 = []

for doc in civic_docs_data:
    doc_text = doc.get('text', '')
    # Look for park projects completed in 2022 using text patterns
    lines = doc_text.lower()
    if 'park' in lines and '2022' in lines and 'completed' in lines:
        park_projects_2022.append('Found park project completed in 2022')

# Count funding records for park-related projects
park_funding = []
for record in funding_data:
    project_name = record.get('Project_Name', '').lower()
    if 'park' in project_name:
        park_funding.append(int(record.get('Amount', 0)))

total_funding = sum(park_funding)

result = {
    'total_funding': total_funding,
    'park_records_found': len(park_funding)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
