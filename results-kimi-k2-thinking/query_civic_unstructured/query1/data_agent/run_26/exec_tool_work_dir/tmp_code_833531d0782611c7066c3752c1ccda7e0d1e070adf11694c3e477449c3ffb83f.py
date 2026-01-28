code = """import json

funding_path = var_functions.query_db:0
civic_path = var_functions.query_db:2

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

funded_lookup = {rec['Project_Name'].strip().lower(): int(rec['Amount']) for rec in funding_data}

project_names = []
for doc in civic_docs:
    text = doc.get('text', '')
    text_upper = text.upper()
    
    if 'CAPITAL IMPROVEMENT PROJECTS (DESIGN)' in text_upper:
        start_idx = text_upper.index('CAPITAL IMPROVEMENT PROJECTS (DESIGN)')
        end_idx = text_upper.find('CAPITAL IMPROVEMENT PROJECTS (CONSTRUCTION)', start_idx)
        if end_idx == -1:
            end_idx = len(text)
        
        section = text[start_idx:end_idx]
        lines = section.split('\n')
        
        for i, line in enumerate(lines):
            line_clean = line.strip()
            if line_clean and len(line_clean) > 5:
                if i + 1 < len(lines) and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]):
                    if '▪' not in line_clean and 'Updates:' not in line_clean and 'Project Schedule:' not in line_clean:
                        if 'Capital Improvement' not in line_clean and 'Page' not in line_clean and 'RECOMMENDED' not in line_clean:
                            project_names.append(line_clean.lower())

count = 0
for name in project_names:
    if name in funded_lookup and funded_lookup[name] > 50000:
        count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
