code = """import json, re

# Load data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding map
funding_map = {}
for r in funding_data:
    amt = int(r['Amount'])
    if amt > 50000:
        funding_map[r['Project_Name']] = amt

# Find design projects
design_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    # Look for design section
    design_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)Capital Improvement Projects', text, re.DOTALL)
    if design_match:
        design_text = design_match.group(1)
        
        # Find all project names in this section
        # Look for title lines followed by updates
        lines = design_text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if len(line) > 10 and line[0].isupper():
                # Check if this is likely a project name
                if any(word in line for word in ['Project', 'Improvements', 'Repair', 'Replacement', 'Road', 'Park', 'Drainage', 'Bridge']):
                    # Check if funded and >50k
                    if line in funding_map:
                        design_projects.add(line)
                    else:
                        # Check for variations
                        for funded in funding_map:
                            if funded.startswith(line) or line.startswith(funded.split(' (')[0]):
                                design_projects.add(funded)
                                break

print('__RESULT__:')
print(json.dumps({'count': len(design_projects)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)
