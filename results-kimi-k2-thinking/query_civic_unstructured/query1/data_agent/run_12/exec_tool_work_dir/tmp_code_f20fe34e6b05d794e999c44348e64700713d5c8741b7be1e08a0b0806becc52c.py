code = """import json

f = open('var_functions.query_db:0')
funding = json.load(f)
f.close()

c = open('var_functions.query_db:1')
docs = json.load(c)
c.close()

funding_lookup = {}
for item in funding:
    amt = int(item['Amount'])
    if amt > 50000:
        funding_lookup[item['Project_Name']] = amt

found = set()
for doc in docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in txt:
        rest = txt[txt.find('Capital Improvement Projects (Design)') + 38:]
        ends = [rest.find(x) for x in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects'] if rest.find(x) > 0]
        cutoff = min(ends) if ends else len(rest)
        section = rest[:cutoff]
        for line in section.splitlines():
            line = line.strip()
            if len(line) < 5: continue
            if line[0] == '!' or line[0] == '-' or line[0] == '*' or line.startswith('('): continue
            if 'Updates' in line or 'Schedule' in line or 'Design' in line.split() or 'Advertise' in line or 'Construction' in line.split(): continue
            if line in funding_lookup: found.add(line)

print('__RESULT__:')
print(json.dumps({'count':len(found), 'projects':list(found)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:24': {'funding_records': 276, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}}

exec(code, env_args)
