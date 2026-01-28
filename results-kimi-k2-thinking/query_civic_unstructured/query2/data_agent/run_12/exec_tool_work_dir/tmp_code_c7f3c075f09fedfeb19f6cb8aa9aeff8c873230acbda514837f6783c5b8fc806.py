code = """import json
import pandas as pd
import re

# Load data from files
print("Loading data...")
with open('/home/user/funding_data.json', 'r') as f:
    funding_data = json.load(f)

with open('/home/user/civic_docs_data.json', 'r') as f:
    civic_docs_data = json.load(f)

# Create dataframe for funding
df_funding = pd.DataFrame(funding_data)
print(f"Funding records: {len(df_funding)}")

# Function to extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs_data:
    text = doc['text'].lower()
    # Check if this document mentions park projects completed in 2022
    if 'park' in text and 'completed' in text and '2022' in text:
        lines = doc['text'].split('\n')
        for i, line in enumerate(lines):
            line_clean = line.strip()
            if not line_clean:
                continue
            # Look for lines that might be project names containing park
            if 'park' in line_clean.lower() and len(line_clean) < 100:
                # Check following lines for completion status
                context = ' '.join(lines[i:i+6]).lower()
                if 'completed' in context and '2022' in context:
                    park_projects_2022.append(line_clean)
                    print(f"Found: {line_clean}")

print(f"Park projects completed in 2022: {len(park_projects_2022)}")

# Clean project names
def clean_project_name(name):
    name = re.sub(r'\s+Project\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Design\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Construction\s*$', '', name, flags=re.IGNORECASE)
    return name.strip()

# Clean names in funding data
df_funding['clean_name'] = df_funding['Project_Name'].apply(clean_project_name)

# Find matching projects and sum funding
total_funding = 0
matched_projects = []
cleaned_park_projects = [clean_project_name(p) for p in park_projects_2022]

for _, fund_row in df_funding.iterrows():
    fund_clean = fund_row['clean_name']
    # Check if this funding matches any park project
    for i, park_clean in enumerate(cleaned_park_projects):
        if park_clean.lower() in fund_clean.lower() or fund_clean.lower() in park_clean.lower():
            amount = int(fund_row['Amount'])
            total_funding += amount
            matched_projects.append({
                'park_project': park_projects_2022[i],
                'funding_record': fund_row['Project_Name'],
                'amount': amount
            })
            print(f"Match: {park_projects_2022[i]} -> {fund_row['Project_Name']} (${amount})")

print(f"\nTotal matched: {len(matched_projects)}")
print(f"Total funding: ${total_funding:,}")

# Create result
result = {
    'total_funding': total_funding,
    'matched_projects': matched_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
