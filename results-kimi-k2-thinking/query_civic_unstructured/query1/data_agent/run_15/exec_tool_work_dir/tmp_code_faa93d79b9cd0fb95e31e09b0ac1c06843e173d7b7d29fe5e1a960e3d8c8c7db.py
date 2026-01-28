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

# Create high-funding project set
high_funding = set()
for item in funding_data:
    if int(item['Amount']) > 50000:
        high_funding.add(item['Project_Name'])

# Extract design capital projects
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Disaster Recovery)', text, re.DOTALL | re.IGNORECASE)
    
    if design_match:
        section = design_match.group(1)
        lines = section.split('\n')
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith('(') and not line.startswith('•') and not line.startswith('-') and 'Updates:' not in line and 'Schedule:' not in line and len(line) > 10:
                clean = re.sub(r'^(cid:\d+)\s*', '', line)
                if len(clean) > 10:
                    design_projects.add(clean)

# Find matches
matches = design_projects.intersection(high_funding)

print(f"High funding: {len(high_funding)}, Design: {len(design_projects)}, Matches: {len(matches)}")

result = {
    "high_funding_count": len(high_funding),
    "design_capital_count": len(design_projects),
    "matching_count": len(matches),
    "matching_projects": sorted(list(matches))
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
