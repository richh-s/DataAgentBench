code = """import json, re

# Load data files
civics = var_functions.query_db:2
funds = var_functions.query_db:5

# Handle file loading
if isinstance(civics, str) and civics.endswith('.json'):
    with open(civics) as f:
        civic_docs = json.load(f)
else:
    civic_docs = civics

if isinstance(funds, str) and funds.endswith('.json'):
    with open(funds) as f:
        funding_records = json.load(f)
else:
    funding_records = funds

# Get funding amounts > $50k
funding_data = {rec['Project_Name']: int(rec['Amount']) for rec in funding_records if int(rec['Amount']) > 50000}

# Extract design projects from civic docs
design_extracted = []

# Skip patterns as separate check
headers = ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION:', 'To:', 'Prepared by:', 'Approved by:', 'Updates:', 'Project Schedule:', 'Estimated Schedule', 'Complete Design', 'Advertise:', 'Begin Construction']

doc_idx = 0
for doc in civic_docs:
    doc_idx += 1
    text_content = doc.get('text', '')
    
    if 'Capital Improvement Projects (Design)' not in text_content:
        continue
    
    # Find start of design section
    design_pos = text_content.find('Capital Improvement Projects (Design)')
    section_end = len(text_content)
    
    # Find end of section
    end_checks = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects', 'PUBLIC WORKS QUARTERLY UPDATE', 'FEMA PROJECTS']
    for end_check in end_checks:
        end_pos = text_content.find(end_check, design_pos + 50)
        if end_pos > 0:
            section_end = min(section_end, end_pos)
    
    design_section = text_content[design_pos:section_end]
    lines = design_section.split('\n')
    
    for line in lines:
        line_data = line.strip()
        if not line_data:
            continue
        
        # Skip header lines
        skip_this = False
        for h in headers:
            if h in line_data:
                skip_this = True
                break
        if skip_this:
            continue
        
        # Skip symbol starts and short lines
        if line_data and line_data[0] in ['•', '-', '◦', '(', ')']:
            continue
        
        if line_data.isupper() and len(line_data) < 60:
            continue
        
        if len(line_data) < 10:
            continue
        
        # Skip update lines
        if any(word in line_data for word in ['Staff', 'City', 'Complete', 'Advertise', 'Begin']) and len(line_data.split()) < 5:
            continue
        
        cleaned_line = line_data.strip('•-– ')
        design_extracted.append(cleaned_line)

# Remove duplicates
design_extracted = list(set(design_extracted))

# Normalize project names for matching
def normalize_name(name):
    n = name.lower()
    n = re.sub(r'\s*\([^)]*\)$', '', n)
    n = n.replace('project', '').replace('improvements', '').replace('improvement', '')
    n = n.replace('repairs', '').replace('repair', '').replace('replacement', '')
    n = re.sub(r'[^a-z0-9\s]', '', n)
    return ' '.join(n.split())

# Create normalized lookup for funding
funding_lookup = {}
for fname, famount in funding_data.items():
    normalized = normalize_name(fname)
    funding_lookup[normalized] = (fname, famount)

# Count matching projects
counter = 0
matched_list = []

for dproject in design_extracted:
    ndesign = normalize_name(dproject)
    
    # Direct match
    if ndesign in funding_lookup:
        counter += 1
        funding_name, amount = funding_lookup[ndesign]
        matched_list.append({'design': dproject, 'funding': funding_name, 'amount': amount})
        continue
    
    # Substring match
    for nfunding, (orig_funding, amount) in funding_lookup.items():
        if ndesign in nfunding or nfunding in ndesign:
            counter += 1
            matched_list.append({'design': dproject, 'funding': orig_funding, 'amount': amount})
            break
        
        # Word overlap for longer project names
        if len(ndesign) > 15 and len(nfunding) > 15:
            dwords = set(re.findall(r'\b\w{4,}\b', ndesign))
            fwords = set(re.findall(r'\b\w{4,}\b', nfunding))
            
            if len(dwords.intersection(fwords)) >= 3:
                counter += 1
                matched_list.append({'design': dproject, 'funding': orig_funding, 'amount': amount})
                break

result = {'count': counter, 'matched': matched_list}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
