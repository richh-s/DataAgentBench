code = """import json
import pandas as pd
import re

# Load funding data
with open(locals()['var_function-call-10032448971430008742'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
# Convert Amount to int
df_funding['Amount'] = df_funding['Amount'].astype(int)

# Create a set of valid project names for matching
valid_projects = set(df_funding['Project_Name'].unique())

# Load civic docs
with open(locals()['var_function-call-17801199440429665660'], 'r') as f:
    civic_docs = json.load(f)

# Helper to normalize text for matching
def normalize(text):
    return text.strip()

# Keywords for disaster
disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster"]

# Function to parse docs
matching_projects = []
debug_log = []

for doc in civic_docs:
    lines = doc['text'].split('\n')
    current_section = "Unknown"
    current_project = None
    current_project_text = []
    
    # We will process line by line. 
    # If we find a line that matches a project name, we start a new project context.
    # We also look for section headers.
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        # Check for section headers
        if "Capital Improvement Projects" in line_clean:
            current_section = "Capital"
            current_project = None # Reset project context
            continue
        if "Disaster Recovery Projects" in line_clean:
            current_section = "Disaster"
            current_project = None
            continue
            
        # Check if line is a project name
        # We try to match the line against known project names. 
        # Sometimes there might be punctuation or whitespace diffs.
        # But given the hint, exact match might work or simple strip.
        
        # Check exact match
        if line_clean in valid_projects:
            # Save previous project info if any
            if current_project:
                # Process previous project
                pass 
            
            current_project = line_clean
            current_project_text = []
            continue
        
        # If we are inside a project, collect text or look for fields
        if current_project:
            current_project_text.append(line_clean)
            
            # Check for start date in this line
            # Patterns: "Begin Construction: <date>", "Start Date: <date>", "st: <date>"
            # We are looking for "2022" in the value
            
            # Also need to determine if it is a disaster project.
            # 1. Name has keyword
            # 2. Section is Disaster
            
            is_disaster = False
            if any(k in current_project for k in disaster_keywords):
                is_disaster = True
            elif current_section == "Disaster":
                is_disaster = True
            
            if is_disaster:
                # Check for Start Date
                # Look for "Begin Construction" or "Start"
                # And check if "2022" is in that line (after the keyword)
                
                lower_line = line_clean.lower()
                if "begin construction" in lower_line or "start date" in lower_line or "st:" in lower_line:
                    if "2022" in line_clean:
                        # Found a match
                        matching_projects.append({
                            "Project_Name": current_project,
                            "Context_Line": line_clean,
                            "Doc": doc['filename']
                        })
                        # We found the date, we can stop looking for this project to avoid double counting from the same doc?
                        # Maybe not, updates might be repeated. But we should count unique projects.
                        # Set current_project to None to avoid re-matching the same project block? 
                        # No, there might be multiple dates? But usually one start date.
                        current_project = None 

# Remove duplicates (same project might be in multiple docs or mentioned multiple times)
# We want unique project names that meet the criteria.
unique_matches = {}
for m in matching_projects:
    unique_matches[m['Project_Name']] = m

matched_names = list(unique_matches.keys())

# Calculate total funding
total_funding = df_funding[df_funding['Project_Name'].isin(matched_names)]['Amount'].sum()

print("__RESULT__:")
print(json.dumps({
    "matched_projects": matched_names,
    "total_funding": int(total_funding),
    "debug_matches": list(unique_matches.values())
}))"""

env_args = {'var_function-call-10032448971430008742': 'file_storage/function-call-10032448971430008742.json', 'var_function-call-17801199440429665660': 'file_storage/function-call-17801199440429665660.json'}

exec(code, env_args)
