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

    # Regex to find Capital Improvement Projects (Design) block
    # The regex for the block extraction needs to be a single string. Backslashes are already escaped by Python string literal rules
    capital_design_block_match = re.search(r'Capital Improvement Projects \(Design\)\n\n(.*?)(?:\n\nCapital Improvement Projects \(Construction\)|\n\nCapital Improvement Projects \(Not Started\)|\n\nDisaster Recovery Projects|\Z)', text, re.DOTALL)
    
    if capital_design_block_match:
        capital_design_block = capital_design_block_match.group(1)
        # Process the block line by line to extract project names
        lines = capital_design_block.split('\n')
        for line in lines:
            stripped_line = line.strip()

            # Filter out empty lines, bullet points, update/schedule lines, page numbers, and agenda items
            is_project_line = True
            if not stripped_line: is_project_line = False
            if stripped_line.startswith('(cid:190)'): is_project_line = False
            if stripped_line.lower().startswith('updates:'): is_project_line = False
            if stripped_line.lower().startswith('project schedule:'): is_project_line = False
            if stripped_line.lower().startswith('estimated schedule:'): is_project_line = False
            if stripped_line.lower().startswith('discussion:'): is_project_line = False
            if stripped_line.lower().startswith('page '): is_project_line = False
            if stripped_line.lower().startswith('agenda item #'): is_project_line = False
            if stripped_line.lower().startswith('item '): is_project_line = False
            if len(stripped_line.split()) < 3: is_project_line = False # Heuristic: project names are usually more than two words
            if not stripped_line and not stripped_line[0].isalnum(): is_project_line = False # Ensure it starts with an alphanumeric character, only if not empty
            
            if is_project_line:
                projects_list.append({'Project_Name': stripped_line, 'type': 'capital', 'status': 'design'})

civic_projects_df = pd.DataFrame(projects_list)

# Merge dataframes
merged_df = pd.merge(funding_df, civic_projects_df, on='Project_Name', how='inner')

# Count the number of unique projects
count = len(merged_df['Project_Name'].unique())

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_function-call-6757835819640547433': 'file_storage/function-call-6757835819640547433.json', 'var_function-call-17491477774021413501': 'file_storage/function-call-17491477774021413501.json'}

exec(code, env_args)
