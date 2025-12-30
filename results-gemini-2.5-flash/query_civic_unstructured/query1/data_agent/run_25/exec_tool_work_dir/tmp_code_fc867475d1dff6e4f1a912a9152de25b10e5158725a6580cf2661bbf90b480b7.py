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
    # Regex to find the "Capital Improvement Projects (Design)" section
    # Correctly escaping parentheses for regex in a raw Python string
    capital_design_pattern = re.compile(r'Capital Improvement Projects \(Design\)\n(.*?)(?=\nCapital Improvement Projects \(|\nDisaster Recovery Projects|\Z)', re.DOTALL)
    
    matches = capital_design_pattern.findall(text)
    for match_text in matches:
        # Extract project names within the "Capital Improvement Projects (Design)" section
        # Project names are usually single lines, followed by '(cid:190) Updates:' or similar.
        # We look for lines that start with a capital letter and are not status/schedule indicators
        # Correctly escaping parentheses for regex in a raw Python string
        project_name_candidates = re.findall(r'\n([A-Z][^\n]+?)(?=\n\s*\(cid:190\)|\n\s*Project Schedule|\n\s*Updates|\n\s*Estimated Schedule|\Z)', match_text)
        for name_candidate in project_name_candidates:
            project_name = name_candidate.strip()
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
