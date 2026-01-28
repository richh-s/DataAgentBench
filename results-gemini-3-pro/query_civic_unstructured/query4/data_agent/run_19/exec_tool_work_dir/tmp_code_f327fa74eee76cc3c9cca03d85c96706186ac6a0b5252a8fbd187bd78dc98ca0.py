code = """import json
import re

# Load data
with open(locals()['var_function-call-6833374196738575429'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-2571732605933953840'], 'r') as f:
    civic_docs = json.load(f)

projects_started_spring_2022 = set()

def is_spring_2022(date_str):
    if not date_str:
        return False
    ds = date_str.lower()
    # Check for "spring 2022" or "spring, 2022"
    if 'spring 2022' in ds or 'spring, 2022' in ds:
        return True
    # Check for specific months in 2022
    if '2022' in ds:
        if 'march' in ds or 'april' in ds or 'may' in ds:
            return True
    return False

# Parse documents
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Iterate to find project headers
    # We look for lines starting with "(cid:190)" which mark sections like Updates or Schedule
    # The project name is likely the non-empty line before that block.
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith('(cid:190)') or line.startswith('Updates:') or 'Project Schedule:' in line:
            # Found a marker. Look backwards for project name.
            project_name = None
            for k in range(i-1, -1, -1):
                prev_line = lines[k].strip()
                if prev_line:
                    # Ignore "Capital Improvement Projects..." headers
                    if 'Capital Improvement Projects' in prev_line or 'Agenda' in prev_line:
                        break
                    project_name = prev_line
                    break
            
            if project_name:
                # Now look forward for start date within this project block
                # The block ends at the next Project Name (which we detect by next marker's pre-line? 
                # or just scan a fixed number of lines or until next marker)
                
                # Let's scan forward until next marker
                block_text = ""
                for j in range(i, len(lines)):
                    next_l = lines[j].strip()
                    # If we hit another marker, check if it belongs to the same project or new
                    # Usually markers are Updates, Schedule, Description.
                    # If we see a new Project Name (no marker immediately?), it's hard to tell.
                    # But usually Project Name is followed by a marker.
                    # So if we see a line that is followed by a marker, it's a new project.
                    
                    # Check if lines[j] is a marker? Yes.
                    # Check if lines[j] starts a new project?
                    # We can just collect text until we find a line that looks like a project name (followed by marker).
                    
                    # Simpler: just search for "Begin Construction" in the next 20 lines.
                    block_text += next_l + " "
                    if len(block_text) > 2000: # Limit lookahead
                        break
                
                # Extract date
                # Regex for "Begin Construction: <date>"
                # Handle variations like "(cid:131) Begin Construction: ..."
                match = re.search(r'Begin [Cc]onstruction:?\s*([^(\n]*)', block_text, re.IGNORECASE)
                if match:
                    date_val = match.group(1).strip()
                    if is_spring_2022(date_val):
                        projects_started_spring_2022.add(project_name)

# Calculate funding
total_funding = 0
funded_projects = []

def clean_name(n):
    # Remove parens like "(FEMA Project)" for matching? 
    # The funding table has names with suffix. The doc might too.
    # Let's keep it simple first.
    return re.sub(r'\s+', ' ', n).strip().lower()

funding_map = {clean_name(r['Project_Name']): int(r['Amount']) for r in funding_data}

for p_name in projects_started_spring_2022:
    cn = clean_name(p_name)
    if cn in funding_map:
        total_funding += funding_map[cn]
        funded_projects.append(p_name)
    else:
        # Try without suffix in doc name? Or check if funding name is in doc name?
        # Hint: "Project_Name in the Funding SQLite table matches the project names..."
        # Maybe I extracted the name with some noise.
        # Let's check for near matches.
        found = False
        for f_name, amount in funding_map.items():
            if f_name in cn or cn in f_name:
                total_funding += amount
                funded_projects.append(p_name)
                found = True
                break
        if not found:
            pass

result = {
    "count": len(funded_projects),
    "total_funding": total_funding,
    "projects": funded_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3413924578737441379': ['civic_docs'], 'var_function-call-3413924578737439684': ['Funding'], 'var_function-call-6833374196738575429': 'file_storage/function-call-6833374196738575429.json', 'var_function-call-6833374196738572946': 'file_storage/function-call-6833374196738572946.json', 'var_function-call-2571732605933953840': 'file_storage/function-call-2571732605933953840.json'}

exec(code, env_args)
