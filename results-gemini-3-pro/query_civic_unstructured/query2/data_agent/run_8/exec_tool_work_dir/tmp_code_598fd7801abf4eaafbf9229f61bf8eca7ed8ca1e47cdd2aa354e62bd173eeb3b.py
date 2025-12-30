code = """import json
import re

# Load data
funding_path = locals()['var_function-call-13109238308160603251']
docs_path = locals()['var_function-call-13109238308160604256']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Extract text from all docs
full_text = "\n".join([d['text'] for d in civic_docs])

# Parse projects
# We look for lines that look like project names followed by updates
# Pattern: Non-empty line, then (cid:190) line
# We'll split by lines
lines = full_text.split('\n')
projects = []
current_project = None
current_text = []

# Regex for bullet point
bullet_pattern = re.compile(r'^\(cid:190\)')

# Helper to check if a line is a likely project name
# It shouldn't be a known header or empty
def is_likely_name(line):
    line = line.strip()
    if not line: return False
    if line.startswith('('): return False # (cid:190) or (cid:131)
    if line.lower() in ["updates:", "project schedule:", "project description:", "capital improvement projects (design)", "capital improvement projects (construction)", "capital improvement projects (not started)", "discussion:", "recommended action:", "subject:", "to:", "from:", "prepared by:", "approved by:"]:
        return False
    if "page" in line.lower() and "of" in line.lower(): return False # Page X of Y
    if "agenda item" in line.lower(): return False
    return True

# Iterate to find starts
# We look for a line starting with (cid:190). The line before it (skipping empty lines) is the name.
# Then we capture everything until the next name.

# Better approach: Iterate lines, identify (cid:190) lines.
# Backtrack to find name.
# Forward track to find end of block.

# Let's group lines into blocks.
# Actually, iterating and maintaining state is easier.

extracted_projects = []

# Indices of lines starting with (cid:190)
bullet_indices = [i for i, line in enumerate(lines) if bullet_pattern.match(line.strip())]

# Group consecutive bullet blocks (sections for one project)
# A project has a name, then one or more bullet sections.
# If two bullet lines are far apart?
# Usually project name is immediately above the first bullet.
# Subsequent bullets belong to the same project until a new Name appears.
# But how to distinguish "Next Project Name" from "Text within Project"?
# Project Names usually don't have preceding text that belongs to the previous bullet?
# Actually, a project block ends when a new Project Name appears.
# A new Project Name appears before a new `(cid:190)` block.

# Strategy:
# For each `(cid:190)` line:
#   Check if we are already inside a project (i.e. this bullet continues previous project).
#   OR if this starts a new project (preceded by a Name).
#   How to distinguish?
#   If the line before (skipping empty) is NOT a bullet line, does it look like a Name?
#   If yes, it's a new project.
#   If no (e.g. it's text text text), it's likely continuation.
#   Wait, "Project Name" is usually short-ish and capitalized?
#   Let's use the property that Project Name is a distinct line.

projects_found = []

i = 0
while i < len(lines):
    line = lines[i].strip()
    
    # Check if this line is a start of a bullet section
    if bullet_pattern.match(line):
        # Determine the project name for this block
        # Look backwards for a candidate name
        # Candidate: non-empty, not a bullet, not a known header
        name_candidate = None
        k = i - 1
        while k >= 0:
            prev_line = lines[k].strip()
            if not prev_line:
                k -= 1
                continue
            # If prev_line is a bullet, then this bullet is a continuation?
            # But we are iterating forward. If we are processing this bullet, we want to know if it starts a new project.
            # If the immediate non-empty prev line is a bullet, then this is continuation.
            if bullet_pattern.match(prev_line):
                # Continuation of whatever project was active
                break # Stop looking for name
            
            # If prev_line is text, is it a name?
            # If it's a long paragraph line, unlikely.
            # If it's "Capital Improvement Projects...", it's a header.
            if is_likely_name(prev_line):
                name_candidate = prev_line
                # But wait, could there be multiple lines of text between bullets?
                # "Updates:\n(cid:131) text..."
                # The `(cid:190)` is the start of the Updates section.
                # So the line before `(cid:190)` might be "Updates:"?
                # In the sample: "(cid:190) Updates:" is on the SAME line?
                # Sample: "(cid:190) Updates:"
                # Sample: "(cid:190) Project Description:"
                # So the line starts with (cid:190).
                # The Name is strictly above it.
                
                # If name_candidate is found, we start a new project.
                # If we are already in a project, we close it?
                # Yes.
            break # Found the line before the bullet
        
        if name_candidate:
            # New project found
            projects_found.append({
                "name": name_candidate,
                "text": line # Start text with this line
            })
        else:
            # Continuation
            if projects_found:
                projects_found[-1]["text"] += "\n" + line
    else:
        # Just text line
        if projects_found:
            projects_found[-1]["text"] += "\n" + line

    i += 1

# Now process extracted projects
park_projects_2022 = []

for p in projects_found:
    name = p['name']
    text = p['text']
    
    # Clean name
    # Sometimes header might be captured.
    # "Capital Improvement Projects (Construction)" might be captured if we are not careful?
    # is_likely_name handles that.
    
    # Keywords
    is_park = False
    name_lower = name.lower()
    text_lower = text.lower()
    
    # Park detection
    park_keywords = ['park', 'playground', 'recreation', 'walkway', 'trail', 'beach'] 
    # Added beach/walkway based on "Point Dume Walkway" possibly being target. 
    # But let's check matches.
    # User said "park-related".
    
    if any(k in name_lower for k in park_keywords):
        is_park = True
    elif "park" in text_lower: # fallback if park is mentioned in text
        # But "parking" contains "park". Be careful.
        if re.search(r'\bpark\b', text_lower):
            is_park = True
            
    # Completion detection
    # Look for "completed" and "2022"
    # "Construction was completed November 2022"
    # "Complete Construction: November 2022"
    completed_2022 = False
    
    # Check for 2022 in text
    if "2022" in text:
        # Check context
        # Regex for completion
        # patterns:
        # completed.*2022
        # complete.*2022
        # notice of completion.*2023 (implies completed before)
        # We need "completed in 2022".
        
        # Matches: "Construction was completed November 2022"
        if re.search(r'(completed|complete construction|construction complete).*?2022', text_lower, re.DOTALL):
            completed_2022 = True
            
    if is_park and completed_2022:
        park_projects_2022.append(name)

print("__RESULT__:")
print(json.dumps(park_projects_2022))"""

env_args = {'var_function-call-4994192944937523556': ['civic_docs'], 'var_function-call-4994192944937523005': ['Funding'], 'var_function-call-4994192944937522454': 'file_storage/function-call-4994192944937522454.json', 'var_function-call-4994192944937521903': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-13109238308160603251': 'file_storage/function-call-13109238308160603251.json', 'var_function-call-13109238308160604256': 'file_storage/function-call-13109238308160604256.json'}

exec(code, env_args)
