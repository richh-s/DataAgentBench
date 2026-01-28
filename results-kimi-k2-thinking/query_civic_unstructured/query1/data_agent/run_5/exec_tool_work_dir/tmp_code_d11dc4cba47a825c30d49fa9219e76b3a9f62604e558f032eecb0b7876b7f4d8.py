code = """import json
import re

# Read the funding data (large file)
funding_file_path = locals()['var_functions.query_db:0']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Read the civic docs data (large file)
civic_docs_file_path = locals()['var_functions.query_db:2']
with open(civic_docs_file_path, 'r') as f:
    civic_docs = json.load(f)

# Process funding data to get projects with Amount > 50000
funding_projects = [f for f in funding_data if f['Amount'] and int(f['Amount']) > 50000]
funding_names = set([p['Project_Name'] for p in funding_projects])

print(f"Found {len(funding_projects)} funding records with Amount > $50,000")

# Extract project information from civic documents
projects_from_docs = []

# Parse each document for project information
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for sections mentioning Design, Construction, Not Started status
    # The format appears to be: Project Name followed by Updates and Project Schedule
    
    # Find project names by looking for lines that are likely project titles
    # They often appear as section headers or at the start of paragraphs
    
    # Split by sections that categorize projects
    design_section = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Disaster Recovery|\Z)', text, re.DOTALL)
    
    if design_section:
        design_text = design_section.group(1)
        # Extract project names - look for lines that appear to be project titles
        # Usually they're at the start of a new paragraph or have project names
        
        # Split by double newlines or look for patterns
        blocks = design_text.split('\n\n')
        
        for block in blocks:
            # Look for project names - typically the first line without leading tab/bullet
            lines = block.strip().split('\n')
            if lines:
                first_line = lines[0].strip()
                # Check if it's a project name (unlikely to be a status marker or instruction)
                if first_line and len(first_line) > 5 and not first_line.startswith('(') and not first_line.startswith('•') and not first_line.startswith('('):
                    # Clean up the name
                    clean_name = first_line.strip('• ').strip()
                    if clean_name and len(clean_name) > 5:
                        projects_from_docs.append({
                            'project_name': clean_name,
                            'type': 'capital',
                            'status': 'design',
                            'source': filename
                        })

# Standardize project names by removing suffixes like (FEMA), (CalJPIA), (CalOES) etc.
def normalize_project_name(name):
    # Remove common suffixes
    name = re.sub(r'\s*\(FEMA[^)]*\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalJPIA[^)]*\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalOES[^)]*\)', '', name, flags=re.IGNORECASE)
    return name.strip()

# Match projects with design status to funding data
matched_projects = []

for doc_project in projects_from_docs:
    doc_name = doc_project['project_name']
    norm_doc_name = normalize_project_name(doc_name)
    
    # Try to match with funding projects
    for fund_proj in funding_projects:
        fund_name = fund_proj['Project_Name']
        norm_fund_name = normalize_project_name(fund_name)
        
        # Check if they match (exact or substring)
        if (norm_doc_name.lower() in norm_fund_name.lower() 
            or norm_fund_name.lower() in norm_doc_name.lower()
            or norm_doc_name.replace('Project', '').strip().lower() in norm_fund_name.lower()
            or norm_fund_name.replace('Project', '').strip().lower() in norm_doc_name.lower()):
            matched_projects.append({
                'project_name': fund_name,
                'amount': int(fund_proj['Amount']),
                'status': 'design',
                'type': 'capital'
            })
            break

# Remove duplicates
unique_matched = []
seen = set()
for proj in matched_projects:
    if proj['project_name'] not in seen:
        unique_matched.append(proj)
        seen.add(proj['project_name'])

print(f"Found {len(unique_matched)} capital projects with design status and funding > $50,000")

# Print a sample of matched projects for verification
for i, proj in enumerate(unique_matched[:10]):
    print(f"{i+1}. {proj['project_name']} - ${proj['amount']}")

# Final result
result = {
    'count': len(unique_matched),
    'projects': unique_matched[:20]  # Include first 20 for detail
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
