code = """import json
import re

# Read funding data
funding_file = locals()['var_functions.query_db:36']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create funding lookup
funding_lookup = {}
for item in funding_data:
    # Convert to lowercase for matching
    proj_name = item['Project_Name'].lower().strip()
    amount = int(item['Amount'])
    funding_lookup[proj_name] = amount

print('Funding lookup created with', len(funding_lookup), 'entries')

# Read civic documents filtered for Spring 2022
civic_file = locals()['var_functions.query_db:44']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Found', len(civic_docs), 'documents mentioning Spring 2022')

# Extract projects with Spring 2022 start dates
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Split into lines for analysis
    lines = text.split('\n')
    
    # Look for project sections with Spring 2022 construction dates
    current_project = None
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty and special lines
        if not line or line.startswith('(') or line.startswith('cid:') or line.startswith('_'):
            continue
            
        # Look for Begin Construction with Spring 2022
        if 'Begin' in line and any(month in line.lower() for month in ['spring', 'march', 'april', 'may']) and '2022' in line:
            # Look back to find project name (skip category headers)
            for j in range(i-1, max(0, i-10), -1):
                prev_line = lines[j].strip()
                if (prev_line and 
                    not prev_line.startswith('(') and 
                    'cid:' not in prev_line and 
                    'Capital Improvement' not in prev_line and
                    'Design' not in prev_line and
                    'Construction' not in prev_line and
                    'Not Started' not in prev_line and
                    'Completed' not in prev_line and
                    len(prev_line) < 100):
                    spring_projects.append(prev_line)
                    break

print('Spring 2022 projects found:', spring_projects)

# Match with funding
matched = []
total_funding = 0
already_matched = set()

for proj in spring_projects:
    proj_low = proj.lower()
    if proj_low in funding_lookup and proj_low not in already_matched:
        amount = funding_lookup[proj_low]
        matched.append({'name': proj, 'funding': amount})
        total_funding += amount
        already_matched.add(proj_low)
    else:
        # Try alternative names (e.g., with FEMA suffixes)
        for fund_proj, amount in funding_lookup.items():
            if (proj_low in fund_proj or 
                fund_proj.replace(' (fema project)', '') == proj_low or
                fund_proj.replace(' (caljpia project)', '') == proj_low or
                fund_proj.replace(' (caloes project)', '') == proj_low):
                matched.append({'name': proj, 'funding': amount})
                total_funding += amount
                break

print('Matched projects:', len(matched))
print('Total funding:', total_funding)

# Also check for other 2022 projects in different documents
spring_2022_files = ['/tmp/civic_docs_2022_spring.json', '/tmp/civic_docs_2022_march.json', '/tmp/civic_docs_2022_april.json']

for file_var in spring_2022_files:
    if file_var in locals():
        try:
            with open(locals()[file_var], 'r') as f:
                docs = json.load(f)
            print(f'Additional doc set: {len(docs)} files')
        except:
            pass

result = {"project_count": len(matched), "total_funding": total_funding, "projects": matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
