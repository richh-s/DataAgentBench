code = """import json

# Load the data files
civic_docs_path = locals()['var_functions.query_db:16']
funding_path = locals()['var_functions.query_db:17']

with open(civic_docs_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_data = json.load(f)

print("Loaded files")

# Simple text search for park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    
    # Look for park mentions with 2022 completion
    if '2022' in text and 'completed' in text.lower() and 'park' in text.lower():
        # Split into lines and look for park project names near completion dates
        lines = text.split('\n')
        for i in range(len(lines)):
            if '2022' in lines[i] and ('completed' in lines[i].lower() or 'completion' in lines[i].lower()):
                # Look at nearby lines for park names
                for j in range(max(0, i-3), min(len(lines), i+3)):
                    line = lines[j].strip()
                    if 'park' in line.lower() and len(line) > 10 and not line.startswith('('):
                        # Clean up the line
                        clean_line = line.replace('•', '').replace('◦', '').strip()
                        if clean_line not in park_projects_2022:
                            park_projects_2022.append(clean_line)

print("Found projects:")
for p in park_projects_2022:
    print("- " + p)

# Match with funding and sum amounts
total_funding = 0

for park in park_projects_2022:
    park_lower = park.lower()
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower()
        # Simple matching
        if park_lower in fund_name or fund_name in park_lower:
            total_funding += int(fund['Amount'])
            break

result = {"total_funding": total_funding}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
