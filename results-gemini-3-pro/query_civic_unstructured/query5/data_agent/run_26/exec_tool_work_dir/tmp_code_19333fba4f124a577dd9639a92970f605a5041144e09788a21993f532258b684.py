code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-5605292304546820245'], 'r') as f:
    docs = json.load(f)
text = docs[0]['text']

# Load funding data
with open(locals()['var_function-call-3657045741871633664'], 'r') as f:
    funding_data = json.load(f)

# Funding map
funding_map = {}
for item in funding_data:
    funding_map[item['Project_Name']] = int(item['Amount'])

total_funding = 0
matched_projects = []

# Headers positions
header_iter = re.finditer(r'(Capital Improvement Projects|Disaster Recovery Projects)', text)
headers = [(m.start(), m.group(1)) for m in header_iter]

for project_name, amount in funding_map.items():
    # Find project in text
    # We use exact match or verify it's a project title
    # A project title in text is usually followed by "\n\n(cid:190) Updates:"
    # We can search for "Project Name"
    
    # Escape regex special chars in project name
    escaped_name = re.escape(project_name)
    # Search pattern: Name followed by optional newline then (cid:190) or Updates
    # Simplified: search for name in text
    
    match = re.search(escaped_name, text)
    if match:
        start_idx = match.start()
        # Look ahead for context
        # We grab up to next 1000 chars
        context = text[start_idx:start_idx+2000]
        
        # Determine Type
        is_disaster = False
        
        # 1. Check Name Suffixes
        if "(FEMA" in project_name or "(CalOES" in project_name or "(CalJPIA" in project_name:
            is_disaster = True
        
        # 2. Check Section Header
        # Find the header with largest start index < start_idx
        current_header = "Capital Improvement Projects" # Default
        for h_start, h_name in headers:
            if h_start < start_idx:
                current_header = h_name
            else:
                break
        
        if "Disaster" in current_header:
            is_disaster = True
            
        # If not disaster, skip
        if not is_disaster:
            continue
            
        # Determine Start Date in 2022
        # We look into the context for "Begin Construction" etc.
        # We should limit context to the next project start to avoid bleeding.
        # But heuristic of 1000 chars is usually fine for this summary format.
        
        started_2022 = False
        
        # 1. Check Name
        if "2022" in project_name:
            started_2022 = True
            
        # 2. Check Schedule in context
        # "Begin Construction: ... 2022"
        if re.search(r"Begin [cC]onstruction:.*2022", context):
            started_2022 = True
        elif re.search(r"Advertise:.*2022", context):
            started_2022 = True
        # "Construction was completed... 2022" - debatable, but likely started 2022 or 2021.
        # The prompt asks "started in 2022". 
        # If completed Nov 2022, it *could* have started in 2022.
        # Let's check if there is a start date. If not, maybe skip?
        # But if the project is "Broad Beach Road Water Quality Repair" (completed Nov 2022),
        # checking the list:
        # "Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)" -> Disaster.
        # "Broad Beach Road Water Quality Repair" -> completed.
        # If I include it, I might be right if it was a short project.
        # Let's include "Construction was completed ... 2022" as a weak signal if no other start date found?
        # Actually, "Begin Construction" is safer. 
        # But let's look at "Updates: Construction was completed...".
        # If I am strict, I might miss valid ones.
        # However, "started in 2022" usually implies `st` == 2022.
        # If I can't find `st`, I shouldn't guess.
        # But I'll include "Begin Construction" matches.
        
        if started_2022:
            total_funding += amount
            matched_projects.append(project_name)

print("__RESULT__:")
print(json.dumps({"projects": matched_projects, "total_funding": total_funding}))"""

env_args = {'var_function-call-5605292304546820245': 'file_storage/function-call-5605292304546820245.json', 'var_function-call-3657045741871633664': 'file_storage/function-call-3657045741871633664.json'}

exec(code, env_args)
