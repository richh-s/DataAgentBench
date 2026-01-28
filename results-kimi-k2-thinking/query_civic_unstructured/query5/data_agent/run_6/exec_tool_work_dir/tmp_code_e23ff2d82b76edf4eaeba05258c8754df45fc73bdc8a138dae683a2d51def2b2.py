code = """import json
import pandas as pd

# Load the full funding data
with open('data/query_result_funding.json', 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

# Convert Amount to numeric
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Identify disaster projects (contain FEMA, CalOES, or CalJPIA)
disaster_mask = funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, na=False)
disaster_projects = funding_df[disaster_mask]

print(f"Total disaster projects found: {len(disaster_projects)}")
print(f"Sample disaster projects: {disaster_projects[['Project_Name', 'Amount']].head(10).to_string()}")

# Filter for projects that started in 2022
# Look for 2022 in the project name
projects_2022 = disaster_projects[disaster_projects['Project_Name'].str.contains('2022', case=False, na=False)]

# Also check the civic documents for 2022 disaster projects
with open('data/query_result_694eef5c4ec675b6b5f5a285.json', 'r') as f:
    civic_docs = json.load(f)

# Extract project mentions from documents that include 2022 and disaster indicators
doc_2022_projects = []
for doc in civic_docs:
    text = doc['text']
    if '2022' in text:
        lines = text.split('\n')
        for line in lines:
            line_lower = line.lower()
            if '2022' in line and ('fema' in line_lower or 'caloes' in line_lower or 'caljpia' in line_lower):
                # Look for project name in the same line or nearby lines
                words = line.strip().split()
                if len(words) > 2:  # Potential project name
                    potential_name = ' '.join(words[:8])  # Take first few words as potential project name
                    doc_2022_projects.append(potential_name)

# Match document projects with funding data
additional_projects = []
for proj_name in doc_2022_projects:
    # Find matching funding records
    matches = disaster_projects[disaster_projects['Project_Name'].str.lower().str.contains(proj_name.lower()[:15])]
    if not matches.empty:
        additional_projects.append(matches)

# Combine explicit 2022 projects with document-discovered ones
if additional_projects:
    additional_df = pd.concat(additional_projects).drop_duplicates()
    all_2022_projects = pd.concat([projects_2022, additional_df]).drop_duplicates()
else:
    all_2022_projects = projects_2022

# Calculate totals
total_funding = all_2022_projects['Amount'].sum()
num_projects = len(all_2022_projects)

print(f"\n2022 Disaster Projects found: {num_projects}")
print(f"Total funding: ${total_funding:,}")

# Show detailed breakdown
print("\nProject breakdown:")
for _, proj in all_2022_projects.iterrows():
    print(f"  - {proj['Project_Name']}: ${proj['Amount']:,}")

result = {
    'total_funding': int(total_funding),
    'num_projects': int(num_projects),
    'projects': all_2022_projects[['Project_Name', 'Amount']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['civic_docs']}

exec(code, env_args)
