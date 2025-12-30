code = """import json
import re

# Load data
with open(locals()['var_function-call-15046969363982349672'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-6734558309770551932'], 'r') as f:
    funding_data = json.load(f)

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    idx = 0
    while idx < len(lines):
        line = lines[idx].strip()
        # Identify project start: Line is not empty/bullet/header, and followed (shortly) by (cid:190)
        is_project_start = False
        # Filter out common headers or noise
        if line and not line.startswith('(cid:') and not line.startswith('Page') and 'Capital Improvement' not in line and 'Agenda Item' not in line and 'Subject:' not in line:
            # Look ahead
            for k in range(1, 6):
                if idx + k < len(lines):
                    nl = lines[idx+k].strip()
                    if nl.startswith('(cid:190)'):
                        is_project_start = True
                        break
        
        if is_project_start:
            p_name = line
            p_text = ""
            current_idx = idx + 1
            # Consume until next project
            while current_idx < len(lines):
                c_line = lines[current_idx].strip()
                # Check if this line is start of NEXT project
                is_next = False
                if c_line and not c_line.startswith('(cid:') and not c_line.startswith('Page') and 'Capital Improvement' not in c_line and 'Agenda Item' not in c_line:
                    for m in range(1, 6):
                        if current_idx + m < len(lines):
                            nnl = lines[current_idx+m].strip()
                            if nnl.startswith('(cid:190)'):
                                is_next = True
                                break
                if is_next:
                    break
                p_text += " " + c_line
                current_idx += 1
            
            projects.append({'name': p_name, 'text': p_text})
            idx = current_idx
        else:
            idx += 1

matched = []
for p in projects:
    name = p['name']
    text = p['text'].lower()
    
    # Check park keywords
    # Prompt: "park"
    if 'park' in name.lower() or 'park' in text or 'playground' in text:
        # Check completed 2022
        # Look for "completed" ... "2022"
        # Regex: completed.{0,100}2022
        if re.search(r'completed.{0,100}2022', text) or re.search(r'completion.{0,100}2022', text):
             matched.append(name)

# Funding
total = 0
funding_map = {item['Project_Name']: item['Amount'] for item in funding_data}
found_names = []

for m in matched:
    # Try exact or stripped
    m_clean = m.strip()
    if m_clean in funding_map:
        total += int(funding_map[m_clean])
        found_names.append(m_clean)

print("__RESULT__:")
print(json.dumps({"total_funding": total, "projects": found_names}))"""

env_args = {'var_function-call-6734558309770552995': 'file_storage/function-call-6734558309770552995.json', 'var_function-call-6734558309770551932': 'file_storage/function-call-6734558309770551932.json', 'var_function-call-15046969363982349672': 'file_storage/function-call-15046969363982349672.json'}

exec(code, env_args)
