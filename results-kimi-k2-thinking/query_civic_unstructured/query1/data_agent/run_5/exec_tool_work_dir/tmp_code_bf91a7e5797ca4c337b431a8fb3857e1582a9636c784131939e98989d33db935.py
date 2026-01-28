code = """import json

# Load funding data > $50k
funding_file = locals()['var_functions.query_db:44']
with open(funding_file) as f:
    funding_recs = json.load(f)

funding_names = set([rec['Project_Name'] for rec in funding_recs])

print('Funding records:', len(funding_names))

# Load civic documents
civic_file = locals()['var_functions.query_db:2']
with open(civic_file) as f:
    civic_docs = json.load(f)

# Extract design projects - look for patterns
# Capital projects in design phase
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    start_marker = 'Capital Improvement Projects (Design)'
    end_marker = 'Capital Improvement Projects (Construction)'
    
    if start_marker in text:
        start = text.index(start_marker)
        end = text.find(end_marker, start)
        if end < 0:
            end = len(text)
        
        section = text[start:end]
        
        # Split by blocks
        blocks = section.split('\n\n')
        for block in blocks:
            block = block.strip()
            if block and len(block) > 15 and 'Design)' not in block:
                lines = [line.strip() for line in block.split('\n') if line.strip()]
                if lines and len(lines[0]) > 5:
                    name = lines[0]
                    if 'Updates' not in name and 'Schedule' not in name and not name.isupper():
                        design_projects.append(name)

print('Design projects found:', len(design_projects))

# Match design projects with funding data
# Simple match: check if design project name appears in funding name or vice versa
matched_count = 0
matched_details = []

for design_name in design_projects:
    # Normalize design name
    design_clean = design_name.split('(')[0].strip().lower()
    design_clean = design_clean.replace('project', '').strip()
    
    for fund_name in funding_names:
        # Normalize funding name
        fund_clean = fund_name.split('(')[0].strip().lower()
        fund_clean = fund_clean.replace('project', '').strip()
        
        # Check substring match
        if (design_clean in fund_clean or fund_clean in design_clean) and len(design_clean) > 5:
            matched_count += 1
            matched_details.append(f"{fund_name}: ${next(rec['Amount'] for rec in funding_recs if rec['Project_Name'] == fund_name)}")
            funding_names.remove(fund_name)  # Avoid duplicates
            break

print('\nMatched projects count:', matched_count)

result = {'count': matched_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
