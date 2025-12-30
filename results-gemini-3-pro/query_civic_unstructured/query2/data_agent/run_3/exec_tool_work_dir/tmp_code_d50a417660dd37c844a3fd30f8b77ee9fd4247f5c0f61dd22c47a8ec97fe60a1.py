code = """import json
import re

# Load data
with open(locals()['var_function-call-13030964589425590204'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-16179877025922844511'], 'r') as f:
    civic_docs = json.load(f)

# Create funding map
funding_map = {item['Project_Name']: item['Amount'] for item in funding_data}
project_names = list(funding_map.keys())

# Sort project names by length descending to match longest names first (greedy match)
project_names.sort(key=len, reverse=True)

processed_projects = set()
matches = []

for doc in civic_docs:
    text = doc['text']
    
    # Find all project occurrences
    # We store (index, name)
    occurrences = []
    for name in project_names:
        # Escape special regex chars in name just in case, though names look clean
        escaped_name = re.escape(name)
        for m in re.finditer(escaped_name, text, re.IGNORECASE):
            occurrences.append((m.start(), name))
            
    # Sort by position
    occurrences.sort(key=lambda x: x[0])
    
    # Filter overlapping occurrences (due to sub-matches)
    # Since we sorted names by length descending, if we have "Project A" and "Project A Phase 2",
    # "Project A Phase 2" would be found. But "Project A" would also be found at the same index.
    # We should keep the longest match at a given position.
    
    clean_occurrences = []
    if occurrences:
        curr_start, curr_name = occurrences[0]
        curr_end = curr_start + len(curr_name)
        clean_occurrences.append((curr_start, curr_name))
        
        for i in range(1, len(occurrences)):
            start, name = occurrences[i]
            end = start + len(name)
            
            # If this occurrence starts inside the previous one, skip (it's a substring match)
            if start < curr_end:
                continue
            
            clean_occurrences.append((start, name))
            curr_start, curr_name = start, name
            curr_end = end
            
    # Now analyze chunks
    for i in range(len(clean_occurrences)):
        start_idx, name = clean_occurrences[i]
        
        # Determine end of chunk
        if i < len(clean_occurrences) - 1:
            end_idx = clean_occurrences[i+1][0]
        else:
            end_idx = len(text)
            
        chunk = text[start_idx:end_idx]
        
        # Check Park-related
        # Topic keyword "park" in name or chunk text
        is_park = False
        if "park" in name.lower() or "park" in chunk.lower():
            is_park = True
            
        # Check Status Completed in 2022
        # Look for patterns
        is_completed_2022 = False
        
        # Regex for completion
        # "Construction was completed[,] [Month] [Year]"
        # "Complete Construction[:] [Month] [Year]"
        # "Completed[:] [Month] [Year]"
        
        # Simplify: find dates near "completed" or "complete"
        # We look for "2022" and ensuring it's associated with completion
        
        # Pattern 1: Explicit "Completed ... 2022"
        # Allow small window of chars between 'completed' and '2022'
        
        # Extract all year mentions in the chunk
        # If "2022" appears, check context.
        
        # Better approach: Extract sentences or lines containing "complete" or "status: completed"
        lines = chunk.split('\n')
        for line in lines:
            line_lower = line.lower()
            if "complete" in line_lower:
                # Check year
                if "2022" in line_lower:
                    # Check if it says "completed" (past tense) or "complete construction: ... 2022"
                    # In the sample: "Construction was completed November 2022" -> Valid
                    # "Complete Construction: Fall 2023" -> Invalid
                    # "Complete Design: Summer 2022" -> This is NOT construction completion.
                    
                    # We need to distinguish between "Design" and "Construction" completion if specified.
                    # Or just "Project Status: Completed"
                    
                    # If "Design" is in the line, ignore? 
                    # Prompt asks for "projects that were completed". Usually implies construction.
                    # Sample: "Capital Improvement Projects (Design)" header.
                    
                    if "design" in line_lower:
                        continue
                        
                    is_completed_2022 = True
                    break
        
        if is_park and is_completed_2022:
            if name not in processed_projects:
                processed_projects.add(name)
                matches.append({
                    "name": name,
                    "funding": funding_map.get(name, 0)
                })

total_funding = sum(m['funding'] for m in matches)
result = {
    "total_funding": total_funding,
    "matches": matches
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-13030964589425589265': 'file_storage/function-call-13030964589425589265.json', 'var_function-call-13030964589425590204': 'file_storage/function-call-13030964589425590204.json', 'var_function-call-16179877025922844511': 'file_storage/function-call-16179877025922844511.json'}

exec(code, env_args)
