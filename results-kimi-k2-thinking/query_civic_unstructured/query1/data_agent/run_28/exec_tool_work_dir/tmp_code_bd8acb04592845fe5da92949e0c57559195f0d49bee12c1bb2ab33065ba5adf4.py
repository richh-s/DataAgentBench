code = """import json, re

funding_path = locals()['var_functions.query_db:5']
civic_docs_path = locals()['var_functions.query_db:8']

funding_data = json.load(open(funding_path))
civic_docs_data = json.load(open(civic_docs_path))

def extract_projects(docs):
    projects = []
    for doc in docs:
        text = doc['text']
        pattern = 'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(|Disaster Recovery Projects \(|$)'
        matches = re.finditer(pattern, text, re.DOTALL)
        for match in matches:
            section = match.group(1)
            lines = section.split('\n')
            for line in lines:
                line = line.strip()
                if (line and not line.startswith('(') and not line.startswith('cid:') and len(line) > 10
                    and 'Updates:' not in line and 'Schedule:' not in line and 'Complete Design:' not in line
                    and 'Advertise:' not in line and 'Begin Construction:' not in line):
                    clean = re.sub('\s*-\s*', '', line)
                    clean = re.sub('\(.*\)$', '', clean).strip()
                    clean = re.sub('^\d+\s*\.\s*', '', clean)
                    if clean and not clean.endswith(':'):
                        projects.append({'Project_Name': clean, 'status': 'design', 'type': 'capital'})
    return projects

extracted_projects = extract_projects(civic_docs_data)
unique_projects = list({p['Project_Name']: p for p in extracted_projects}.values())

print('__RESULT__:')
result = {'extracted': len(extracted_projects), 'unique': len(unique_projects), 'sample': unique_projects[:10]}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:32': {'funding_count': 276, 'civic_docs_count': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}}

exec(code, env_args)
