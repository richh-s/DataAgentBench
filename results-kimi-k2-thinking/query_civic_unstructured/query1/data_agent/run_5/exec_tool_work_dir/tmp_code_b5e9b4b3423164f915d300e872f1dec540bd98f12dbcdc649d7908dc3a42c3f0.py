code = """import json

# Load funding data from database query
funding_path = locals()['var_functions.query_db:0']
with open(funding_path) as f:
    funding_records = json.load(f)

# Load civic documents from database query
civic_path = locals()['var_functions.query_db:2']
with open(civic_path) as f:
    civic_docs = json.load(f)

# Filter for projects with funding > $50,000
funding_map = {}
for rec in funding_records:
    amount = int(rec.get('Amount', 0))
    if amount > 50000:
        funding_map[rec['Project_Name']] = amount

print('Projects with funding > $50k:', len(funding_map))

# Extract design status projects from civic documents
design_candidates = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check for design section
    start_marker = 'Capital Improvement Projects (Design)'
    if start_marker in text:
        start = text.index(start_marker) + len(start_marker)
        end = text.find('Capital Improvement Projects (Construction)', start)
        if end < 0:
            end = len(text)
        
        section = text[start:end]
        parts = section.split('\n\n')
        
        for part in parts:
            part = part.strip()
            if len(part) > 15 and 'Design)' not in part:
                lines = [L.strip() for L in part.split('\n') if L.strip()]
                if lines:
                    name = lines[0]
                    # Filter metadata
                    if name and 'Updates' not in name and 'Schedule' not in name and len(name) > 8:
                        design_candidates.append(name)

print('Design status candidates:', len(design_candidates))

# Match projects
matched_projects = []
matched_names = set()

for design_name in design_candidates:
    # Normalize design name
    d_clean = design_name.split('(')[0].strip().lower()
    d_clean = d_clean.replace('project', '').replace('improvements', '').strip()
    
    for fund_name in funding_map:
        if fund_name in matched_names:
            continue
        
        # Normalize funding name
        f_clean = fund_name.split('(')[0].strip().lower()
        f_clean = f_clean.replace('project', '').replace('improvements', '').strip()
        
        # Check match
        if d_clean in f_clean or f_clean in d_clean:
            matched_projects.append({
                'name': fund_name,
                'amount': funding_map[fund_name]
            })
            matched_names.add(fund_name)

print('Matched projects:', len(matched_projects))

result = {'count': len(matched_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
