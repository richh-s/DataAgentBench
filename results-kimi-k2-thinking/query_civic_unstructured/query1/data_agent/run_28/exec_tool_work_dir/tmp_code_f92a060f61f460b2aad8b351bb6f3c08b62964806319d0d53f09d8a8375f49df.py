code = """import json
import re

funding_path = locals()['var_functions.query_db:5']
civic_docs_path = locals()['var_functions.query_db:8']

funding = json.load(open(funding_path))
docs = json.load(open(civic_docs_path))

def extract_projects(docs):
    projects = []
    for doc in docs:
        txt = doc['text']
        pattern = r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(|Disaster Recovery Projects \(|$)'
        m = re.search(pattern, txt, re.DOTALL)
        if m:
            section = m.group(1)
            for line in section.splitlines():
                line = line.strip()
                if line and len(line) > 10:
                    if not line.startswith(('(', 'cid', '•', '-')) and not line.endswith(':'):
                        if all(x not in line for x in ['Updates:', 'Schedule:', 'Complete Design', 'Advertise:', 'Begin Construction']):
                            clean = re.sub(r'\s*-\s*', '', line)
                            clean = re.sub(r'\(.*?\)$', '', clean).strip()
                            clean = re.sub(r'^\d+\.\s*', '', clean)
                            if clean:
                                projects.append({'Project_Name': clean, 'status': 'design', 'type': 'capital'})
    return projects

extracted = extract_projects(docs)
unique = list({p['Project_Name']: p for p in extracted}.values())

print('__RESULT__:')
print(json.dumps({'extracted_count': len(extracted), 'unique_count': len(unique), 'sample': unique[:8]}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:32': {'funding_count': 276, 'civic_docs_count': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}}

exec(code, env_args)
