code = """import json
import re

file_path = locals()['var_function-call-13876112048585230110']
with open(file_path, 'r') as f:
    docs = json.load(f)

projects = []
# Regex for start date
date_pattern = re.compile(r'(Begin Construction|Construction Start)[:\s]+([A-Za-z0-9\s,]+)', re.IGNORECASE)
spring_2022_patterns = ['spring 2022', 'march 2022', 'april 2022', 'may 2022']

def is_spring_2022(date_str):
    ds = date_str.lower()
    for p in spring_2022_patterns:
        if p in ds:
            return True
    return False

extracted_projects = []

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    project_start_lines = []
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line: continue
        
        found_marker = False
        for j in range(i + 1, min(i + 5, len(lines))):
            next_line = lines[j].strip()
            if not next_line: continue
            if ('Updates:' in next_line or 'Project Description:' in next_line or 'Project Updates:' in next_line):
                found_marker = True
            break
        
        if ('Updates:' in line or 'Project Description:' in line):
            continue

        if found_marker:
            project_start_lines.append(i)
            
    for k in range(len(project_start_lines)):
        start_idx = project_start_lines[k]
        end_idx = project_start_lines[k+1] if k < len(project_start_lines) - 1 else len(lines)
        
        p_name = lines[start_idx].strip()
        p_text = '\n'.join(lines[start_idx+1 : end_idx])
        
        matches = date_pattern.findall(p_text)
        
        for label, date_str in matches:
             if is_spring_2022(date_str):
                 extracted_projects.append(p_name)
                 break

print('__RESULT__:')
print(json.dumps(extracted_projects))"""

env_args = {'var_function-call-11551916714829244463': 'file_storage/function-call-11551916714829244463.json', 'var_function-call-11551916714829245086': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-13876112048585230110': 'file_storage/function-call-13876112048585230110.json'}

exec(code, env_args)
