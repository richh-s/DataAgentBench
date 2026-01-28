code = """import json
import re

# Load funding data
with open(locals()['var_function-call-14868683301931886144'], 'r') as f:
    funding_data = json.load(f)

# Create a dictionary for funding: Project Name -> Amount
# Note: There might be multiple funding records for one project (e.g. different sources).
# The query asks for "total funding", so I should probably sum all funding records for a matching project.
funding_map = {}
for record in funding_data:
    p_name = record['Project_Name'].strip()
    amount = record['Amount']
    if p_name in funding_map:
        funding_map[p_name] += amount
    else:
        funding_map[p_name] = amount

# Load civic docs
with open(locals()['var_function-call-8294190329449223734'], 'r') as f:
    civic_docs = json.load(f)

# Combine text from all docs
full_text = "\n".join([doc['text'] for doc in civic_docs])

# Split text into lines
lines = full_text.split('\n')

# Logic to extract projects and their completion status
# We will look for lines that match a project name in our funding_map
current_project = None
project_info = {} # Name -> {'is_park': Bool, 'completed_2022': Bool}

# We need to sort project names by length (descending) to match longer names first 
# to avoid partial matches if one name is a substring of another.
known_projects = sorted(funding_map.keys(), key=len, reverse=True)

# Helper to checking completion
def check_completion(text_segment):
    # Look for "completed" and "2022"
    # Patterns based on preview:
    # "Construction was completed November 2022"
    # "Construction was completed, November 2022"
    # "Complete Construction: November 2022"
    text_lower = text_segment.lower()
    if '2022' in text_lower:
        if 'complete construction' in text_lower or 'construction was completed' in text_lower or 'completed construction' in text_lower:
             return True
    return False

# Iterate lines to segment text by project
# This is a heuristic. A line might exactly match a project name.
# Or a line might be just the project name.
# Given the preview, headers are often clean lines.

found_projects = []
current_lines = []
current_proj_name = None

for line in lines:
    line_stripped = line.strip()
    
    # Check if this line is a project name
    is_new_project = False
    if line_stripped in funding_map:
        is_new_project = True
        matched_name = line_stripped
    
    if is_new_project:
        # Save previous project
        if current_proj_name:
            found_projects.append({'name': current_proj_name, 'text': "\n".join(current_lines)})
        
        # Start new project
        current_proj_name = matched_name
        current_lines = []
    else:
        if current_proj_name:
            current_lines.append(line_stripped)

# Add the last project
if current_proj_name:
    found_projects.append({'name': current_proj_name, 'text': "\n".join(current_lines)})

# Filter and calculate
target_projects = []
total_funding = 0

for proj in found_projects:
    p_name = proj['name']
    p_text = proj['text']
    
    # Check if park related
    # 1. Check Name
    is_park = 'park' in p_name.lower()
    # 2. Check Text (Topic keywords or description)
    # The hint says "topic field contains comma-separated keywords". 
    # But we don't have a structured topic field here, just text. 
    # We will check if "park" appears in the text context if not in name?
    # Actually, looking at the preview "Bluffs Park Shade Structure", "Trancas Canyon Park", "Legacy Park".
    # It seems most park projects have "Park" in the name.
    # Let's rely on name first, and if description strongly implies it (e.g. mentions "playground", "recreation").
    # The hint says common topics include "park", "playground".
    if not is_park:
        if 'park' in p_text.lower() or 'playground' in p_text.lower():
            # Be careful not to match "parking".
            # Use regex for whole word match
            if re.search(r'\bpark\b', p_text.lower()) or re.search(r'\bplayground\b', p_text.lower()):
                is_park = True
    
    # Check if completed in 2022
    is_completed_2022 = check_completion(p_text)
    
    if is_park and is_completed_2022:
        target_projects.append(p_name)
        total_funding += funding_map[p_name]

print("__RESULT__:")
print(json.dumps({
    "target_projects": target_projects,
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-8294190329449223734': 'file_storage/function-call-8294190329449223734.json', 'var_function-call-14868683301931886144': 'file_storage/function-call-14868683301931886144.json'}

exec(code, env_args)
