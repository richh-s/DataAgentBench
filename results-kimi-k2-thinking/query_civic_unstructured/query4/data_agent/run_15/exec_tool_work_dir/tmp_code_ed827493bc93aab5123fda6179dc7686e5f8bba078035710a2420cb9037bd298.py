code = """import json
import re

# Load data
civic_docs = json.load(open(locals()['var_functions.query_db:20']))
funding = json.load(open(locals()['var_functions.query_db:24']))

# Create funding map
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding}

# Find Spring 2022 projects
spring_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' not in text:
        continue

    # Check for Spring months
    if any(term in text.lower() for term in ['spring', 'march', 'april', 'may', '2022-03', '2022-04', '2022-05']):
        # Extract project names from lines containing project keywords
        for line in text.split('\n'):
            line = line.strip()
            if len(line) > 15 and ('Project' in line or 'Improvements' in line or 'Repairs' in line):
                if '2022' in line and 'updates' not in line.lower():
                    clean = re.sub(r'^[\d\*\-.]+\s*', '', line).strip()
                    if clean:
                        spring_projects.add(clean)

# Projects with explicit 2022 in their name
for name in funding_map.keys():
    if '2022' in name:
        spring_projects.add(name)

# Match with funding
results = {}
total = 0
for proj in spring_projects:
    if proj in funding_map:
        results[proj] = funding_map[proj]
        total += funding_map[proj]
    else:
        # Fuzzy match
        proj_norm = proj.lower().replace('project', '').strip()
        for fund_name in funding_map:
            fund_norm = fund_name.lower().replace('project', '').strip()
            if proj_norm in fund_norm and len(proj_norm) > 20:
                if fund_name not in results:
                    results[fund_name] = funding_map[fund_name]
                    total += funding_map[fund_name]
                break

print('__RESULT__:')
print(json.dumps({'count': len(results), 'total': total, 'sample': list(results.items())[:5]}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_docs_sample': "{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\"}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'civic_docs_loaded': 5, 'first_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
