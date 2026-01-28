code = """import json
import re

# Load data
with open(locals()['var_function-call-8238280487498580574'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-8238280487498581651'], 'r') as f:
    civic_docs = json.load(f)

# Get all project names from funding table
project_names = sorted(list(set(item['Project_Name'] for item in funding_data)), key=len, reverse=True)

# Define Spring 2022 patterns
spring_2022_patterns = [
    r'Spring 2022',
    r'March 2022',
    r'April 2022',
    r'May 2022',
    r'March, 2022',
    r'April, 2022',
    r'May, 2022'
]

def is_spring_2022(date_str):
    if not date_str:
        return False
    for pat in spring_2022_patterns:
        if re.search(pat, date_str, re.IGNORECASE):
            return True
    return False

found_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    project_indices = []
    for pname in project_names:
        start = 0
        while True:
            idx = text.find(pname, start)
            if idx == -1:
                break
            project_indices.append((idx, pname))
            start = idx + len(pname)
            
    project_indices.sort(key=lambda x: x[0])
    
    for i in range(len(project_indices)):
        start_idx, pname = project_indices[i]
        
        if i < len(project_indices) - 1:
            end_idx = project_indices[i+1][0]
        else:
            end_idx = len(text)
            
        block = text[start_idx:end_idx]
        
        # Regex to capture the date line
        # Use \\n for newline in the regex string
        match = re.search(r'Begin [cC]onstruction:?\s*(.*?)(?:\\n|\\r|\\(cid:)', block)
        if match:
            date_str = match.group(1).strip()
            if is_spring_2022(date_str):
                found_projects.add(pname)
        
        if not match:
             match_st = re.search(r'Start [tT]ime:?\s*(.*?)(?:\\n|\\r|\\(cid:)', block)
             if match_st:
                 date_str = match_st.group(1).strip()
                 if is_spring_2022(date_str):
                     found_projects.add(pname)

total_funding = 0
for pname in found_projects:
    records = [f for f in funding_data if f['Project_Name'] == pname]
    for r in records:
        total_funding += int(r['Amount'])

result = {
    "project_count": len(found_projects),
    "projects": list(found_projects),
    "total_funding": total_funding
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8238280487498580574': 'file_storage/function-call-8238280487498580574.json', 'var_function-call-8238280487498581651': 'file_storage/function-call-8238280487498581651.json'}

exec(code, env_args)
