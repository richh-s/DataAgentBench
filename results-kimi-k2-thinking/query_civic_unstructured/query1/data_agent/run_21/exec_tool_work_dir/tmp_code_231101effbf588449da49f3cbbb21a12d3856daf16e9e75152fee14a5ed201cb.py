code = """import json, pandas as pd

# Load funding data
fpath = locals().get('var_functions.query_db:2', '')
if isinstance(fpath, str) and fpath:
    with open(fpath, 'r') as f:
        funding = json.load(f)
else:
    funding = locals().get('var_functions.query_db:2', [])

funding_df = pd.DataFrame(funding)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Load civic documents
dpath = locals().get('var_functions.query_db:10', '')
if isinstance(dpath, str) and dpath:
    with open(dpath, 'r') as f:
        docs = json.load(f)
else:
    docs = locals().get('var_functions.query_db:10', [])

# Extract projects from documents
capital_design_projects = []

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        if '(Design)' in line_clean:
            in_design_section = True
            continue
        
        if any(marker in line_clean for marker in ['(Construction)', '(Completed)', '(Not Started)']):
            in_design_section = False
            continue
        
        if not in_design_section:
            continue
        
        if not line_clean or 'Page' in line_clean or 'Agenda Item' in line_clean:
            continue
        
        if len(line_clean) > 15 and i + 2 < len(lines):
            next_lines = lines[i+1] + lines[i+2]
            if 'Updates' in next_lines or 'Schedule' in next_lines:
                if 'fema' not in line_clean.lower() and 'caloes' not in line_clean.lower() and 'disaster' not in line_clean.lower():
                    capital_design_projects.append(line_clean)

# Get unique projects
capital_design_unique = list(set(capital_design_projects))

# Match with funding data
count = 0

for proj in capital_design_unique:
    proj_lower = proj.lower()
    
    for _, fund in funding_df.iterrows():
        fund_name = fund['Project_Name'].lower()
        
        if proj_lower in fund_name or fund_name in proj_lower:
            if fund['Amount'] > 50000:
                count += 1
                break

result = {'count_design_capital_over_50000': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': {'funding_records_over_50000': 276}, 'var_functions.list_db:6': ['civic_docs'], 'var_functions.list_db:8': ['civic_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_documents': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
