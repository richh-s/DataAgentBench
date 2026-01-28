code = """import json

# Get funding data with amount > 50000
funding_path = var_functions.query_db:70
with open(funding_path) as f:
    funding_records = json.load(f)

# Get civic documents 
civic_path = var_functions.query_db:78
with open(civic_path) as f:
    civic_documents = json.load(f)

# Create set of high funding project names for fast lookup
high_funding_names = set()
for record in funding_records:
    amount = int(record['Amount'])
    if amount > 50000:
        high_funding_names.add(record['Project_Name'])

# Extract capital design projects from civic documents
design_projects = []

for doc in civic_documents:
    text = doc.get('text', '')
    
    # Find design section  
    design_marker = 'Capital Improvement Projects (Design)'
    if design_marker not in text:
        continue
    
    # Get section after design marker
    design_section = text[text.find(design_marker) + len(design_marker):]
    
    # Cut at next major section
    end_markers = ['Capital Improvement Projects (Construction)', 
                   'Capital Improvement Projects (Not Started)', 
                   'Disaster Recovery Projects']
    
    for marker in end_markers:
        pos = design_section.find(marker)
        if pos > 0:
            design_section = design_section[:pos]
            break
    
    # Find project names - look for paragraphs that start with capitalized words
    paragraphs = design_section.split('\n\n')
    for para in paragraphs:
        para = para.strip()
        # Skip short lines and obvious non-project entries
        if len(para) < 10 or 'Updates:' in para or 'Schedule:' in para or para.startswith('('):
            continue
        
        # Get first line
        lines = para.split('\n')
        first_line = lines[0].strip() if lines else ''
        
        # Filter for likely project names
        if len(first_line) > 10 and not first_line.isupper():
            design_projects.append(first_line)

# Find matches using flexible name matching
matched = 0
for proj in design_projects:
    proj_lower = proj.lower()
    for fund in high_funding_names:
        fund_lower = fund.lower()
        if proj_lower == fund_lower or proj in fund or fund in proj:
            matched += 1
            break
        proj_words = set(proj_lower.split())
        fund_words = set(fund_lower.split())
        if len(proj_words) >= 2 and len(fund_words) >= 2 and len(proj_words & fund_words) >= 2:
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}], 'var_functions.query_db:56': [{'count': '276'}], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json'}

exec(code, env_args)
