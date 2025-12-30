code = """import json
import re
import pandas as pd

# Load data
funding_path = locals()['var_function-call-4559408233983332253']
docs_path = locals()['var_function-call-4559408233983329834']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_df = pd.DataFrame(funding_data)
all_project_names = funding_df['Project_Name'].unique().tolist()

def get_base_name(name):
    # Escape: \\s, \\(
    return re.sub(r'\s*\(.*?\)$', '', name).strip()

base_to_full = {}
for name in all_project_names:
    base = get_base_name(name)
    if base not in base_to_full:
        base_to_full[base] = []
    base_to_full[base].append(name)

base_names_set = set(base_to_full.keys())
sorted_base_names = sorted(list(base_names_set), key=len, reverse=True)

project_metadata = {}

for doc in civic_docs:
    text = doc['text']
    
    found_positions = []
    for base_name in sorted_base_names:
        safe_name = re.escape(base_name)
        for m in re.finditer(safe_name, text):
            found_positions.append((m.start(), base_name))
            
    found_positions.sort(key=lambda x: (x[0], -len(x[1])))
    
    final_matches = []
    last_end = -1
    for pos, name in found_positions:
        if pos >= last_end:
            final_matches.append((pos, name))
            last_end = pos + len(name)
            
    for i, (pos, name) in enumerate(final_matches):
        start_idx = pos
        end_idx = final_matches[i+1][0] if i+1 < len(final_matches) else len(text)
        block = text[start_idx:end_idx]
        
        st = None
        # Regex: \\s, \\n
        m = re.search(r'(?:Begin|Start)\s*Construction:?\s*([^\n]*)', block, re.IGNORECASE)
        if m:
            st = m.group(1).strip()
        else:
            m2 = re.search(r'Construction\s*began:?\s*([^\n]*)', block, re.IGNORECASE)
            if m2:
                st = m2.group(1).strip()
        
        is_disaster = False
        disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Woolsey', 'Fire', 'Disaster', 'Recovery', 'Emergency']
        for kw in disaster_keywords:
            if kw.lower() in block.lower():
                is_disaster = True
                break
        
        if name not in project_metadata:
            project_metadata[name] = {'st': st, 'is_disaster': is_disaster}
        else:
            if st and not project_metadata[name]['st']:
                project_metadata[name]['st'] = st
            if is_disaster:
                project_metadata[name]['is_disaster'] = True

included_funding_amounts = []
included_projects = []

for base_name in base_names_set:
    meta = project_metadata.get(base_name)
    if not meta:
        continue
        
    st = meta['st']
    is_disaster_text = meta['is_disaster']
    
    if st and '2022' in st:
        is_disaster = is_disaster_text
        funding_records = base_to_full[base_name]
        
        for fname in funding_records:
            if any(x in fname for x in ['FEMA', 'CalOES', 'CalJPIA']):
                is_disaster = True
                break
        
        if is_disaster:
            project_total = 0
            for fname in funding_records:
                rows = funding_df[funding_df['Project_Name'] == fname]
                amount = rows['Amount'].astype(int).sum()
                project_total += amount
            
            included_funding_amounts.append(project_total)
            included_projects.append({'name': base_name, 'amount': project_total, 'st': st})

total_funding = sum(included_funding_amounts)

print("__RESULT__:")
print(json.dumps({
    "total_funding": total_funding,
    "projects": included_projects
}))"""

env_args = {'var_function-call-4559408233983329834': 'file_storage/function-call-4559408233983329834.json', 'var_function-call-4559408233983332253': 'file_storage/function-call-4559408233983332253.json'}

exec(code, env_args)
