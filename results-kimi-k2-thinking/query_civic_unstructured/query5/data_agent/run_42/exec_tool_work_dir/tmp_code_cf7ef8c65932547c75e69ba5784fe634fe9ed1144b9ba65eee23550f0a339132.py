code = """import json
import os

# Load funding data
funding_path = locals()['var_functions.query_db:12']
with open(funding_path) as f:
    funding = json.load(f)

# Load civic documents
civic_path = locals()['var_functions.query_db:14']
with open(civic_path) as f:
    civic_docs = json.load(f)

# Identify disaster projects that started in 2022 in civic documents
disaster_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    for line in lines:
        line_clean = line.strip()
        # Look for lines with 2022 and disaster indicators
        if '2022' in line_clean and ('FEMA' in line_clean or 'CalOES' in line_clean or 'CalJPIA' in line_clean or 'fire' in line_clean.lower()):
            # Extract a short name (limit length)
            if len(line_clean) < 200:
                # Clean up the line to get a reasonable project name
                if 'Project' in line_clean:
                    disaster_projects_2022.append(line_clean)

# Remove duplicates
disaster_projects_2022 = list(set(disaster_projects_2022))

print('DISASTER 2022 projects found:', disaster_projects_2022)

# Match with funding data and sum amounts
total_funding = 0
matched_projects = []
for proj in disaster_projects_2022:
    # Search funding for matching disaster project
    for rec in funding:
        fund_name = rec['Project_Name']
        # Check if disaster project
        if '(FEMA' in fund_name or '(CalOES' in fund_name or '(CalJPIA' in fund_name:
            # Heuristic match: if project words overlap
            proj_words = set(proj.lower().replace('2022','').replace('project','').replace('improvements','').split())
            fund_words = set(fund_name.lower().replace('(fema project)','').replace('(caloes project)','').replace('(caljpia project)','').split())
            # Check if significant overlap
            overlap = proj_words.intersection(fund_words)
            if len(overlap) >= 2:  # at least 2 words match
                amount = int(rec['Amount'])
                total_funding += amount
                matched_projects.append({'project': proj, 'funding': fund_name, 'amount': amount})
                break

print('MATCHED funding records:', len(matched_projects))
print('TOTAL funding:', total_funding)

print('__RESULT__:')
print(json.dumps({'total_funding': total_funding}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'success': True, 'num_docs': 5}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_total': 500, 'civic_docs_total': 5, 'disaster_funding_count': 27}}

exec(code, env_args)
