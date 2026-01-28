code = """import json
import re

# Load data
with open(locals()['var_function-call-15201244734315748547'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-15201244734315749312'], 'r') as f:
    civic_docs = json.load(f)

# Funding map
funding_map = {}
for entry in funding_data:
    name = entry['Project_Name'].strip()
    amount = int(entry['Amount'])
    # Handle duplicates by summing?
    # Or just store valid names.
    if name not in funding_map:
        funding_map[name] = 0
    funding_map[name] += amount

def get_start_date(text):
    # Regex for start date
    # Capture up to newline or reasonable length
    # Note double escaping for JSON string
    patterns = [
        r'Begin [Cc]onstruction[:\\s]+([^\\n]{1,50})',
        r'Start [Dd]ate[:\\s]+([^\\n]{1,50})',
        r'Advertise[:\\s]+([^\\n]{1,50})' # Maybe Advertise is also relevant? Let's stick to Construction/Start
    ]
    
    for pat in patterns:
        matches = re.findall(pat, text)
        for m in matches:
            if '2022' in m:
                return m.strip()
    return None

def is_disaster_related(text, name):
    keywords = ['FEMA', 'CalOES', 'Disaster', 'Woolsey', 'Fire', 'Emergency']
    blob = (name + " " + text).lower()
    return any(k.lower() in blob for k in keywords)

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\\n') # Use \\n because we are in exec string context?
    # Actually, in the python environment, text.split('\n') works if the string has actual newlines.
    # The JSON loader produces string with actual newlines.
    # So `lines = text.split('\n')` is correct.
    # But in the tool argument code string, I write `lines = text.split('\\n')` to pass `\n` to python?
    # No, `\n` in python code is newline character.
    # `\\n` in python code is `\` followed by `n`.
    # `text` from JSON load has `\n` characters.
    # So `text.split('\n')` is what I want.
    # Inside the JSON string for `code`, I should write `text.split('\\n')` to produce `text.split('\n')` in python source?
    # Yes.
    
    # Wait, `\n` in the code string becomes a newline in the source code.
    # `\\n` in the code string becomes `\n` (literal backslash n) which is how we write newline char in python string literal.
    # So `text.split('\n')` in python source means split by newline.
    # So in JSON `code` string: `text.split('\\n')`.
    
    # But wait, earlier I used `text.split('\\n')` and it worked (no syntax error), but maybe logic was wrong.
    # Let's assume `text.split('\n')` is correct python code.
    # So JSON string: `text.split('\\n')`.
    
    # Identify headers
    header_indices = []
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        if line.startswith('(cid:') or line.startswith('\u00be'): continue # Bullet line
        if not (line[0].isupper() or line[0].isdigit()): continue # Must start with Cap or Digit
        
        # Check lookahead
        is_header = False
        for j in range(i + 1, min(i + 5, len(lines))):
            nl = lines[j].strip()
            if not nl: continue
            if nl.startswith('(cid:190)') or nl.startswith('\u00be'):
                is_header = True
            break # Stop at first non-empty
        
        if is_header:
            header_indices.append(i)
            
    # Extract blocks
    for k in range(len(header_indices)):
        start_idx = header_indices[k]
        end_idx = header_indices[k+1] if k+1 < len(header_indices) else len(lines)
        
        # Name is the line at start_idx
        name = lines[start_idx].strip()
        
        # Text is the rest
        block_lines = lines[start_idx+1:end_idx]
        block_text = " ".join([l.strip() for l in block_lines])
        
        projects.append({'name': name, 'text': block_text})

# Analyze
results = []
for p in projects:
    name = p['name']
    text = p['text']
    
    start_date = get_start_date(text)
    if start_date: # Started in 2022
        disaster = is_disaster_related(text, name)
        
        if disaster:
            # Find funding
            amount = 0
            matched = "No"
            
            # 1. Exact match
            if name in funding_map:
                amount = funding_map[name]
                matched = "Exact"
            else:
                # 2. Fuzzy match
                # Check if name contains funding name or vice versa
                # Normalize
                n_name = name.lower()
                best_f = None
                
                for f_name in funding_map:
                    nf = f_name.lower()
                    # Check for substantial overlap
                    # E.g. "Clover Heights Storm Drain" in "Clover Heights Storm Drainage Improvements"
                    if nf in n_name and len(nf) > 10:
                        best_f = f_name
                        break
                    # Or reverse?
                    if n_name in nf and len(n_name) > 10:
                        best_f = f_name
                        break
                
                if best_f:
                    amount = funding_map[best_f]
                    matched = "Fuzzy: " + best_f
            
            results.append({
                'name': name,
                'start_date': start_date,
                'matched': matched,
                'amount': amount
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15201244734315748547': 'file_storage/function-call-15201244734315748547.json', 'var_function-call-15201244734315749312': 'file_storage/function-call-15201244734315749312.json', 'var_function-call-4266469490325009920': [{'name': '(cid:131) The project consultant has started the design of this project.', 'start_date': 'Spring 2022 Storm Drain Master Plan ', 'match_source': 'None', 'amount': 0}, {'name': 'that was damaged by the Woolsey Fire.', 'start_date': 'Spring 2022', 'match_source': 'None', 'amount': 0}, {'name': 'Fire.', 'start_date': 'Spring 2022', 'match_source': 'None', 'amount': 0}, {'name': 'that was damaged by the Woolsey Fire.', 'start_date': 'Spring 2022', 'match_source': 'None', 'amount': 0}, {'name': 'Fire.', 'start_date': 'Spring 2022', 'match_source': 'None', 'amount': 0}]}

exec(code, env_args)
