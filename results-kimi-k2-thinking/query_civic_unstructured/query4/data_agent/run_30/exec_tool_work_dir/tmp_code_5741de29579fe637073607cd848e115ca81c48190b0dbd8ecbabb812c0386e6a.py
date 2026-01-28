code = """import json

civic_path = locals()['var_functions.query_db:38']
funding_path = locals()['var_functions.query_db:8']

with open(civic_path) as f:
    civic_docs = json.load(f)
with open(funding_path) as f:
    funding_data = json.load(f)

# Find Spring 2022 projects from documents
spring_2022_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022-Spring' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if not line or len(line) < 10:
                continue
            if line.istitle() and ('Project' in line or 'Improvements' in line):
                proj_name = line
                spring_2022_projects.append({'Project_Name': proj_name})
                break

# Remove duplicates
unique_projects = []
seen_names = set()
for p in spring_2022_projects:
    if p['Project_Name'] not in seen_names:
        unique_projects.append(p)
        seen_names.add(p['Project_Name'])

# Match with funding records
funding_map = {f['Project_Name']: f for f in funding_data}
matched = []
for p in unique_projects:
    name = p['Project_Name']
    if name in funding_map:
        matched.append(funding_map[name])
    else:
        # Try with disaster project suffixes
        for suffix in [' (FEMA Project)', ' (CalOES Project)', ' (CalJPIA Project)']:
            var_name = name + suffix
            if var_name in funding_map:
                matched.append(funding_map[var_name])
                break

total = sum(int(f['Amount']) for f in matched)

result = {
    'spring_2022_projects': len(unique_projects),
    'matching_funding_records': len(matched),
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_civic_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:12': {'num_civic_docs': 5, 'num_funding_records': 500}, 'var_functions.execute_python:18': {'civic_type': "<class 'str'>", 'is_str': True, 'endswith_json': True}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
