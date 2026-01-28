code = """import json

# Load data
with open(locals()['var_function-call-8710431092191465218'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-268115837659623776'], 'r') as f:
    civic_docs = json.load(f)

# Funding Candidates (>50k)
funding_projects = []
for item in funding_data:
    try:
        if float(item['Amount']) > 50000:
            funding_projects.append(item['Project_Name'])
    except:
        pass

# Extract from Docs
extracted_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    section_title = 'Capital Improvement Projects (Design)'
    idx = text.find(section_title)
    if idx == -1:
        continue
    
    content = text[idx + len(section_title):]
    lines = content.splitlines()
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        if 'Capital Improvement Projects' in line and '(Design)' not in line:
            break
        if 'Disaster Recovery Projects' in line:
            break
        if 'Agenda Item' in line:
            continue
            
        is_proj = False
        # scan next few lines
        for offset in range(1, 5):
            if i + offset < len(lines):
                next_line = lines[i+offset].strip()
                if 'Updates:' in next_line or 'Project Description:' in next_line:
                    is_proj = True
                    break
        
        if is_proj:
            extracted_projects.add(line)

# Matching
def clean(s):
    s = s.lower()
    # Remove parens content manually or via simple replace if standard
    for pattern in ['(fema project)', '(caloes project)', '(caljpia project)', '(fema)', '(design)']:
        s = s.replace(pattern, '')
    s = s.replace('  ', ' ').strip()
    # Remove year prefix
    if len(s) > 5 and s[:4].isdigit() and s[4] == ' ':
        s = s[5:]
    return s.strip()

cleaned_extracted = [clean(p) for p in extracted_projects]
matched = set()

for fp in funding_projects:
    cfp = clean(fp)
    if cfp in cleaned_extracted:
        matched.add(fp)
        continue
    
    # Substring
    found = False
    for cep in cleaned_extracted:
        if cfp in cep or cep in cfp:
            # Length check
            if len(cfp) > 5 and len(cep) > 5:
                matched.add(fp)
                found = True
                break
    
    if not found:
        # Token
        fp_tok = set(cfp.split())
        for cep in cleaned_extracted:
            cep_tok = set(cep.split())
            if not fp_tok or not cep_tok: continue
            common = fp_tok.intersection(cep_tok)
            if len(common) / len(fp_tok) > 0.75:
                matched.add(fp)
                break

res = {
    'count': len(matched),
    'matched_list': list(matched),
    'extracted_debug': list(extracted_projects)[:10]
}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_function-call-8710431092191465218': 'file_storage/function-call-8710431092191465218.json', 'var_function-call-8710431092191464643': 'file_storage/function-call-8710431092191464643.json', 'var_function-call-268115837659623776': 'file_storage/function-call-268115837659623776.json'}

exec(code, env_args)
