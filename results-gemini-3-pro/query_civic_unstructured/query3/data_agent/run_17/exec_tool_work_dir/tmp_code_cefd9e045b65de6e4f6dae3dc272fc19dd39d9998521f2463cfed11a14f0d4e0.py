code = """import json
import pandas as pd

# Load funding data
funding_path = locals()['var_function-call-5188433826363097598']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load civic docs
docs_path = locals()['var_function-call-7088797317398377498']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)

projects = []

for doc in docs_data:
    text = doc['text']
    lines = text.split('\n')
    
    current_status = None
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Detect Section Headers
        if 'Capital Improvement Projects (Design)' in line:
            current_status = 'design'
            continue
        elif 'Capital Improvement Projects (Construction)' in line:
            current_status = 'construction' 
            continue
        elif 'Capital Improvement Projects (Not Started)' in line:
            current_status = 'not started'
            continue
            
        # Heuristic for project name
        is_bullet = line.startswith('(cid:') or line.startswith('-')
        is_keyword = line.startswith('Updates:') or line.startswith('Project Schedule:') or line.startswith('Estimated Schedule:') or line.startswith('Project Description:')
        
        # Look ahead
        next_line = ''
        for j in range(i + 1, len(lines)):
            if lines[j].strip():
                next_line = lines[j].strip()
                break
        
        is_project_start = False
        if current_status and not is_bullet and not is_keyword:
            if next_line.startswith('(cid:') or next_line.startswith('Updates:') or next_line.startswith('Project Description:') or next_line.startswith('Project Updates:'):
                is_project_start = True
                if 'Page' in line and 'of' in line: is_project_start = False
                if 'Agenda Item' in line: is_project_start = False
                if 'Public Works' in line and 'Commission' in line: is_project_start = False
                
        if is_project_start:
            if current_project:
                projects.append(current_project)
            
            current_project = {
                'Project_Name': line,
                'status': current_status,
                'text_lines': [],
                'st': None,
                'et': None
            }
        elif current_project:
            current_project['text_lines'].append(line)

    if current_project:
        projects.append(current_project)

final_projects = []
for p in projects:
    full_text = ' '.join(p['text_lines'])
    
    # Refine status
    status = p['status']
    if 'Construction was completed' in full_text or 'Notice of completion filed' in full_text:
        status = 'completed'
    
    # Extract dates
    st = None
    et = None
    
    for line in p['text_lines']:
        lower_line = line.lower()
        if 'begin construction' in lower_line:
            if ':' in line:
                st = line.split(':', 1)[1].strip()
        if 'complete construction' in lower_line:
            if ':' in line:
                et = line.split(':', 1)[1].strip()
        
    p['st'] = st
    p['et'] = et
    p['status'] = status
    
    # Check relevance
    is_related = False
    name_upper = p['Project_Name'].upper()
    text_upper = full_text.upper()
    
    if 'EMERGENCY' in name_upper or 'FEMA' in name_upper:
        is_related = True
    elif 'EMERGENCY' in text_upper or 'FEMA' in text_upper:
        is_related = True
        
    if is_related:
        final_projects.append(p)

extracted_df = pd.DataFrame(final_projects)

if not extracted_df.empty:
    merged = pd.merge(extracted_df, funding_df, on='Project_Name', how='inner')
    result_df = merged[['Project_Name', 'Funding_Source', 'Amount', 'status', 'st', 'et']]
    result = result_df.to_dict(orient='records')
else:
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-1936795018027182717': ['Funding'], 'var_function-call-1936795018027181912': 'file_storage/function-call-1936795018027181912.json', 'var_function-call-5188433826363097598': 'file_storage/function-call-5188433826363097598.json', 'var_function-call-7088797317398377498': 'file_storage/function-call-7088797317398377498.json'}

exec(code, env_args)
