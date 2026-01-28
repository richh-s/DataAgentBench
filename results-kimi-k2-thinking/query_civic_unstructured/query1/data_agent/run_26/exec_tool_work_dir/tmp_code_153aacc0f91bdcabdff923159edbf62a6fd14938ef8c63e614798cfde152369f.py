code = """import json

# Use the stored results
funding_file = var_functions.query_db:0
civic_file = var_functions.query_db:2

# Load funding data
funding_data = json.load(open(funding_file, 'r'))

# Load civic docs  
civic_docs = json.load(open(civic_file, 'r'))

# Build funding lookup
funded = {}
for r in funding_data:
    funded[r['Project_Name'].lower()] = int(r['Amount'])

# Extract design projects - simpler approach
design = []
for doc in civic_docs:
    text = doc['text']
    
    # Find design section
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('(Design)')
        if len(parts) > 1:
            design_section = parts[1].split('(Construction)')[0]
            for line in design_section.split('\n'):
                line = line.strip()
                if line and len(line) > 5:
                    if 'Updates:' not in line and 'Project Schedule:' not in line:
                        if 'Page' not in line and 'Capital Improvement' not in line:
                            design.append(line.lower())

# Count projects funded > 50000
count = 0
for p in set(design):
    if p in funded and funded[p] > 50000:
        count += 1

result = count
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:54': 0, 'var_functions.execute_python:72': {'funding': 'var_functions.query_db:0', 'civic': 'var_functions.query_db:2'}}

exec(code, env_args)
