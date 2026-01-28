code = """import json
import sqlite3
import pandas as pd

# Load previous tool results
# civic docs
with open(locals()['var_function-call-11358458194836773499'], 'r') as f:
    civic_docs = json.load(f)

# funding data
with open(locals()['var_function-call-2972859759702192456'], 'r') as f:
    funding_data = json.load(f)

# Create a set of known project names for extraction
funding_df = pd.DataFrame(funding_data)
project_names = funding_df['Project_Name'].unique().tolist()

# Helper to normalize text
def normalize(text):
    return text.lower()

# Process documents
matched_projects = []

for doc in civic_docs:
    text = doc['text']
    # Find start positions of all projects in this text
    # We look for project names from our funding list that appear in the text
    found_projects = []
    for pname in project_names:
        # Simple string search. Ensure it's not a substring of another word if possible, 
        # but exact match of full project name is a good start.
        # Check if pname exists in text.
        idx = text.find(pname)
        if idx != -1:
            found_projects.append({'name': pname, 'start': idx})
    
    # Sort by position
    found_projects.sort(key=lambda x: x['start'])
    
    # Determine text segments for each project
    for i in range(len(found_projects)):
        p = found_projects[i]
        start = p['start']
        # End is the start of the next project, or end of text
        if i < len(found_projects) - 1:
            end = found_projects[i+1]['start']
        else:
            end = len(text)
        
        segment = text[start:end]
        
        # Analyze segment for "Completed in 2022"
        # Logic: Look for "completed" or "Complete Construction" near "2022"
        # We need to be careful not to match "Begin Construction: Fall 2022"
        # A simple heuristic: check for lines containing "complete" and "2022"
        
        segment_lower = segment.lower()
        
        is_completed_2022 = False
        
        # Split into lines to be safer with context
        lines = segment.split('\n')
        for line in lines:
            line_lower = line.lower()
            if '2022' in line_lower:
                if 'complete' in line_lower and 'construction' in line_lower:
                     # e.g. "Complete Construction: Summer 2022", "Construction was completed November 2022"
                     is_completed_2022 = True
                elif 'completed' in line_lower:
                     # e.g. "Construction was completed, November 2022"
                     is_completed_2022 = True
                elif 'notice of completion' in line_lower:
                     # "Notice of completion filed ... 2022" - this implies completion.
                     # But usually notice is after completion.
                     pass
        
        # Check for "park" topic
        # 1. In Project Name
        # 2. In text segment
        is_park = False
        if 'park' in p['name'].lower():
            is_park = True
        elif 'park' in segment_lower:
            is_park = True
            
        if is_park and is_completed_2022:
            matched_projects.append(p['name'])

# Remove duplicates (same project might be in multiple agenda docs, or mentioned multiple times)
# We need to decide if we sum multiple times or just once. 
# Usually, funding is per project. We should sum unique projects.
unique_projects = list(set(matched_projects))

# Filter funding DF
total_funding = funding_df[funding_df['Project_Name'].isin(unique_projects)]['Amount'].astype(float).sum()

print("__RESULT__:")
print(json.dumps({
    "matched_projects": unique_projects,
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-11358458194836773499': 'file_storage/function-call-11358458194836773499.json', 'var_function-call-2972859759702192456': 'file_storage/function-call-2972859759702192456.json'}

exec(code, env_args)
