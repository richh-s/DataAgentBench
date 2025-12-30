code = """import json
import re

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
    # Find start of Design section
    section_title = 'Capital Improvement Projects (Design)'
    idx = text.find(section_title)
    if idx == -1:
        continue
    
    # Slice text from header
    content = text[idx + len(section_title):]
    
    # Process lines
    lines = content.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Stop at next section
        if 'Capital Improvement Projects' in line and '(Design)' not in line:
            break
        if 'Disaster Recovery Projects' in line:
            break
        if 'Agenda Item' in line:
            continue
            
        # Check if it looks like a project name
        # Look ahead for 'Updates:'
        is_proj = False
        # scan next few lines
        for offset in range(1, 5):
            if i + offset < len(lines):
                next_line = lines[i+offset].strip()
                if 'Updates:' in next_line or 'Project Description:' in next_line:
                    is_proj = True
                    break
                if next_line and not next_line.startswith('('): 
                    # If we hit text that doesn't look like a bullet, maybe it's the next project?
                    # Be conservative.
                    pass
        
        if is_proj:
            extracted_projects.add(line)

# Matching
def clean(s):
    # Remove parens and common words
    s = s.lower()
    s = s.replace('(fema project)', '').replace('(caloes project)', '').replace('(caljpia project)', '')
    s = s.replace('(fema)', '').replace('(design)', '')
    s = re.sub(r'\s+', ' ', s).strip()
    # Remove year prefix like '2022'
    s = re.sub(r'^\d{4}\s+', '', s)
    return s

cleaned_extracted = [clean(p) for p in extracted_projects]
matched = set()

for fp in funding_projects:
    cfp = clean(fp)
    # Check exact match in cleaned list
    if cfp in cleaned_extracted:
        matched.add(fp)
        continue
    
    # Check substring
    found = False
    for cep in cleaned_extracted:
        if cfp in cep or cep in cfp:
            # Verify length ratio to avoid short partial matches
            if len(cfp) > 5 and len(cep) > 5:
                matched.add(fp)
                found = True
                break
    
    if not found:
        # Token overlap
        fp_tok = set(cfp.split())
        for cep in cleaned_extracted:
            cep_tok = set(cep.split())
            if not fp_tok or not cep_tok: continue
            common = fp_tok.intersection(cep_tok)
            if len(common) / len(fp_tok) > 0.7:
                matched.add(fp)
                break

res = {
    'count': len(matched),
    'matched_list': list(matched),
    'extracted_sample': list(extracted_projects)[:5]
}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_function-call-8710431092191465218': 'file_storage/function-call-8710431092191465218.json', 'var_function-call-8710431092191464643': 'file_storage/function-call-8710431092191464643.json', 'var_function-call-268115837659623776': 'file_storage/function-call-268115837659623776.json'}

exec(code, env_args)
