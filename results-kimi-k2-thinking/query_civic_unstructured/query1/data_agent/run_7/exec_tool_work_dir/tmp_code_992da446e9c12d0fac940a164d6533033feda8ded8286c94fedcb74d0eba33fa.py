code = """import json
import re

# Load the data from stored variable names
mongo_key = 'var_functions.query_db:10'
funding_key = 'var_functions.query_db:5'

# Get the actual data from locals()
mongo_result = locals().get(mongo_key)
funding_result = locals().get(funding_key)

# Load MongoDB data
if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_result if mongo_result else []

# Load funding data from the string path
if isinstance(funding_result, str):
    with open(funding_result, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_result if funding_result else []

# Extract project information from MongoDB documents
# We'll look for projects mentioned in the text with 'design' status
design_projects = []

for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Look for sections about design projects
    # Pattern: look for project names followed by design-related keywords
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for capital improvement projects in design phase
        if 'design' in text.lower() and 'capital improvement' in text.lower():
            # Extract project names from the document
            # This is a simplified extraction - looking for project-like names
            if line and len(line) > 10 and not line.startswith('(') and not line.isupper():
                # Skip common headers and noise
                skip_words = ['Public Works', 'Commission', 'Agenda', 'Item', 'Page', 'To:', 'From:', 'Subject:', 'Recommended Action']
                if not any(skip in line for skip in skip_words):
                    # Look for project names that might appear
                    if i > 0:
                        prev_line = lines[i-1].strip()
                        # Check if this looks like a project name
                        if len(line.split()) <= 8 and not line.endswith(':') and not line.startswith('•'):
                            design_projects.append(line)

# Get unique design projects from MongoDB
unique_design_projects = list(set(design_projects))

# Filter funding records for those with Amount > 50000
high_funding_records = []
for record in funding_records:
    try:
        amount = int(record.get('Amount', 0))
        if amount > 50000:
            high_funding_records.append(record)
    except:
        continue

# Create a mapping of project names to funding amounts
funding_map = {}
for record in high_funding_records:
    project_name = record.get('Project_Name', '')
    if project_name:
        funding_map[project_name] = int(record.get('Amount', 0))

# Try to match design projects with funding
matched_design_projects = []

# Check if we can find any projects with 'design' in their context
for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Look for sections marked as (Design)
    if '(Design)' in text or '(Design Phase)' in text:
        # Extract project names around these markers
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if '(Design)' in line or '(Design Phase)' in line:
                # Look for project name in previous lines
                for j in range(max(0, i-5), i):
                    prev_line = lines[j].strip()
                    if prev_line and len(prev_line) > 10 and not any(prev_line.startswith(x) for x in ['(', '•', '-']):
                        if not any(skip in prev_line for skip in ['Public Works', 'Commission', 'Agenda', 'Item', 'Page', 'To:', 'From:', 'Subject:']):
                            if prev_line not in matched_design_projects:
                                matched_design_projects.append(prev_line)

# Try to match these with funding
final_matches = []
for project_name in matched_design_projects:
    for funded_project, amount in funding_map.items():
        # Simple matching - check if project name is similar to funded project
        if project_name.lower() in funded_project.lower() or funded_project.lower() in project_name.lower():
            if funded_project not in [p['name'] for p in final_matches]:
                final_matches.append({'name': funded_project, 'amount': amount, 'status': 'design'})

# If no matches found with (Design) marker, try a broader search
if not final_matches:
    # Look for capital projects in the text
    capital_projects_mentioned = []
    for doc in mongo_docs:
        text = doc.get('text', '')
        
        # Look for capital improvement projects section
        if 'Capital Improvement' in text or 'capital improvement' in text:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                # Skip empty and header lines
                if line and len(line) > 10 and not line.startswith('(') and not line.endswith(':'):
                    if not any(skip in line for skip in ['Public Works', 'Commission', 'Agenda']):
                        if 'Project' in line or 'Improvement' in line or 'Repair' in line or 'Road' in line:
                            if 'design' in text.lower() or 'Design' in text:
                                capital_projects_mentioned.append(line)
    
    # Remove duplicates and try to match with funding
    unique_projects = list(set(capital_projects_mentioned))[:20]  # Limit to avoid noise
    
    for project_name in unique_projects:
        for funded_project, amount in funding_map.items():
            # Check for substring matches
            proj_clean = project_name.replace('Project', '').replace('Improvement', '').strip()
            if len(proj_clean) > 10:
                if proj_clean.lower() in funded_project.lower() or funded_project.lower() in proj_clean.lower():
                    if funded_project not in [p['name'] for p in final_matches]:
                        final_matches.append({'name': funded_project, 'amount': amount, 'status': 'design'})

# Create final result
result_count = len(final_matches)

result_json = json.dumps({
    'count': result_count,
    'matches': final_matches[:10]  # Return first 10 for preview
})

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
