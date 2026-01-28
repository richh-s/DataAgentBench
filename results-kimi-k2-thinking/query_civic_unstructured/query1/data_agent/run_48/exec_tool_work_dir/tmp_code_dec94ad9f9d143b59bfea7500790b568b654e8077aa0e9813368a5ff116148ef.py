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
    
    # Find design section - multiple approaches
    
    # Approach 1: Look for "Capital Improvement Projects (Design)" section
    design_patterns = [
        r'Capital Improvement Projects \(Design\)(.*?)(?=(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$))',
        r'Capital Improvement Projects \(Design\)(.*?)(?=\n\n[A-Z][A-Z\s]+\n\n|$)'
    ]
    
    design_section = None
    for pattern in design_patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            design_section = match.group(1)
            break
    
    if not design_section:
        continue
    
    # Find project names in the design section
    # Project names are typically on their own lines between blank lines
    paragraphs = design_section.split('\n\n')
    
    for para in paragraphs:
        # Clean up the paragraph
        para = para.strip()
        if not para or len(para) < 10:
            continue
        
        # Skip common non-project patterns
        skip_terms = [
            'Updates:', 'Project Schedule:', 'Estimated Schedule:',
            '(cid:', 'RECOMMENDED ACTION', 'DISCUSSION:',
            'Public Works', 'Commission', 'Agenda', 'To:',
            'Prepared by', 'Approved by', 'Date prepared',
            'Meeting date', 'Subject:', 'Page', 'Item',
            'Project is currently', 'Construction was completed',
            'Staff is working', 'City submitted', 'City received'
        ]
        
        should_skip = False
        for term in skip_terms:
            if term in para:
                should_skip = True
                break
        
        if should_skip:
            continue
        
        # Extract first line as project name
        first_line = para.split('\n')[0].strip()
        
        # Clean up project name
        first_line = re.sub(r'^[A-Z]\.\s*', '', first_line)  # Remove bullet points
        first_line = re.sub(r'^\d+\.\s*', '', first_line)    # Remove numbered lists
        first_line = re.sub(r'\s+$', '', first_line)         # Remove trailing spaces
        
        if first_line and len(first_line) >= 10:
            projects.append({
                'Project_Name': first_line,
                'status': 'design',
                'type': 'capital'
            })

print(f"DEBUG: Found {len(projects)} potential capital projects in design status")
for i, p in enumerate(projects[:10]):
    print(f"  {i+1}. {p['Project_Name']}")

# Normalize function for name comparison
def normalize_name(name):
    if not name:
        return ''
    # Lowercase, remove extra spaces, remove project suffixes
    name = name.lower().strip()
    name = re.sub(r'\s+', ' ', name)
    name = re.sub(r'\(fema[^)]*\)', '', name)
    name = re.sub(r'\(caljpia[^)]*\)', '', name)
    name = re.sub(r'\(caloes[^)]*\)', '', name)
    name = re.sub(r'\s+project\s*$', '', name)
    name = re.sub(r'[^a-z0-9\s]', '', name)
    return name.strip()

# Filter funding for projects > $50,000
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

print(f"\nDEBUG: {len(high_funding)} funding projects with amount > $50,000")

# Match projects
count = 0
for project in projects:
    proj_name = project['Project_Name']
    proj_normalized = normalize_name(proj_name)
    
    if len(proj_normalized) < 8:
        continue
    
    for fund in high_funding:
        # Exact match
        if proj_normalized == fund['Normalized_Name']:
            count += 1
            break
        
        # Substring match if one is significantly longer
        if (proj_normalized in fund['Normalized_Name'] and len(proj_normalized) > 12) or \
           (fund['Normalized_Name'] in proj_normalized and len(fund['Normalized_Name']) > 12):
            count += 1
            break

print(f'__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
