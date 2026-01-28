code = """import json
import re

# Load data files
civic_file = var_functions.query_db:2
funding_file = var_functions.query_db:5

if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_file

if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_file

# Get funding projects over $50k
funding_projects = {}
for rec in funding_records:
    try:
        amount = int(rec['Amount'])
        if amount > 50000:
            funding_projects[rec['Project_Name']] = int(rec['Amount'])
    except:
        pass

# Extract design projects from civic docs
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    design_marker = 'Capital Improvement Projects (Design)'
    if design_marker not in text:
        continue
    
    start = text.find(design_marker)
    section_end = len(text)
    
    end_markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects', 'PUBLIC WORKS QUARTERLY UPDATE', 'FEMA PROJECTS']
    
    for marker in end_markers:
        pos = text.find(marker, start + len(design_marker))
        if pos > 0 and pos < section_end:
            section_end = pos
    
    section_text = text[start:section_end]
    lines = section_text.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        skip_terms = ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION', 'To:', 'Prepared by', 'Approved by', 'Updates:', 'Project Schedule', 'Estimated Schedule', 'Complete Design', 'Advertise:', 'Begin Construction', 'Staff is', 'City is', 'Subject:']
        if any(term in line for term in skip_terms):
            continue
        
        if line.isupper() and len(line) < 60:
            continue
        
        if line[0] in ['•', '-', '◦', '(', ')']:
            continue
        
        if len(line) < 10:
            continue
        
        if re.match(r'^[A-Za-z]+ \d{4}$', line):
            continue
        
        cleaned = line.strip('•-– ')
        update_words = ['Staff', 'City', 'Project', 'Complete', 'Advertise', 'Begin']
        if any(word in cleaned for word in update_words) and len(cleaned.split()) < 4:
            continue
        
        if cleaned:
            design_projects.append(cleaned)

# Remove duplicates
design_projects = list(set(design_projects))

# Match projects using flexible string matching
def simplify_name(name):
    n = name.lower().replace('project', '').replace('improvements', '').replace('improvement', '')
    n = n.replace('repairs', '').replace('repair', '').replace('replacement', '')
    n = re.sub(r'\s*\([^)]*\)$', '', n)
    return ' '.join(n.split())

counted = []
for design in design_projects:
    design_simple = simplify_name(design)
    
    for funding in funding_projects:
        funding_simple = simplify_name(funding)
        
        # Direct match
        if design_simple in funding_simple or funding_simple in design_simple:
            counted.append({'design': design, 'funding': funding, 'amount': funding_projects[funding]})
            break
        
        # Clean match
        d_clean = re.sub(r'[^a-z0-9\s]', '', design_simple)
        f_clean = re.sub(r'[^a-z0-9\s]', '', funding_simple)
        if d_clean in f_clean or f_clean in d_clean:
            counted.append({'design': design, 'funding': funding, 'amount': funding_projects[funding]})
            break
        
        # Word overlap
        if len(design_simple) > 12 and len(funding_simple) > 12:
            d_words = set(re.findall(r'\b\w{4,}\b', design_simple))
            f_words = set(re.findall(r'\b\w{4,}\b', funding_simple))
            if len(d_words.intersection(f_words)) >= 2:
                counted.append({'design': design, 'funding': funding, 'amount': funding_projects[funding]})
                break

result = {'count': len(counted), 'matches': counted}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
