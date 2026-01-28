code = """import json

# Load funding data
funding_file = var_functions.query_db:4
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs
civic_file = var_functions.query_db:28
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Find high funding projects > $50,000
high_funding = []
for record in funding_data:
    try:
        amount = int(record.get('Amount', 0))
        if amount > 50000:
            high_funding.append({
                'name': record['Project_Name'],
                'amount': amount
            })
    except:
        pass

# Extract capital design project names from civic documents
design_names = []
for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Find design section
    design_pos = lower_text.find('capital improvement projects (design)')
    if design_pos >= 0:
        section = text[design_pos:design_pos+3000]
        section_lower = section.lower()
        
        # Find end of section
        end_pos = len(section)
        for marker in ['capital improvement projects (construction)', 'disaster recovery projects', 'capital improvement projects (not started)']:
            pos = section_lower.find(marker)
            if pos > 0 and pos < end_pos:
                end_pos = pos
        
        design_section = section[:end_pos]
        lines = design_section.split('\n')
        
        for line in lines:
            clean_line = line.strip()
            if not clean_line or len(clean_line) < 5:
                continue
            
            lower_clean = clean_line.lower()
            if any(exclude in lower_clean for exclude in ['capital improvement', 'design:', 'updates:', 'project schedule', 'subject:', 'recommended action', 'cid:']):
                continue
            
            if clean_line in ['•', '●', '■', '□']:
                continue
            
            design_names.append(clean_line)

# Match by name similarity
matched = []
for design in design_names:
    design_lower = design.lower()
    for fund in high_funding:
        fund_lower = fund['name'].lower()
        
        # Direct match or containment
        if design_lower == fund_lower or design_lower in fund_lower or fund_lower in design_lower:
            matched.append(design)
            break

# Count unique matched projects
count = len(set(matched))

print('Funding records > $50,000:', len(high_funding))
print('Design projects extracted:', len(design_names))
print('Matched projects:', count)

result = {'capital_design_projects_with_funding_over_50k': count}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'count': '276'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
