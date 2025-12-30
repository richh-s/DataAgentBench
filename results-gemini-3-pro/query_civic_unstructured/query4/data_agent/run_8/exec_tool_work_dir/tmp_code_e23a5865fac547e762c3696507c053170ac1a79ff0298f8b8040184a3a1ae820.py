code = """import json
import re

# Load data
with open(locals()['var_function-call-18089333164037500904'], 'r') as f:
    docs = json.load(f)
    
with open(locals()['var_function-call-7145739676015495870'], 'r') as f:
    funding_data = json.load(f)

known_projects = set(item['Project_Name'] for item in funding_data)

# Sort projects by length descending to match longest names first (if names are substrings of each other)
sorted_projects = sorted(list(known_projects), key=len, reverse=True)

matching_projects = set()

for doc in docs:
    text = doc['text']
    # Normalize text slightly? No, keep it raw.
    
    # Find positions of all known projects
    # We want to find which project a section of text belongs to.
    # We can search for all occurrences of all project names.
    # But this is slow if many projects. 
    # Optimization: Use regex with alternation, but escape special chars.
    
    # Create a giant regex? might be too big.
    # Let's iterate.
    
    project_indices = []
    for proj in sorted_projects:
        # Simple string find can be ambiguous if one name is suffix of another.
        # But we sorted by length descending, so we should be okay if we handle overlaps?
        # Actually, finding all start indices is enough.
        
        # Use simple string search (case insensitive?)
        # Titles usually match case, but let's be safe with re.IGNORECASE if needed.
        # But specific capitalization in DB might match text.
        
        # Let's assume exact match first.
        start = 0
        while True:
            idx = text.find(proj, start)
            if idx == -1:
                break
            project_indices.append((idx, proj))
            start = idx + len(proj)
            
    # Sort by index
    project_indices.sort()
    
    # Filter out overlaps? (e.g. "Project A" and "Project A Phase 2")
    # If we sorted by length descending and found "Project A Phase 2" first, we might also find "Project A" at the same index.
    # We should keep the longer one.
    
    final_indices = []
    if project_indices:
        curr = project_indices[0]
        final_indices.append(curr)
        for next_proj in project_indices[1:]:
            prev_start, prev_name = final_indices[-1]
            prev_end = prev_start + len(prev_name)
            
            next_start, next_name = next_proj
            
            if next_start < prev_end:
                # Overlap. Since we sorted project_indices by start index, and earlier we searched long to short?
                # Wait, "sorted_projects" was long to short. 
                # But "project_indices" was collected then sorted by index.
                # If "Project A Phase 2" is at 100, and "Project A" is at 100.
                # Sort is stable? Or secondary sort key?
                # We should prefer longer name.
                if len(next_name) > len(prev_name):
                     final_indices.pop()
                     final_indices.append(next_proj)
                # Else ignore the shorter/substring one
            else:
                final_indices.append(next_proj)
                
    # Now iterate through blocks
    for i in range(len(final_indices)):
        start_idx, proj_name = final_indices[i]
        
        # End of this block is start of next or end of text
        if i + 1 < len(final_indices):
            end_idx = final_indices[i+1][0]
        else:
            end_idx = len(text)
            
        block = text[start_idx:end_idx]
        
        # Analyze block for start date
        # Look for "Spring 2022", "March 2022", "April 2022", "May 2022"
        # AND context implies Start
        
        # Simplify: If the block mentions "Begin Construction: ... Spring 2022"
        # or "Start Date: ... Spring 2022"
        
        # Regex for Start line
        # Capture the line containing "Begin Construction" or "Start"
        
        lines = block.splitlines()
        found_start = False
        for line in lines:
            if "Begin Construction" in line or "Start Date" in line or "beginning in" in line:
                # Check for date match
                lower_line = line.lower()
                if "2022" in lower_line:
                    if "spring" in lower_line or "march" in lower_line or "april" in lower_line or "may" in lower_line:
                        # Double check it's not "Spring 2023" (which wouldn't match "2022" logic if exact)
                        # But "March 2022" is clear.
                        # "Spring 2022" is clear.
                        matching_projects.add(proj_name)
                        found_start = True
                        break
        
print("__RESULT__:")
print(json.dumps(list(matching_projects)))"""

env_args = {'var_function-call-6715434972998628537': 'file_storage/function-call-6715434972998628537.json', 'var_function-call-18089333164037500904': 'file_storage/function-call-18089333164037500904.json', 'var_function-call-5763327326687142161': ['PCH Signal Synchronization System Improvements Project', 'sending this project out to bid during the Spring of 2022.', 'scheduled for the April 11, 2022 Council meeting.', 'beginning in Spring 2022.', 'agreement will be sent to City Council in March.', '(cid:131) Next public community meeting is scheduled for March 25th.', 'timber with non-combustible materials.', 'that was damaged by the Woolsey Fire.', 'beginning in April 2022.', '(cid:131) The project consultant has started the design of this project.', 'is finalizing the bid documents.', 'assessment district will be created.', 'Fire.', 'advertised for construction bids shortly after this date.'], 'var_function-call-7145739676015495870': 'file_storage/function-call-7145739676015495870.json'}

exec(code, env_args)
