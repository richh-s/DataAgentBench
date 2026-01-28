code = """import json
import pandas as pd
import re

# Load funding
with open(locals()['var_function-call-870935293140318429'], 'r') as f:
    funding = json.load(f)
df = pd.DataFrame(funding)
df['Amount'] = pd.to_numeric(df['Amount'])

def clean_name(n):
    n = re.sub(r'\\s*\\((?:FEMA|CalOES|CalJPIA).*?\\)', '', n, flags=re.IGNORECASE)
    n = re.sub(r'\\s*\\(FEMA\\)', '', n, flags=re.IGNORECASE)
    n = re.sub(r'\\s*-\\s*Design', '', n, flags=re.IGNORECASE)
    return n.strip()

df['BaseName'] = df['Project_Name'].apply(clean_name)
funding_map = df.groupby('BaseName')['Amount'].sum().to_dict()
base_names = sorted(list(funding_map.keys()), key=len, reverse=True)

with open(locals()['var_function-call-870935293140317738'], 'r') as f:
    docs = json.load(f)

def get_date_str(fname):
    m = re.search(r'(\\d{8})', fname)
    if m:
        d = m.group(1)
        return d[4:] + d[:2] + d[2:4]
    return '00000000'

docs.sort(key=lambda d: get_date_str(d['filename']), reverse=True)

project_dates = {}
start_re = re.compile(r'(?:Begin Construction|Start Construction|Construction Start)[:\\s\\W]+([^\\n\\r]+)', re.IGNORECASE)

for doc in docs:
    text = doc['text']
    matches = []
    for name in base_names:
        for m in re.finditer(re.escape(name), text, re.IGNORECASE):
            matches.append((m.start(), len(name), name))
    
    matches.sort(key=lambda x: (x[0], -x[1]))
    
    final_matches = []
    curr_end = -1
    for start, length, name in matches:
        if start >= curr_end:
            final_matches.append((start, name))
            curr_end = start + length
            
    for i in range(len(final_matches)):
        start_idx, name = final_matches[i]
        if name in project_dates: continue
        
        end_idx = final_matches[i+1][0] if i+1 < len(final_matches) else len(text)
        chunk = text[start_idx:end_idx]
        
        m = start_re.search(chunk)
        if m:
            project_dates[name] = m.group(1).strip()

spring_22_projects = []
for name, d_str in project_dates.items():
    s = d_str.lower()
    if '2022' in s:
        if 'spring' in s:
            spring_22_projects.append(name)
        elif any(m in s for m in ['march', 'april', 'may']):
            spring_22_projects.append(name)
        elif re.search(r'(?:03|04|05)[/-]2022', s):
            spring_22_projects.append(name)
        elif re.search(r'2022[/-](?:03|04|05)', s):
            spring_22_projects.append(name)

total_funding = sum(funding_map[n] for n in spring_22_projects)

print("__RESULT__:")
print(json.dumps({
    "count": len(spring_22_projects),
    "total_funding": total_funding,
    "projects": spring_22_projects,
    "dates": {p: project_dates[p] for p in spring_22_projects}
}))"""

env_args = {'var_function-call-870935293140317738': 'file_storage/function-call-870935293140317738.json', 'var_function-call-870935293140318429': 'file_storage/function-call-870935293140318429.json'}

exec(code, env_args)
