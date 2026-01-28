code = """import json, re

funding_path = locals()['var_functions.query_db:5']
civic_docs_path = locals()['var_functions.query_db:8'] 

with open(funding_path, 'r') as f:
    funding = json.load(f)
with open(civic_docs_path, 'r') as f:
    docs = json.load(f)

def get_design_projects(docs):
    result = []
    for doc in docs:
        txt = doc['text']
        # Find design section
        start = txt.find('Capital Improvement Projects (Design)')
        if start > 0:
            end = txt.find('Capital Improvement Projects (', start + 1)
            if end < 0:
                end = len(txt)
            section = txt[start:end]
            lines = section.split('\n')
            for line in lines:
                line = line.strip().replace('cid:', '').replace('(', '').replace(')', '')
                if len(line) > 10 and 'Updates:' not in line and 'Schedule:' not in line:
                    if not line.startswith('•') and not line.startswith('-') and not line.endswith(':'):
                        result.append({'Project_Name': line, 'status': 'design', 'type': 'capital'})
    return result

projects = get_design_projects(docs)
unique = list({p['Project_Name']: p for p in projects}.values())

print('__RESULT__:')
print(json.dumps({'total': len(projects), 'unique': len(unique), 'sample': unique[:5]}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:32': {'funding_count': 276, 'civic_docs_count': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}}

exec(code, env_args)
