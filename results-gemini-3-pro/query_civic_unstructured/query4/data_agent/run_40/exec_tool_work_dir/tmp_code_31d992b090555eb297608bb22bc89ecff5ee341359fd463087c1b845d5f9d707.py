code = """import json
import re
import pandas as pd

# Load MongoDB results
with open(locals()['var_function-call-956811650377216769'], 'r') as f:
    civic_docs = json.load(f)

# Load Funding results
with open(locals()['var_function-call-956811650377216698'], 'r') as f:
    funding_data = json.load(f)
    
df_funding = pd.DataFrame(funding_data)

# Regex patterns
# Pattern to find project block start: looks for the bullet point followed by Updates or Project Description
# The project name should be on the preceding lines.
block_trigger = re.compile(r'\(cid:190\)\s*(Updates|Project Description|Project Updates)', re.IGNORECASE)

# Pattern to find Start Date in Spring 2022
# We look for "Begin Construction" or similar keywords, and then the date.
# Date formats: Spring 2022, 2022-Spring, March 2022, April 2022, May 2022, 03/2022, 04/2022, 05/2022, 2022-03, ...
# Hint says: Spring = March-May
date_pattern_str = r'(Spring[\s,]*2022|2022[\s-]*Spring|March[\s,]*2022|April[\s,]*2022|May[\s,]*2022|2022[\s-]*0?3|2022[\s-]*0?4|2022[\s-]*0?5|0?3/\d{0,2}/?2022|0?4/\d{0,2}/?2022|0?5/\d{0,2}/?2022)'
start_key_pattern = re.compile(r'(Begin Construction|Start Construction|Construction Start|Start Date)', re.IGNORECASE)
date_pattern = re.compile(date_pattern_str, re.IGNORECASE)

matching_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Iterate lines to find projects
    for i, line in enumerate(lines):
        # Clean line
        line_clean = line.strip()
        
        if block_trigger.search(line_clean):
            # Found a trigger. The project name is likely in the previous non-empty line.
            # We look backwards from i-1
            project_name = None
            for j in range(i-1, -1, -1):
                prev_line = lines[j].strip()
                if not prev_line:
                    continue
                # If the previous line is a header (e.g. "Capital Improvement Projects..."), then maybe we missed the name or it's not a project block in standard format.
                # However, typically the name is just above.
                # Also avoid page numbers or headers "Agenda Item..."
                if "Agenda Item" in prev_line or "Page" in prev_line or "Capital Improvement" in prev_line:
                    break
                
                project_name = prev_line
                break
            
            if project_name:
                # Now scan forward from i to find the schedule
                # We stop at the next trigger or end of text? 
                # Actually, we just look for the schedule lines within reasonable distance or until next project.
                # Simplification: Scan until next line that looks like a project name (hard to detect) or next trigger.
                # Better: Scan until next `(cid:190)` that is followed by Updates/Description (which indicates next project)
                # OR until we see "Page" or "Agenda".
                
                # Let's collect lines for this project
                project_lines = []
                for k in range(i, len(lines)):
                    curr_line = lines[k].strip()
                    # Check if this is a start of a NEW project (another trigger)
                    # We need to look ahead to see if lines[k] is a trigger line?
                    # No, lines[k] is the current line. If lines[k] matches block_trigger, and k > i, it's a new project.
                    if k > i and block_trigger.search(curr_line):
                        break
                    project_lines.append(curr_line)
                
                # Analyze project_lines for Start Date
                started_spring_2022 = False
                for pline in project_lines:
                    if start_key_pattern.search(pline):
                        # Found a start key, check if it has the date
                        if date_pattern.search(pline):
                            started_spring_2022 = True
                            break
                
                if started_spring_2022:
                    # Clean project name (remove extra spaces, etc)
                    # sometimes name might be split across lines? Assuming single line for now based on preview.
                    matching_projects.add(project_name.strip())

# Filter funding data
# Check for exact matches or partial matches?
# "The Project_Name in the Funding SQLite table matches the project names that can be extracted..."
# I will try exact match first.
df_filtered = df_funding[df_funding['Project_Name'].isin(matching_projects)]

# Calculate result
num_projects = len(df_filtered)
total_funding = df_filtered['Amount'].astype(float).sum()

print("__RESULT__:")
print(json.dumps({
    "matching_projects_list": list(matching_projects),
    "found_in_funding": df_filtered['Project_Name'].tolist(),
    "count": num_projects,
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-956811650377216769': 'file_storage/function-call-956811650377216769.json', 'var_function-call-956811650377216698': 'file_storage/function-call-956811650377216698.json'}

exec(code, env_args)
