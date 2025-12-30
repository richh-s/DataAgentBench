code = """import json

# Load funding
funding_path = locals()['var_function-call-14868683301931886144']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

funding_map = {}
for record in funding_data:
    p_name = record['Project_Name'].strip()
    val = record['Amount']
    if isinstance(val, str):
        val = int(val)
    if p_name in funding_map:
        funding_map[p_name] += val
    else:
        funding_map[p_name] = val

# Load docs
docs_path = locals()['var_function-call-8294190329449223734']
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

full_text = ""
for doc in civic_docs:
    full_text = full_text + doc['text'] + chr(10)

lines = full_text.splitlines()

# Known projects
known_projects_set = set(funding_map.keys())

found_projects = []
current_lines = []
current_proj_name = None

for line in lines:
    line_stripped = line.strip()
    if line_stripped in known_projects_set:
        if current_proj_name:
            found_projects.append({'name': current_proj_name, 'text': " ".join(current_lines)})
        current_proj_name = line_stripped
        current_lines = []
    else:
        if current_proj_name:
            current_lines.append(line_stripped)

if current_proj_name:
    found_projects.append({'name': current_proj_name, 'text': " ".join(current_lines)})

target_projects = []
total_funding = 0

for proj in found_projects:
    p_name = proj['name']
    p_text_lower = proj['text'].lower()
    
    # Check Is Park
    is_park = False
    if 'park' in p_name.lower():
        is_park = True
    elif ' park ' in p_text_lower or 'playground' in p_text_lower:
        is_park = True
    
    # Check Completed 2022
    is_comp_2022 = False
    
    # Check for specific phrases
    phrases = ['construction was completed', 'complete construction', 'completed construction']
    
    for phrase in phrases:
        if phrase in p_text_lower:
            idx = p_text_lower.find(phrase)
            # Look at the substring starting from phrase
            sub = p_text_lower[idx:idx+150]
            if '2022' in sub:
                is_comp_2022 = True
                break

    if is_park and is_comp_2022:
        target_projects.append(p_name)
        total_funding += funding_map[p_name]

print("__RESULT__:")
print(json.dumps({
    "target_projects": target_projects,
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-8294190329449223734': 'file_storage/function-call-8294190329449223734.json', 'var_function-call-14868683301931886144': 'file_storage/function-call-14868683301931886144.json'}

exec(code, env_args)
