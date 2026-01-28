code = """import json

# Load funding data
funding_path = var_functions.query_db:0
with open(funding_path) as f:
    funding_data = json.load(f)

# Load civic documents
civic_path = var_functions.query_db:2
with open(civic_path) as f:
    civic_docs = json.load(f)

# Get projects with funding > $50,000
high_funding_projects = []
for record in funding_data:
    amount = int(record['Amount'])
    if amount > 50000:
        high_funding_projects.append({'name': record['Project_Name'], 'amount': amount})

# Extract capital design project names from civic documents
design_project_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Extract content after header
    content_after_header = text[design_start + 37:]  # Length of "Capital Improvement Projects (Design)"
    
    # Find where design section ends (look for next major section)
    design_content = content_after_header
    next_sections = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
    
    for next_section in next_sections:
        section_pos = design_content.find(next_section)
        if section_pos > 0:
            design_content = design_content[:section_pos]
            break
    
    # Split into blocks and extract potential project names
    blocks = design_content.split('\n\n')
    for block in blocks:
        block = block.strip()
        if len(block) < 10:
            continue
        
        # Get the first line which is likely the project name
        lines = block.split('\n')
        if not lines:
            continue
        
        first_line = lines[0].strip()
        
        # Apply filters to identify project names
        if len(first_line) < 10:
            continue
        
        if first_line.isupper():
            continue
        
        if 'Updates:' in first_line or 'Schedule:' in first_line:
            continue
        
        # Skip known non-project patterns
        if first_line.startswith('(') and 'cid:' in first_line:
            continue
        
        if 'Project is currently' in first_line or 'Construction was completed' in first_line:
            continue
        
        # Remove bullet prefixes if present
        clean_name = first_line
        if len(clean_name) >= 3:
            # Remove patterns like "A. ", "1. ", "2. ", etc.
            if clean_name[0].isalpha() and clean_name[1] == '.':
                clean_name = clean_name[2:].strip()
            elif clean_name[0].isdigit() and clean_name[1] == '.':
                clean_name = clean_name[2:].strip()
        
        # Final length check
        if len(clean_name) > 10:
            design_project_names.append(clean_name)

# Remove duplicates while preserving order (for cleaner matching)
unique_design_projects = []
seen = set()
for proj in design_project_names:
    if proj not in seen:
        seen.add(proj)
        unique_design_projects.append(proj)

# Debug info
print(f"Found {len(unique_design_projects)} capital projects in design status")
print('First 10 projects:', unique_design_projects[:10])

# Now match these with high funding projects
matched_projects = []

# Normalize project names for matching
import re

def normalize_project_name(name):
    # Convert to lowercase
    normalized = name.lower()
    # Remove special characters but keep spaces
    normalized = re.sub(r'[^a-z0-9\s]', '', normalized)
    # Remove extra spaces
    normalized = ' '.join(normalized.split())
    # Remove common suffixes like "project", "repair", "construction"
    normalized = re.sub(r'\s+project\s*$', '', normalized)
    normalized = re.sub(r'\s+repair\s*$', '', normalized)
    normalized = re.sub(r'\s+repairs\s*$', '', normalized)
    normalized = re.sub(r'\s+improvements\s*$', '', normalized)
    normalized = re.sub(r'\s+improvement\s*$', '', normalized)
    normalized = re.sub(r'\s+construction\s*$', '', normalized)
    return normalized.strip()

# Try to match each design project with funding projects
for design_proj in unique_design_projects:
    design_normalized = normalize_project_name(design_proj)
    
    if len(design_normalized) < 5:
        continue
    
    for fund_proj in high_funding_projects:
        fund_name = fund_proj['name']
        fund_normalized = normalize_project_name(fund_name)
        
        # Direct match
        if design_normalized == fund_normalized:
            matched_projects.append({
                'project_name': design_proj,
                'funding_name': fund_name,
                'amount': fund_proj['amount']
            })
            break
        
        # Substring match (if one contains the other and is long enough)
        if (len(design_normalized) > 15 and design_normalized in fund_normalized) or \
           (len(fund_normalized) > 15 and fund_normalized in design_normalized):
            matched_projects.append({
                'project_name': design_proj,
                'funding_name': fund_name,
                'amount': fund_proj['amount']
            })
            break
        
        # Word overlap matching for multi-word names
        design_words = set(design_normalized.split())
        fund_words = set(fund_normalized.split())
        
        if len(design_words) >= 3 and len(fund_words) >= 3:
            common_words = design_words.intersection(fund_words)
            if len(common_words) >= 3:
                matched_projects.append({
                    'project_name': design_proj,
                    'funding_name': fund_name,
                    'amount': fund_proj['amount']
                })
                break

print(f"Matched {len(matched_projects)} projects with funding > $50,000")
print('Sample matches:')
for mp in matched_projects[:5]:
    print(f"  {mp['project_name']} -> ${mp['amount']}")

# The answer is the count
result = len(matched_projects)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}], 'var_functions.query_db:56': [{'count': '276'}]}

exec(code, env_args)
