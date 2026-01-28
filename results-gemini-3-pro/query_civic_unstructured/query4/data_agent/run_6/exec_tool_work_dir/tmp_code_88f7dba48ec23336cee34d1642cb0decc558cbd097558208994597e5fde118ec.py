code = """import json
import re

# Load the civic docs
with open('var_function-call-8728366382386706787', 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
with open('var_function-call-8728366382386704966', 'r') as f:
    funding_data = json.load(f)

funding_map = {row['Project_Name']: row['Amount'] for row in funding_data}

extracted_projects = []

def is_spring_2022(date_str):
    if not date_str:
        return False
    d = date_str.lower()
    if '2022' in d:
        if 'spring' in d:
            return True
        # Check months
        if any(m in d for m in ['march', 'april', 'may']):
            return True
        # Check numeric 03/2022 etc is harder without regex, but let's try simple text check
        # "03-22", "04-22", "05-22" might be day, or month-year. 
        # But usually these docs use "Spring 2022" or "March 2022".
    return False

# Regex to clean up lines
def clean_line(line):
    return line.strip()

projects_found = {} # Name -> Start Date found

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_project = None
    
    # Iterate to find project blocks
    # Logic: Look for lines followed by a line with (cid:190) or special bullet
    # In the provided text, (cid:190) appears as a bullet for Updates or Schedule.
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line is a project name
        # Heuristic: The NEXT non-empty line starts with (cid:190)
        # Find next non-empty line
        j = i + 1
        next_line = None
        while j < len(lines):
            if lines[j].strip():
                next_line = lines[j].strip()
                break
            j += 1
            
        if next_line and '(cid:190)' in next_line:
            # This line 'line' is likely a project name
            # But sometimes "Updates:" is not preceded by project name immediately if there was a header.
            # However, looking at the sample:
            # "2022 Morning View ... \n\n (cid:190) Updates:"
            # So 'line' is the project name.
            # Verify if 'line' is not a header like "Capital Improvement Projects (Design)"
            # Headers usually don't have "(cid:190) Updates" right after? 
            # Actually "Capital Improvement Projects (Design)" is followed by "2022 Morning View..."
            # So the project name is safe.
            current_project = line
            if current_project not in projects_found:
                projects_found[current_project] = set()
        
        if current_project:
            # Look for start date in the current line
            # "Begin Construction: ..."
            # "Construction Start: ..."
            # "Start Date: ..."
            # "Scheduled to begin: ..."
            
            lower_line = line.lower()
            if 'begin construction' in lower_line or 'construction start' in lower_line or 'construction to begin' in lower_line or 'start date' in lower_line or 'scheduled to begin' in lower_line:
                # Extract date
                parts = line.split(':')
                if len(parts) > 1:
                    date_part = parts[-1].strip()
                    projects_found[current_project].add(date_part)
            # Also check for "Construction was completed" to exclude?
            # No, user asks "started".
            # What if "Construction started in..."
            if 'construction started' in lower_line:
                 # Extract date
                 # This might be in the sentence.
                 projects_found[current_project].add(line)

# Now filter for Spring 2022
spring_2022_projects = []
for proj, dates in projects_found.items():
    for date_str in dates:
        if is_spring_2022(date_str):
            spring_2022_projects.append(proj)
            break

# Calculate funding
total_funding = 0
found_funding_projects = []
missing_funding_projects = []

for proj in spring_2022_projects:
    # Try exact match
    if proj in funding_map:
        total_funding += funding_map[proj]
        found_funding_projects.append(proj)
    else:
        # Try to match loosely?
        # Maybe remove special chars or spaces
        found = False
        for f_proj in funding_map:
            if proj.lower() == f_proj.lower():
                total_funding += funding_map[f_proj]
                found_funding_projects.append(proj)
                found = True
                break
            if proj in f_proj or f_proj in proj:
                # Be careful with partial matches
                pass
        if not found:
            missing_funding_projects.append(proj)

print("__RESULT__:")
print(json.dumps({
    "spring_2022_projects": spring_2022_projects,
    "total_funding": total_funding,
    "found_funding_count": len(found_funding_projects),
    "missing_funding_projects": missing_funding_projects,
    "all_extracted_dates": {k: list(v) for k, v in projects_found.items()}
}))"""

env_args = {'var_function-call-8728366382386706787': 'file_storage/function-call-8728366382386706787.json', 'var_function-call-8728366382386704966': 'file_storage/function-call-8728366382386704966.json'}

exec(code, env_args)
