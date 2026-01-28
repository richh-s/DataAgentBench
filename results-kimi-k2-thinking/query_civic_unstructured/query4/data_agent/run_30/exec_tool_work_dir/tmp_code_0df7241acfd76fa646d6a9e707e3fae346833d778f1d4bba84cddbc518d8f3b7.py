code = """import json
civic_docs = json.load(open('file_storage/functions.query_db:38.json'))
funding_data = json.load(open('file_storage/functions.query_db:8.json'))

spring_2022_names = set()
for doc in civic_docs:
    text = doc.get('text','')
    if text.find('2022-Spring') >= 0:
        lines = text.split('\n')
        for line in lines:
            clean = line.strip()
            if clean.istitle() and len(clean) > 10:
                if clean.find('Project') >= 0 or clean.find('Improvements') >= 0 or clean.find('Repairs') >= 0:
                    spring_2022_names.add(clean)

funding_map = {}
for f in funding_data:
    funding_map[f['Project_Name']] = int(f['Amount'])

matched = 0
total = 0
for name in spring_2022_names:
    if name in funding_map:
        matched += 1
        total += funding_map[name]
    else:
        for suffix in [' (FEMA Project)', ' (CalOES Project)', ' (CalJPIA Project)']:
            var = name + suffix
            if var in funding_map:
                matched += 1
                total += funding_map[var]
                break

result = dict()
result['spring_2022_projects'] = len(spring_2022_names)
result['matching_funding_records'] = matched
result['total_funding'] = total
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_civic_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:12': {'num_civic_docs': 5, 'num_funding_records': 500}, 'var_functions.execute_python:18': {'civic_type': "<class 'str'>", 'is_str': True, 'endswith_json': True}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:58': {'var_type': "<class 'str'>", 'var_value': 'file_storage/functions.query_db:38.json', 'is_string': True, 'is_list': False, 'endswith_json': True, 'file_exists': True, 'first_bytes': '[\n  {\n    "_id": "694eef5c4ec675b6b5f5a285",\n    "'}}

exec(code, env_args)
