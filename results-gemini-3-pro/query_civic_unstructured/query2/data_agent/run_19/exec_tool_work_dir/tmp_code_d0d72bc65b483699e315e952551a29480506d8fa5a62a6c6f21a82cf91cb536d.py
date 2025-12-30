code = """import json
import re

# Load data
with open(locals()['var_function-call-990771525359343970'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-990771525359343617'], 'r') as f:
    funding_data = json.load(f)

# Create a list of project names from funding data
# Sort by length descending to match longer names first (avoid partial matches if names are substrings)
project_names = [item['Project_Name'] for item in funding_data]
project_names.sort(key=len, reverse=True)

# Map project names to funding amounts
project_funding = {item['Project_Name']: int(item['Amount']) for item in funding_data}

qualifying_projects = set()

# Process each document
for doc in civic_docs:
    text = doc['text']
    
    # Find all project occurrences in the text
    # We'll store (start_index, project_name)
    project_hits = []
    for pname in project_names:
        # Simple string search; might need regex for exact phrases if simple search is too noisy
        # But given the specific format "Project Name\n...", exact substring search is probably okay.
        # We start searching from 0.
        start = 0
        while True:
            idx = text.find(pname, start)
            if idx == -1:
                break
            project_hits.append((idx, pname))
            start = idx + len(pname)
    
    # Sort hits by index
    project_hits.sort(key=lambda x: x[0])
    
    # Filter overlapping hits (keep the longest match which we sorted first if starting at same pos, 
    # but here we just sorted by position. If we have "Project A" and "Project A Extended" at same pos,
    # we want "Project A Extended".
    # Since we sorted project_names by length desc, if "Project A Extended" is found, "Project A" will also be found at same index.
    # We should keep the one that spans furthest.
    
    cleaned_hits = []
    if project_hits:
        curr_start, curr_name = project_hits[0]
        curr_end = curr_start + len(curr_name)
        
        for i in range(1, len(project_hits)):
            next_start, next_name = project_hits[i]
            # If next match starts within current match
            if next_start < curr_end:
                # If next match ends after current match, take it (longer)
                if next_start + len(next_name) > curr_end:
                    curr_name = next_name
                    curr_start = next_start
                    curr_end = next_start + len(next_name)
                # Else ignore (it's a substring)
            else:
                # Non-overlapping, add current and start new
                cleaned_hits.append((curr_start, curr_name))
                curr_start = next_start
                curr_name = next_name
                curr_end = next_start + len(next_name)
        cleaned_hits.append((curr_start, curr_name))
    
    # Extract segments
    for i in range(len(cleaned_hits)):
        pname = cleaned_hits[i][1]
        start_idx = cleaned_hits[i][0]
        # End index is start of next project or end of text
        end_idx = cleaned_hits[i+1][0] if i + 1 < len(cleaned_hits) else len(text)
        
        segment = text[start_idx:end_idx]
        
        # Lowercase for analysis
        segment_lower = segment.lower()
        
        # Check topic: "park"
        # The prompt says topic field contains keywords. 
        # But here I'm checking if the project is park-related.
        # Check in project name or segment text
        is_park = "park" in pname.lower() or "park" in segment_lower
        
        if not is_park:
            continue
            
        # Check completion in 2022
        # Look for patterns indicating completion
        # Examples: 
        # "Complete Construction: November 2022"
        # "Construction was completed November 2022"
        # "completed in 2022"
        
        # Let's use regex to find dates associated with "complete"
        # Search for "complete" followed by something and then "2022"
        # Be careful not to match "Complete Design: 2022" if we want construction completion.
        # The prompt asks for "projects that were completed in 2022". Usually means construction completed.
        # But "completed" status is general.
        # Let's look for "status: completed" or "construction ... completed" or "complete construction"
        
        # Pattern 1: "Complete Construction: <...2022...>"
        # Pattern 2: "Construction was completed <...2022...>"
        # Pattern 3: "Construction completed <...2022...>"
        
        # Let's try to match "2022" in the same line or context as "completed" or "complete construction"
        
        # Split segment into lines to be safer?
        lines = segment.split('\n')
        completed_2022 = False
        
        for line in lines:
            line_lower = line.lower()
            if "2022" in line_lower:
                # Check for completion keywords
                if "complete construction" in line_lower:
                    completed_2022 = True
                elif "construction" in line_lower and "completed" in line_lower:
                    completed_2022 = True
                elif "status" in line_lower and "completed" in line_lower:
                    completed_2022 = True
                # Case from example: "Construction was completed, November 2022"
        
        # Also check just general "completed" near "2022" if specific phrases miss
        # But be careful of "Complete Design: 2022"
        
        if completed_2022:
            qualifying_projects.add(pname)

# Calculate total funding
total_funding = sum(project_funding[pname] for pname in qualifying_projects)

print("__RESULT__:")
print(json.dumps({
    "qualifying_projects": list(qualifying_projects),
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-990771525359343970': 'file_storage/function-call-990771525359343970.json', 'var_function-call-990771525359343617': 'file_storage/function-call-990771525359343617.json'}

exec(code, env_args)
