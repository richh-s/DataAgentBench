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

# Extract capital design projects from documents
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Check for design section
        if line.find('(Design)') >= 0:
            in_design_section = True
            continue
        
        # Exit design section when hitting other sections
        if line.find('(Construction)') >= 0 or line.find('(Completed)') >= 0 or line.find('(Not Started)') >= 0:
            in_design_section = False
            continue
        
        if not in_design_section:
            continue
        
        # Skip empty lines and page markers
        if not line or line.find('Page') >= 0 or line.find('Agenda Item') >= 0:
            continue
        
        # Look for project names (reasonable length, not headers)
        if len(line) > 15 and i + 2 < len(lines):
            # Check if followed by project indicators
            next_content = lines[i+1] + lines[i+2]
            if next_content.find('Updates') >= 0 or next_content.find('Schedule') >= 0 or next_content.find('Description') >= 0:
                # Skip common headers
                if line.find('Capital Improvement Projects') >= 0 or line.find('DISCUSSION') >= 0 or line.find('RECOMMENDED ACTION') >= 0:
                    continue
                
                # Determine if disaster project
                line_lower = line.lower()
                if line_lower.find('fema') >= 0 or line_lower.find('caloes') >= 0 or line_lower.find('disaster') >= 0:
                    continue  # Skip disaster projects
                
                capital_design_projects.append(line)

# Get unique project names
capital_design_unique = list(set(capital_design_projects))

# Match with funding data
count = 0

for proj in capital_design_unique:
    proj_lower = proj.lower()
    
    for _, fund in funding_df.iterrows():
        fund_name = fund['Project_Name']
        fund_lower = fund_name.lower()
        
        # Check if project names match
        if proj_lower.find(fund_lower) >= 0 or fund_lower.find(proj_lower) >= 0:
            if fund['Amount'] > 50000:
                count += 1
                break

result = {'count_design_capital_funding_over_50000': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': {'funding_records_over_50000': 276}, 'var_functions.list_db:6': ['civic_docs'], 'var_functions.list_db:8': ['civic_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_documents': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
