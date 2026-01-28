code = """import json
import re

# Load data
with open(locals()['var_function-call-10751851316187988885'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-2019060603328784572'], 'r') as f:
    civic_docs = json.load(f)

# 1. Identify the latest document
def get_date_from_filename(fname):
    m = re.search(r'(\d{2})(\d{2})(\d{4})', fname)
    if m:
        return f"{m.group(3)}-{m.group(1)}-{m.group(2)}"
    return '0000-00-00'

civic_docs.sort(key=lambda x: get_date_from_filename(x['filename']), reverse=True)
latest_doc = civic_docs[0]
print(f"Latest doc: {latest_doc['filename']}")

text = latest_doc['text']

# 2. Extract Capital Projects (Design) section
start_marker = 'Capital Improvement Projects (Design)'
start_idx = text.find(start_marker)

design_projects = []

if start_idx != -1:
    sub_text = text[start_idx + len(start_marker):]
    next_headers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
    end_idx = len(sub_text)
    for h in next_headers:
        idx = sub_text.find(h)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    design_section = sub_text[:end_idx]
    
    # 3. Extract project names
    # Split by (cid:190) Updates:
    # Use re.split to handle potential variations or just string split
    parts = design_section.split('(cid:190) Updates:')
    
    for i in range(len(parts) - 1):
        segment = parts[i].strip()
        lines = segment.split('\n')
        lines = [l.strip() for l in lines if l.strip()]
        
        if lines:
            # Candidate is the last line
            candidate = lines[-1]
            # Check for page/agenda artifacts
            while (candidate.lower().startswith('page ') or candidate.lower().startswith('agenda item')) and len(lines) > 1:
                lines.pop()
                candidate = lines[-1]
            
            design_projects.append(candidate)

print('Extracted Design Projects:')
for p in design_projects:
    print(f" - {p}")

# 4. Filter by funding > 50,000
funded_projects = set()
for rec in funding_data:
    try:
        amt = float(rec['Amount'])
        if amt > 50000:
            funded_projects.add(rec['Project_Name'].strip())
    except:
        pass

print(f"Funded Projects count: {len(funded_projects)}")

# 5. Count matches
count = 0
matched_names = []
used_funded = set()

for dp in design_projects:
    # Exact match
    if dp in funded_projects:
        count += 1
        matched_names.append(dp)
        used_funded.add(dp)
    else:
        # Fuzzy match
        found = False
        for fp in funded_projects:
            if fp in used_funded: continue # Avoid double counting? No, dp is unique. But if multiple dp map to same fp?
            
            # Check overlap
            # If fp is "Clover Heights Storm Drain" and dp is "Clover Heights Storm Drainage Improvements"
            # fp in dp is True.
            
            if (fp in dp) or (dp in fp):
                if len(fp) > 10 and len(dp) > 10:
                    count += 1
                    matched_names.append(f"{dp} (matched {fp})")
                    found = True
                    break
        if not found:
            print(f"Unmatched: {dp}")

print('Matches:')
for m in matched_names:
    print(m)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_function-call-10751851316187988885': 'file_storage/function-call-10751851316187988885.json', 'var_function-call-10751851316187990910': 'file_storage/function-call-10751851316187990910.json', 'var_function-call-1560571324400942804': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-2019060603328784572': 'file_storage/function-call-2019060603328784572.json'}

exec(code, env_args)
