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
    lines = text.split('\n')
    
    in_design_section = False
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        # Track when we are in a design section
        if '(Design)' in line_clean:
            in_design_section = True
            continue
        
        if any(x in line_clean for x in ['(Construction)', '(Completed)', '(Not Started)']):
            in_design_section = False
            continue
        
        if not in_design_section:
            continue
        
        # Skip non-content lines
        if not line_clean or 'Page' in line_clean or 'Agenda Item' in line_clean:
            continue
        
        # Look for project names (reasonable length, not headers)
        if len(line_clean) > 15 and i + 2 < len(lines):
            line_next1 = lines[i+1].strip()
            line_next2 = lines[i+2].strip()
            
            # Check if followed by project descriptions
            if 'Updates' in line_next1 or 'Schedule' in line_next1 or 'Description' in line_next1 or 'Updates' in line_next2 or 'Schedule' in line_next2:
                project_name = line_clean
                
                # Skip common headers
                if any(x in project_name for x in ['Capital Improvement Projects', 'DISCUSSION', 'RECOMMENDED ACTION']):
                    continue
                
                # Check if it's a capital project (not disaster/FEMA)
                name_lower = project_name.lower()
                is_disaster = 'fema' in name_lower or 'caloes' in name_lower or 'disaster' in name_lower
                
                if not is_disaster:
                    capital_design_projects.append(project_name)

# Get unique projects
capital_design_unique = list(set(capital_design_projects))

# Match with funding data (> 50000)
matched_projects = []

for proj in capital_design_unique:
    proj_lower = proj.lower()
    
    for _, fund in funding_df.iterrows():
        fund_name = fund['Project_Name']
        
        # Check for name overlap
        if proj_lower in fund_name.lower() or fund_name.lower() in proj_lower:
            if fund['Amount'] > 50000:
                matched_projects.append(proj)
                break

# Result
count = len(matched_projects)

print('__RESULT__:')
print(json.dumps({'count_design_capital_over_50000': count}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': {'funding_records_over_50000': 276}, 'var_functions.list_db:6': ['civic_docs'], 'var_functions.list_db:8': ['civic_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_documents': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
