code = """import json

# Load data from both sources
funding_file = var_functions.query_db:4
with open(funding_file) as f:
    funding_data = json.load(f)

civic_file = var_functions.query_db:28
with open(civic_file) as f:
    civic_docs = json.load(f)

# Filter funding for amounts > $50,000
high_funding = []
for record in funding_data:
    if record.get('Amount'):
        try:
            amount = int(record['Amount'])
            if amount > 50000:
                high_funding.append(record)
        except:
            pass

print('Funding records > 50k:', len(high_funding))

# Extract capital design projects from civic documents
design_names = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section index
    design_index = text.lower().find('projects (design)')
    if design_index > 0:
        # Extract section text
        section = text[design_index:design_index+3000]
        
        # Find where section ends
        end_pos = len(section)
        for marker in ['projects (construction)', 'disaster recovery projects', 'projects (not started)']:
            pos = section.lower().find(marker)
            if pos > 0 and pos < end_pos:
                end_pos = pos
        
        # Get project names from lines
        design_section = section[:end_pos]
        lines = design_section.split('\n')
        
        for i in range(len(lines)):
            line = lines[i].strip()
            
            if len(line) < 6:
                continue
            
            lower_line = line.lower()
            # Skip header lines
            if any(s in lower_line for s in ['capital improvement', 'design', 'updates:', 'project schedule', 'subject:', 'recommended']):
                continue
            
            # Check if line is likely a project name (followed by details)
            if i + 1 < len(lines):
                next_line = lines[i+1].lower()
                if 'updates:' in next_line or 'project schedule' in next_line or next_line.startswith('('):
                    clean_name = line.lstrip('0123456789.-•')
                    clean_name = clean_name.strip()
                    if len(clean_name) > 8:
                        design_names.append(clean_name)

print('Design project names extracted:', len(design_names))

# Match with funding data > $50,000
matched_projects = set()
for design_name in design_names:
    design_lower = design_name.lower()
    
    for fund_item in high_funding:
        fund_name = fund_item['Project_Name'].lower()
        
        # Simple matching logic
        if design_lower in fund_name or fund_name in design_lower:
            matched_projects.add(design_name)
            break

result = {'capital_design_projects_with_funding_over_50k': len(matched_projects)}
print('Matched count:', len(matched_projects))
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'count': '276'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
