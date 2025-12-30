code = """import json
import re

# Load data
with open(locals()['var_function-call-3179318639355232823']) as f:
    docs = json.load(f)

with open(locals()['var_function-call-7560016992368588221']) as f:
    funding = json.load(f)

# Create funding map
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding}
project_names = list(funding_map.keys())
# Sort by length descending to prioritize longer matches
project_names.sort(key=len, reverse=True)

completed_park_projects = set()
debug_matches = []

for doc in docs:
    text = doc['text']
    # Normalize text newlines for easier regex? No, keep it.
    
    # 1. Find all project name occurrences
    matches = []
    for name in project_names:
        # Escape special regex chars in name
        pattern = re.escape(name)
        for m in re.finditer(pattern, text, re.IGNORECASE):
            matches.append({
                'start': m.start(),
                'end': m.end(),
                'name': name,
                'matched_text': m.group() 
            })
            
    # 2. Resolve overlaps
    # Sort by start asc, then length desc (which corresponds to end desc roughly)
    matches.sort(key=lambda x: (x['start'], -(x['end'] - x['start'])))
    
    final_matches = []
    if matches:
        curr = matches[0]
        for next_m in matches[1:]:
            # If next starts after current ends, it's a new segment
            if next_m['start'] >= curr['end']:
                final_matches.append(curr)
                curr = next_m
            else:
                # Overlap. Since we sorted by length desc for same start, 
                # or if it starts later but before current ends:
                # If 'curr' covers 'next', we skip 'next' (keep 'curr' which is longer/earlier)
                # But we need to check if 'next' extends beyond 'curr'.
                # Example: "Project A" (0-9) and "Project A Part 2" (0-16).
                # Sorted: (0, 16, "Project A Part 2"), (0, 9, "Project A")
                # curr is "Project A Part 2". next is "Project A".
                # next starts (0) < curr end (16). 
                # We ignore next.
                pass
        final_matches.append(curr)
        
    # 3. Analyze segments
    for i, m in enumerate(final_matches):
        seg_start = m['end']
        seg_end = final_matches[i+1]['start'] if i+1 < len(final_matches) else len(text)
        segment = text[seg_start:seg_end]
        s_lower = segment.lower()
        
        # Check completion
        # Pattern: "construction was completed" followed closely by "2022"
        # Or "completed" ... "2022"
        # We'll use a regex that looks for "construction was completed" and "2022" in the segment
        # allowing for some chars in between.
        
        # Check for completion status
        completed_pattern = r"construction\s+was\s+completed.{0,100}2022"
        if re.search(completed_pattern, s_lower):
            # Check if park related
            name_lower = m['name'].lower()
            if "park" in name_lower or "park" in s_lower:
                completed_park_projects.add(m['name'])
                debug_matches.append((m['name'], "Matched"))

total_amount = 0
for name in completed_park_projects:
    total_amount += funding_map[name]

print("__RESULT__:")
print(json.dumps(total_amount))"""

env_args = {'var_function-call-4554034855452536121': ['civic_docs'], 'var_function-call-4554034855452533864': ['Funding'], 'var_function-call-4554034855452535703': 'file_storage/function-call-4554034855452535703.json', 'var_function-call-7560016992368588221': 'file_storage/function-call-7560016992368588221.json', 'var_function-call-3179318639355232823': 'file_storage/function-call-3179318639355232823.json'}

exec(code, env_args)
