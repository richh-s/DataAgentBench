code = """import json
import re

civic_docs_file = locals()['var_functions.query_db:2']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

funding_file = locals()['var_functions.query_db:6']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Find disaster projects with 2022 start dates
disaster_projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Look for FEMA/CalOES projects in the text
    if '2022' in text and ('FEMA' in text or 'CalOES' in text):
        # Extract lines that look like project names
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 0 and (line.istitle() or line.isupper()):
                if 'Subject' not in line and 'To:' not in line and 'Date:' not in line:
                    disaster_projects.append(line)

# Remove duplicates
unique_disaster = list(set(disaster_projects))

print('__RESULT__:')
print(json.dumps({'projects': unique_disaster, 'count': len(unique_disaster)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
