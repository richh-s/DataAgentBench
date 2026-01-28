code = """import json
import re

# Load Funding Data
with open(locals()['var_function-call-15201244734315748547'], 'r') as f:
    funding_data = json.load(f)

# Create funding map
funding_map = {}
for entry in funding_data:
    name = entry['Project_Name'].strip()
    amount = int(entry['Amount'])
    if name not in funding_map:
        funding_map[name] = 0
    funding_map[name] += amount

# Load Civic Docs
with open(locals()['var_function-call-15201244734315749312'], 'r') as f:
    civic_docs = json.load(f)

projects_found = []

def extract_start_date(text):
    # Regex to find start date
    # Escape backslashes for JSON: \\s
    matches = re.findall(r'Begin [Cc]onstruction[:\\s]+([A-Za-z0-9\\s,]+)', text)
    if not matches:
        matches = re.findall(r'Start [Dd]ate[:\\s]+([A-Za-z0-9\\s,]+)', text)
    
    for m in matches:
        if '2022' in m:
            return m
    return None

def is_disaster(text, name):
    keywords = ['FEMA', 'CalOES', 'Disaster', 'Woolsey', 'Fire', 'Emergency']
    if any(k.lower() in text.lower() for k in keywords):
        return True
    if any(k.lower() in name.lower() for k in keywords):
        return True
    return False

# Parse Documents
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\\n')
    
    current_name = None
    current_text_lines = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check header
        is_header = False
        for j in range(i + 1, min(i + 5, len(lines))):
            nl = lines[j].strip()
            if not nl:
                continue
            if nl.startswith('(cid:190)'):
                if not line.startswith('(cid:190)'):
                    is_header = True
                break
            else:
                break
        
        if is_header:
            if current_name:
                projects_found.append({'name': current_name, 'text': ' '.join(current_text_lines)})
            current_name = line
            current_text_lines = []
        else:
            if current_name:
                current_text_lines.append(line)

    if current_name:
        projects_found.append({'name': current_name, 'text': ' '.join(current_text_lines)})

# Filter and Match
final_list = []

for p in projects_found:
    name = p['name']
    text = p['text']
    
    start_date = extract_start_date(text)
    if not start_date:
        continue
        
    disaster = is_disaster(text, name)
    
    if disaster:
        amount = 0
        match_source = "None"
        
        # Exact match
        if name in funding_map:
            amount = funding_map[name]
            match_source = "Exact: " + name
        else:
            # Fuzzy match
            # Try removing common words
            norm_name = name.lower().replace('improvements', '').replace('project', '').strip()
            best_match = None
            
            for fname in funding_map:
                norm_fname = fname.lower()
                if norm_name in norm_fname and len(norm_name) > 10:
                    best_match = fname
                    break
            
            if best_match:
                amount = funding_map[best_match]
                match_source = "Fuzzy: " + best_match
        
        final_list.append({
            'name': name,
            'start_date': start_date,
            'match_source': match_source,
            'amount': amount
        })

print("__RESULT__:")
print(json.dumps(final_list))"""

env_args = {'var_function-call-15201244734315748547': 'file_storage/function-call-15201244734315748547.json', 'var_function-call-15201244734315749312': 'file_storage/function-call-15201244734315749312.json'}

exec(code, env_args)
