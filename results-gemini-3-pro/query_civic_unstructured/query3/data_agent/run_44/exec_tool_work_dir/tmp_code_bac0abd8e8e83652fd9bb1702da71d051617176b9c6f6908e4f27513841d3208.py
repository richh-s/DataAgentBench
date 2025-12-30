code = """import json
import pandas as pd
import re

# Keys
key_funding = locals()['var_function-call-12539470358665637498']
key_docs = locals()['var_function-call-12539470358665634517']

# Load Funding
with open(key_funding, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

# Load Docs
with open(key_docs, 'r') as f:
    docs_data = json.load(f)

texts = []
for d in docs_data:
    texts.append(d.get('text', ''))
full_text = chr(10).join(texts)

keywords = ['emergency', 'fema']

def normalize(s):
    if not s: return ""
    # Remove content in parenthesis first
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    return s

def is_related(text):
    if not text: return False
    t = text.lower()
    return any(k in t for k in keywords)

lines = full_text.split(chr(10))
projects_list = []

current_section = "Unknown"
section_headers = [
    "Capital Improvement Projects (Design)",
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]

# Map sections
section_map = {}
for i, line in enumerate(lines):
    l = line.strip()
    for h in section_headers:
        if h in l:
            section_map[i] = h

sorted_sections = sorted(section_map.items())

for i, line in enumerate(lines):
    # Check for Updates or Description markers
    if "Updates:" in line or "Project Description:" in line:
        j = i - 1
        while j >= 0 and not lines[j].strip():
            j -= 1
        
        if j < 0: continue
        title = lines[j].strip()
        
        # Identify section
        p_section = "Unknown"
        last_idx = -1
        for idx, name in sorted_sections:
            if idx < j and idx > last_idx:
                last_idx = idx
                p_section = name
        
        # Extract content
        content_lines = []
        for k in range(i, len(lines)):
            if k > i and ("Updates:" in lines[k] or "Project Description:" in lines[k]):
                break
            if any(h in lines[k] for h in section_headers):
                break
            content_lines.append(lines[k])
        
        content = " ".join(content_lines)
        
        # Determine Status
        status = "not started"
        if "Design" in p_section:
            status = "design"
        elif "Construction" in p_section:
            if "completed" in content.lower():
                status = "completed"
            else:
                status = "construction"
        elif "Not Started" in p_section:
            status = "not started"
            
        projects_list.append({
            'title': title,
            'norm_title': normalize(title),
            'status': status,
            'content': content
        })

results = []
for _, row in df_funding.iterrows():
    f_name = row['Project_Name']
    f_norm = normalize(f_name)
    
    # Match
    matched_p = None
    for p in projects_list:
        if len(p['norm_title']) > 5:
            if p['norm_title'] in f_norm or f_norm in p['norm_title']:
                matched_p = p
                break
    
    related = False
    if is_related(f_name):
        related = True
    if matched_p and (is_related(matched_p['content']) or is_related(matched_p['title'])):
        related = True
        
    if related:
        st = matched_p['status'] if matched_p else "not started"
        results.append({
            "Project_Name": f_name,
            "Funding_Source": row['Funding_Source'],
            "Amount": row['Amount'],
            "Status": st
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3750553953043117850': ['Funding'], 'var_function-call-3750553953043118673': ['civic_docs'], 'var_function-call-12539470358665637498': 'file_storage/function-call-12539470358665637498.json', 'var_function-call-12539470358665634517': 'file_storage/function-call-12539470358665634517.json', 'var_function-call-10065264714784678123': 'file_storage/function-call-10065264714784678123.json'}

exec(code, env_args)
