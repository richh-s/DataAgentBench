code = """import json

# Load data
with open(locals()['var_function-call-990771525359343970'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-990771525359343617'], 'r') as f:
    funding_data = json.load(f)

project_names = [item['Project_Name'] for item in funding_data]
# Sort by length descending to handle substrings
project_names.sort(key=len, reverse=True)

project_funding = {item['Project_Name']: int(item['Amount']) for item in funding_data}

qualifying_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    # Identify project sections
    # We find all start positions of all projects
    starts = []
    for pname in project_names:
        idx = text.find(pname)
        while idx != -1:
            starts.append((idx, pname))
            idx = text.find(pname, idx + 1)
    
    starts.sort()
    
    # Filter overlaps
    # If we have (10, "Long Name") and (10, "Long"), we keep "Long Name".
    # Since we sort by length desc initially, finding "Long Name" first is not guaranteed in `starts` list (which is sorted by index).
    # But for same index, we want the longest one.
    
    clean_starts = []
    i = 0
    while i < len(starts):
        current = starts[i]
        # Check if there are other starts at the same index or overlapping
        # Since we just want to process the text, it's fine if we process "Long" and "Long Name" separately, 
        # but "Long" text would be a subset of "Long Name" text usually, or vice versa.
        # Let's just define the segment from current start to next start.
        
        # To avoid processing a substring project name inside another, we can skip if start index is within previous range.
        # But here we just take the list and process.
        
        # Let's determine the end of this section
        start_idx = current[0]
        pname = current[1]
        
        # Find next start index
        next_idx = len(text)
        for j in range(i + 1, len(starts)):
            if starts[j][0] > start_idx + len(pname): # Must be after the current project name
                next_idx = starts[j][0]
                break
        
        segment = text[start_idx:next_idx]
        
        # Analyze segment
        segment_lower = segment.lower()
        
        # 1. Check Topic: "park"
        is_park = "park" in pname.lower() or "park" in segment_lower
        
        if is_park:
            # 2. Check Status/Date: Completed in 2022
            # Check lines
            lines = segment.split('\n')
            for line in lines:
                line_lower = line.lower()
                if "2022" in line_lower:
                    # Check for completion indicators
                    # "Construction was completed"
                    # "Complete Construction"
                    # "Status: Completed"
                    
                    # Exclude "design"
                    if "design" in line_lower:
                        continue
                        
                    if "complete" in line_lower and "construction" in line_lower:
                        qualifying_projects.add(pname)
                    elif "completed" in line_lower and ("was" in line_lower or "is" in line_lower): # "was completed"
                        qualifying_projects.add(pname)
                    # Handle "Construction was completed, November 2022"
        
        i += 1

total_funding = sum(project_funding[p] for p in qualifying_projects)

print("__RESULT__:")
print(json.dumps({
    "qualifying_projects": list(qualifying_projects),
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-990771525359343970': 'file_storage/function-call-990771525359343970.json', 'var_function-call-990771525359343617': 'file_storage/function-call-990771525359343617.json'}

exec(code, env_args)
