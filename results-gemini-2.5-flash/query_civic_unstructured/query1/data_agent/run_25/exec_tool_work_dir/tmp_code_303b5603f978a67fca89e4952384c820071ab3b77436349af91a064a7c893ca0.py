code = """import pandas as pd
import json
import re

# Load the funding data
with open(locals()['var_function-call-1550151759561691630'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load the civic documents
with open(locals()['var_function-call-18198628068361189622'], 'r') as f:
    civic_docs = json.load(f)

# Function to extract project details from text
def extract_project_details(text):
    projects = []
    # Regex to find project names and their status/type based on the section headers
    # Looking for "Capital Improvement Projects (Design)" and similar patterns
    capital_design_pattern = re.compile(r"Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(|Disaster Recovery Projects|\Z)", re.DOTALL)
    
    matches = capital_design_pattern.findall(text)
    for match in matches:
        # Extract project names within the "Capital Improvement Projects (Design)" section
        # Project names are usually followed by updates or schedules, and start with a capital letter
        project_names = re.findall(r"\n([A-Z][^\n(]+?)(?:\n\(cid:190\)|\nProject Schedule|\nUpdates|\Z)", match)
        for name in project_names:
            project_name = name.strip()
            if project_name:
                projects.append({'Project_Name': project_name, 'type': 'capital', 'status': 'design'})
                
    return projects

all_projects_data = []
for doc in civic_docs:
    all_projects_data.extend(extract_project_details(doc['text']))

civic_projects_df = pd.DataFrame(all_projects_data)

# Ensure Project_Name in funding_df is string for consistent merge
funding_df['Project_Name'] = funding_df['Project_Name'].astype(str)
civic_projects_df['Project_Name'] = civic_projects_df['Project_Name'].astype(str)

# Merge dataframes
merged_df = pd.merge(
    funding_df,
    civic_projects_df,
    on='Project_Name',
    how='inner'
)

# Filter for capital projects with 'design' status (already done by extraction and merge logic but good to re-verify)
final_projects = merged_df[(merged_df['type'] == 'capital') & (merged_df['status'] == 'design')]

# Count unique project names
result_count = final_projects['Project_Name'].nunique()

print("__RESULT__:")
print(json.dumps(result_count))"""

env_args = {'var_function-call-1550151759561691630': 'file_storage/function-call-1550151759561691630.json', 'var_function-call-18198628068361189622': 'file_storage/function-call-18198628068361189622.json'}

exec(code, env_args)
