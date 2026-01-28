code = """import pandas as pd
import json
import re

# Load the funding data
with open(locals()['var_function-call-17014294750015647345'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Load the civic docs data
with open(locals()['var_function-call-7117339431964219411'], 'r') as f:
    civic_docs_data = json.load(f)

projects = []
for doc in civic_docs_data:
    text = doc['text']
    
    lines = text.split('\n')
    
    in_design_section = False
    
    # Minimal exclude_keywords
    exclude_keywords = ['Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Project Description:', '(cid:190)', 'Page ', 'Agenda Item #']
    
    # Keywords that signal the end of the current section
    section_end_triggers = [
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)',
        'Disaster Recovery Projects',
        'RECOMMENDED ACTION:'
    ]

    for line in lines:
        cleaned_line = line.strip()
        
        if 'Capital Improvement Projects (Design)' in cleaned_line:
            in_design_section = True
            continue
        
        if in_design_section:
            # Check if this line marks the start of a new section, ending the design section parsing
            if any(keyword in cleaned_line for keyword in section_end_triggers):
                in_design_section = False
                continue
            
            # Heuristic for project names: starts with upper/digit, not in exclude list, and has more than one word
            if cleaned_line and (cleaned_line[0].isupper() or cleaned_line[0].isdigit()) and \
               len(cleaned_line.split()) > 1 and not any(keyword in cleaned_line for keyword in exclude_keywords):
                projects.append({'Project_Name': cleaned_line, 'type': 'capital', 'status': 'design'})

# Create a DataFrame for projects from civic documents
civic_projects_df = pd.DataFrame(projects)

# Merge the two dataframes
merged_df = pd.merge(funding_df, civic_projects_df, on='Project_Name', how='inner')

# Count unique projects
count = merged_df['Project_Name'].nunique()

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_function-call-17014294750015647345': 'file_storage/function-call-17014294750015647345.json', 'var_function-call-7117339431964219411': 'file_storage/function-call-7117339431964219411.json'}

exec(code, env_args)
