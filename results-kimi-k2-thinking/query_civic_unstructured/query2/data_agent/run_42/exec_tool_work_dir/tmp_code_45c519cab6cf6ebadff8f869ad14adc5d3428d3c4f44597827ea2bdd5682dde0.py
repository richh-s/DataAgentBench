code = """import json

# Load civic docs
docs_file = locals()['var_functions.query_db:8']
docs = json.load(open(docs_file))

# Find park projects completed in 2022
completed_2022 = []

for doc in docs:
    text = doc.get('text','')
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Check for park project name (simple heuristic)
        if 'park' in line.lower() and len(line) < 150:
            # Check if line is not a header
            if 'capital improvement' not in line.lower() and 'disaster recovery' not in line.lower() and 'status report' not in line.lower():
                if not line.startswith('(') and not line.startswith('cid:'):
                    # Look ahead for completion status
                    for j in range(i, min(len(lines), i+8)):
                        next_line = lines[j]
                        if 'completed' in next_line.lower() and '2022' in next_line:
                            completed_2022.append(line)
                            break
        i += 1

# Deduplicate
completed_2022 = list(set(completed_2022))

# Load funding records and match
funding_file = locals()['var_functions.query_db:6']
funding = json.load(open(funding_file))

funding_total = 0

for project in completed_2022:
    for record in funding:
        if record['Project_Name'].find(project) >= 0 or project.find(record['Project_Name']) >= 0:
            funding_total += int(record['Amount'])

result = {'total_funding': funding_total, 'projects_matched': len(completed_2022)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:26': {'potential_docs_with_2022_completion': 5, 'park_projects_in_funding': 20}}

exec(code, env_args)
