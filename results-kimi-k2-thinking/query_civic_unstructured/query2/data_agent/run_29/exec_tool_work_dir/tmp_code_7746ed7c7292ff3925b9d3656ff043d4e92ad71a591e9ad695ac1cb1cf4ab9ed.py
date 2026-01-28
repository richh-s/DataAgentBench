code = """import json

# Get the data from the storage variables
civic_docs = locals()['var_functions.query_db:2']
funding_data = locals()['var_functions.query_db:16']

# Process civic documents to find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    if isinstance(doc, dict):
        text = doc.get('text', '')
    else:
        text = str(doc)
    
    lines = text.split(chr(10))
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check for park-related project names
        if 'park' in line.lower() or 'playground' in line.lower():
            # Look ahead for completion in 2022
            for j in range(i, min(i+10, len(lines))):
                check_line = lines[j]
                if 'completed' in check_line.lower() and '2022' in check_line:
                    park_projects_2022.append(line)
                    break

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Match with funding data
funding_total = 0
for park_proj in park_projects_2022:
    park_lower = park_proj.lower()
    for fund in funding_data:
        fund_name = fund['Project_Name']
        fund_lower = fund_name.lower()
        if park_lower in fund_lower or fund_lower in park_lower:
            funding_total += int(fund['Amount'])

result = {
    'total_funding': funding_total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:30': [], 'var_functions.execute_python:34': {'civic_docs_count': 38, 'funding_records_count': 39, 'sample_civic_doc': 'f'}}

exec(code, env_args)
