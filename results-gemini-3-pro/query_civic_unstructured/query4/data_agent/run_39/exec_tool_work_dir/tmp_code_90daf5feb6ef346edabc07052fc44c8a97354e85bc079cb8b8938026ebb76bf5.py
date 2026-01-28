code = """import json
import sqlite3
import pandas as pd
import re

# Load Funding data
funding_path = locals()['var_function-call-5679613479952350120']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
# Create a set of project names for lookup
project_names = set(df_funding['Project_Name'].unique())
project_funding_map = df_funding.set_index('Project_Name')['Amount'].to_dict()

# Load Civic Docs
docs_path = locals()['var_function-call-5679613479952350149']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)

# Define target dates
target_dates = ["Spring 2022", "March 2022", "April 2022", "May 2022", "Mar 2022", "Apr 2022"]
target_year = "2022"
target_season = "Spring"
target_months = ["March", "April", "May"]

found_projects = set()

for doc in docs_data:
    text = doc.get('text', '')
    # Normalize text a bit?
    # Iterate over known project names to find them in text
    for proj in project_names:
        if proj in found_projects:
            continue
            
        # Check if project name is in text
        # Use regex to ensure it's not part of another word, but exact match might be strict due to spaces/newlines
        # Let's try simple string text.find first
        if proj in text:
            # Locate the project section
            # Assume section starts with Project Name and ends at the next Project Name or end of a block
            # This is tricky.
            # Let's verify context.
            # Find all occurrences
            idx = text.find(proj)
            while idx != -1:
                # Look at the context after the project name (e.g., next 500 chars)
                context = text[idx:idx+2000] # 2000 chars should cover the schedule
                
                # Check for "Begin Construction" or "Start"
                # Regex for "Begin Construction: <Date>"
                # Date could be "Spring 2022", "March 2022", etc.
                
                date_pattern = r"(Begin Construction|Construction Start|Start Date|Date)[:\s\-]+([A-Za-z0-9\s,]+)"
                matches = re.findall(date_pattern, context, re.IGNORECASE)
                
                is_target = False
                for label, date_str in matches:
                    # Clean date_str
                    date_str = date_str.strip()
                    # Check if date_str contains target
                    lower_date = date_str.lower()
                    
                    # Stop at newline or valid date end
                    if '\n' in date_str:
                        date_str = date_str.split('\n')[0]
                        lower_date = date_str.lower()
                        
                    if "2022" in lower_date:
                        if "spring" in lower_date:
                            is_target = True
                        elif any(m.lower() in lower_date for m in target_months):
                            is_target = True
                            
                    # Also check strictly "Start: ..." if "Begin Construction" not found?
                    # In sample, "Begin Construction" is used.
                    
                    if is_target:
                        break
                
                if is_target:
                    found_projects.add(proj)
                    break
                
                # Move to next occurrence
                idx = text.find(proj, idx+1)

print(f"Found projects: {list(found_projects)}")

# Calculate total funding
total_funding = 0
count = 0
for proj in found_projects:
    amt = project_funding_map.get(proj, 0)
    # Amount is string in JSON?
    if isinstance(amt, str):
        amt = int(amt)
    total_funding += amt
    count += 1

print("__RESULT__:")
print(json.dumps({"count": count, "total_funding": total_funding, "projects": list(found_projects)}))"""

env_args = {'var_function-call-10787328583776950224': ['civic_docs'], 'var_function-call-10787328583776949317': ['Funding'], 'var_function-call-8503351920656414567': 'file_storage/function-call-8503351920656414567.json', 'var_function-call-5679613479952350149': 'file_storage/function-call-5679613479952350149.json', 'var_function-call-5679613479952350120': 'file_storage/function-call-5679613479952350120.json'}

exec(code, env_args)
