code = """import json
import re

# Access data directly using the variable names stored in locals
funding_key = [key for key in locals().keys() if 'query_db:0' in key][0]
civic_key = [key for key in locals().keys() if 'query_db:4' in key][0]

funding_data = locals()[funding_key]
civic_docs_data = locals()[civic_key]

# Find projects with emergency/FEMA in name
matches = []
for record in funding_data:
    name = record['Project_Name'].lower()
    if 'emergency' in name or 'fema' in name:
        matches.append(record)

# Output as JSON
result = json.dumps(matches)
print('RESULT:', result[:100])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
