code = """import json
import re

# Load data
with open(locals()['var_function-call-18183921602987609697'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-18183921602987608670'], 'r') as f:
    civic_docs = json.load(f)

projects = {} 

funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}
project_names = list(funding_map.keys())
project_names.sort(key=len, reverse=True)

def is_disaster_name(name):
    keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey"]
    return any(k in name for k in keywords)

for doc in civic_docs:
    text = doc['text']
    
    # Identify sections
    disaster_indices = []
    idx = text.lower().find("disaster recovery projects")
    while idx != -1:
        disaster_indices.append(idx)
        idx = text.lower().find("disaster recovery projects", idx + 1)
        
    capital_indices = []
    idx = text.lower().find("capital improvement projects")
    while idx != -1:
        capital_indices.append(idx)
        idx = text.lower().find("capital improvement projects", idx + 1)
    
    sections = []
    for pos in disaster_indices:
        sections.append((pos, 'disaster'))
    for pos in capital_indices:
        sections.append((pos, 'capital'))
    sections.sort()
    
    for name in project_names:
        search_start = 0
        while True:
            match_pos = text.find(name, search_start)
            if match_pos == -1:
                break
            
            start_pos = match_pos
            end_pos = match_pos + len(name)
            search_start = end_pos
            
            project_type = "unknown"
            current_section_type = None
            for sec_pos, sec_type in sections:
                if sec_pos < start_pos:
                    current_section_type = sec_type
                else:
                    break
            
            if is_disaster_name(name):
                project_type = "disaster"
            elif current_section_type == 'disaster':
                project_type = "disaster"
            else:
                project_type = "capital"
            
            context = text[end_pos:end_pos+1000]
            st = None
            
            patterns = ["Begin Construction", "Start Date", "Construction Start"]
            
            for pat in patterns:
                pidx = context.lower().find(pat.lower())
                if pidx != -1:
                    remainder = context[pidx + len(pat):]
                    clean_start = 0
                    while clean_start < len(remainder) and remainder[clean_start] in " :-":
                        clean_start += 1
                    remainder = remainder[clean_start:]
                    
                    nl_idx = remainder.find(chr(10)) # chr(10) is newline
                    if nl_idx != -1:
                        val = remainder[:nl_idx]
                    else:
                        val = remainder[:50]
                    st = val.strip()
                    break
            
            if name not in projects:
                projects[name] = {'type': project_type, 'st': st, 'amount': funding_map[name]}
            else:
                if projects[name]['st'] is None and st is not None:
                    projects[name]['st'] = st
                    projects[name]['type'] = project_type
                if project_type == 'disaster':
                    projects[name]['type'] = 'disaster'

total_funding = 0
found_projects = []

for name, info in projects.items():
    if info['type'] == 'disaster':
        start_date = info.get('st', '')
        if start_date and '2022' in start_date:
            total_funding += info['amount']
            found_projects.append({'name': name, 'st': start_date, 'amount': info['amount']})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": found_projects}))"""

env_args = {'var_function-call-18183921602987609697': 'file_storage/function-call-18183921602987609697.json', 'var_function-call-18183921602987608670': 'file_storage/function-call-18183921602987608670.json'}

exec(code, env_args)
