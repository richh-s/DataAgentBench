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

# Debug: print info about the data
print(f"Total funding records: {len(funding_data)}")
print(f"Total civic documents: {len(civic_docs)}")

# Extract capital projects with design status from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for the Capital Improvement Projects (Design) section
    # Pattern to find the design section
    design_section_pattern = r'Capital Improvement Projects \(Design\)([\s\S]*?)(?=Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)'
    design_sections = re.findall(design_section_pattern, text)
    
    for section in design_sections:
        # Split by blank lines to find project names
        paragraphs = section.split('\n\n')
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
                
            # Skip known non-project lines
            skip_patterns = [
                '^Updates:$', '^Project Schedule:', '^Estimated Schedule:',
                '^\\(cid:', '^RECOMMENDED ACTION', '^DISCUSSION:',
                '^Public Works', '^Commission', '^Agenda', '^To:',
                '^Prepared by', '^Approved by', '^Date prepared',
                '^Meeting date', '^Subject:', '^Page \\d+',
                '^Item', '^Malibu Road', '^Encinal Canyon', '^Bluffs Park'
            ]
            
            should_skip = False
            for pattern in skip_patterns:
                if re.search(pattern, para, re.IGNORECASE):
                    should_skip = True
                    break
            
            if should_skip:
                continue
            
            # Extract project name (usually up to the first newline if there are multiple)
            project_name = para.split('\n')[0].strip()
            
            # Skip if too short or contains common non-project text
            if (len(project_name) < 10 or 
                'Project is currently' in project_name or
                'Construction was completed' in project_name or
                'Staff is working' in project_name):
                continue
            
            # Clean up the name
            project_name = re.sub(r'^[A-Z]\\.\\s*', '', project_name)  # Remove bullet points
            project_name = re.sub(r'^\\d+\\.\\s*', '', project_name)  # Remove numbered lists
            
            if project_name and not project_name.startswith('('):
                projects.append({
                    'Project_Name': project_name,
                    'status': 'design',
                    'type': 'capital'
                })

print(f"\nExtracted {len(projects)} potential capital projects in design status")
for i, p in enumerate(projects[:15]):
    print(f"  {i+1}. {p['Project_Name']}")

# Now match with funding data
def normalize_name(name):
    """Normalize project name for comparison"""
    if not name:
        return ''
    # Convert to lowercase, remove extra spaces, remove project suffixes
    name = name.lower().strip()
    name = re.sub(r'\\s+', ' ', name)
    name = re.sub(r'\\(fema[^)]*\\)', '', name)
    name = re.sub(r'\\(caljpia[^)]*\\)', '', name)
    name = re.sub(r'\\(caloes[^)]*\\)', '', name)
    name = re.sub(r'\\s+project\\s*$', '', name)
    name = re.sub(r'[^a-z0-9\\s]', '', name)
    return name.strip()

# Create a list of funding projects with amount > 50000
high_funding_projects = []
for fund in funding_data:
    if int(fund['Amount']) > 50000:
        high_funding_projects.append({
            'Project_Name': fund['Project_Name'],
            'Amount': int(fund['Amount']),
            'Normalized_Name': normalize_name(fund['Project_Name']),
            'Original_Name': fund['Project_Name']
        })

print(f"\nTotal funding projects > $50k: {len(high_funding_projects)}")

# Match projects
matched_count = 0
matched_details = []

for project in projects:
    proj_name = project['Project_Name']
    proj_normalized = normalize_name(proj_name)
    
    # Skip very short names
    if len(proj_normalized) < 5:
        continue
    
    for fund in high_funding_projects:
        # Check for exact normalized match
        if proj_normalized == fund['Normalized_Name']:
            matched_count += 1
            matched_details.append({
                'project_name': proj_name,
                'funding_name': fund['Original_Name'],
                'amount': fund['Amount']
            })
            break
        
        # Check if project name is contained in funding name
        if proj_normalized in fund['Normalized_Name'] and len(proj_normalized) > 10:
            matched_count += 1
            matched_details.append({
                'project_name': proj_name,
                'funding_name': fund['Original_Name'],
                'amount': fund['Amount']
            })
            break
        
        # Check if funding name is contained in project name
        if fund['Normalized_Name'] in proj_normalized and len(fund['Normalized_Name']) > 10:
            matched_count += 1
            matched_details.append({
                'project_name': proj_name,
                'funding_name': fund['Original_Name'],
                'amount': fund['Amount']
            })
            break

print(f"\nFound {matched_count} matches with funding > $50,000")
for i, detail in enumerate(matched_details[:10]):
    print(f"  {i+1}. {detail['project_name']} - ${detail['amount']}")

result = matched_count
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
