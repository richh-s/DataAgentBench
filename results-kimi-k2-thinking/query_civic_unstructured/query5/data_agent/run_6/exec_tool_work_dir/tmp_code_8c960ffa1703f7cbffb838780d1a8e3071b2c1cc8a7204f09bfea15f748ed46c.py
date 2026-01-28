code = """import json
import pandas as pd
import re

# Load the civic documents data
with open('/tmp/tmp2v7m_6l3.json', 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
with open('/tmp/tmpf4d6q2f3.json', 'r') as f:
    funding_data = json.load(f)

# Convert funding data to DataFrame
funding_df = pd.DataFrame(funding_data)

print(f"Loaded {len(funding_df)} funding records")
print(f"Loaded {len(civic_docs)} civic documents")

# Find disaster-related funding directly from funding data
# Disaster projects often have suffixes like (FEMA Project), (CalJPIA Project), (CalOES Project)
is_disaster = funding_df['Project_Name'].str.contains(
    r'\(FEMA|FEMA\b|\(CalOES|\(CalJPIA|Disaster|Fire|Emergency', 
    case=False, 
    na=False
)

disaster_funding_df = funding_df[is_disaster].copy()
disaster_funding_df['Amount'] = disaster_funding_df['Amount'].astype(int)

print(f"Found {len(disaster_funding_df)} disaster-related funding records")
print("Sample disaster projects:")
print(disaster_funding_df[['Project_Name', 'Amount']].head(10).to_string())

# Try to extract start years from project names and descriptions
# Projects like "2022..." or "2021..." in their names indicate the year
year_from_name = disaster_funding_df['Project_Name'].str.extract(r'(202\d)')
disaster_funding_df['year_from_name'] = year_from_name[0]

# Also extract year from civic documents for projects that started in 202nprojects_2022_from_docs = []

for doc in civic_docs:
    text = doc['text']
    
    # Look for project names and start dates
    # Simplified approach - look for patterns that indicate disaster projects starting in 2022
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        # Check if line contains both a year and disaster indicators
        if ('2022' in line and 
            any(indicator in line.lower() for indicator in ['fema', 'caloes', 'disaster', 'fire'])):
            # This might be a disaster project starting in 2022
            # Look for project name (previous line or this line)
            proj_name = line
            # Extract project name if it exists
            for proj in disaster_funding_df['Project_Name']:
                if proj.lower() in line.lower() or any(part.lower() in line.lower() for part in proj.split() if len(part) > 3):
                    projects_2022_from_docs.append(proj)

# Find exact matches between disaster_funding_df and 2022 projects
projects_2022_set = set(projects_2022_from_docs)
print(f"Found {len(projects_2022_set)} potential 2022 projects from documents")

# Also include projects that explicitly mention 2022 in their name
explicit_2022 = disaster_funding_df[disaster_funding_df['Project_Name'].str.contains('2022', case=False, na=False)]

# Combine explicit 2022 projects with projects found through document analysis
projects_2022_by_name = disaster_funding_df[disaster_funding_df['year_from_name'] == '2022']

# Union of all 2022 disaster projects
all_2022_disaster = pd.concat([
    explicit_2022,
    projects_2022_by_name,
    # Add any projects we found from document matching
    disaster_funding_df[disaster_funding_df['Project_Name'].isin(projects_2022_set)]
]).drop_duplicates()

print(f"\nTotal 2022 disaster projects identified: {len(all_2022_disaster)}")

if len(all_2022_disaster) > 0:
    total_funding = all_2022_disaster['Amount'].sum()
    print(f"Total funding: ${total_funding:,}")
    print("\n2022 Disaster Projects:")
    for _, proj in all_2022_disaster.iterrows():
        print(f"  - {proj['Project_Name']}: ${proj['Amount']:,}")
else:
    # If we couldn't find specific 2022 projects, provide an estimate or show all disaster projects
    total_funding = disaster_funding_df['Amount'].sum()
    print(f"Could not identify specific 2022 projects. Total disaster funding overall: ${total_funding:,}")

# Prepare result
if len(all_2022_disaster) > 0:
    result = {
        'total_funding': int(total_funding),
        'num_projects': len(all_2022_disaster),
        'projects': all_2022_disaster[['Project_Name', 'Amount']].to_dict('records')
    }
else:
    # Fallback - count all disaster projects (the data might not have clear 2022 indicators)
    result = {
        'total_funding': int(disaster_funding_df['Amount'].sum()),
        'num_projects': len(disaster_funding_df),
        'note': 'Using all disaster projects - specific 2022 start dates not clearly marked',
        'projects': disaster_funding_df[['Project_Name', 'Amount']].head(10).to_dict('records')
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
