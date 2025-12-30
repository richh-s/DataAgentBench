code = """import json
import pandas as pd
import re

# Load Funding Data
with open(locals()['var_function-call-6790771977792377935'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load Civic Docs
with open(locals()['var_function-call-17703270697767214172'], 'r') as f:
    civic_docs = json.load(f)

found_projects = set()

# Terms to look for
start_terms = ["Begin Construction", "Start Construction", "Construction Start", "Project Start"]
target_dates = ["Spring 2022", "March 2022", "April 2022", "May 2022"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Identify project names and their associated text blocks
    # Logic: A line followed by a line containing "Updates:" or "Project Description:" is a project name.
    
    for i in range(len(lines) - 1):
        line = lines[i].strip()
        next_line = lines[i+1].strip()
        
        # Check if next_line is an update/desc header
        # The marker might be present or not, just check for keywords
        if ("Updates:" in next_line or "Project Description:" in next_line) and line:
            project_name = line
            
            # Now scan the following lines for this project until the next project starts
            # The next project starts when we see another line followed by Updates/Desc
            # or end of file.
            
            # Simple heuristic: scan next 50 lines or until another "Updates:" block is found
            # But better: define the block.
            
            block_content = ""
            for j in range(i+1, min(len(lines), i+100)): # Look ahead up to 100 lines
                sub_line = lines[j]
                # If we encounter a new project header, stop.
                # A new project header is a line followed by "Updates:"
                if j < len(lines)-1:
                    if ("Updates:" in lines[j+1] or "Project Description:" in lines[j+1]) and lines[j].strip():
                        break
                block_content += sub_line + " "
            
            # Check for start date in block_content
            # We look for "Begin Construction: Spring 2022" etc.
            
            found = False
            for term in start_terms:
                for date in target_dates:
                    # Construct regex pattern loosely: term ... date
                    # e.g. "Begin Construction ... Spring 2022"
                    # Allow some characters in between (like ": " or " - ")
                    pattern = re.escape(term) + r".{0,50}" + re.escape(date)
                    if re.search(pattern, block_content, re.IGNORECASE):
                        found_projects.add(project_name)
                        found = True
                        break
                if found: break

# Filter Funding
# Clean project names (remove potential leading bullets or weird chars if any)
# The preview showed clean names like "2022 Morning View..."
# But let's strip just in case.

clean_found = {p.strip() for p in found_projects}

# Match
matched = funding_df[funding_df['Project_Name'].isin(clean_found)]

print("__RESULT__:")
print(json.dumps({
    "found_projects": list(clean_found),
    "matched_projects": matched['Project_Name'].tolist(),
    "matched_count": len(matched),
    "total_funding": int(matched['Amount'].astype(int).sum())
}))"""

env_args = {'var_function-call-6629743294879476725': ['civic_docs'], 'var_function-call-6629743294879475928': ['Funding'], 'var_function-call-6790771977792377935': 'file_storage/function-call-6790771977792377935.json', 'var_function-call-6790771977792376994': 'file_storage/function-call-6790771977792376994.json', 'var_function-call-17703270697767214172': 'file_storage/function-call-17703270697767214172.json'}

exec(code, env_args)
