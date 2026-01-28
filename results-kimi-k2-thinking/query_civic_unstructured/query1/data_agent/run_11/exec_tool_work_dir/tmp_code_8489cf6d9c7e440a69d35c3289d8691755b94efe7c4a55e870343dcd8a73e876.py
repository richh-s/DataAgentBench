code = """import json
import re

civic_docs = json.load(open('file_storage/functions.query_db:30.json'))
funding_data = json.load(open('file_storage/functions.query_db:22.json'))

design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    start_marker = 'Capital Improvement Projects (Design)'
    end_marker = 'Capital Improvement Projects ('
    
    start = text.find(start_marker)
    if start == -1: continue
    
    end = text.find(end_marker, start + len(start_marker))
    if end == -1: end = len(text)
    
    section = text[start:end]
    for line in section.split('\n'):
        line = line.strip()
        if len(line) < 10: continue
        if any(x in line for x in ['Updates:', 'Project Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'Page', 'Agenda Item', 'cid:']): continue
        
        keywords = ['road', 'street', 'park', 'drainage', 'bridge', 'walkway', 'median', 'signal', 'canyon', 'beach', 'storm', 'water']
        if any(kw in line.lower() for kw in keywords):
            if line.istitle() or line[0].isupper():
                design_projects.add(line)

funded = set()
for f in funding_data:
    if int(f.get('Amount', 0)) > 50000:
        funded.add(f.get('Project_Name', ''))

matched = set()
for proj in design_projects:
    if proj in funded:
        matched.add(proj)
    else:
        proj_low = proj.lower()
        for fund in funded:
            fund_low = fund.lower()
            if proj_low in fund_low or fund_low in proj_low:
                matched.add(proj)

print('__RESULT__:')
print(json.dumps(len(matched)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'civic_docs_count': 0, 'civic_docs_sample': None, 'funding_data_count': 0, 'funding_data_sample': None}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 38, 'sample_doc': 'f'}, 'var_functions.execute_python:12': {'json_files': [], 'available_vars': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:6', 'var_functions.query_db:8', 'var_functions.execute_python:10'], 'current_dir_files': ['tmp_code_b262fd095b36b5236393345bb8d1ca0a3d195790acfd855432118fb96265da25.py', 'tmp_code_ec12d0aa8e6ef28366e7553f1de624160a0ec8fe0b8dcd1d857bdc21d2ac6101.py', 'tmp_code_571c1044f3b97a69aa8a7d818bee03068db011ff8bc05dfe8973c1b9d8bffe19.py', 'tmp_code_e5ff25f71b3e4ce5f3ce1c812f4ebf25f913fb64b2bed77fbaa660f1d36156fc.py', 'file_storage']}, 'var_functions.execute_python:14': {'civic_docs_loaded': 38, 'funding_data_loaded': 38, 'civic_docs_type': 'str'}, 'var_functions.execute_python:16': {'civic_docs_path': 'file_storage/functions.query_db:8.json', 'funding_data_path': 'file_storage/functions.query_db:2.json', 'civic_docs_loaded': 5, 'funding_data_loaded': 276}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_doc_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an', 'funding_data_count': 276, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
