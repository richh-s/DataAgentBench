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

    start_marker = 'Capital Improvement Projects (Design)\n\n'
    end_markers = ['\n\nCapital Improvement Projects (Construction)',
                   '\n\nCapital Improvement Projects (Not Started)',
                   '\n\nDisaster Recovery Projects']

    # Find the start of the relevant block
    start_index = text.find(start_marker)
    if start_index == -1:
        continue

    block_start_content_index = start_index + len(start_marker)
    
    # Find the earliest end marker after the start
    end_index = -1
    for marker in end_markers:
        current_end_index = text.find(marker, block_start_content_index)
        if current_end_index != -1:
            if end_index == -1 or current_end_index < end_index:
                end_index = current_end_index

    capital_design_block = ""
    if end_index != -1:
        capital_design_block = text[block_start_content_index:end_index]
    else: # If no explicit end marker, go to the end of the document
        capital_design_block = text[block_start_content_index:]
    
    # Process the block line by line to extract project names
    lines = capital_design_block.split('\n')
    for line in lines:
        stripped_line = line.strip()

        # Filter out empty lines, bullet points, update/schedule lines, page numbers, and agenda items
        # Using multiple 'startswith' and 'in' checks to avoid complex regex that might cause parsing issues
        is_project_line = True
        if not stripped_line:
            is_project_line = False
        elif stripped_line.startswith('(cid:190)'):
            is_project_line = False
        elif stripped_line.lower().startswith('updates:'):
            is_project_line = False
        elif stripped_line.lower().startswith('project schedule:'):
            is_project_line = False
        elif stripped_line.lower().startswith('estimated schedule:'):
            is_project_line = False
        elif stripped_line.lower().startswith('discussion:'):
            is_project_line = False
        elif stripped_line.lower().startswith('page '):
            is_project_line = False
        elif stripped_line.lower().startswith('agenda item #'):
            is_project_line = False
        elif stripped_line.lower().startswith('item '):
            is_project_line = False
        elif len(stripped_line.split()) < 3: # Heuristic: project names are usually more than two words
            is_project_line = False
        elif not re.match(r'^[A-Z0-9]', stripped_line): # Ensure it starts with a capital letter or digit
            is_project_line = False
            
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
