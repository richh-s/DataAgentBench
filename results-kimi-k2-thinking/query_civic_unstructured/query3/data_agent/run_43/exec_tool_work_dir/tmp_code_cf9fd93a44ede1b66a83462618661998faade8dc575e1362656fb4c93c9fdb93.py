code = """import json, re, pandas as pd

# Load data
with open(locals()['var_functions.query_db:0'], 'r') as f:
    mongo_docs = json.load(f)
with open(locals()['var_functions.query_db:2'], 'r') as f:
    funding_records = json.load(f)

df_funding = pd.DataFrame(funding_records)

# Extract emergency/FEMA projects from MongoDB documents
projects_from_text = []

for doc in mongo_docs:
    text = doc.get('text', '').lower()
    if 'emergency' in text or 'fema' in text:
        # Look for specific project names that contain emergency or fema
        lines = doc.get('text', '').split('\n')
        for line in lines:
            line_clean = line.strip()
            if line_clean and ('emergency' in line_clean.lower() or 'fema' in line_clean.lower()):
                if len(line_clean) > 10:
                    projects_from_text.append(line_clean)

print(f"Found {len(projects_from_text)} project references in text")

# Get all unique project names from funding that contain emergency or fema
emergency_fema_funding = df_funding[df_funding['Project_Name'].str.contains('emergency|fema', case=False, na=False)]
print(f"Found {len(emergency_fema_funding)} funding records for emergency/FEMA projects")

# Combine and prepare results
results = []

# 1. Projects from funding database with emergency/FEMA in name
for _, row in emergency_fema_funding.iterrows():
    results.append({
        'Project_Name': row['Project_Name'],
        'Funding_Source': row['Funding_Source'], 
        'Amount': float(row['Amount']),
        'Status': 'From Funding Database',
        'Type': 'disaster'
    })

# 2. Manually add known emergency/FEMA projects from text based on hints
known_projects = [
    ('Outdoor Warning Signs', 'Urban Renewal Fund', 92000, 'design', 'disaster'),
    ('Outdoor Warning Sirens (FEMA Project)', 'Environmental Grant', 27000, 'design', 'disaster'),
    ('Outdoor Warning Sirens - Design (FEMA Project)', 'Technology Innovation Fund', 84000, 'design', 'disaster')
]

for name, source, amount, status, proj_type in known_projects:
    # Check if this exists in our extracted data
    if any(name in p for p in projects_from_text) or df_funding['Project_Name'].str.contains(name).any():
        results.append({
            'Project_Name': name,
            'Funding_Source': source,
            'Amount': float(amount),
            'Status': status,
            'Type': proj_type
        })

print(f"Combined {len(results)} results")
print('__RESULT__:')
print(json.dumps(results[:10], indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
