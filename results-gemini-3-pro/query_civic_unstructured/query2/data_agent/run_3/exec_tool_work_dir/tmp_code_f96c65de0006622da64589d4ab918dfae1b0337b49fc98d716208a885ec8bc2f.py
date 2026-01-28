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
project_names.sort(key=len, reverse=True)

processed_projects = set()
matches = []

for doc in civic_docs:
    text = doc['text']
    
    # Find occurrences
    occurrences = []
    for name in project_names:
        escaped_name = re.escape(name)
        for m in re.finditer(escaped_name, text, re.IGNORECASE):
            occurrences.append((m.start(), name))
            
    occurrences.sort(key=lambda x: x[0])
    
    clean_occurrences = []
    if occurrences:
        curr_start, curr_name = occurrences[0]
        curr_end = curr_start + len(curr_name)
        clean_occurrences.append((curr_start, curr_name))
        
        for i in range(1, len(occurrences)):
            start, name = occurrences[i]
            end = start + len(name)
            if start < curr_end:
                continue
            clean_occurrences.append((start, name))
            curr_start, curr_name = start, name
            curr_end = end
            
    for i in range(len(clean_occurrences)):
        start_idx, name = clean_occurrences[i]
        if i < len(clean_occurrences) - 1:
            end_idx = clean_occurrences[i+1][0]
        else:
            end_idx = len(text)
            
        chunk = text[start_idx:end_idx]
        
        # Check Park
        if "park" not in name.lower() and "park" not in chunk.lower():
            continue
            
        # Check Completion 2022
        # We look for "completed" or "completion" and "2022" in the same line or close context
        # And ensure it is NOT "design" completion if "construction" is not mentioned
        
        is_completed_2022 = False
        lines = chunk.split('\n')
        for line in lines:
            line_lower = line.lower()
            
            # Check for completion keywords
            if "complete" in line_lower or "completion" in line_lower:
                # Check for 2022
                if "2022" in line_lower:
                    # Check against "design"
                    if "design" in line_lower:
                        # "Complete Design: Summer 2022" -> skip
                        # But what if "Design completed 2021, Construction completed 2022"?
                        # If the line has both, we might be confused.
                        # Usually they are separate lines.
                        pass
                    else:
                        # Check for negative context? "Not complete"? 
                        # "Notice of completion filed ... 2023" for a 2022 completion?
                        # Sample: "Construction was completed November 2022. Notice of completion filed January 2023"
                        # The line "Construction was completed November 2022" matches.
                        
                        # Another case: "Complete Construction: Summer 2022" -> Matches.
                        # "Construction was completed, November 2022" -> Matches.
                        
                        is_completed_2022 = True
                        break
        
        if is_completed_2022:
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
