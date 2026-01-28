code = """import json

# Access variables from storage variable names
civic_docs_storage = 'var_functions.query_db:5'
funding_storage = 'var_functions.query_db:30'

# Load the data files (they're file paths as strings)
with open(locals()[civic_docs_storage]) as f:
    civic_docs = json.load(f)

with open(locals()[funding_storage]) as f:
    funding_over_50k = json.load(f)

# Build funding lookup
funded = {rec['Project_Name']: int(rec['Amount']) for rec in funding_over_50k}

# Find capital design projects
capital_design = set()

for doc in civic_docs:
    txt = doc.get('text', '')
    start_pos = txt.find('Capital Improvement Projects (Design)')
    if start_pos != -1:
        end_pos = txt.find('Capital Improvement Projects (Construction)', start_pos)
        if end_pos == -1:
            section = txt[start_pos:]
        else:
            section = txt[start_pos:end_pos]
        
        # Look for project names
        for line in section.split('\n'):
            clean = line.strip()
            if clean in funded and 'fema' not in clean.lower():
                capital_design.add(clean)

print('__RESULT__:')
print(len(capital_design))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
