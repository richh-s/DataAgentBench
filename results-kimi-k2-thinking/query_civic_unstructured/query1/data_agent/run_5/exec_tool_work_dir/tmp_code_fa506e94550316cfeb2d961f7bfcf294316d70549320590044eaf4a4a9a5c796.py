code = """import json

# Load the data
with open(locals()['var_functions.query_db:44']) as f:
    funding_records = json.load(f)

with open(locals()['var_functions.query_db:2']) as f:
    civic_docs = json.load(f)

# Get funding projects > $50k
funding_projects = {}
for rec in funding_records:
    name = rec['Project_Name']
    amt = int(rec['Amount'])
    funding_projects[name] = amt

print('Funding projects count:', len(funding_projects))

# Extract design status projects
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Design' in text and 'Capital Improvement' in text:
        # Look for project names in design section
        chunks = text.split('\n')
        for i, chunk in enumerate(chunks):
            if '(Design)' in chunk and 'Capital Improvement' in chunk:
                for j in range(i+1, min(i+5, len(chunks))):
                    project = chunks[j].strip()
                    if project and '\t' not in project and len(project) > 10:
                        if not project.startswith('(') and not project.startswith('cid'):
                            design_projects.append(project)
                            break

print('Design projects found:', len(design_projects))

# Match projects
matches = 0
matched_names = set()

for design in design_projects:
    # Clean design name
    d_clean = design.split('(')[0].lower()
    d_clean = d_clean.replace('project', '').replace('improvements', '').strip()
    
    for fund_name in funding_projects:
        if fund_name in matched_names:
            continue
        # Clean fund name
        f_clean = fund_name.split('(')[0].lower()
        f_clean = f_clean.replace('project', '').replace('improvements', '').strip()
        
        if d_clean in f_clean or f_clean in d_clean:
            matches += 1
            matched_names.add(fund_name)
            break

print('Final match count:', matches)
result = {'count': matches}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
