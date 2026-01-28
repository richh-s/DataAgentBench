code = """import json, re
funding = json.load(open('/tmp/tmp_hb9f3fdk.json', 'r'))
civic_docs = json.load(open('/tmp/tmp_cdv8r04p.json', 'r'))
funding_lookup = {item['Project_Name']: int(item['Amount']) for item in funding}
all_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line and '(' in line and ')' in line and i + 4 < len(lines):
            parts = line.rsplit('(', 1)
            if len(parts) == 2:
                name = parts[0].strip()
                status = parts[1].replace(')', '').strip().lower()
                topic_line = lines[i+1].strip()
                type_line = lines[i+2].strip()
                st_line = lines[i+3].strip()
                et_line = lines[i+4].strip()
                if 'topic:' in topic_line and 'type:' in type_line and 'st:' in st_line and 'et:' in et_line:
                    topic = topic_line.replace('topic:', '').strip()
                    type_val = type_line.replace('type:', '').strip()
                    st = st_line.replace('st:', '').strip()
                    et = et_line.replace('et:', '').strip()
                    all_projects.append({'name': name, 'topic': topic, 'type': type_val, 'status': status, 'st': st, 'et': et})
        i += 1

disaster_2022 = []
fema_pattern = re.compile(r'\((FEMA|CalJPIA|CalOES)\s*Project\)', re.IGNORECASE)
for proj in all_projects:
    if '2022' in proj['st']:
        if proj['type'] == 'disaster' or fema_pattern.search(proj['name']):
            disaster_2022.append(proj)

unique_names = set()
unique_projects = []
for proj in disaster_2022:
    if proj['name'] not in unique_names:
        unique_names.add(proj['name'])
        unique_projects.append(proj)

total_funding = 0
matched_projects = []
for proj in unique_projects:
    if proj['name'] in funding_lookup:
        amount = funding_lookup[proj['name']]
        total_funding += amount
        matched_projects.append({'project_name': proj['name'], 'amount': amount})

result = {'total_funding': total_funding, 'project_count': len(matched_projects), 'projects': matched_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': 'file_storage/functions.query_db:21.json'}

exec(code, env_args)
