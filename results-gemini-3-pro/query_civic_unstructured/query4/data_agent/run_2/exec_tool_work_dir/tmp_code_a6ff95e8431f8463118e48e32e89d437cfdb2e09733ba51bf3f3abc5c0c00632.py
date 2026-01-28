code = """import json
import re

# Load data
with open(locals()['var_function-call-18189666317777667959'], 'r') as f:
    funding_list = json.load(f)

with open(locals()['var_function-call-9598999800864405820'], 'r') as f:
    civic_docs = json.load(f)

# Map Project Name to Amount
project_funding = {}
for item in funding_list:
    name = item.get('Project_Name')
    try:
        amount = float(item.get('Amount', 0))
    except:
        amount = 0
    if name:
        project_funding[name] = amount

# Get all project names for searching
project_names = list(project_funding.keys())
# Sort by length descending to match longest names first
project_names.sort(key=len, reverse=True)

started_projects = set()

# Regex for Spring 2022
# Spring = March, April, May
# Patterns: Spring 2022, 2022-Spring, March 2022, April 2022, May 2022, 2022-03, 2022-04, 2022-05
# Also allow separators like / or - or space
date_pattern = r"(Spring[\s,]+2022|2022[\s\-]+Spring|March[\s,]+2022|April[\s,]+2022|May[\s,]+2022|2022[\s\-]0?3|2022[\s\-]0?4|2022[\s\-]0?5)"

# Regex for Start Context
# Look for "Begin Construction", "Start", "Commence", "Construction Start"
# appearing shortly before the date
start_context = r"(Begin Construction|Construction Start|Start Date|Construction Period|Schedule|Timeline)"

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Identify project sections
    # Find all occurrences of all project names
    matches = []
    for pname in project_names:
        # Escape regex special characters in project name
        # Use simple string find or regex with word boundaries? 
        # Project names might contain parens " (FEMA Project)"
        # Use strict string finding to be safe
        idx = text.find(pname)
        while idx != -1:
            matches.append((idx, pname))
            idx = text.find(pname, idx + 1)
            
    # Sort matches by position
    matches.sort(key=lambda x: x[0])
    
    # Filter overlaps (simple approach: if match starts inside previous match, skip? 
    # But we sorted by length desc first, so if we found "Long Name" and "Name", "Long Name" is found.
    # But "Name" might be found inside "Long Name".
    # Wait, simple find finds substrings.
    # If "Project A Phase 2" is at index 10, and "Project A" is at index 10.
    # We want to keep "Project A Phase 2".
    # With matches sorted by index, we might have multiple matches at same index.
    # We should pick the longest one at that index.
    
    cleaned_matches = []
    if matches:
        # Group by start index
        from itertools import groupby
        for start_idx, group in groupby(matches, key=lambda x: x[0]):
            # Pick longest name at this index
            best_match = max(group, key=lambda x: len(x[1]))
            cleaned_matches.append(best_match)
            
    # Now filter out matches that are contained within previous matches (if any)
    # e.g. "Project A Phase 2" at 10 (len 17) covers 10-27.
    # "Phase 2" at 20 (len 7) covers 20-27.
    # We should remove "Phase 2".
    
    final_matches = []
    last_end = -1
    for start, name in cleaned_matches:
        end = start + len(name)
        if start >= last_end:
            final_matches.append((start, name))
            last_end = end
        # Else: this match is inside the previous one, skip
        
    # Now extract text segments
    for i in range(len(final_matches)):
        start, name = final_matches[i]
        if i < len(final_matches) - 1:
            next_start = final_matches[i+1][0]
            segment = text[start:next_start]
        else:
            segment = text[start:]
            
        # Check for start date in segment
        # We look for the pattern.
        # Check if the date is preceded by "Begin Construction" etc.
        # We can look for lines containing both.
        
        # Split segment into lines to avoid cross-line false positives (though some formatting might span lines)
        # But usually "Begin Construction: Spring 2022" is on one line or adjacent.
        
        # Let's search for the pattern with a window
        # re.search(f"{start_context}.{{0,50}}{date_pattern}", segment, re.IGNORECASE | re.DOTALL)
        
        # Refined regex:
        # Look for "Begin Construction" followed by date within reasonable distance
        regex = re.compile(f"({start_context}).{{0,100}}?({date_pattern})", re.IGNORECASE | re.DOTALL)
        
        match = regex.search(segment)
        if match:
            # Found a start date matching Spring 2022
            # Check if it's not "Complete Design" (which shouldn't match start_context)
            # The start_context includes "Schedule", which is broad.
            # If "Schedule" matches, we must ensure "Begin Construction" is the line.
            # Text: "Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n(cid:131) Begin Construction: Fall 2023"
            # If we match "Project Schedule" and then "Spring 2022", it might be "Complete Design: Spring 2022".
            # This is risky.
            
            # Let's be more specific.
            # Find the date. Check the immediate prefix (last 30 chars).
            # "Begin Construction: Spring 2022" -> Prefix "Begin Construction: "
            # "Complete Design: Spring 2022" -> Prefix "Complete Design: "
            
            # Find all date matches
            date_matches = list(re.finditer(date_pattern, segment, re.IGNORECASE))
            for dm in date_matches:
                d_start = dm.start()
                # Look at text before d_start
                prefix = segment[max(0, d_start - 50):d_start]
                # Check if prefix contains "Begin Construction", "Start", etc.
                # And DOES NOT contain "Complete Design", "Advertise", "End", "Completion".
                
                if re.search(r"(Begin Construction|Construction Start|Commence|Start Date)", prefix, re.IGNORECASE):
                    # It's a start!
                    started_projects.add(name)
                    break # Found for this project
                elif re.search(r"(Complete Design|Final Design|Advertise|Bid|Completion|End)", prefix, re.IGNORECASE):
                    # Explicitly NOT start
                    continue
                else:
                    # Ambiguous. "Project Schedule: Spring 2022"?
                    # Maybe check if segment has "Status: ... Started Spring 2022"
                    pass

print("__RESULT__:")
print(json.dumps(list(started_projects)))"""

env_args = {'var_function-call-18189666317777669424': 'file_storage/function-call-18189666317777669424.json', 'var_function-call-18189666317777667959': 'file_storage/function-call-18189666317777667959.json', 'var_function-call-9598999800864405820': 'file_storage/function-call-9598999800864405820.json'}

exec(code, env_args)
