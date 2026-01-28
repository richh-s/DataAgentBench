code = """import json, re

civic_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:1']

with open(civic_path) as f:
    civic_docs = json.load(f)
with open(funding_path) as f:
    funding = json.load(f)

# Track park projects from civic docs
park_info = {}

for doc in civic_docs:
    text = doc.get('text','')
    filename = doc.get('filename','')
    doc_lines = text.split('\n')
    
    for idx, line in enumerate(doc_lines):
        line_clean = line.strip()
        line_lower = line_clean.lower()
        
        # Look for project names (usually uppercase or containing Project)
        if line_clean and (line_clean.isupper() or 'Project' in line_clean) and len(line_clean) > 10:
            project_name = line_clean
            
            # Check subsequent lines for status and dates
            for next_line in doc_lines[idx+1:idx+5]:
                next_lower = next_line.lower()
                if 'completed' in next_lower and '2022' in next_line:
                    if 'park' in project_name.lower():
                        park_info[project_name] = {'status': 'completed', 'year': '2022'}
                    break

# Calculate funding for park projects completed in 2022
total_funding = 0
for project in park_info.keys():
    project_lower = project.lower()
    # Find matching funding records
    for fund in funding:
        fund_name_lower = fund['Project_Name'].lower()
        # Match by checking if key terms appear in both names
        project_terms = project_lower.replace('project','').replace('improvements','').replace('repairs','').strip()
        if 'park' in fund_name_lower:
            # Check for significant word overlap
            proj_words = set(project_terms.split())
            fund_words = set(fund_name_lower.split())
            if len(proj_words.intersection(fund_words)) > 0:
                amount = int(fund['Amount'])
                total_funding += amount

# Return just the total funding number
result = json.dumps({'total_funding': total_funding})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
