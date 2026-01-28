code = """import json
import pandas as pd

# Access the file paths from the variables
path_civic = locals()['var_function-call-16246873831533624735']
path_funding = locals()['var_function-call-7325626147316931914']

with open(path_civic, 'r') as f:
    civic_docs = json.load(f)
    
with open(path_funding, 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
projects_started_spring_2022 = set()

spring_tokens = [
    "spring 2022", "2022-spring", "spring, 2022",
    "march 2022", "april 2022", "may 2022",
    "03/2022", "04/2022", "05/2022",
    "03-2022", "04-2022", "05-2022",
    "2022-03", "2022-04", "2022-05"
]

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
        
        for bl in block_lines:
            lbl = bl.lower()
            if "begin construction" in lbl or "start date" in lbl:
                is_match = False
                for token in spring_tokens:
                    if token in lbl:
                        is_match = True
                        break
                if is_match:
                    projects_started_spring_2022.add(p_name)
                    break 

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
    "projects": matched_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16246873831533624735': 'file_storage/function-call-16246873831533624735.json', 'var_function-call-7325626147316931914': 'file_storage/function-call-7325626147316931914.json'}

exec(code, env_args)
