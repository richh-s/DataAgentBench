code = """import pandas as pd
import json
import re

# Load the funding data
with open(locals()['var_function-call-6757835819640547433'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load the civic documents
with open(locals()['var_function-call-17491477774021413501'], 'r') as f:
    civic_docs_data = json.load(f)

projects_list = []

for doc in civic_docs_data:
    text = doc['text']

    # Regex to find Capital Improvement Projects (Design)
    capital_design_projects = re.findall(r'Capital Improvement Projects \(Design\)\n\n(.*?)(?:\n\nCapital Improvement Projects \(Construction\)|\n\nCapital Improvement Projects \(Not Started\)|\n\nDisaster Recovery Projects|\Z)', text, re.DOTALL)
    if capital_design_projects:
        for block in capital_design_projects:
            project_names = re.findall(r'^([A-Za-z0-9&,\s-]+\s*(?:\(FEMA Project\)|\(CalOES Project\)|\(CalJPIA Project\))?)(?:\n\n|\n\(cid:190\))' , block, re.MULTILINE)
            for name in project_names:
                # Clean up extracted project name, remove leading/trailing whitespace and bullet points/special characters
                cleaned_name = name.strip()
                if cleaned_name:
                    projects_list.append({'Project_Name': cleaned_name, 'type': 'capital', 'status': 'design'})

civic_projects_df = pd.DataFrame(projects_list)

# Merge dataframes
merged_df = pd.merge(funding_df, civic_projects_df, on='Project_Name', how='inner')

# Filter for capital projects with 'design' status and funding > $50,000 (already filtered in SQL query)
# Count the number of unique projects
count = len(merged_df['Project_Name'].unique())

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_function-call-6757835819640547433': 'file_storage/function-call-6757835819640547433.json', 'var_function-call-17491477774021413501': 'file_storage/function-call-17491477774021413501.json'}

exec(code, env_args)
