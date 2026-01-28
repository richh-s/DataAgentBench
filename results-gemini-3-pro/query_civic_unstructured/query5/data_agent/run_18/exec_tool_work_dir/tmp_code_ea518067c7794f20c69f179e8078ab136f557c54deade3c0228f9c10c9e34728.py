code = """import json
import re

with open(locals()['var_function-call-6099601671334015320'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-9845122995383564769'], 'r') as f:
    funding_data = json.load(f)

def normalize(name):
    return re.sub(r'\s*\((?:FEMA|CalOES|CalJPIA).*?\)$', '', name, flags=re.IGNORECASE).strip()

funding_base_names = set()
for row in funding_data:
    funding_base_names.add(normalize(row['Project_Name']))

project_data = {}

for doc in civic_docs:
    lines = doc['text'].splitlines()
    current_proj = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        found = None
        if line_clean in funding_base_names:
            found = line_clean
        else:
            for base in funding_base_names:
                if base in line_clean and len(line_clean) < len(base) + 10:
                    found = base
                    break
        
        if found:
            current_proj = found
            if current_proj not in project_data:
                project_data[current_proj] = {'disaster': False, 'started_2022': False}
            continue
            
        if current_proj:
            disaster_kw = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster", "Emergency"]
            for kw in disaster_kw:
                if kw.lower() in line_clean.lower():
                    project_data[current_proj]['disaster'] = True
            
            if "2022" in line_clean:
                if "Begin Construction" in line_clean or "Start Construction" in line_clean:
                    project_data[current_proj]['started_2022'] = True
                if "Construction was completed" in line_clean:
                    project_data[current_proj]['started_2022'] = True
                if "Awarded" in line_clean:
                    project_data[current_proj]['started_2022'] = True

total_funding = 0
matched_projects = []

for row in funding_data:
    raw_name = row['Project_Name']
    base = normalize(raw_name)
    amount = int(row['Amount'])
    
    is_disaster_name = False
    if re.search(r'\((?:FEMA|CalOES|CalJPIA).*?\)', raw_name, re.IGNORECASE):
        is_disaster_name = True
    
    is_disaster_text = False
    started_2022 = False
    
    if base in project_data:
        if project_data[base]['disaster']:
            is_disaster_text = True
        if project_data[base]['started_2022']:
            started_2022 = True
            
    if (is_disaster_name or is_disaster_text) and started_2022:
        total_funding += amount
        matched_projects.append(raw_name)

print("__RESULT__:")
print(json.dumps({'total_funding': total_funding, 'matched_projects': matched_projects}))"""

env_args = {'var_function-call-18312166134834260107': 'file_storage/function-call-18312166134834260107.json', 'var_function-call-6099601671334015320': 'file_storage/function-call-6099601671334015320.json', 'var_function-call-9845122995383564769': 'file_storage/function-call-9845122995383564769.json'}

exec(code, env_args)
