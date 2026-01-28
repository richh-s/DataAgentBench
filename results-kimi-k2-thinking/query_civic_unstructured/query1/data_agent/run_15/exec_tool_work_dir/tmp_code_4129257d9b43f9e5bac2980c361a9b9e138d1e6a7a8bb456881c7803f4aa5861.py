code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:38']
with open(funding_path) as f:
    funding_data = json.load(f)

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:40']
with open(civic_docs_path) as f:
    civic_docs = json.load(f)

# Step 1: Create set of high-funding projects (> $50,000)
high_funding_projects = set()
for record in funding_data:
    amount = int(record['Amount'])
    if amount > 50000:
        high_funding_projects.add(record['Project_Name'])

print("Total high-funding projects:", len(high_funding_projects))

# Step 2: Extract capital projects with 'design' status from civic docs
design_capital_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
    
    if design_start != -1:
        # Extract design section
        if construction_start != -1:
            design_section = text[design_start:construction_start]
        else:
            # Look for next section or end of document
            disaster_start = text.find('Disaster Recovery Projects', design_start)
            if disaster_start != -1:
                design_section = text[design_start:disaster_start]
            else:
                design_section = text[design_start:]
        
        # Split into lines and extract project names
        lines = design_section.split('\n')
        in_project_list = False
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines, headers, footers
            if not line or len(line) < 15:
                continue
            
            # Skip page numbers and markers
            if re.match(r'^Page \d+', line) or re.match(r'^\d+ of \d+', line):
                continue
            
            # Skip internal formatting markers
            if line.startswith('(') and 'cid:' in line:
                continue
            
            # Skip update/schedule markers
            if any(marker in line for marker in ['Updates:', 'Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:']):
                continue
            
            # Skip section headers
            if 'Capital Improvement Projects' in line and 'Design' in line:
                in_project_list = True
                continue
            
            # If we're in the project list section, add the line as a project name
            if in_project_list:
                # Clean the line
                clean_line = re.sub(r'^(cid:\d+)\s*', '', line)
                clean_line = clean_line.strip()
                
                # Skip if too short or looks like a marker
                if len(clean_line) > 15 and not clean_line.startswith('•'):
                    design_capital_projects.add(clean_line)

print("Design capital projects found:", len(design_capital_projects))

# Step 3: Find matches with flexible matching
def normalize_name(name):
    """Normalize project name for comparison"""
    name = name.lower().strip()
    # Remove common suffixes
    name = re.sub(r'\s*\(fema[^\)]*\)', '', name)
    name = re.sub(r'\s*\(caloes[^\)]*\)', '', name)
    name = re.sub(r'\s*\(caljpia[^\)]*\)', name)
    name = re.sub(r'\s*project\s*$', '', name)
    return name.strip()

# Create normalized versions for matching
normalized_high_funding = {normalize_name(name): name for name in high_funding_projects}

matches = []
for design_proj in design_capital_projects:
    norm_design = normalize_name(design_proj)
    
    # Direct match
    if norm_design in normalized_high_funding:
        matches.append({
            'design_project': design_proj,
            'funded_project': normalized_high_funding[norm_design],
            'funding': int(next(r['Amount'] for r in funding_data if r['Project_Name'] == normalized_high_funding[norm_design]))
        })
    else:
        # Partial match check
        for norm_funded, original_funded in normalized_high_funding.items():
            if (norm_design in norm_funded or norm_funded in norm_design) and len(norm_design) > 10:
                matches.append({
                    'design_project': design_proj,
                    'funded_project': original_funded,
                    'funding': int(next(r['Amount'] for r in funding_data if r['Project_Name'] == original_funded))
                })
                break

print("Matching projects:", len(matches))

# Output results
result = {
    'total_high_funding_projects': len(high_funding_projects),
    'total_design_capital_projects': len(design_capital_projects),
    'matching_projects_count': len(matches),
    'matching_projects': matches
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
