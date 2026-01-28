code = """import json
import re

civic_docs_file = locals()['var_functions.query_db:20']
funding_file = locals()['var_functions.query_db:6']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

disaster_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if len(line) < 5:
            continue
        
        if line.istitle() or line.isupper():
            # Check for disaster indicators
            if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line:
                disaster_projects.append(line)

unique_projects = list(set(disaster_projects))

print('__RESULT__:')
print(json.dumps({
    'disaster_projects': unique_projects,
    'count': len(unique_projects),
    'sample_size': len(civic_docs)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
