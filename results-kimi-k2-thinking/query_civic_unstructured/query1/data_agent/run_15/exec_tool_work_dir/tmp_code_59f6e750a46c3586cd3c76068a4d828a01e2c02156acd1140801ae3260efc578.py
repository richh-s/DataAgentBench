code = """import json
import re

# Load the funding data
funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load the civic documents
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Create a set of high-funding project names (> $50,000)
high_funding_projects = set()
for record in funding_data:
    amount = int(record['Amount'])
    if amount > 50000:
        high_funding_projects.add(record['Project_Name'])

# Process civic documents to extract design capital projects
# This is a more robust approach
all_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Find sections about capital improvement projects in design
    # Pattern: "Capital Improvement Projects (Design)" followed by project list
    pattern = r'capital improvement projects \(design\)(.*?)capital improvement projects \(construction\)'
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        design_section = match.group(1)
        # Split into lines and extract project names
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip internal formatting
            if line and not line.startswith('(') and not line.startswith('•') and 'updates:' not in line.lower() and 'schedule:' not in line.lower() and len(line) > 15:
                # Clean up common prefixes
                clean_line = re.sub(r'^(cid:\d+)\s*', '', line)
                if clean_line and len(clean_line) > 15:
                    all_design_projects.add(clean_line)

# Match project names (handle variations and clean names)
matching_count = 0
matching_projects = []

# Create normalized versions for matching
def normalize_name(name):
    name = name.lower().strip()
    # Remove common suffixes
    name = re.sub(r'\s*\(fema[^\)]*\)', '', name)
    name = re.sub(r'\s*\(caloes[^\)]*\)', '', name)
    name = re.sub(r'\s*\(caljpia[^\)]*\)', '', name)
    name = re.sub(r'\s*\(fema/[^\)]*\)', '', name)
    return name.strip()

# Check for matches
for design_proj in all_design_projects:
    # Direct match
    if design_proj in high_funding_projects:
        matching_count += 1
        matching_projects.append(design_proj)
    else:
        # Try normalized matching
        for funded_proj in high_funding_projects:
            if normalize_name(design_proj) in normalize_name(funded_proj) or \
               normalize_name(funded_proj) in normalize_name(design_proj):
                matching_count += 1
                matching_projects.append(f"{design_proj} -> {funded_proj}")
                break

result_summary = {
    "high_funding_projects_count": len(high_funding_projects),
    "design_projects_extracted": len(all_design_projects),
    "matching_projects_count": matching_count,
    "matching_projects": sorted(matching_projects)
}

print("__RESULT__:")
print(json.dumps(result_summary))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
