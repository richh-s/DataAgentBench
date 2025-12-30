code = """import json
import re

# Load Funding Data
with open(locals()['var_function-call-777734505766911732'], 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs
with open(locals()['var_function-call-777734505766909915'], 'r') as f:
    civic_docs = json.load(f)

candidates = []

cid_marker = "(cid:190)"

def is_completed_2022(text):
    text_lower = text.lower()
    if re.search(r'completed\W+(?:[a-z]+\W+)?2022', text_lower):
        return True
    if re.search(r'completed\s+in\s+2022', text_lower):
        return True
    return False

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\\n') 
    
    for i in range(len(lines) - 1):
        line = lines[i].strip()
        next_line = lines[i+1].strip()
        
        if next_line.startswith(cid_marker) or next_line.startswith(chr(190)):
            project_name = line
            if not project_name and i > 0:
                project_name = lines[i-1].strip()
            
            if not project_name:
                continue
            
            block_lines = []
            for j in range(i + 1, len(lines) - 1):
                block_line = lines[j].strip()
                block_next = lines[j+1].strip()
                if block_next.startswith(cid_marker) or block_next.startswith(chr(190)):
                    break
                block_lines.append(lines[j])
            
            project_text = " ".join(block_lines)
            
            if is_completed_2022(project_text):
                candidates.append({
                    "name": project_name,
                    "text_snippet": project_text[:200]
                })

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-5669291864972532438': ['Funding'], 'var_function-call-5669291864972531351': ['civic_docs'], 'var_function-call-777734505766911732': 'file_storage/function-call-777734505766911732.json', 'var_function-call-777734505766909915': 'file_storage/function-call-777734505766909915.json', 'var_function-call-7978636356572862470': {'total_funding': 21000, 'completed_park_projects': ['Bluffs Park Shade Structure'], 'found_projects_details': [['Bluffs Park Shade Structure', 21000]], 'missing_projects': []}}

exec(code, env_args)
