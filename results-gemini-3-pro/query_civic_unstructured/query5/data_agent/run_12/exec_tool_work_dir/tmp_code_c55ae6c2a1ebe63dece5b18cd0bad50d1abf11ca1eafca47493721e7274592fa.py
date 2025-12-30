code = """import json
import re

with open(locals()['var_function-call-15201244734315748547'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-15201244734315749312'], 'r') as f:
    civic_docs = json.load(f)

funding_map = {}
for entry in funding_data:
    name = entry['Project_Name'].strip()
    amount = int(entry['Amount'])
    if name not in funding_map:
        funding_map[name] = 0
    funding_map[name] += amount

def get_start_date(text):
    # Search for date containing 2022
    # Patterns: Begin Construction: ..., Start Date: ...
    # Be careful with escaping in JSON string
    patterns = [
        r'Begin [Cc]onstruction[:\\s]+([^\\n]{1,50})',
        r'Start [Dd]ate[:\\s]+([^\\n]{1,50})'
    ]
    for pat in patterns:
        matches = re.findall(pat, text)
        for m in matches:
            if '2022' in m:
                return m.strip()
    return None

projects = []
for doc in civic_docs:
    text = doc['text']
    # Split lines
    lines = text.split('\n') 
    
    header_indices = []
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        # Check if line looks like a bullet
        if line.startswith('(cid:'): continue
        if not (line[0].isupper() or line[0].isdigit()): continue
        
        # Check if next non-empty line starts with (cid:190)
        is_header = False
        for j in range(i + 1, min(i + 5, len(lines))):
            nl = lines[j].strip()
            if not nl: continue
            if nl.startswith('(cid:190)'):
                is_header = True
            break
        
        if is_header:
            header_indices.append(i)
            
    for k in range(len(header_indices)):
        start_idx = header_indices[k]
        end_idx = header_indices[k+1] if k+1 < len(header_indices) else len(lines)
        name = lines[start_idx].strip()
        block_text = " ".join([l.strip() for l in lines[start_idx+1:end_idx]])
        projects.append({'name': name, 'text': block_text})

results = []
for p in projects:
    name = p['name']
    text = p['text']
    start_date = get_start_date(text)
    
    # Check disaster
    keywords = ['FEMA', 'CalOES', 'Disaster', 'Woolsey', 'Fire', 'Emergency']
    is_disaster = any(k.lower() in (name + " " + text).lower() for k in keywords)
    
    if start_date and is_disaster:
        amount = 0
        match_info = "None"
        
        if name in funding_map:
            amount = funding_map[name]
            match_info = "Exact"
        else:
            # Fuzzy match
            n_name = name.lower()
            best = None
            for f_name in funding_map:
                fn = f_name.lower()
                if fn in n_name and len(fn) > 10:
                    best = f_name
                    break
                if n_name in fn and len(n_name) > 10:
                    best = f_name
                    break
            if best:
                amount = funding_map[best]
                match_info = "Fuzzy: " + best
        
        results.append({
            'name': name,
            'start_date': start_date,
            'match': match_info,
            'amount': amount
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15201244734315748547': 'file_storage/function-call-15201244734315748547.json', 'var_function-call-15201244734315749312': 'file_storage/function-call-15201244734315749312.json', 'var_function-call-4266469490325009920': [{'name': '(cid:131) The project consultant has started the design of this project.', 'start_date': 'Spring 2022 Storm Drain Master Plan ', 'match_source': 'None', 'amount': 0}, {'name': 'that was damaged by the Woolsey Fire.', 'start_date': 'Spring 2022', 'match_source': 'None', 'amount': 0}, {'name': 'Fire.', 'start_date': 'Spring 2022', 'match_source': 'None', 'amount': 0}, {'name': 'that was damaged by the Woolsey Fire.', 'start_date': 'Spring 2022', 'match_source': 'None', 'amount': 0}, {'name': 'Fire.', 'start_date': 'Spring 2022', 'match_source': 'None', 'amount': 0}]}

exec(code, env_args)
