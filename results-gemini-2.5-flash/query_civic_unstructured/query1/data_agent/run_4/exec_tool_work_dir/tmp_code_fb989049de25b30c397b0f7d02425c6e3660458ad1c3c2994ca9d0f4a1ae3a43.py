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
    capital_design_block_match = re.search(r'Capital Improvement Projects \(Design\)\n\n(.*?)(?:\n\nCapital Improvement Projects \(Construction\)|\n\nCapital Improvement Projects \(Not Started\)|\n\nDisaster Recovery Projects|\Z)', text, re.DOTALL)
    
    if capital_design_block_match:
        capital_design_block = capital_design_block_match.group(1)
        # Process the block line by line to extract project names
        # Project names are usually on a single line and do not start with bullet points or schedule/update indicators.
        lines = capital_design_block.split('\n')
        for line in lines:
            stripped_line = line.strip()
            # Filter out empty lines, bullet points, update/schedule lines, page numbers, and agenda items
            if stripped_line and \
               not stripped_line.startswith('(cid:190)') and \
               not stripped_line.lower().startswith('updates:') and \
               not stripped_line.lower().startswith('project schedule:') and \
               not stripped_line.lower().startswith('estimated schedule:') and \
               not stripped_line.lower().startswith('discussion:') and \
               not stripped_line.lower().startswith('page ') and \
               not stripped_line.lower().startswith('agenda item #') and \
               not stripped_line.lower().startswith('item'):
                
                # Further refinement: sometimes there are sub-headings, ensure we get main project names
                # A simple check for length and presence of certain keywords might help
                if len(stripped_line.split()) > 2: # Project names are usually more than two words
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
