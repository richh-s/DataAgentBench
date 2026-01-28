code = """import json
import pandas as pd

# Load data
funding_path = locals()['var_functions.query_db:4']
civic_path = locals()['var_functions.query_db:5']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Process funding data
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Process civic documents to find completed 2022 park projects
completed_2022_parks = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for completion statements in 2022
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for completion with 2022
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            # Look backwards for project name (up to 5 lines)
            for j in range(i-1, max(0, i-6), -1):
                prev_line = lines[j].strip()
                # Skip metadata lines
                if (prev_line and len(prev_line) > 10 and 
                    not any(skip in prev_line.lower() for skip in 
                           ['project schedule', 'project description', 'updates:', 
                            'to:', 'from:', 'subject:', 'date:', 'prepared by:', 
                            'approved by:']) and
n                    not prev_line.startswith('(') and
                    not prev_line.startswith('•') and
                    not prev_line.startswith('●')):
                    
                    # Check if it's park-related
                    if any(keyword in prev_line.lower() for keyword in ['park', 'playground', 'bluff']):
                        completed_2022_parks.append(prev_line)
                        break
        
        # Also check for construction completed statements
        if 'construction was completed' in line.lower() and '2022' in line:
            for j in range(i-1, max(0, i-6), -1):
                prev_line = lines[j].strip()
                if (prev_line and len(prev_line) > 10 and 
                    not any(skip in prev_line.lower() for skip in 
                           ['project schedule', 'project description', 'updates:'])):
                    
                    if any(keyword in prev_line.lower() for keyword in ['park', 'playground', 'bluff']):
                        completed_2022_parks.append(prev_line)
                        break
        
        i += 1

# Remove duplicates
completed_2022_parks = list(set(completed_2022_parks))

print('__RESULT__:')
print(json.dumps({
    'completed_2022_park_projects': completed_2022_parks,
    'count': len(completed_2022_parks)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_documents': 5, 'park_projects_found': 21, 'total_park_funding': 1123000, 'completed_2022_projects_raw': 2}}

exec(code, env_args)
