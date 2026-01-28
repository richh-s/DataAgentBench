code = """import json

# Load the funding data (Amount > 50000)
funding_file = open(var_functions.query_db:60)
funding_records = json.load(funding_file)
funding_file.close()

# Load the civic documents
civic_file = open(var_functions.query_db:6)
civic_documents = json.load(civic_file)
civic_file.close()

# Build funding lookup map
funding_by_project = {}
for item in funding_records:
    funding_by_project[item['Project_Name']] = int(item['Amount'])

# Find capital projects with design status
design_capital_names = set()

for doc in civic_documents:
    text = doc.get('text', '')
    # Check for capital improvement projects
    if 'Capital Improvement Projects' in text:
        # Look for design status
        if 'Design' in text:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line and len(line) > 10:
                    # Skip meta lines
                    if any(x in line for x in ['Page', 'Schedule:', 'Updates:']):
                        continue
                    if line.startswith('202') or line.startswith('Item'):
                        continue
                    # Extract project name
                    clean_name = line.replace('•', '').replace('○', '').strip()
                    if len(clean_name) > 8:
                        design_capital_names.add(clean_name)

# Count matches with funding > 50000
match_count = 0

for design_name in design_capital_names:
    d_lower = design_name.lower()
    for funded_name in funding_by_project:
        f_lower = funded_name.lower()
        # Check name similarity (substring match with length threshold)
        if (d_lower in f_lower or f_lower in d_lower):
            if abs(len(design_name) - len(funded_name)) < 40:
                match_count += 1
                break

result = {'count': match_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
