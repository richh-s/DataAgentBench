code = """import json

civic_docs = json.load(open(locals()['var_functions.query_db:38']))
funding_data = json.load(open(locals()['var_functions.query_db:8']))

# Simple project extraction
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        if line.istitle() and line.find('Project') >= 0:
            proj_name = line
            st_date = None
            # Look for Spring dates
            for j in range(i+1, min(i+25, len(lines))):
                if 'Schedule' in lines[j]:
                    for k in range(j+1, min(j+10, len(lines))):
                        s_line = lines[k].strip()
                        if '2022-Spring' in s_line:
                            st_date = '2022-Spring'
                            break
            if proj_name:
                projects.append({'Project_Name': proj_name, 'st': st_date})

spring_2022 = [p for p in projects if p['st'] and p['st'].find('2022') >= 0]
funding_map = {f['Project_Name']: f for f in funding_data}
matched = []
for p in spring_2022:
    name = p['Project_Name']
    if name in funding_map:
        matched.append(funding_map[name])
    else:
        for suffix in [' (FEMA Project)', ' (CalOES Project)', ' (CalJPIA Project)']:
            var_name = name + suffix
            if var_name in funding_map:
                matched.append(funding_map[var_name])
                break

total = sum(int(f['Amount']) for f in matched)
result = {'spring_2022_projects': len(spring_2022), 'matching_funding_records': len(matched), 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_civic_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:12': {'num_civic_docs': 5, 'num_funding_records': 500}, 'var_functions.execute_python:18': {'civic_type': "<class 'str'>", 'is_str': True, 'endswith_json': True}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
