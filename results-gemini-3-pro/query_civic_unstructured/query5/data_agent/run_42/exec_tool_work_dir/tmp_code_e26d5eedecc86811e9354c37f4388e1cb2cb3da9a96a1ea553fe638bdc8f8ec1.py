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
    disaster_headers_iter = re.finditer(r"Disaster Recovery Projects", text, re.IGNORECASE)
    capital_headers_iter = re.finditer(r"Capital Improvement Projects", text, re.IGNORECASE)
    
    disaster_starts = [m.start() for m in disaster_headers_iter]
    capital_starts = [m.start() for m in capital_headers_iter]
    
    sections = []
    for pos in disaster_starts:
        sections.append((pos, 'disaster'))
    for pos in capital_starts:
        sections.append((pos, 'capital'))
    
    sections.sort()
    
    for name in project_names:
        try:
            matches = list(re.finditer(re.escape(name), text))
        except:
            continue
            
        for m in matches:
            start_pos = m.start()
            end_pos = m.end()
            
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
            # Doubled backslashes for JSON transport
            date_match = re.search(r"(Begin Construction|Start Date|Construction Start)\s*[:-]?\s*([A-Za-z0-9\s,]+)", context, re.IGNORECASE)
            
            st = None
            if date_match:
                st = date_match.group(2).strip()
                st = st.split('\n')[0]
            
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
