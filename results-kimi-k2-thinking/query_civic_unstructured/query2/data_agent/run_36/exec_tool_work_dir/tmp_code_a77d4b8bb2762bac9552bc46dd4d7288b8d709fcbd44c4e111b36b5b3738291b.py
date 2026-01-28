code = """import json
import pandas as pd
import re

# Load data from the storage variables
# For park projects completed in 2022 (stored in var_functions.query_db:12)
import os

park_docs_file = var_functions.query_db:12
print("Working with park docs file:", park_docs_file)

# Load the park-related documents
if isinstance(park_docs_file, str) and os.path.exists(park_docs_file):
    with open(park_docs_file, 'r') as f:
        park_docs = json.load(f)
else:
    park_docs = []

print(f"Loaded {len(park_docs)} park-related documents")

# Load funding data (stored in var_functions.query_db:13)
funding_file = var_functions.query_db:13
if isinstance(funding_file, str) and os.path.exists(funding_file):
    with open(funding_file, 'r') as f:
        # Read and parse the JSON array
        content = f.read().strip()
        if content.startswith('['):
            funding_data = json.loads(content)
        else:
            funding_data = []
else:
    funding_data = []

print(f"Loaded {len(funding_data)} funding records")

# Create funding dataframe
funding_df = pd.DataFrame(funding_data)
if not funding_df.empty:
    funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')
    print("Funding data columns:", funding_df.columns.tolist())
    print("Sample funding data:")
    print(funding_df.head())
else:
    print("No funding data found")

# Extract park projects completed in 2022 from documents
park_2022_projects = []

for doc in park_docs:
    text = doc.get('text', '').lower()
    
    # Look for mentions of park/playground AND completed AND 2022
    has_park = any(term in text for term in ['park', 'playground'])
    has_completed = 'completed' in text
    has_2022 = '2022' in text
    
    if has_park and has_completed and has_2022:
        # Try to find project names in this document
        # Look for patterns like "Bluffs Park Shade Structure" which has funding
        project_patterns = [
            r'([A-Z][a-zA-Z\s]+Park[A-Za-z\s]*)',
            r'([A-Z][a-zA-Z\s]+Playground[A-Za-z\s]*)',
        ]
        
        doc_text = doc.get('text', '')
        for pattern in project_patterns:
            matches = re.finditer(pattern, doc_text)
            for match in matches:
                project_name = match.group(1).strip()
                if len(project_name) > 10 and len(project_name) < 100:  # Reasonable length
                    # Check if this project was completed in 2022
                    # Look for context around the project name
                    start_pos = max(0, match.start() - 200)
                    end_pos = min(len(doc_text), match.end() + 200)
                    context = doc_text[start_pos:end_pos].lower()
                    
                    if 'completed' in context and '2022' in context:
                        park_2022_projects.append(project_name)

# Remove duplicates
park_2022_projects = list(set(park_2022_projects))

print(f"\nFound {len(park_2022_projects)} park projects completed in 2022:")
for proj in park_2022_projects:
    print(f"  - {proj}")

# Now find funding for these projects
if not funding_df.empty:
    matched_funding = []
    
    for park_proj in park_2022_projects:
        # Find exact or close matches in funding database
        for _, fund_row in funding_df.iterrows():
            fund_proj_name = str(fund_row['Project_Name']).lower()
            park_proj_lower = park_proj.lower()
            
            # Check if funding project name contains our park project name
            if park_proj_lower in fund_proj_name:
                matched_funding.append({
                    'Project_Name': fund_row['Project_Name'],
                    'Amount': fund_row['Amount'],
                    'Funding_Source': fund_row['Funding_Source']
                })
    
    # Also look for projects with "park" and check if they might be 2022 completions
    park_funding = funding_df[funding_df['Project_Name'].str.contains('park|playground', case=False, na=False)]
    
    print(f"\nTotal park-related projects in funding DB: {len(park_funding)}")
    
    # Show relevant matches
    relevant_projects = []
    for _, row in park_funding.iterrows():
        proj_name = row['Project_Name']
        amount = row['Amount']
        
        # Check if it matches our 2022 completed projects or looks like it could be
        if any(park_proj.lower() in proj_name.lower() for park_proj in park_2022_projects):
            relevant_projects.append({
                'Project_Name': proj_name,
                'Amount': amount,
                'Funding_Source': row['Funding_Source']
            })
    
    print(f"\nFound {len(relevant_projects)} relevant funding matches:")
    for proj in relevant_projects:
        print(f"  - {proj['Project_Name']}: ${proj['Amount']:,}")
    
    # Calculate total funding
    if relevant_projects:
        total_funding = sum(proj['Amount'] for proj in relevant_projects)
        print(f"\nTotal funding: ${total_funding:,}")
        
        result = json.dumps({
            'projects': relevant_projects,
            'total_funding': total_funding,
            'count': len(relevant_projects)
        })
    else:
        # Try a different approach - just get all park project funding
        print("\nNo exact matches, trying broader search...")
        park_funding_high_value = park_funding[park_funding['Amount'] > 10000]
        total_funding = park_funding_high_value['Amount'].sum()
        
        result = json.dumps({
            'message': 'Using broader search criteria',
            'total_funding': int(total_funding),
            'projects_considered': len(park_funding_high_value)
        })
else:
    result = json.dumps({'error': 'No funding data available'})

print("__RESULT__:")
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)
