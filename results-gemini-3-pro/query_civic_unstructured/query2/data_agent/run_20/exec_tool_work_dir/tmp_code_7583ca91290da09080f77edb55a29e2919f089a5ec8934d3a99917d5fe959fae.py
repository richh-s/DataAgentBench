code = """import json
import re

with open(locals()['var_function-call-11529138748773800259'], 'r') as f:
    civic_docs = json.load(f)
with open(locals()['var_function-call-6363168235283738913'], 'r') as f:
    funding_data = json.load(f)

# Funding lookup
funding_map = {}
for item in funding_data:
    funding_map[item['Project_Name'].strip()] = float(item['Amount'])

matches = set()
separator = "(cid:190)"

for doc in civic_docs:
    text = doc['text']
    parts = text.split(separator)
    
    current_proj = None
    
    # Check first part for initial project name
    p0 = parts[0].strip()
    if p0:
        lines = [l.strip() for l in p0.split('\n') if l.strip()]
        # Simple heuristic for header filtering
        if lines:
            # Take last line that is not a known header
            candidate = lines[-1]
            if "Capital" not in candidate and "Agenda" not in candidate:
                current_proj = candidate
    
    proj_text_map = {}
    
    for i in range(1, len(parts)):
        chunk = parts[i]
        if current_proj:
            if current_proj not in proj_text_map:
                proj_text_map[current_proj] = ""
            proj_text_map[current_proj] += " " + chunk
            
        # Try to find next project name at end of chunk
        lines = [l.strip() for l in chunk.strip().split('\n') if l.strip()]
        if not lines:
            continue
            
        # Iterate backwards to find a potential name
        # It must be before any 'Updates:' or 'Schedule:' lines
        # And not contain 'Agenda Item'
        cand = None
        for line in reversed(lines):
            if "Updates:" in line or "Schedule:" in line or "Construction:" in line:
                break
            if "Agenda" in line or "Page" in line:
                continue
            # Assume project name is short and doesn't end with '.'
            if len(line) < 100 and not line.endswith('.'):
                cand = line
                break
        
        if cand:
            current_proj = cand

    # Process extracted projects
    for name, content in proj_text_map.items():
        if 'park' in name.lower():
            # Check completion in 2022
            # "Construction was completed November 2022"
            # "Construction was completed, November 2022"
            # "Complete Construction: ... 2022"
            
            # Use regex
            # [Cc]onstruction.*?completed.*?\d{4}
            # or completed.*?2022
            
            if "2022" in content:
                # Validate context
                if re.search(r"Construction (was )?completed.*2022", content, re.IGNORECASE):
                    matches.add(name)
                elif re.search(r"Complete Construction:.*2022", content, re.IGNORECASE):
                    matches.add(name)

# Calculate total
total = 0.0
matched_names = []

for m in matches:
    # Try exact match
    if m in funding_map:
        total += funding_map[m]
        matched_names.append(m)
    else:
        # Try fuzzy
        # Check if m is a prefix of any funding key (ignoring parens)
        # or if funding key starts with m
        found = False
        for k, v in funding_map.items():
            if k.startswith(m) or m in k:
                # Ensure it's not a false positive
                # e.g. "Park" in "Parker"
                # But m is "Bluffs Park Shade Structure", k is "Bluffs Park Shade Structure (FEMA)"
                total += v
                matched_names.append(k)
                found = True
        
        # Note: If multiple funding records match one project?
        # e.g. "Project A" and "Project A (FEMA)" and "Project A (CalOES)"
        # Should we sum them all?
        # Yes, "Total funding for park-related projects..."
        # So if one project from civic docs (completed) corresponds to multiple funding sources, we sum them.
        # But we must ensure we don't double count if 'matches' has duplicates. 'matches' is a set.
        # But if 'matched_names' adds multiple entries for one 'm', that's correct (multiple sources).
        # But what if 'm1' and 'm2' both map to 'k'?
        # 'm1' = "Project A", 'm2' = "Project A (CalOES)" -> unlikely from docs parsing (docs usually list main name).
        
        # We should iterate through funding_map and see if any completed project 'm' matches it.
        pass

# Re-calculate cleanly
# Iterate all funding records. If a record belongs to a completed project (m), add it.
final_total = 0.0
final_matches = []

# Clean matches list
clean_matches = [m.strip() for m in matches]

for fname, amount in funding_map.items():
    # Check if fname corresponds to any project in clean_matches
    # Correspondence: fname starts with m? or m starts with fname? or m == fname?
    
    is_match = False
    for m in clean_matches:
        if m == fname:
            is_match = True
        elif fname.startswith(m):
             # verify it's a suffix like " (FEMA...)"
             suffix = fname[len(m):]
             if suffix.startswith(" (") or suffix == "":
                 is_match = True
        
        if is_match:
            break
            
    if is_match:
        final_total += amount
        final_matches.append(fname)

print("__RESULT__:")
print(json.dumps({"matches": final_matches, "total_funding": final_total}))"""

env_args = {'var_function-call-9104980258508522346': ['Funding'], 'var_function-call-9104980258508522899': ['civic_docs'], 'var_function-call-6363168235283738913': 'file_storage/function-call-6363168235283738913.json', 'var_function-call-6363168235283742026': 'file_storage/function-call-6363168235283742026.json', 'var_function-call-11529138748773800259': 'file_storage/function-call-11529138748773800259.json', 'var_function-call-7649956521544806152': 'Loaded successfully'}

exec(code, env_args)
