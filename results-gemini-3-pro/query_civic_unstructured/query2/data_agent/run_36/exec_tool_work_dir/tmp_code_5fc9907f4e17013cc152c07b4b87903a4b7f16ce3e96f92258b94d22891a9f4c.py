code = """import json
import re

# Load data
with open(locals()['var_function-call-105374427897259333'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-105374427897260990'], 'r') as f:
    civic_docs = json.load(f)

# Create a map of Project Name to Amount
project_amounts = {}
for row in funding_data:
    project_amounts[row['Project_Name']] = row['Amount']

project_names = list(project_amounts.keys())
# Sort project names by length descending to match longest first (to avoid partial matches like "Project A" inside "Project A Phase 2")
project_names.sort(key=len, reverse=True)

matched_projects = set()

# Debugging list
debug_info = []

for doc in civic_docs:
    text = doc['text']
    
    # Find all project occurrences
    # We'll store (start_index, project_name)
    occurrences = []
    
    # Use simple find since regex might be slow with many patterns or complex
    # But we need to be careful about overlapping matches. 
    # Since we sorted by length, we can try to find them. 
    # Actually, scanning the text once is better. 
    # Or just iterating names. Given the document size (preview 10k chars, likely not huge), iterating names is fine.
    
    # We want to find locations of project names to segment the text.
    # To handle overlapping or repeated names, let's just find all start indices for all names.
    # But checking 100+ names against text is cheap.
    
    found_indices = []
    for p_name in project_names:
        # Case insensitive search? The names in funding seems Title Case. Text seems Title Case. 
        # Let's do case insensitive to be safe.
        start = 0
        while True:
            idx = text.lower().find(p_name.lower(), start)
            if idx == -1:
                break
            found_indices.append((idx, p_name))
            start = idx + len(p_name)
            
    # Sort by index
    found_indices.sort(key=lambda x: x[0])
    
    # Filter overlaps? 
    # If "Bluffs Park" and "Bluffs Park Shade Structure" both match at same index, keep longer one.
    # Since we scan for all, if "Bluffs Park Shade Structure" is at 100, "Bluffs Park" is also at 100.
    # We should keep the one that spans further.
    
    clean_indices = []
    if found_indices:
        current_idx = -1
        current_end = -1
        
        # This overlap logic is tricky. 
        # Let's simple strategy: if a new match starts before the previous one ends, skip it?
        # But we must prefer the longer one.
        # found_indices might have (100, "Bluffs Park"), (100, "Bluffs Park Shade Structure").
        # If we iterate, we see "Bluffs Park". We accept it. Then "Bluffs Park Shade Structure" starts at 100.
        # We need to pick the best one covering that spot.
        # Since we want to segment, the headers are what matters.
        # Let's assume the headers are the full project names.
        
        # Better approach: 
        # For each found match, calculate end index.
        # If multiple matches start at same position, pick longest.
        # If a match starts inside another, ignore it? (Likely substring match).
        
        # Group by start index
        by_start = {}
        for idx, name in found_indices:
            if idx not in by_start:
                by_start[idx] = []
            by_start[idx].append(name)
            
        sorted_starts = sorted(by_start.keys())
        
        final_segments = []
        last_end = -1
        
        for start in sorted_starts:
            if start < last_end:
                continue
            
            # Pick longest name at this start
            names = by_start[start]
            longest_name = max(names, key=len)
            end = start + len(longest_name)
            
            final_segments.append((start, longest_name))
            last_end = end
            
        # Now we have non-overlapping project occurrences. 
        # Create segments.
        for i in range(len(final_segments)):
            idx, p_name = final_segments[i]
            # Segment goes until next project or reasonable limit
            if i + 1 < len(final_segments):
                next_idx = final_segments[i+1][0]
                segment_text = text[idx:next_idx]
            else:
                segment_text = text[idx:]
            
            # Analyze segment
            lower_seg = segment_text.lower()
            lower_name = p_name.lower()
            
            # Check Park Related
            # Topic keywords: park, playground
            is_park = False
            if "park" in lower_name or "playground" in lower_name:
                is_park = True
            elif "park" in lower_seg or "playground" in lower_seg:
                # Be careful, "parking" matches "park". 
                # Use regex for whole word?
                if re.search(r'\bpark\b', lower_seg) or re.search(r'\bplayground\b', lower_seg):
                    is_park = True
            
            # Check Completed in 2022
            # Look for "completed" and "2022"
            is_completed_2022 = False
            if "2022" in lower_seg:
                # Check for completion keywords
                # We want "construction (was) completed" or "completed ... 2022"
                # Exclude "design completed"
                
                # Split into lines to be more specific
                lines = segment_text.split('\n')
                for line in lines:
                    l_line = line.lower()
                    if "2022" in l_line:
                        if "completed" in l_line or "complete" in l_line:
                            # Check if it is design
                            if "design" in l_line:
                                # "Complete Design: Summer 2022" -> No
                                # "Design completed: 2022" -> No (status is completed design, not project)
                                pass
                            elif "construction" in l_line or "project" in l_line or "updates" in l_line or "status" in l_line:
                                # "Construction was completed November 2022" -> Yes
                                # "Updates: ... completed ... 2022" -> Yes
                                if "completed" in l_line or "completion" in l_line:
                                     is_completed_2022 = True
                            elif "construction was completed" in l_line: # fallback if construction not in line
                                is_completed_2022 = True
                            elif "notice of completion filed" in l_line:
                                # This might be 2023 for a 2022 completion. 
                                # But if the line says "Notice of completion filed ... 2022", it counts?
                                # Usually filed after.
                                pass
                            
                            # Specific check for pattern "Construction was completed, Month 2022"
                            if "construction was completed" in l_line and "2022" in l_line:
                                is_completed_2022 = True
            
            if is_park and is_completed_2022:
                matched_projects.add(p_name)
                debug_info.append({"project": p_name, "reason": "Matched Park & Completed 2022"})

# Calculate total
total_funding = 0
for p in matched_projects:
    # Amount is string in JSON?
    amt = project_amounts[p]
    total_funding += int(amt)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": list(matched_projects)}))"""

env_args = {'var_function-call-105374427897260990': 'file_storage/function-call-105374427897260990.json', 'var_function-call-105374427897259333': 'file_storage/function-call-105374427897259333.json'}

exec(code, env_args)
