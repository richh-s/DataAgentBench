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

# Extract capital projects in design status from civic documents
# Look for the design section and extract project names
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for design section marker
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Split text and look for design section
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) < 2:
        continue
    
    # Get the part after the Design header, up to the next major section
    design_part = parts[1]
    
    # Find where the design section ends
    for marker in ['Capital Improvement Projects (Construction)',
                   'Capital Improvement Projects (Not Started)',
                   'Disaster Recovery Projects']:
        if marker in design_part:
            design_part = design_part.split(marker)[0]
            break
    
    # Split into paragraphs (double newlines indicate new section/project)
    sections = design_part.split('\n\n')
    
    for section in sections:
        section = section.strip()
        if not section or len(section) < 10:
            continue
        
        # Skip various non-project headers
        first_line = section.split('\n')[0].strip()
        
        skip = False
        check_line = first_line.upper()
        
        # Skip if contains update/schedule terms
        skip_terms = ['UPDATES', 'PROJECT SCHEDULE', 'ESTIMATED SCHEDULE',
                     'COMPLETE DESIGN', 'ADVERTISE', 'BEGIN CONSTRUCTION',
                     'RECOMMENDED ACTION', 'DISCUSSION']
        for term in skip_terms:
            if term in check_line:
                skip = True
                break
        
        if skip:
            continue
        
        # Skip if appears to be a short heading
        if len(first_line.split()) <= 2 and first_line.isupper():
            continue
        
        # Clean up the name
        name = first_line
        name = re.sub(r'^[A-Z]\.\s*', '', name)  # Remove A. B. bullets
        name = re.sub(r'^\d+\.\s*', '', name)    # Remove numbered bullets
        name = re.sub(r'\s+project\s*$', '', name, flags=re.IGNORECASE)
        name = name.strip()
        
        # Add if it looks like a real project name (reasonable length)
        if 10 <= len(name) <= 150:
            projects.append({
                'Project_Name': name,
                'status': 'design',
                'type': 'capital'
            })

# Normalize function for comparison
def normalize_name(name):
    if not name:
        return ''
    n = name.lower().strip()
    n = re.sub(r'\s+', ' ', n)  # Normalize spaces
    n = re.sub(r'\(fema[^)]*\)', '', n)  # Remove FEMA suffix
    n = re.sub(r'\(caljpia[^)]*\)', '', n)  # Remove CalJPIA suffix
    n = re.sub(r'\(caloes[^)]*\)', '', n)  # Remove CalOES suffix
    n = re.sub(r'\s+project\s*$', '', n)  # Remove 'project' at end
    n = re.sub(r'[^a-z0-9\s]', '', n)  # Remove special chars
    return n.strip()

# Filter funding for amounts > 50000
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

# Match projects with funding
matched_count = 0

for project in projects:
    proj_name = project['Project_Name']
    proj_normalized = normalize_name(proj_name)
    
    # Skip very short normalized names
    if len(proj_normalized) < 8:
        continue
    
    for fund in high_funding:
        fund_normalized = fund['Normalized_Name']
        
        # Direct match
        if proj_normalized == fund_normalized:
            matched_count += 1
            break
        
        # Substring match for longer names
        if len(proj_normalized) > 12 and proj_normalized in fund_normalized:
            matched_count += 1
            break
        
        if len(fund_normalized) > 12 and fund_normalized in proj_normalized:
            matched_count += 1
            break
        
        # Word overlap match for multi-word names
        proj_words = proj_normalized.split()
        fund_words = fund_normalized.split()
        
        if len(proj_words) >= 4 and len(fund_words) >= 4:
            common = set(proj_words) & set(fund_words)
            if len(common) >= 3:
                matched_count += 1
                break

result = matched_count
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
