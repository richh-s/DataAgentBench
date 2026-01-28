code = """import json, pandas as pd, re

# Load data
fpath = locals().get('var_functions.query_db:2', '')
if isinstance(fpath, str) and fpath:
    with open(fpath, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = locals().get('var_functions.query_db:2', [])

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

dpath = locals().get('var_functions.query_db:10', '')
if isinstance(dpath, str) and dpath:
    with open(dpath, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = locals().get('var_functions.query_db:10', [])

# Extract capital projects with design status
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    lines = text.split('\n')
    
    in_design_section = False
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        # Track when we enter/exit design sections
        if '(Design)' in line_clean:
            in_design_section = True
            continue
        
        if any(x in line_clean for x in ['(Construction)', '(Completed)', '(Not Started)']):
            in_design_section = False
            continue
        
        # Skip processing if not in design section
        if not in_design_section:
            continue
        
        # Skip metadata lines
        if not line_clean or 'Page' in line_clean or 'Agenda Item' in line_clean:
            continue
        
        if line_clean.startswith('To:') or line_clean.startswith('From:') or line_clean.startswith('Date:'):
            continue
        
        # Look for potential project names (reasonable length and followed by project details)
        if len(line_clean) > 15 and i + 2 < len(lines):
            next_content = lines[i+1] + lines[i+2]
            if 'Updates' in next_content or 'Schedule' in next_content or 'Description' in next_content:
                project_name = line_clean
                
                # Skip common headers
                if any(x in project_name for x in ['Capital Improvement Projects', 'DISCUSSION', 'RECOMMENDED ACTION']):
                    continue
                
                # Determine project type
                is_disaster = 'fema' in project_name.lower() or 'caloes' in project_name.lower()
                project_type = 'disaster' if is_disaster else 'capital'
                
                if project_type == 'capital':
                    capital_design_projects.append(project_name)

# Count unique capital design projects with funding > 50000
matched = []
for proj_name in capital_design_projects:
    proj_lower = proj_name.lower()
    
    for _, fund in funding_df.iterrows():
        fund_name = fund['Project_Name']
        fund_lower = fund_name.lower()
        
        # Check if project names overlap
        name_match = proj_lower in fund_lower or fund_lower in proj_lower
        
        if name_match:
            if fund['Amount'] > 50000:
                matched.append(proj_name)
                break

# Get count of unique projects
unique_count = len(set(matched))

result = {'count_design_capital_over_50000': unique_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': {'funding_records_over_50000': 276}, 'var_functions.list_db:6': ['civic_docs'], 'var_functions.list_db:8': ['civic_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_documents': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
