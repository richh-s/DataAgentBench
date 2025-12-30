code = """import json
import re

# Load data
with open(locals()['var_function-call-8970245157857899516'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-8970245157857899203'], 'r') as f:
    funding_data = json.load(f)

# Build funding map: Project_Name -> Total Amount (sum of all sources)
# Normalize project names: strip, lower
project_funding = {}
for row in funding_data:
    p_name = row['Project_Name'].strip()
    amount = float(row['Amount'])
    # Store with original casing for debugging, but use normalized key for lookup?
    # Or just store by normalized key.
    key = p_name.lower()
    if key not in project_funding:
        project_funding[key] = 0.0
    project_funding[key] += amount

# Extract projects
completed_park_projects = set()

# Regex to find project starts: Name followed by (cid:190) Updates or Project Description
# We capture the line preceding the marker.
marker_pattern = re.compile(r'(?P<name>[^\n]+)\s*\n+\(cid:190\)\s*(?:Updates|Project Description)', re.IGNORECASE)

debug_info = []

for doc in civic_docs:
    text = doc['text']
    matches = list(marker_pattern.finditer(text))
    
    for i, match in enumerate(matches):
        raw_name = match.group('name').strip()
        
        # Get text block
        start_idx = match.start()
        if i < len(matches) - 1:
            end_idx = matches[i+1].start()
            block = text[start_idx:end_idx]
        else:
            block = text[start_idx:]
        
        # Check if park related
        # "park" in name OR "park" in block?
        # Hint says topic field has "park". I'll search for "park" as a whole word in the block or name.
        is_park = "park" in raw_name.lower() # Primary check
        
        # If not in name, check block for keywords like "Topic: Park" if it exists, or just "park" mentioned?
        # Risk of false positive (e.g. "parking").
        # The preview didn't show "Topic:". 
        # I'll stick to "park" in name for now as it's safer.
        
        if is_park:
            # Check completed in 2022
            # Look for "Construction was completed" ... "2022"
            # Or "Construction completed" ... "2022"
            # Or "Notice of completion" ... "2022" (This might be later)
            # User asks "completed in 2022".
            
            # Normalize block for search
            block_lower = block.lower()
            
            # Check for completion phrases
            # 1. "Construction was completed [Month] 2022"
            # 2. "Construction completed [Month] 2022"
            if re.search(r'construction (was )?completed.*2022', block_lower):
                 completed_park_projects.add(raw_name)
                 debug_info.append(f"Found: {raw_name}")

# Calculate total funding
total_funding = 0.0
matched_projects = []

for p_name in completed_park_projects:
    key = p_name.strip().lower()
    if key in project_funding:
        total_funding += project_funding[key]
        matched_projects.append({"name": p_name, "amount": project_funding[key]})
    else:
        # Try fuzzy match?
        # Maybe the name in text has extra words?
        # Check if any funding project is a substring or vice versa?
        pass

result = {
    "total_funding": total_funding,
    "projects_found": matched_projects,
    "debug_projects_raw": list(completed_park_projects)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8970245157857899516': 'file_storage/function-call-8970245157857899516.json', 'var_function-call-8970245157857899203': 'file_storage/function-call-8970245157857899203.json'}

exec(code, env_args)
