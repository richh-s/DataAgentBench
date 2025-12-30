code = """import json
import re

# Load data
with open(locals()['var_function-call-13241760497320549299'], 'r') as f:
    civic_docs = json.load(f)
with open(locals()['var_function-call-8006204082577017619'], 'r') as f:
    funding = json.load(f)

projects_started_spring_2022 = []
total_funding = 0

spring_patterns = [
    r"Spring,? 2022",
    r"March,? 2022",
    r"April,? 2022",
    r"May,? 2022"
]

def is_spring_2022(text):
    for pat in spring_patterns:
        if re.search(pat, text, re.IGNORECASE):
            return True
    return False

project_map = {p['Project_Name']: int(p['Amount']) for p in funding}
found_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    for proj_name in project_map.keys():
        if proj_name in found_projects:
            continue
            
        if proj_name in text:
            idx = text.find(proj_name)
            chunk = text[idx:idx+2000]
            
            # Check Begin Construction
            match = re.search(r"Begin Construction[:\s]+([^\n]+)", chunk, re.IGNORECASE)
            if match:
                date_str = match.group(1).strip()
                if is_spring_2022(date_str):
                    found_projects.add(proj_name)
                    continue 

count = len(found_projects)
total_funding = sum(project_map[p] for p in found_projects)

print("__RESULT__:")
print(json.dumps({"count": count, "total_funding": total_funding, "projects": list(found_projects)}))"""

env_args = {'var_function-call-14343582955729451491': 'file_storage/function-call-14343582955729451491.json', 'var_function-call-8006204082577017619': 'file_storage/function-call-8006204082577017619.json', 'var_function-call-13241760497320549299': 'file_storage/function-call-13241760497320549299.json', 'var_function-call-857092213890831436': 5}

exec(code, env_args)
