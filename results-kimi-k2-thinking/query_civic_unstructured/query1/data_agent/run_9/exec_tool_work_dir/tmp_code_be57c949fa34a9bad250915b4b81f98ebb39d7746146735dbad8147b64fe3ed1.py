code = """import json
funding_path = locals()['var_functions.query_db:2']
civic_path = locals()['var_functions.query_db:8']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

high_funding = {}
for f in funding_data:
    if int(f['Amount']) > 50000:
        high_funding[f['Project_Name'].lower()] = int(f['Amount'])

print('High funding map size:', len(high_funding))

design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        section = text.split('Capital Improvement Projects (Design)')[1]
        # Truncate
        if 'Capital Improvement Projects (Construction)' in section:
            section = section.split('Capital Improvement Projects (Construction)')[0]
        
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 10 and line[0].isupper():
                skip_checks = ['Updates', 'Schedule', 'Design', 'Advertise', 'Construction', 'Page ', 'Agenda Item', '(cid:']
                if not any(c in line for c in skip_checks):
                    design_projects.append(line)

print('Design projects count:', len(design_projects))

matched_count = 0
seen = set()
for proj in design_projects:
    if proj.lower() in high_funding and proj not in seen:
        matched_count += 1
        seen.add(proj)

print('__RESULT__:')
print(matched_count)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
