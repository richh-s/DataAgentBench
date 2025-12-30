code = """import json
import re
import pandas as pd

with open('var_function-call-1460894796141311373', 'r') as f:
    civic_docs = json.load(f)

with open('var_function-call-16354438159657144766', 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

target_projects = set()

spring_2022_patterns = [
    r'Spring 2022', r'Spring, 2022',
    r'March 2022', r'March, 2022',
    r'April 2022', r'April, 2022',
    r'May 2022', r'May, 2022',
    r'2022-Spring', r'2022-03', r'2022-04', r'2022-05'
]

def is_spring_2022(text_chunk):
    match = re.search(r'Begin Construction:\s*(.*)', text_chunk, re.IGNORECASE)
    if match:
        date_str = match.group(1).strip()
        for pat in spring_2022_patterns:
            if re.search(pat, date_str, re.IGNORECASE):
                return True
    return False

newline_char = chr(10)

for doc in civic_docs:
    text = doc['text']
    lines = text.split(newline_char)
    
    project_starts = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        has_update = 'Updates:' in line
        has_desc = 'Project Description:' in line
        has_schedule = 'Project Schedule' in line
        
        if (has_update or has_desc) and not has_schedule:
             # Look back
             j = i - 1
             while j >= 0 and not lines[j].strip():
                 j -= 1
             if j >= 0:
                 project_name = lines[j].strip()
                 if 'Capital Improvement Projects' not in project_name:
                     project_starts.append((j, project_name))
        i += 1
        
    for k in range(len(project_starts)):
        start_idx, name = project_starts[k]
        end_idx = project_starts[k+1][0] if k + 1 < len(project_starts) else len(lines)
        
        block_lines = lines[start_idx:end_idx]
        block_text = newline_char.join(block_lines)
        
        if is_spring_2022(block_text):
            target_projects.add(name)

matched = funding_df[funding_df['Project_Name'].isin(target_projects)]
count = len(matched)
total_funding = matched['Amount'].astype(int).sum()

result = {
    'count': count,
    'total_funding': int(total_funding),
    'projects': matched['Project_Name'].tolist(),
    'target_projects_debug': list(target_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-5721682823366817575': 'file_storage/function-call-5721682823366817575.json', 'var_function-call-1460894796141311373': 'file_storage/function-call-1460894796141311373.json', 'var_function-call-16354438159657144766': 'file_storage/function-call-16354438159657144766.json'}

exec(code, env_args)
