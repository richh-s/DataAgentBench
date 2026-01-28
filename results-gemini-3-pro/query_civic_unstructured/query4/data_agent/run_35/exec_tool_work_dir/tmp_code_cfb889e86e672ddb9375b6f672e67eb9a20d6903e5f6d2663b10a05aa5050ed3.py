code = """import json
import re
import pandas as pd

with open('var_function-call-16246873831533624735.json', 'r') as f:
    civic_docs = json.load(f)
    
with open('var_function-call-7325626147316931914.json', 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

projects_started_spring_2022 = set()

for doc in civic_docs:
    lines = doc['text'].splitlines()
    
    project_indices = []
    for i, line in enumerate(lines):
        if '(cid:190)' in line:
            k = i - 1
            while k >= 0:
                stripped = lines[k].strip()
                if stripped:
                    project_indices.append((k, stripped))
                    break
                k -= 1
                
    for j in range(len(project_indices)):
        start_line_idx, p_name = project_indices[j]
        
        if j < len(project_indices) - 1:
            end_line_idx = project_indices[j+1][0]
        else:
            end_line_idx = len(lines)
            
        block_lines = lines[start_line_idx:end_line_idx]
        block_text = '\n'.join(block_lines)
        
        # Regex needs double backslashes for \s, \n inside the string passed to tool
        match = re.search(r'(?:Begin Construction|Start Date|Construction Start)[:\s]+(.*?)(?:\n|$)', block_text, re.IGNORECASE)
        if match:
            date_str = match.group(1).strip()
            
            is_match = False
            ds = date_str.lower()
            
            if 'spring 2022' in ds or '2022-spring' in ds or 'spring, 2022' in ds:
                is_match = True
            elif '2022' in ds:
                if 'march' in ds or 'april' in ds or 'may' in ds:
                    is_match = True
                if re.search(r'(03|04|05)[/-]2022', ds) or re.search(r'2022[/-](03|04|05)', ds):
                    is_match = True
            
            if is_match:
                projects_started_spring_2022.add(p_name)

matched_projects = []
total_funding = 0

unique_projects = list(projects_started_spring_2022)

for index, row in df_funding.iterrows():
    f_name = row['Project_Name'].strip()
    if f_name in unique_projects:
        matched_projects.append(f_name)
        total_funding += row['Amount']

result = {
    "count": len(matched_projects),
    "total_funding": total_funding,
    "projects": matched_projects,
    "debug_project_names": unique_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16246873831533624735': 'file_storage/function-call-16246873831533624735.json', 'var_function-call-7325626147316931914': 'file_storage/function-call-7325626147316931914.json'}

exec(code, env_args)
