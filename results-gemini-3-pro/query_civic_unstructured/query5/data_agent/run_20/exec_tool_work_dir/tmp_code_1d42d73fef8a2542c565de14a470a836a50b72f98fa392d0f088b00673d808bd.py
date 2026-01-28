code = """import json
import pandas as pd
import re

# Load Funding Data
funding_file = locals()['var_function-call-5321786749699906543']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

# Load Civic Docs
docs_file = locals()['var_function-call-13929900393569377328']
with open(docs_file, 'r') as f:
    civic_docs = json.load(f)

projects = {} # Name -> {starts_2022: bool, is_disaster: bool}

# Helper to check if text implies disaster
def check_disaster(text_context):
    keywords = ["FEMA", "CalOES", "CalJPIA", "Disaster Recovery"]
    for k in keywords:
        if k.lower() in text_context.lower():
            return True
    return False

# Regex for start date
# Patterns to look for in "Project Schedule" or text
start_patterns = [
    r"Begin Construction:?\s*([A-Za-z]+\s*\d{4})",
    r"Construction Start:?\s*([A-Za-z]+\s*\d{4})",
    r"Start Date:?\s*([A-Za-z]+\s*\d{4})",
    r"Advertise:?\s*([A-Za-z]+\s*\d{4})", # Advertise is NOT start of project (usually construction start is 'st')
    # But prompt says "st: Start time/date". Usually for construction projects 'st' is construction start.
    # The sample shows "Begin Construction" as a key milestone.
    # I will strictly look for "Begin Construction" or similar.
]

# The prompt says "st: Start time/date". 
# Flexible formats: "2022-Spring", "2022-Fall", "2022-02", "2022-March".
# The sample text has "Begin Construction: Fall 2023".
# So I should look for the line containing "Begin Construction" and check if it has "2022".

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_section = ""
    
    # Iterate lines to find projects
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
            
        # Check for Section Headers
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            # But ensure it's a header (maybe ends with ')' or is short?)
            # Or just update current_section based on presence
            if "Disaster" in line:
                current_section = "Disaster"
            elif "Capital" in line:
                current_section = "Capital"
                
        # Check for Project Name
        # Look ahead for (cid:190) followed by Updates/Description
        is_project = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if next_line.startswith("(cid:190)") and ("Updates" in next_line or "Description" in next_line or "Status" in next_line):
                is_project = True
        
        # Sometimes there's an empty line between name and updates
        if not is_project and i + 2 < len(lines) and not lines[i+1].strip():
            next_next_line = lines[i+2].strip()
            if next_next_line.startswith("(cid:190)") and ("Updates" in next_next_line or "Description" in next_next_line or "Status" in next_next_line):
                is_project = True
        
        if is_project:
            p_name = line
            # Clean name
            p_name = p_name.strip()
            
            # Determine if disaster
            is_dis = False
            if current_section == "Disaster":
                is_dis = True
            if check_disaster(p_name):
                is_dis = True
            
            # Extract info from the block
            # Block ends at next project or end of file.
            # We can scan forward until we hit another project start line.
            # But that requires complex lookahead.
            # Instead, scan a reasonable number of lines or until a new header/project heuristic.
            # Let's just scan the next 50 lines.
            
            started_2022 = False
            
            # Look in next 50 lines for "Begin Construction"
            for j in range(i+1, min(i+50, len(lines))):
                subline = lines[j].strip()
                # Stop if we hit a new project marker (heuristic)
                # This might be tricky, so let's just search.
                # If we hit a new project, we might overlap, but that's okay, we just want to find if *this* project started in 2022.
                # Actually, overlapping might attribute 2022 start to the wrong project.
                # Better: only scan until next line that looks like a project name?
                # A project name is not starting with (cid:190).
                # Most lines in the block start with (cid:131) or (cid:190) or are text.
                # A new project name usually doesn't start with special chars.
                
                # Check for Start Date
                # Check for "Begin Construction" and "2022"
                if "Begin Construction" in subline or "Construction Start" in subline or "Start Date" in subline:
                    if "2022" in subline:
                        started_2022 = True
                
                # Also check "Construction was completed" in 2022? 
                # No, that's end date.
                # What if "Notice to Proceed" in 2022?
                if "Notice to Proceed" in subline and "2022" in subline:
                    started_2022 = True
                    
            # Store/Update project
            if p_name not in projects:
                projects[p_name] = {'is_disaster': is_dis, 'started_2022': started_2022}
            else:
                # Update if we found new info
                if is_dis: projects[p_name]['is_disaster'] = True
                if started_2022: projects[p_name]['started_2022'] = True

# Filter projects
target_projects = []
for name, info in projects.items():
    if info['is_disaster'] and info['started_2022']:
        target_projects.append(name)

# Join with Funding
total_funding = 0
matched_projects = []

# Normalize names for joining
# Funding table names vs extracted names
# Extracted names might have extra spaces or be slightly different.
# I'll create a map of normalized_funding_name -> amount
funding_map = {}
for idx, row in df_funding.iterrows():
    n = row['Project_Name'].strip().lower()
    # Funding table might have multiple entries for one project? 
    # The schema says "Funding_ID" is unique. Project_Name might repeat?
    # "Funding table contains funding records... Project names can be joined..."
    # Let's sum amounts for the same project name in funding table first?
    # Or just iterate matches.
    if n not in funding_map:
        funding_map[n] = 0
    funding_map[n] += int(row['Amount'])

found_amount = 0
for tp in target_projects:
    tp_norm = tp.strip().lower()
    if tp_norm in funding_map:
        found_amount += funding_map[tp_norm]
        matched_projects.append(tp)
    else:
        # Try fuzzy match or suffix handling?
        # "Disaster project names often include suffixes like '(FEMA Project)'"
        # Maybe the funding table name has the suffix but the doc name doesn't?
        # Or vice versa?
        # Sample funding: "Corral Canyon Culvert Repairs (FEMA Project)"
        # Sample doc: "Corral Canyon Culvert Repairs"
        # If doc says "Corral Canyon Culvert Repairs" is disaster (via section/content), and funding has "(FEMA Project)", they match.
        # So I should check if `tp_norm` is a substring of funding keys or vice versa.
        
        # Check if funding name starts with tp_norm
        for fname in funding_map:
            if fname.startswith(tp_norm) or tp_norm.startswith(fname):
                 # Verify it's a good match
                 # e.g. "Project A" and "Project A (FEMA)"
                 found_amount += funding_map[fname]
                 matched_projects.append(fname)
                 # Be careful not to double count if multiple funding entries match?
                 # Actually, funding_map keys are unique (lower case).
                 # But if tp_norm matches multiple funding keys?
                 # e.g. "Project A" matches "Project A" and "Project A (FEMA)"?
                 # If "Project A" started in 2022, do we count both funding sources?
                 # Yes, "Total funding for disaster-related projects".
                 # If the base project is the same, and one funding is labeled FEMA, they are likely related.
                 pass

# But wait, checking startsWith might overmatch. 
# e.g. "Road Repair" matches "Road Repair Phase 2".
# I should be careful.
# However, the prompt says "The Project_Name in the Funding SQLite table matches the project names that can be extracted from the civic documents".
# This suggests exact match might work or is intended.
# But suffixes are mentioned. 
# Let's try to match exact first. If not, try suffix.

# Let's refine the join.
# I will output the identified target projects and then do the join carefully.
# I'll print the target projects first to debug.

print("__RESULT__:")
print(json.dumps(target_projects))"""

env_args = {'var_function-call-1518905300948613366': ['Funding'], 'var_function-call-1518905300948614017': ['civic_docs'], 'var_function-call-5321786749699906543': 'file_storage/function-call-5321786749699906543.json', 'var_function-call-5321786749699905058': 'file_storage/function-call-5321786749699905058.json', 'var_function-call-130987581307727602': 'file_storage/function-call-130987581307727602.json', 'var_function-call-13929900393569377328': 'file_storage/function-call-13929900393569377328.json'}

exec(code, env_args)
