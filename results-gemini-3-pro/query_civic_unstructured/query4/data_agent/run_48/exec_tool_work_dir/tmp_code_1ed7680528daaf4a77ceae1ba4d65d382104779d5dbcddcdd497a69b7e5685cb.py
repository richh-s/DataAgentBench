code = """import json
import re
import pandas as pd

# Load civic docs
with open('var_function-call-16068548023573727845.json', 'r') as f:
    civic_docs = json.load(f)

# Load funding
with open('var_function-call-9691267540857789545.json', 'r') as f:
    funding = json.load(f)

funding_df = pd.DataFrame(funding)

# Helper to check for Spring 2022
def is_spring_2022(text):
    text = text.lower()
    # Patterns for Spring 2022
    patterns = [
        r'spring\s*2022',
        r'2022\s*-\s*spring',
        r'(?:march|april|may)\s*,?\s*2022',
        r'2022\s*-\s*0?[345]',
        r'0?[345]/2022'
    ]
    for p in patterns:
        if re.search(p, text):
            return True
    return False

# Extract projects and their schedules
projects = []
for doc in civic_docs:
    text = doc['text']
    # The text seems to separate projects.
    # Looking at the example: "Project Name\n\n(cid:190) Updates:"
    # We can split by "(cid:190) Updates:"
    # But first, let's normalize the cid marker if needed. 
    # The preview showed "(cid:190)".
    
    # Split text into segments based on the Updates marker
    # The marker seems to be part of a block.
    # A project block starts with the Name and contains Updates and Schedule.
    # We can use regex to find the structure.
    
    # Strategy: Find all indices of "(cid:190) Updates:". 
    # The text before this (up to the previous end or newline) is the project name.
    # The text after this (up to the next project name) is the content.
    
    # Actually, let's look at the structure more simply.
    # We can iterate line by line? No, blocks are better.
    
    parts = re.split(r'\(cid:190\)\s*Updates:', text)
    
    # parts[0] is header junk or the first project name?
    # parts[1] starts with the updates for the first project, then eventually contains the next project name at the end.
    
    # This split is tricky because the project name is at the end of the *previous* part.
    
    for i in range(1, len(parts)):
        # content of the current project (updates + schedule)
        # It goes until the next project name.
        # But split removed the marker.
        # So parts[i] starts with the updates content.
        # And ends with the *next* project name.
        
        current_part = parts[i]
        
        # The project name for this part is at the end of parts[i-1].
        # Let's extract it.
        prev_part = parts[i-1]
        lines_prev = prev_part.strip().split('\n')
        
        # Project name should be the last non-empty line(s) of prev_part.
        # But be careful about page headers etc.
        # In the example: 
        # "Capital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements"
        # So it might be the last line.
        
        # Let's take the last non-empty line of prev_part as the candidate name.
        candidate_name = ""
        if lines_prev:
            candidate_name = lines_prev[-1].strip()
            # If the line is short or looks like a category (e.g. "Capital Improvement Projects (Design)"), 
            # maybe look further back? 
            # But the example shows the category then the project name.
        
        # Now search for Spring 2022 in current_part
        # We want to identify if this project started in Spring 2022.
        # Extract lines mentioning Spring 2022.
        
        lines_curr = current_part.split('\n')
        relevant_lines = []
        for line in lines_curr:
            if is_spring_2022(line):
                relevant_lines.append(line.strip())
        
        if relevant_lines:
            projects.append({
                "name": candidate_name,
                "lines": relevant_lines,
                "full_text": current_part[:200] # preview
            })

print("__RESULT__:")
print(json.dumps(projects, indent=2))"""

env_args = {'var_function-call-16068548023573727845': 'file_storage/function-call-16068548023573727845.json', 'var_function-call-9691267540857789545': 'file_storage/function-call-9691267540857789545.json'}

exec(code, env_args)
