code = """import pandas as pd
import json
import re

# Load Funding Data
funding_rows = pd.read_json(locals()['var_function-call-3462127422727608690'])
# Normalize Amounts
funding_rows['Amount'] = pd.to_numeric(funding_rows['Amount'])

# Load Civic Docs
with open(locals()['var_function-call-3462127422727608521'], 'r') as f:
    civic_docs = json.load(f)

# Concatenate text
full_text = "\n".join([d['text'] for d in civic_docs])

# List of project names
project_names = funding_rows['Project_Name'].unique().tolist()
# Sort by length descending to match longest names first (though with the Updates check, it's less critical)
project_names.sort(key=len, reverse=True)

# Find project blocks
# Store as (start_index, name)
found_blocks = []

for name in project_names:
    # Pattern: Name followed shortly by "Updates:"
    # We allow some whitespace and maybe some garbage chars like bullets
    # The preview shows (cid:190) which is a unicode char.
    # We'll just look for the name, then check if "Updates:" is within the next 100 characters.
    
    matches = [m.start() for m in re.finditer(re.escape(name), full_text)]
    for m in matches:
        # Check context
        snippet = full_text[m+len(name):m+len(name)+150]
        if "Updates:" in snippet:
            # Check if this index is already covered by a longer match?
            # Since we iterate longest to shortest, if we find a match, it's the specific one.
            # But "Trancas Canyon Park Playground" vs "Trancas Canyon Park Playground Resurfacing".
            # If "Resurfacing" matched, it consumed that text. 
            # We haven't implemented "consumption".
            # If we find "Trancas Canyon Park Playground" at index X, and "Trancas Canyon Park Playground Resurfacing" at index X,
            # we prefer the Resurfacing one.
            # But we are iterating longest first.
            # So if Resurfacing is found at X, we add it.
            # Then when we check the shorter one, we'll find it at X too.
            # We should check if X is already in found_blocks.
            
            # Actually, just storing them all and sorting by start index, then filtering overlaps is better.
            found_blocks.append({'name': name, 'start': m, 'length': len(name)})

# Sort by start index
found_blocks.sort(key=lambda x: x['start'])

# Remove overlaps (keep longest match at same start)
unique_blocks = []
if found_blocks:
    current = found_blocks[0]
    for i in range(1, len(found_blocks)):
        next_block = found_blocks[i]
        # If next block starts within the current block's name range, it's an overlap (substring match)
        # Since we sorted longest first in the original search, the logic is tricky.
        # But here we sorted by start.
        # If start is same (or very close), picking the longest length is best.
        if next_block['start'] < current['start'] + current['length']:
            # Overlap.
            if next_block['length'] > current['length']:
                current = next_block
            # Else keep current
        else:
            unique_blocks.append(current)
            current = next_block
    unique_blocks.append(current)

# Now define text content for each block
# From block['start'] to next_block['start']
projects_with_text = []
for i in range(len(unique_blocks)):
    start = unique_blocks[i]['start']
    name = unique_blocks[i]['name']
    if i < len(unique_blocks) - 1:
        end = unique_blocks[i+1]['start']
    else:
        end = len(full_text)
    
    block_text = full_text[start:end]
    projects_with_text.append({'name': name, 'text': block_text})

# Filter and Sum
total_funding = 0.0
matched_projects = []

completion_regex = re.compile(r"(construction\s+was\s+completed|complete\s+construction).*?2022", re.IGNORECASE | re.DOTALL)

print("Processing Projects:")
for p in projects_with_text:
    name = p['name']
    text = p['text']
    
    # 1. Check Topic (Park)
    is_park = False
    name_lower = name.lower()
    
    if "park" in name_lower:
        is_park = True
        # Exclude "Malibu Park" infrastructure
        if "malibu park" in name_lower and "malibu bluffs" not in name_lower:
             # Check for infrastructure keywords
             if any(x in name_lower for x in ['drainage', 'resurfacing', 'storm drain', 'culvert']):
                 is_park = False
    # Include if "Playground" or "Skate" or "Green Streets" (maybe? No, Green Streets is usually runoff)
    if "playground" in name_lower or "skate" in name_lower:
        is_park = True
        
    if not is_park:
        continue

    # 2. Check Status (Completed in 2022)
    # Scan the text snippet (Updates section usually first)
    if completion_regex.search(text):
        amount = funding_rows[funding_rows['Project_Name'] == name]['Amount'].values[0]
        print(f"MATCH: {name} | Amount: {amount}")
        matched_projects.append(name)
        total_funding += amount

print(f"__RESULT__:\n{json.dumps(total_funding)}")"""

env_args = {'var_function-call-3462127422727608690': 'file_storage/function-call-3462127422727608690.json', 'var_function-call-3462127422727608521': 'file_storage/function-call-3462127422727608521.json'}

exec(code, env_args)
