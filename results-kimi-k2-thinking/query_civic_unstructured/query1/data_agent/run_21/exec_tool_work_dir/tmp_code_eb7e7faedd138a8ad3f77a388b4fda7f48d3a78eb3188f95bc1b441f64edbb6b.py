code = """import json, pandas as pd, re

# Load funding data
fpath = locals().get('var_functions.query_db:2', '')
if isinstance(fpath, str) and fpath:
    with open(fpath, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = locals().get('var_functions.query_db:2', [])

f funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Load civic documents
dpath = locals().get('var_functions.query_db:10', '')
if isinstance(dpath, str) and dpath:
    with open(dpath, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = locals().get('var_functions.query_db:10', [])

# Extract capital design projects
capital_design = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design = False
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        if '(Design)' in line:
            in_design = True
            continue
        
        if any(x in line for x in ['(Construction)', '(Completed)', '(Not Started)']):
            in_design = False
            continue
        
        if not in_design:
            continue
        
        if not line or 'Page' in line or 'Agenda Item' in line:
            continue
        
        if i + 2 < len(lines) and len(line) > 15:
            next1 = lines[i + 1]
            next2 = lines[i + 2]
            combined_next = next1 + next2
            
            if 'Updates' in combined_next or 'Schedule' in combined_next:
                is_disaster = 'fema' in line.lower() or 'caloes' in line.lower()
                
                if not is_disaster:
                    capital_design.append(line)

# Match with funding
capital_design_unique = list(set(capital_design))
matched = []

for proj in capital_design_unique:
    proj_lower = proj.lower()
    
    for _, fund in funding_df.iterrows():
        if proj_lower in fund['Project_Name'].lower() or fund['Project_Name'].lower() in proj_lower:
            if fund['Amount'] > 50000:
                matched.append(proj)
                break

result = {'count': len(matched)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': {'funding_records_over_50000': 276}, 'var_functions.list_db:6': ['civic_docs'], 'var_functions.list_db:8': ['civic_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_documents': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
