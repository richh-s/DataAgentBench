code = """import json

funding = json.load(open('var_functions.query_db:0', 'r'))
docs = json.load(open('var_functions.query_db:1', 'r'))

funding_lookup = {item['Project_Name']: int(item['Amount']) for item in funding if int(item['Amount']) > 50000}

projects = set()
for doc in docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in txt:
        section = txt[txt.find('Capital Improvement Projects (Design)') + 38:]
        boundaries = [section.find(x) for x in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects'] if section.find(x) > 0]
        section_end = min(boundaries) if boundaries else len(section)
        section = section[:section_end]
        for line in section.split('\n'):
            line = line.strip()
            if len(line) >= 5 and not line.startswith('(') and not line.startswith('-') and not any(x in line for x in ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 'Capital Improvement', 'Project Description']):
                if line in funding_lookup:
                    projects.add(line)

print('__RESULT__:')
print(json.dumps({'count': len(projects), 'projects': list(projects)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:24': {'funding_records': 276, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}}

exec(code, env_args)
