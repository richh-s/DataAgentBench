code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs)}")

# Create a set of high-funding project names for fast lookup
high_funding_projects = set()
for item in funding_data:
    if int(item['Amount']) > 50000:
        high_funding_projects.add(item['Project_Name'])

print(f"Projects with >$50k funding: {len(high_funding_projects)}")
print("Sample high-funding projects:", list(high_funding_projects)[:10])

# Process civic documents to find capital projects with design status
design_capital_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for "Capital Improvement Projects (Design)" section
    # Pattern to find project names under this section
    design_section = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Disaster Recovery Projects|\Z)', 
                                text, re.DOTALL | re.IGNORECASE)
    
    if design_section:
        section_text = design_section.group(1)
        
        # Extract project names - they typically appear as titles/headings
        # Look for lines that are likely project names
        lines = section_text.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and common markers
            if (line and 
                not line.startswith('(') and 
                not line.startswith('•') and 
                not line.startswith('-') and
                not line.startswith('Page') and
                'Updates:' not in line and
                'Schedule:' not in line and
                len(line) > 10 and  # Reasonable length for a project name
                not re.match(r'^[\d\s]+$', line)):  # Not just numbers
                
                # Clean up the line - remove common prefixes
                clean_line = re.sub(r'^(cid:\d+)\s*', '', line)
                clean_line = re.sub(r'^[A-Z]\s+', '', clean_line)
                
                if len(clean_line) > 10:
                    design_capital_projects.add(clean_line)

print(f"Capital projects in design status found: {len(design_capital_projects)}")
print("Sample design capital projects:", list(design_capital_projects)[:10])

# Find intersection - projects that are both in design status AND have >$50k funding
matching_projects = design_capital_projects.intersection(high_funding_projects)

print(f"\nMatching projects (design + >$50k): {len(matching_projects)}")
if matching_projects:
    print("Matching project names:")
    for proj in sorted(matching_projects):
        print(f"  - {proj}")

result = {
    "high_funding_count": len(high_funding_projects),
    "design_capital_count": len(design_capital_projects),
    "matching_count": len(matching_projects),
    "matching_projects": sorted(list(matching_projects))
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
