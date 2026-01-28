code = """import json, pandas as pd

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

# Extract capital design projects from documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        # Track design sections
        if '(Design)' in line_clean:
            in_design_section = True
            continue
        
        if any(marker in line_clean for marker in ['(Construction)', '(Completed)', '(Not Started)']):
            in_design_section = False
            continue
        
        if not in_design_section:
            continue
        
        # Skip metadata
        if not line_clean or 'Page' in line_clean or 'Agenda Item' in line_clean:
            continue
        
        # Look for project names
        if len(line_clean) > 15 and i + 2 < len(lines):
            # Check if line is followed by project description
            next1 = lines[i + 1]
            next2 = lines[i + 2]
            
            has_updates = 'Updates' in next1 or 'Updates' in next2
            has_schedule = 'Schedule' in next1 or 'Schedule' in next2
            has_description = 'Description' in next1 or 'Description' in next2
            
            if has_updates or has_schedule or has_description:
                # Skip disaster projects
                if 'fema' not in line_clean.lower() and 'caloes' not in line_clean.lower():
                    projects.append(line_clean)

# Get unique projects
unique_projects = list(set(projects))

# Count matches with funding > 50000
count = 0

for proj in unique_projects:
    proj_lower = proj.lower()
    
    for _, fund_row in funding_df.iterrows():
        fund_name = fund_row['Project_Name'].lower()
        
        # Check for name overlap
        if proj_lower in fund_name or fund_name in proj_lower:
            if fund_row['Amount'] > 50000:
                count += 1
                break

result = {'count_design_capital_over_50000': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': {'funding_records_over_50000': 276}, 'var_functions.list_db:6': ['civic_docs'], 'var_functions.list_db:8': ['civic_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_documents': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
