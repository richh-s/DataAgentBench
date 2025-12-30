code = """import json
import pandas as pd
import re
import datetime

# Load Funding Data
with open(locals()['var_function-call-17289363314070391295'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

# Load Civic Docs
with open(locals()['var_function-call-14887521830663367550'], 'r') as f:
    civic_docs = json.load(f)

def extract_date(filename):
    match = re.search(r'(\d{2})(\d{2})(\d{4})', filename)
    if match:
        return datetime.datetime(int(match.group(3)), int(match.group(1)), int(match.group(2)))
    return datetime.datetime.min

civic_docs.sort(key=lambda x: extract_date(x['filename']), reverse=True)

header_pattern = re.compile(r'(Capital Improvement Projects|Disaster Recovery Projects)\s*\((Design|Construction|Not Started|Completed)\)', re.IGNORECASE)

relevant_projects = []

for index, row in funding_df.iterrows():
    project_name = row['Project_Name']
    funding_source = row['Funding_Source']
    amount = row['Amount']
    
    name_relevant = False
    if 'FEMA' in project_name.upper() or 'EMERGENCY' in project_name.upper():
        name_relevant = True
        
    status = 'not started'
    found_in_doc = False
    is_relevant_in_text = False
    
    norm_project_name = ' '.join(project_name.split())
    
    for doc in civic_docs:
        text = doc['text']
        
        if norm_project_name.lower() in ' '.join(text.split()).lower():
            
            lines = text.split('\n')
            current_section_status = None
            
            for line in lines:
                h_match = header_pattern.search(line)
                if h_match:
                    s_str = h_match.group(2).lower()
                    if 'design' in s_str: current_section_status = 'design'
                    elif 'construction' in s_str: current_section_status = 'construction'
                    elif 'not started' in s_str: current_section_status = 'not started'
                
                if norm_project_name.lower() in ' '.join(line.split()).lower():
                    if current_section_status:
                        status = current_section_status
                    
                    found_in_doc = True
                    
                    start_idx = text.lower().find(project_name.lower())
                    if start_idx == -1:
                        start_idx = text.lower().find(norm_project_name.lower())
                        
                    if start_idx != -1:
                        context = text[start_idx:start_idx+800]
                        if 'fema' in context.lower() or 'emergency' in context.lower():
                            is_relevant_in_text = True
                        if 'construction was completed' in context.lower() or 'project was completed' in context.lower() or 'notice of completion' in context.lower():
                            status = 'completed'
                            
                    break
            
            if found_in_doc:
                break
    
    if name_relevant or is_relevant_in_text:
        relevant_projects.append({
            'Project_Name': project_name,
            'Funding_Source': funding_source,
            'Amount': amount,
            'Status': status
        })

print('__RESULT__:')
print(json.dumps(relevant_projects))"""

env_args = {'var_function-call-14887521830663364851': ['civic_docs'], 'var_function-call-14887521830663367550': 'file_storage/function-call-14887521830663367550.json', 'var_function-call-17289363314070391640': ['Funding'], 'var_function-call-17289363314070391295': 'file_storage/function-call-17289363314070391295.json'}

exec(code, env_args)
