code = """import json, re

# Load data
civic_file = locals()['var_functions.query_db:6']
funding_file = locals()['var_functions.query_db:5']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Build funding map by project name
funding_map = {}
for rec in funding_records:
    proj_name = rec.get('Project_Name', '')
    amount = int(str(rec.get('Amount', 0)))
    if proj_name and amount > 0:
        funding_map[proj_name] = funding_map.get(proj_name, 0) + amount

# Extract Spring 2022 projects from civic documents
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Search for text patterns indicating Spring 2022 projects
    if '2022' in text and ('Spring' in text or 'March' in text or 'April' in text or 'May' in text):
        # Split text and scan for project-looking lines
        lines = [ln.strip() for ln in text.split('\n') if ln.strip()]
        
        for idx, line in enumerate(lines):
            # Heuristic: project names are typically uppercase and not too long
            if (len(line) > 5 and len(line) < 80 and 
                line[0].isupper() and 
                not any(w in line.lower() for w in ['page', 'agenda', 'item', 'commission', 'public works'])):
                
                # Check following lines for Spring 2022 context
                context_lines = lines[idx:idx+7]
                context_text = ' '.join(context_lines).lower()
                
                has_2022 = '2022' in context_text
                has_spring = any(s in context_text for s in ['spring', 'march', 'april', 'may'])
                
                if has_2022 and has_spring:
                    spring_2022_projects.add(line)

# Now match these project names with funding data
project_matches = []
matched_funding = 0

for proj_name in spring_2022_projects:
    # Try direct match first
    if proj_name in funding_map:
        amt = funding_map[proj_name]
        project_matches.append([proj_name, amt])
        matched_funding += amt
        continue
    
    # Try flexible match (handle suffixes like (FEMA Project))
    proj_base = proj_name.split(' (')[0]
    for funded_proj in funding_map:
        if (proj_name.lower() in funded_proj.lower() or 
            funded_proj.lower() in proj_name.lower() or
            (proj_base and proj_base.lower() in funded_proj.lower())):
            amt = funding_map[funded_proj]
            project_matches.append([proj_name, amt])
            matched_funding += amt
            break

result = {
    'project_count': len(project_matches),
    'total_funding': matched_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_documents': 5, 'status': 'loaded'}}

exec(code, env_args)
