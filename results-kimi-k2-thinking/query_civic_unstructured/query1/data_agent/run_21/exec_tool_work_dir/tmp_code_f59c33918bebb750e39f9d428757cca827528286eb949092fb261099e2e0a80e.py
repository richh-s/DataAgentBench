code = """import json, pandas as pd, re

# Load funding data
fpath = locals().get('var_functions.query_db:2', '')
if isinstance(fpath, str) and fpath:
    with open(fpath, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = locals().get('var_functions.query_db:2', [])

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Load civic documents
dpath = locals().get('var_functions.query_db:10', '')
if isinstance(dpath, str) and dpath:
    with open(dpath, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = locals().get('var_functions.query_db:10', [])

# Extract design projects
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design = False
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        # Track section
        if '(Design)' in line_clean:
            in_design = True
            continue
        if any(x in line_clean for x in ['(Construction)', '(Completed)', '(Not Started)']):
            in_design = False
            continue
        
        # Skip non-content lines
        if not line_clean or 'Page' in line_clean or 'Agenda Item' in line_clean:
            continue
        
        # Extract project names in design section
        if in_design and len(line_clean) > 10:
            # Check for headers to skip
            if any(line_clean.startswith(x) for x in ['To:', 'From:', 'Date:', 'Subject:']):
                continue
            
            # Check if followed by project content
            if i + 2 < len(lines) and ('Updates' in lines[i+1] + lines[i+2] or 'Schedule' in lines[i+1] + lines[i+2]):
                ptype = 'disaster' if 'fema' in line_clean.lower() or 'caloes' in line_clean.lower() else 'capital'
                projects.append({'Project_Name': line_clean, 'status': 'design', 'type': ptype})

# Filter capital design projects
capital_design = [p for p in projects if p['type'] == 'capital']

# Match with funding data
matched = []
for proj in capital_design:
    pname = proj['Project_Name'].lower()
    for _, fund in funding_df.iterrows():
        if pname in fund['Project_Name'].lower() or fund['Project_Name'].lower() in pname:
            if fund['Amount'] > 50000:
                matched.append(proj['Project_Name'])
                break

# Count unique projects
count = len(set(matched))

result = {'count': count, 'sample': matched[:5]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': {'funding_records_over_50000': 276}, 'var_functions.list_db:6': ['civic_docs'], 'var_functions.list_db:8': ['civic_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_documents': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
