code = """import json
import re

funding_path = locals()['var_functions.query_db:5']
civic_docs_path = locals()['var_functions.query_db:8']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

def extract_projects(docs):
    projects = []
    for doc in docs:
        text = doc['text']
        pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(|Disaster Recovery Projects \(|$)'
        matches = re.finditer(pattern, text, re.DOTALL)
        for match in matches:
            section = match.group(1)
            lines = section.split('\n')
            for line in lines:
                line = line.strip()
                if (line and not line.startswith('(') and not line.startswith('cid:') and 
                    not any(kw in line for kw in ['Updates:', 'Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:']) and
                    len(line) > 10):
                    clean = re.sub(r'\s*-\s*', '', line)
                    clean = re.sub(r'\(.*\)$', '', clean).strip()
                    clean = re.sub(r'^\d+\s*\.\s*', '', clean)
                    if clean and not clean.endswith(':'):
                        projects.append({'Project_Name': clean, 'status': 'design', 'type': 'capital'})
    return projects

extracted = extract_projects(civic_docs)
unique = list({p['Project_Name']: p for p in extracted}.values())

print('__RESULT__:')
print(json.dumps({'extracted': len(extracted), 'unique': len(unique), 'sample': unique[:10]}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:32': {'funding_count': 276, 'civic_docs_count': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}}

exec(code, env_args)
