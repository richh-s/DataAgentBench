code = """import json, re
civic_path = locals()['var_functions.query_db:5']
with open(civic_path) as f:
    civic_docs = json.load(f)
funding_path = locals()['var_functions.query_db:8']
with open(funding_path) as f:
    funding_data = json.load(f)

projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.istitle() and len(line) > 10:
            project_name = line
            start_date = None
            j = i + 1
            while j < min(i + 30, len(lines)):
                next_line = lines[j].strip()
                if 'Schedule:' in next_line:
                    k = j + 1
                    while k < min(j + 15, len(lines)):
                        s_line = lines[k].strip()
                        d_match = re.search(r'\d{4}-(Spring|Fall|Summer|Winter|March|April|May)', s_line)
                        if d_match and not start_date:
                            start_date = d_match.group(0)
                        if ':' in s_line and not any(x in s_line for x in ['Complete', 'Design', 'Construction', 'Advertise', 'Begin']):
                            break
                        k += 1
                j += 1
            if project_name and len(project_name) > 5:
                projects.append({'Project_Name': project_name, 'st': start_date})
        i += 1

spring_2022 = [p for p in projects if p['st'] and '2022' in p['st'] and any(s in p['st'] for s in ['Spring', 'March', 'April', 'May'])]

funding_by_name = {f['Project_Name']: f for f in funding_data}
matched = []
for project in spring_2022:
    name = project['Project_Name']
    if name in funding_by_name:
        matched.append(funding_by_name[name])
    else:
        suffixes = [' (FEMA Project)', ' (CalOES Project)', ' (CalJPIA Project)']
        for s in suffixes:
            if (name + s) in funding_by_name:
                matched.append(funding_by_name[name + s])
                break

total = sum(int(f['Amount']) for f in matched)
print('__RESULT__:')
print(json.dumps({
    'spring_2022_count': len(spring_2022),
    'matching_funding_records': len(matched),
    'total_funding': total
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_civic_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:12': {'num_civic_docs': 5, 'num_funding_records': 500}, 'var_functions.execute_python:18': {'civic_type': "<class 'str'>", 'is_str': True, 'endswith_json': True}}

exec(code, env_args)
