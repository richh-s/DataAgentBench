code = """import json

# Load funding data
funding_file = var_functions.query_db:4
with open(funding_file) as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = var_functions.query_db:28
with open(civic_file) as f:
    civic_docs = json.load(f)

# Get high funding projects > $50,000
high_funding = []
for item in funding_data:
    if item.get('Amount'):
        try:
            amount = int(item['Amount'])
            if amount > 50000:
                high_funding.append(item)
        except:
            continue

print('High funding projects:', len(high_funding))

# Extract capital design projects from documents
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    start_pos = -1
    for i in range(len(text) - 30):
        if text[i:i+30].lower() == 'capital improvement projects (design)':
            start_pos = i + 30
            break
    
    if start_pos >= 0:
        # Find end of section
        end_pos = len(text)
        for i in range(start_pos, min(len(text), start_pos + 3000)):
            if text[i:i+35].lower() == 'capital improvement projects (construction)':
                end_pos = i
                break
            elif text[i:i+20].lower() == 'disaster recovery projects':
                end_pos = i
                break
        
        section = text[start_pos:end_pos]
        
        # Get project names (lines that are likely project names)
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 8:
                lower_line = line.lower()
                # Skip common headers
                if 'capital improvement' in lower_line or 'project schedule' in lower_line or 'updates:' in lower_line or 'subject:' in lower_line:
                    continue
                if line in ['•', '●', '■', '□']:
                    continue
                
                # Remove leading numbers and symbols
                while line and (line[0].isdigit() or line[0] in ['•', '-', '.', '■']):
                    line = line[1:]
                line = line.strip()
                
                if len(line) > 8 and line not in design_projects:
                    design_projects.append(line)

print('Design projects extracted:', len(design_projects))

# Match with funding
matches = set()
for design_name in design_projects:
    design_lower = design_name.lower()
    for fund_item in high_funding:
        fund_name = fund_item['Project_Name'].lower()
        
        # Check if one name contains the other
        if design_lower in fund_name or fund_name in design_lower:
            matches.add(design_name)
            break

result = {'count': len(matches)}
print('Matched projects:', len(matches))
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'count': '276'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
