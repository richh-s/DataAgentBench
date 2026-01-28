code = """import pandas as pd
import re
import json

funding_data = json.loads(locals()['var_function-call-13812960451374386902'])
civic_docs_file = locals()['var_function-call-8903793629185941567']

with open(civic_docs_file, 'r') as f:
    civic_docs_data = json.load(f)

extracted_projects = []

for doc in civic_docs_data:
    text = doc['text']
    lines = text.split('\\n')

    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Check for completion in 2022
        if 'construction was completed' in stripped_line.lower() and '2022' in stripped_line:
            # Now, look backwards for the project name.
            # Project name is usually a non-bulleted line preceding the update.
            project_name_found = False
            for j in range(i - 1, max(-1, i - 5), -1): # Look back up to 5 lines
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith(('to:', 'prepared by:', 'approved by:', 'date prepared:', 'meeting date:', 'subject:', 'recommended action:', 'discussion:', 'updates:', 'project schedule:', 'estimated schedule:', 'project description:', 'capital improvement projects', 'disaster recovery projects')):\
                    # Found a potential project name. Check if it\'s park-related.
                    if 'park' in prev_line.lower():
                        extracted_projects.append({
                            'Project_Name': prev_line,
                            'status': 'completed',
                            'et_year': '2022',
                            'topic': 'park'
                        })
                        project_name_found = True
                        break # Found the project name, stop looking further back
            if project_name_found:
                pass


# Convert extracted projects to DataFrame and remove duplicates
projects_df = pd.DataFrame(extracted_projects).drop_duplicates(subset=['Project_Name'])

# Convert funding data to DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Merge dataframes
merged_df = pd.merge(projects_df, funding_df, on='Project_Name', how='inner')

# Calculate total funding
total_funding = merged_df['Amount'].sum()

# If no projects are found, sum will be NaN, return 0.
if pd.isna(total_funding):
    total_funding = 0

print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_function-call-13812960451374386902': 'file_storage/function-call-13812960451374386902.json', 'var_function-call-8903793629185941567': 'file_storage/function-call-8903793629185941567.json'}

exec(code, env_args)
