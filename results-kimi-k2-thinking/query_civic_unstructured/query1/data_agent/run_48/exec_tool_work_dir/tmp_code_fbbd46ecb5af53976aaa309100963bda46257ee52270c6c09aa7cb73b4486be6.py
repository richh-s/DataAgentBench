code = """import json
import re

# Load funding data
funding_file_path = var_functions.query_db:0
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file_path = var_functions.query_db:2
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Extract capital projects with design status from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    section_start = text.find('Capital Improvement Projects (Design)')
    if section_start == -1:
        continue
    
    # Find where the design section ends (look for next major section)
    section_end = text.find('Capital Improvement Projects (Construction)', section_start)
    if section_end == -1:
        section_end = text.find('Capital Improvement Projects (Not Started)', section_start)
    if section_end == -1:
        section_end = text.find('Disaster Recovery Projects', section_start)
    if section_end == -1:
        section_end = len(text)
    
    design_section = text[section_start:section_end]
    
    # Find project names - they appear as bolded/standalone lines
    # Split into paragraphs (double newlines)
    paragraphs = design_section.split('\n\n')
    
    for para in paragraphs:
        para = para.strip()
        if not para or len(para) < 10:
            continue
        
        # Skip non-project lines
        skip_terms = ['Updates:', 'Project Schedule:', 'Estimated Schedule:',
                     '(cid:', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Public Works',
                     'Commission', 'Agenda', 'To:', 'Prepared by', 'Approved by',
                     'Date prepared', 'Meeting date', 'Subject:', 'Page', 'Item',
                     'Project is currently', 'Construction was completed',
                     'Staff is working', 'City submitted', 'City received',
                     'On September', 'On February', 'On', 'Staff has',
                     'Complete Design:', 'Advertise:', 'Begin Construction:']
        
        should_skip = False
        for term in skip_terms:
            if term in para:
                should_skip = True
                break
        
        if should_skip:
            continue
        
        # Get first line
        first_line = para.split('\n')[0].strip()
        
        # Clean name
        first_line = re.sub(r'^[A-Z]\.\s*', '', first_line)
        first_line = re.sub(r'^\d+\.\s*', '', first_line)
        first_line = re.sub(r'\s+project\s*$', '', first_line, flags=re.IGNORECASE)
        
        # Skip if too short or contains certain patterns
        if (len(first_line) >= 10 and 
            not first_line.startswith('(') and
            not re.match(r'^[A-Z\s]+$', first_line) and  # Skip all caps headings
            len(first_line.split()) > 2):  # At least 3 words
            
            projects.append({
                'Project_Name': first_line,
                'status': 'design',
                'type': 'capital'
            })

# Normalize function
def normalize_name(name):
    if not name:
        return ''
    name = name.lower().strip()
    name = re.sub(r'\s+', ' ', name)
    name = re.sub(r'\(fema[^)]*\)', '', name)
    name = re.sub(r'\(caljpia[^)]*\)', '', name)
    name = re.sub(r'\(caloes[^)]*\)', '', name)
    name = re.sub(r'\s+project\s*$', '', name)
    name = re.sub(r'[^a-z0-9\s]', '', name)
    return name.strip()

# Get funding > $50k
high_funding = []
for fund in funding_data:
    amount = int(fund['Amount'])
    if amount > 50000:
        high_funding.append({
            'Project_Name': fund['Project_Name'],
            'Amount': amount,
            'Normalized_Name': normalize_name(fund['Project_Name']),
            'Original_Name': fund['Project_Name']
        })

# Match projects
count = 0
matched_names = []

for project in projects:
    proj_name = project['Project_Name']
    proj_normalized = normalize_name(proj_name)
    
    if len(proj_normalized) < 8:
        continue
    
    for fund in high_funding:
        fund_normalized = fund['Normalized_Name']
        
        # Various matching strategies
        if proj_normalized == fund_normalized:
            count += 1
            matched_names.append(proj_name)
            break
        
        # Substring matching for longer names
        if (len(proj_normalized) > 15 and proj_normalized in fund_normalized) or \
           (len(fund_normalized) > 15 and fund_normalized in proj_normalized):
            count += 1
            matched_names.append(proj_name)
            break
        
        # Key words matching (if 4+ key words match)
        proj_words = set(proj_normalized.split())
        fund_words = set(fund_normalized.split())
        if len(proj_words.intersection(fund_words)) >= 4 and len(proj_words) >= 5:
            count += 1
            matched_names.append(proj_name)
            break

result = count
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
