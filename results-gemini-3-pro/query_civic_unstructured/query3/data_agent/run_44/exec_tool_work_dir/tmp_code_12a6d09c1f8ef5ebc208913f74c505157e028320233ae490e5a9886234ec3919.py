code = """import json
import pandas as pd
import re

# Load Funding Data
with open(locals()['var_function-call-12539470358665637498'], 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

# Load Civic Docs Data
with open(locals()['var_function-call-12539470358665634517'], 'r') as f:
    docs_data = json.load(f)

full_text = "\n".join([d.get('text', '') for d in docs_data])

# Keywords
keywords = ['emergency', 'fema']

def normalize(s):
    if not s: return ""
    return re.sub(r'[^a-zA-Z0-9]', '', s.lower())

def is_related(text):
    if not text: return False
    t = text.lower()
    return any(k in t for k in keywords)

# Parse text
lines = full_text.split('\n')
projects_list = []

# Headers to identifying sections
# We will iterate lines. 
# Keep track of current section.
# Identify project titles by looking for "Updates:" line and taking the preceding line.

current_section = "Unknown"
section_headers = [
    "Capital Improvement Projects (Design)",
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]

# We need to find section positions first to be robust
section_map = {}
for i, line in enumerate(lines):
    l = line.strip()
    for h in section_headers:
        if h in l:
            section_map[i] = h

# Sort section indices
sorted_sections = sorted(section_map.items())

# Iterate to find projects
for i, line in enumerate(lines):
    if "Updates:" in line or "Project Description:" in line:
        # Title is likely the previous non-empty line
        j = i - 1
        while j >= 0 and not lines[j].strip():
            j -= 1
        
        if j < 0: continue
        
        title = lines[j].strip()
        
        # Determine section for this project
        # Find the max section index <= j
        p_section = "Unknown"
        last_idx = -1
        for idx, name in sorted_sections:
            if idx < j and idx > last_idx:
                last_idx = idx
                p_section = name
        
        # Extract content (lines from i until next project or end)
        # We need to find the start of the next project
        # A next project starts at some line k where k-1 is a title...
        # Simpler: content goes until next "Updates:" block or next Section Header
        
        content_lines = []
        for k in range(i, len(lines)):
            # Check if this line is a start of new project or section
            if k > i and ("Updates:" in lines[k] or "Project Description:" in lines[k]):
                break
            # Check if this line is a section header
            if any(h in lines[k] for h in section_headers):
                break
            content_lines.append(lines[k])
        
        content = "\n".join(content_lines)
        
        # Determine Status
        status = "not started"
        if "Design" in p_section:
            status = "design"
        elif "Construction" in p_section:
            if "completed" in content.lower():
                status = "completed"
            else:
                status = "construction" # Or 'design' per hint constraint? I'll keep construction.
        elif "Not Started" in p_section:
            status = "not started"
            
        projects_list.append({
            'title': title,
            'norm_title': normalize(title),
            'status': status,
            'content': content,
            'section': p_section
        })

# Join with Funding
results = []
for _, row in df_funding.iterrows():
    f_name = row['Project_Name']
    f_norm = normalize(f_name)
    f_amount = row['Amount']
    f_source = row['Funding_Source']
    
    # Check match
    matched_p = None
    for p in projects_list:
        # Check fuzzy match
        # If one contains the other
        if p['norm_title'] in f_norm or f_norm in p['norm_title']:
            # Prevent empty match
            if len(p['norm_title']) > 5:
                matched_p = p
                break
    
    related = False
    # Check Name
    if is_related(f_name):
        related = True
    # Check Content
    if matched_p and (is_related(matched_p['content']) or is_related(matched_p['title'])):
        related = True
        
    if related:
        st = matched_p['status'] if matched_p else "not started" # Default if not found in text but name matches FEMA
        results.append({
            "Project_Name": f_name,
            "Funding_Source": f_source,
            "Amount": f_amount,
            "Status": st
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3750553953043117850': ['Funding'], 'var_function-call-3750553953043118673': ['civic_docs'], 'var_function-call-12539470358665637498': 'file_storage/function-call-12539470358665637498.json', 'var_function-call-12539470358665634517': 'file_storage/function-call-12539470358665634517.json', 'var_function-call-10065264714784678123': 'file_storage/function-call-10065264714784678123.json'}

exec(code, env_args)
