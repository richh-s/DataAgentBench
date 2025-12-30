code = """import json
import re

# Load Funding Data
with open(locals()['var_function-call-777734505766911732'], 'r') as f:
    funding_data = json.load(f)

funding_map = {}
for entry in funding_data:
    name = entry['Project_Name'].strip()
    amount = int(str(entry['Amount']))
    funding_map[name] = amount

# Load Civic Docs
with open(locals()['var_function-call-777734505766909915'], 'r') as f:
    civic_docs = json.load(f)

completed_park_projects = set()

def is_park_related(name):
    name_lower = name.lower()
    return 'park' in name_lower or 'playground' in name_lower or 'recreation' in name_lower

def is_completed_2022(text):
    text_lower = text.lower()
    if re.search(r'completed\W+(?:[a-z]+\W+)?2022', text_lower):
        return True
    if re.search(r'completed\s+in\s+2022', text_lower):
        return True
    return False

cid_marker = "(cid:190)"
# Unicode char for fraction 3/4 is \u00be, but text might literally have "(cid:190)" or the char.
# The preview showed "(cid:190)".

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines) - 1):
        line = lines[i].strip()
        next_line = lines[i+1].strip()
        
        # Check for marker
        # We check both literal string and potential unicode mapping if needed, but preview said "(cid:190)"
        if next_line.startswith(cid_marker) or next_line.startswith(chr(190)):
            project_name = line
            if not project_name and i > 0:
                project_name = lines[i-1].strip()
            
            if not project_name:
                continue
            
            # Extract block
            block_lines = []
            for j in range(i + 1, len(lines) - 1):
                block_line = lines[j].strip()
                block_next = lines[j+1].strip()
                if block_next.startswith(cid_marker) or block_next.startswith(chr(190)):
                    break
                block_lines.append(lines[j])
            
            project_text = " ".join(block_lines)
            
            if is_park_related(project_name):
                if is_completed_2022(project_text):
                    completed_park_projects.add(project_name)

total_funding = 0
found_projects = []
missing_projects = []

for proj in completed_park_projects:
    if proj in funding_map:
        total_funding += funding_map[proj]
        found_projects.append((proj, funding_map[proj]))
    else:
        missing_projects.append(proj)

print("__RESULT__:")
print(json.dumps({
    "total_funding": total_funding,
    "completed_park_projects": list(completed_park_projects),
    "found_projects_details": found_projects,
    "missing_projects": missing_projects
}))"""

env_args = {'var_function-call-5669291864972532438': ['Funding'], 'var_function-call-5669291864972531351': ['civic_docs'], 'var_function-call-777734505766911732': 'file_storage/function-call-777734505766911732.json', 'var_function-call-777734505766909915': 'file_storage/function-call-777734505766909915.json'}

exec(code, env_args)
