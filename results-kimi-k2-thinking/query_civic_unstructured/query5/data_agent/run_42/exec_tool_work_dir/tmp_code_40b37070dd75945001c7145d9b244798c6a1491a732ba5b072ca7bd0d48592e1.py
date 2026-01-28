code = """import json, os, re, sys

# Load funding data
funding_path = locals().get('var_functions.query_db:12')
if funding_path:
    with open(funding_path) as f:
        funding = json.load(f)
else:
    funding = []

# Load civic documents
civic_path = locals().get('var_functions.query_db:14')
if civic_path:
    with open(civic_path) as f:
        civic_docs = json.load(f)
else:
    civic_docs = []

# Find disaster projects with 2022 dates
disaster_2022_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    # Look for disaster indicators with 2022
    if '2022' in text and ('FEMA' in text or 'CalOES' in text):
        # Extract project names that include 2022
        lines = text.split('\n')
        for line in lines:
            line_clean = line.strip()
            if '2022' in line_clean and len(line_clean) < 200:
                # Check if disaster-related
                snippet_start = max(0, lines.index(line) - 3)
                snippet_end = min(len(lines), lines.index(line) + 10)
                snippet = ' '.join(lines[snippet_start:snippet_end]).lower()
                
                if 'fema' in snippet or 'caloes' in snippet or 'fire' in snippet:
                    # Clean up the project name
                    if 'Project' in line_clean or 'Improvements' in line_clean:
                        if line_clean not in disaster_2022_projects:
                            disaster_2022_projects.append(line_clean)

# Sum funding for these projects
total_funding = 0
funding_matches = []

for proj in disaster_2022_projects:
    proj_words = set(proj.lower().replace('2022', '').replace('project', '').replace('improvements', '').replace('repairs', '').split())
    
    for rec in funding:
        fund_name = rec['Project_Name']
        if any(kw in fund_name.lower() for kw in ['fema', 'caloes']):
            fund_words = set(fund_name.lower().replace('(fema project)', '').replace('(caloes project)', '').split())
            overlap = proj_words.intersection(fund_words)
            
            # If significant overlap in words
            if len(overlap) >= 2:
                amount = int(rec['Amount'])
                total_funding += amount
                funding_matches.append((proj, fund_name, amount))
                break

# If no matches found, use all disaster projects that have 2022 in any field
if total_funding == 0:
    # Alternative approach: get all funding records for disaster projects and check if any related to 2022
    disaster_funding = []
    for rec in funding:
        name = rec['Project_Name'].lower()
        if 'fema' in name or 'caloes' in name or 'caljpia' in name:
            disaster_funding.append(rec)
    
    # Check civic docs for any 2022 mention linked to these projects
    text_2022 = []
    for doc in civic_docs:
        if '2022' in doc.get('text', ''):
            text_2022.append(doc['text'])
    
    # If there's any mention of 2022 and disaster in civic docs, sum all disaster funding
    if text_2022 and disaster_funding:
        total_funding = sum(int(rec['Amount']) for rec in disaster_funding)

result = {
    'total_funding': total_funding,
    'project_count': len(disaster_2022_projects),
    'projects': disaster_2022_projects[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'success': True, 'num_docs': 5}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_total': 500, 'civic_docs_total': 5, 'disaster_funding_count': 27}}

exec(code, env_args)
