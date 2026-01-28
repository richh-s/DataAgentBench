code = """import json
import pandas as pd

# Load data
funding_path = locals().get('var_functions.query_db:2', '')
if isinstance(funding_path, str) and funding_path:
    with open(funding_path) as f:
        funding = json.load(f)
else:
    funding = locals().get('var_functions.query_db:2', [])

funding_df = pd.DataFrame(funding)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

docs_path = locals().get('var_functions.query_db:10', '')
if isinstance(docs_path, str) and docs_path:
    with open(docs_path) as f:
        docs = json.load(f)
else:
    docs = locals().get('var_functions.query_db:10', [])

# Extract design capital projects
design_capital = []

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design = False
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        # Track sections
        if '(Design)' in line_clean:
            in_design = True
            continue
        if any(x in line_clean for x in ['(Construction)', '(Completed)', '(Not Started)']):
            in_design = False
            continue
            
        if not in_design:
            continue
        
        # Skip metadata
        if not line_clean or 'Page' in line_clean or 'Agenda Item' in line_clean:
            continue
        
        # Extract project names
        if len(line_clean) > 15 and i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if len(next_line) > 0:
                # Skip disaster projects
                line_lower = line_clean.lower()
                if 'fema' not in line_lower and 'caloes' not in line_lower:
                    design_capital.append(line_clean)

# Get unique projects
unique_projects = list(set(design_capital))

# Match with funding > 50000
count = 0
matched = []

for proj in unique_projects:
    proj_lower = proj.lower()
    
    for _, fund in funding_df.iterrows():
        if proj_lower in fund['Project_Name'].lower() or fund['Project_Name'].lower() in proj_lower:
            if fund['Amount'] > 50000:
                count += 1
                matched.append(proj)
                break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': {'funding_records_over_50000': 276}, 'var_functions.list_db:6': ['civic_docs'], 'var_functions.list_db:8': ['civic_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_documents': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
