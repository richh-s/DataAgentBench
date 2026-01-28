code = """import json

# Load funding data
funding_file = locals()['var_functions.query_db:72']
with open(funding_file) as f:
    funding_records = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:2']
with open(civic_file) as f:
    civic_docs = json.load(f)

# Get projects with funding > $50,000
funding_dict = {}
for rec in funding_records:
    name = rec['Project_Name']
    amount = int(rec['Amount'])
    funding_dict[name] = amount

print('Funding projects > $50k:', len(funding_dict))

# Extract design status projects from civic documents
design_project_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    start_pos = text.find('Capital Improvement Projects (Design)')
    if start_pos >= 0:
        end_pos = text.find('Capital Improvement Projects (Construction)', start_pos)
        if end_pos < 0:
            end_pos = len(text)
        
        design_section = text[start_pos:end_pos]
        
        # Split into blocks
        blocks = design_section.split('\n\n')
        for block in blocks:
            block = block.strip()
            if block and len(block) > 20 and 'Design)' not in block:
                lines = block.split('\n')
                if lines:
                    first_line = lines[0].strip()
                    # Validate
                    if (first_line and 'Updates' not in first_line and 
                        'Schedule' not in first_line and not first_line.isupper() and
                        len(first_line) > 10):
                        design_project_names.append(first_line)

print('Design status projects:', len(design_project_names))

# Match design projects with funding data
matched_count = 0
matched_names = set()

for design_name in design_project_names:
    # Normalize design name
    design_clean = design_name.split('(')[0].strip().lower()
    design_clean = design_clean.replace('project', '').strip()
    
    for fund_name in funding_dict:
        if fund_name in matched_names:
            continue
        
        # Normalize funding name
        fund_clean = fund_name.split('(')[0].strip().lower()
        fund_clean = fund_clean.replace('project', '').strip()
        
        # Check substring match
        if design_clean in fund_clean or fund_clean in design_clean:
            matched_count += 1
            matched_names.add(fund_name)
            break

print('Matched count:', matched_count)
result = {'count': matched_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
