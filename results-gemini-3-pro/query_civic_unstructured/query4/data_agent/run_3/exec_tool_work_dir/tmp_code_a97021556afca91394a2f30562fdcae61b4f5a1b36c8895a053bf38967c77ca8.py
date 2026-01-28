code = """import json

file_path = locals()['var_function-call-13876112048585230110']
with open(file_path, 'r') as f:
    docs = json.load(f)

extracted_projects = []
spring_keywords = ['spring 2022', 'march 2022', 'april 2022', 'may 2022', 'mar 2022', 'apr 2022']

for doc in docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    
    project_start_lines = []
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line: continue
        
        found_marker = False
        # Look ahead for marker
        for j in range(i + 1, min(i + 5, len(lines))):
            next_line = lines[j].strip()
            if not next_line: continue
            if 'Updates:' in next_line or 'Project Description:' in next_line or 'Project Updates:' in next_line:
                found_marker = True
            break
        
        if 'Updates:' in line or 'Project Description:' in line:
            continue

        if found_marker:
            project_start_lines.append(i)
            
    for k in range(len(project_start_lines)):
        start_idx = project_start_lines[k]
        end_idx = project_start_lines[k+1] if k < len(project_start_lines) - 1 else len(lines)
        
        p_name = lines[start_idx].strip()
        
        # Check block content
        start_date_found = False
        for m in range(start_idx + 1, end_idx):
            content_line = lines[m].lower()
            if 'begin construction' in content_line or 'construction start' in content_line or 'start date' in content_line:
                for sk in spring_keywords:
                    if sk in content_line:
                        start_date_found = True
                        break
            if start_date_found: break
        
        if start_date_found:
            extracted_projects.append(p_name)

print('__RESULT__:')
print(json.dumps(extracted_projects))"""

env_args = {'var_function-call-11551916714829244463': 'file_storage/function-call-11551916714829244463.json', 'var_function-call-11551916714829245086': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-13876112048585230110': 'file_storage/function-call-13876112048585230110.json'}

exec(code, env_args)
