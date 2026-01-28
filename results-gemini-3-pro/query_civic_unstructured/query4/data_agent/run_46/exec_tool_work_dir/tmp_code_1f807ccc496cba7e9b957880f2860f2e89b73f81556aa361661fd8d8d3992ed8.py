code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-10071465858978758167'], 'r') as f:
    civic_docs = json.load(f)

# Load funding
with open(locals()['var_function-call-10071465858978756684'], 'r') as f:
    funding_data = json.load(f)

# Convert funding to dict for easier lookup
funding_map = {item['Project_Name'].strip(): item['Amount'] for item in funding_data}

projects_found = {} # Name -> Start Date

def normalize_text(text):
    return " ".join(text.split())

def is_header(line):
    headers = [
        "Capital Improvement Projects",
        "Public Works Commission",
        "Agenda Report",
        "Page",
        "Agenda Item",
        "Prepared by",
        "Approved by",
        "Date prepared",
        "Meeting date",
        "Subject:",
        "RECOMMENDED ACTION:",
        "DISCUSSION:",
        "To:",
        "Item",
        "Updates:",
        "Project Schedule:",
        "Estimated Schedule:",
        "Project Description:",
        "Project Updates:"
    ]
    if not line.strip():
        return True
    if len(line.strip()) < 3: # Very short lines
        return True
    for h in headers:
        if h.lower() in line.lower():
            return True
    if line.strip().startswith("(") and "cid" in line: # Bullet points lines are content, not titles
        return True
    return False

# Keywords for Spring 2022
spring_2022_patterns = [
    r"spring.*2022",
    r"march.*2022",
    r"april.*2022",
    r"may.*2022",
    r"2022.*spring",
    r"2022.*03",
    r"2022.*04",
    r"2022.*05"
]

def check_date(line):
    line_lower = line.lower()
    for pat in spring_2022_patterns:
        if re.search(pat, line_lower):
            return True
    return False

# Parsing
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        clean_line = line.strip()
        
        # Heuristic for Project Title:
        # Not a header, not a bullet, looks like a title.
        # Often all caps or Title Case.
        # Check if next lines contain "Updates:" or "Project Description" or "Project Schedule" to confirm it's a project block.
        
        is_candidate_title = True
        if "(cid:" in clean_line: is_candidate_title = False
        if clean_line.startswith("Page"): is_candidate_title = False
        if clean_line.startswith("Agenda"): is_candidate_title = False
        
        # Check against known project names in funding map to be sure?
        # That would be a strong signal.
        if clean_line in funding_map:
            current_project = clean_line
            continue
            
        # Also, sometimes the name in text is slightly different or funding name has extra stuff.
        # But let's try to detect project structure.
        # If line is followed by "(cid:190) Updates:" or similar within next few lines, it's likely a project.
        
        # Look ahead
        is_project_header = False
        for offset in range(1, 5): # Check next 4 lines
            if i + offset < len(lines):
                next_l = lines[i+offset].strip()
                if "(cid:190)" in next_l and ("Updates" in next_l or "Project" in next_l or "Description" in next_l):
                    is_project_header = True
                    break
        
        if is_project_header and not "(cid:" in clean_line and len(clean_line) > 5:
             # Likely a project title
             # Clean it up (remove leading/trailing spaces)
             current_project = clean_line
        
        if current_project:
            # Search for Start Date info
            # We look for "Begin Construction: ..." or "Start: ..."
            # We only care if it matches Spring 2022.
            
            # Check for "Begin Construction"
            if "Begin Construction" in clean_line or "Start" in clean_line or "Construction start" in clean_line.lower():
                if check_date(clean_line):
                    projects_found[current_project] = clean_line

            # Also check for "Construction was completed". If it was completed, it started earlier.
            # But query specifically asks "projects started in Spring 2022".
            # So I will stick to "Begin Construction" or explicit Start.
            # Wait, sometimes it says "Estimated Schedule: ... Begin Construction: Spring 2022".
            
            # What if line is just "Spring 2022" under a "Schedule" header?
            # The text layout in preview:
            # (cid:131) Begin Construction: Fall 2023
            
            # So looking for "Begin Construction" line is good.
            pass

# Filter and Match with Funding
# We need to be careful about Project Name matching.
# I'll create a normalized map for funding.

funding_norm = {k.lower(): v for k, v in funding_map.items()}

matched_projects = []
total_funding = 0

for proj_name, date_str in projects_found.items():
    # Try to find funding
    # Exact match
    amt = funding_map.get(proj_name)
    if amt is None:
        # Try case insensitive
        amt = funding_norm.get(proj_name.lower())
    
    if amt is None:
        # Try substring match? 
        # "PCH Median Improvements Project" in text vs "PCH Median Improvements Project" in DB.
        # Maybe text has newlines?
        # I did strip().
        pass
    
    if amt is not None:
        matched_projects.append({"name": proj_name, "date": date_str, "amount": amt})
        total_funding += amt
    else:
        # Log missing funding (maybe name mismatch)
        # For debugging I'll print them
        pass

print("__RESULT__:")
print(json.dumps({"count": len(matched_projects), "total_funding": total_funding, "projects": matched_projects, "debug_found_raw": projects_found}))"""

env_args = {'var_function-call-600716714873686583': ['Funding'], 'var_function-call-600716714873684502': 'file_storage/function-call-600716714873684502.json', 'var_function-call-10071465858978756684': 'file_storage/function-call-10071465858978756684.json', 'var_function-call-10071465858978758167': 'file_storage/function-call-10071465858978758167.json'}

exec(code, env_args)
