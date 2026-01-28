code = """import json, re

civic_path = 'file_storage/functions.query_db:38.json'
funding_path = 'file_storage/functions.query_db:8.json'

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

all_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    lines = text.split('\n')
    for idx, line in enumerate(lines):
        line_clean = line.strip()
        if not line_clean or len(line_clean) < 10:
            continue
        if line_clean.istitle() and ('Project' in line_clean or 'Improvements' in line_clean or 'Repairs' in line_clean):
            proj_name = line_clean
            st_date = None
            for j in range(idx+1, min(idx+30, len(lines))):
                next_line = lines[j].strip()
                if 'Schedule:' in next_line:
                    for k in range(j+1, min(j+10, len(lines))):
                        sched_line = lines[k].strip()
                        date_match = re.search(r'2022-Spring', sched_line)
                        if date_match and not st_date:
                            st_date = date_match.group(0)
                        if ':' in sched_line and ('Design' not in sched_line and 'Construction' not in sched_line):
                            break
            if proj_name and st_date == '2022-Spring':
                all_projects.append({'Project_Name': proj_name, 'st': st_date})

unique_names = list(set([p['Project_Name'] for p in all_projects]))
funding_map = {f['Project_Name']: int(f['Amount']) for f in funding_data}
matched = 0
total = 0
for name in unique_names:
    if name in funding_map:
        matched += 1
        total += funding_map[name]
    else:
        for suffix in [' (FEMA Project)', ' (CalOES Project)', ' (CalJPIA Project)']:
            var_name = name + suffix
            if var_name in funding_map:
                matched += 1
                total += funding_map[var_name]
                break

print('__RESULT__:')
print(json.dumps({'spring_2022_projects': len(unique_names), 'matched_funding_records': matched, 'total_funding': total}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_civic_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:12': {'num_civic_docs': 5, 'num_funding_records': 500}, 'var_functions.execute_python:18': {'civic_type': "<class 'str'>", 'is_str': True, 'endswith_json': True}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:58': {'var_type': "<class 'str'>", 'var_value': 'file_storage/functions.query_db:38.json', 'is_string': True, 'is_list': False, 'endswith_json': True, 'file_exists': True, 'first_bytes': '[\n  {\n    "_id": "694eef5c4ec675b6b5f5a285",\n    "'}}

exec(code, env_args)
