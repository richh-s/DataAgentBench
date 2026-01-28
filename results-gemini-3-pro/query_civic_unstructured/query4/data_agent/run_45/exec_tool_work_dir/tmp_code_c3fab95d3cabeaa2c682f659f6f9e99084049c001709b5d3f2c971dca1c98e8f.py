code = """import json
import re

# Load data
civic_docs_key = 'var_function-call-11755073423388004543'
funding_data_key = 'var_function-call-11755073423388006536'

with open(locals()[civic_docs_key], 'r') as f:
    civic_docs = json.load(f)

with open(locals()[funding_data_key], 'r') as f:
    funding_data = json.load(f)

# Valid projects
valid_projects = set(item['Project_Name'] for item in funding_data)

# Regex for finding start dates in Spring 2022
# We look for 'Begin Construction' or 'Start' followed by Spring/March/April/May 2022
start_keywords = ['Begin Construction', 'Construction Start', 'Start Date', 'Scheduled Start']
time_keywords = ['Spring', 'March', 'April', 'May']
year_keyword = '2022'

projects_spring_2022 = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if line is a project name
        if line in valid_projects:
            current_project = line
            continue
        
        if current_project:
            # Check if line contains start info
            is_start_line = False
            for k in start_keywords:
                if k.lower() in line.lower():
                    is_start_line = True
                    break
            
            if is_start_line:
                # Check for Spring 2022
                has_year = year_keyword in line
                has_time = False
                for t in time_keywords:
                    if t.lower() in line.lower():
                        has_time = True
                        break
                
                if has_year and has_time:
                    projects_spring_2022.add(current_project)

# Calculate funding
total_funding = 0
project_count = 0
final_projects = []

for p in projects_spring_2022:
    p_funding = 0
    found = False
    for record in funding_data:
        if record['Project_Name'] == p:
            p_funding += int(record['Amount'])
            found = True
    
    if found:
        total_funding += p_funding
        project_count += 1
        final_projects.append(p)

print('__RESULT__:')
print(json.dumps({
    'count': project_count,
    'total_funding': total_funding,
    'projects': final_projects
}))"""

env_args = {'var_function-call-11755073423388006536': 'file_storage/function-call-11755073423388006536.json', 'var_function-call-11755073423388004543': 'file_storage/function-call-11755073423388004543.json'}

exec(code, env_args)
