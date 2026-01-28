code = """import json
import re

mongo_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_recs = json.load(f)

park_projects = []

for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
            
        # Clean line
        clean_line = re.sub(r'^[•\-●■\s]+', '', line)
        
        # Skip headers
        header_words = ['Page', 'Agenda', 'To:', 'Prepared', 'Approved', 'Subject:', 'RECOMMENDED', 'DISCUSSION:', 'Date', 'Meeting', 'Public', 'Commission', 'Capital', '(cid:']
        is_header = any(clean_line.startswith(word) for word in header_words)
        
        if is_header or len(clean_line) < 5 or len(clean_line) > 200:
            continue
            
        clean_line_lower = clean_line.lower()
        
        # Check for park projects completed in 2022
        if 'park' in clean_line_lower:
            for j in range(i+1, min(i+12, len(lines))):
                next_line_lower = lines[j].strip().lower()
                if 'completed' in next_line_lower and '2022' in lines[j]:
                    park_projects.append(clean_line)
                    break

# Remove duplicates
park_projects = list(set(park_projects))

# Calculate total funding
funding_map = {}
for rec in funding_recs:
    funding_map[rec['Project_Name']] = int(rec['Amount'])

total_fund = 0
matches = []

for proj in park_projects:
    for fund_name in funding_map:
        proj_lower = proj.lower()
        fund_lower = fund_name.lower()
        if proj_lower in fund_lower or fund_lower in proj_lower:
            amt = funding_map[fund_name]
            total_fund += amt
            matches.append({'project': proj, 'fund_name': fund_name, 'amount': amt})

result = {'total_funding': total_fund, 'matches': matches, 'projects': park_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}}

exec(code, env_args)
