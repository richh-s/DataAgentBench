code = """import json
import re
import os

# Load the data from the file paths
funding_path = "file_storage/functions.query_db:46/result.json"
civic_path = "file_storage/functions.query_db:5/result.json"

# Load funding data (projects with >$50k funding)
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents - but need to load all of them
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(funding_data)} funding records")
print(f"Loaded {len(civic_docs)} civic documents")

# Step 1: Create a lookup for high-funded projects
funded_projects_lookup = {}
for record in funding_data:
    project_name = record.get('Project_Name')
    amount = int(record.get('Amount', 0))
    funded_projects_lookup[project_name.lower()] = {
        'original_name': project_name,
        'amount': amount,
        'funding_source': record.get('Funding_Source')
    }

print(f"Found {len(funded_projects_lookup)} projects with >$50k funding")

# Step 2: Search for capital projects in design phase in civic documents
matching_projects = []

# Combine all text from civic documents
all_civic_text = ""
for doc in civic_docs:
    all_civic_text += " \n " + doc.get('text', '')

civic_text_lower = all_civic_text.lower()

# For each funded project, check if it appears in the civic text with capital and design indicators
for project_name_key in funded_projects_lookup:
    project_info = funded_projects_lookup[project_name_key]
    original_name = project_info['original_name']
    
    # Check if project name appears in civic text
    if project_name_key in civic_text_lower:
        # Find position in text
        idx = civic_text_lower.find(project_name_key)
        
        # Get surrounding context for status/type checking
        context_start = max(0, idx - 300)
        context_end = min(len(civic_text_lower), idx + 400)
        context = civic_text_lower[context_start:context_end]
        
        # Check for capital and design indicators
        has_capital = "capital" in context
        has_design = "design" in context
        
        # Avoid counting disaster projects if we can identify them
        is_capital = has_capital and "capital" in context
        
        if has_design and is_capital:
            matching_projects.append({
                'project_name': original_name,
                'funding_amount': project_info['amount'],
                'funding_source': project_info['funding_source']
            })

# Remove duplicates
unique_projects = []
seen = set()
for proj in matching_projects:
    if proj['project_name'] not in seen:
        seen.add(proj['project_name'])
        unique_projects.append(proj)

print(f"\nFound {len(unique_projects)} capital projects with design status and >$50,000 funding")

# Show some examples
if unique_projects:
    print("\nFirst few matching projects:")
    for proj in unique_projects[:5]:
        print(f"  - {proj['project_name']}: ${proj['funding_amount']}")

# Create final result
result = {
    'total_count': len(unique_projects),
    'projects': unique_projects[:10]  # Show first 10 for preview
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
