code = """import json
import re

# Load funding data
funding_path = locals()['var_function-call-61089627249181938']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs
docs_path = locals()['var_function-call-61089627249180915']
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Create a map of project names to amounts and a list of names for searching
funding_map = {item['Project_Name']: item['Amount'] for item in funding_data}
project_names = list(funding_map.keys())

# Sort project names by length descending to match longest first (avoid partial matching issues)
project_names.sort(key=len, reverse=True)

relevant_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    # Find all project occurrences
    # We store (start_index, project_name)
    occurrences = []
    for name in project_names:
        # Simple case-insensitive search or exact? The sample matches exact casing mostly.
        # But let's be safe with case-insensitive, then map back to original name.
        # Regex escaping name is important.
        pattern = re.compile(re.escape(name), re.IGNORECASE)
        for match in pattern.finditer(text):
            occurrences.append((match.start(), name))
    
    # Sort by position
    occurrences.sort(key=lambda x: x[0])
    
    # Process each segment
    for i in range(len(occurrences)):
        start_idx, name = occurrences[i]
        # End index is start of next project or end of text
        end_idx = occurrences[i+1][0] if i + 1 < len(occurrences) else len(text)
        
        # Limit the segment length to avoid capturing too much garbage if next project is far
        # But documents seem dense. Let's stick to next project.
        segment = text[start_idx:end_idx]
        
        # Check criteria
        lower_segment = segment.lower()
        lower_name = name.lower()
        
        # 1. Park-related
        # Topic keywords: "park"
        is_park = "park" in lower_name or "park" in lower_segment
        
        # 2. Completed in 2022
        # Patterns to look for in the segment
        # - "completed ... 2022"
        # - "complete construction ... 2022"
        # - "status: completed" check dates?
        # The prompt says: "completed" (finished). 
        # And "Dates (st, et fields) use flexible formats... 2022-Spring... Use substring matching... for year-based queries"
        
        is_completed_2022 = False
        
        # Check for completion keywords
        if "completed" in lower_segment or "complete construction" in lower_segment or "notice of completion" in lower_segment:
             # Check for 2022 in the segment
             # We should look for "completed" and "2022" appearing close to each other or in a specific phrase.
             # Simple heuristic: if "completed" and "2022" are both present, likely matches.
             # But "Completed design 2022" is NOT completed project.
             # Must distinguish between "Complete Design" and "Complete Construction" or just "Completed".
             
             # Let's look for specific completion indicators
             # "Construction was completed November 2022"
             # "Complete Construction: ... 2022"
             # "Notice of completion filed ... 2022" (This implies completion)
             # "Status: completed"
             
             # Avoid "Complete Design: ... 2022"
             
             # Lines analysis
             lines = segment.split('\n')
             for line in lines:
                 l_line = line.lower()
                 if "2022" in l_line:
                     if "design" in l_line and "complete" in l_line:
                         # Likely "Complete Design: Summer 2022", not project completion
                         continue
                     
                     if "construction" in l_line and ("complete" in l_line or "completed" in l_line):
                         # "Complete Construction: Summer 2022"
                         # "Construction was completed November 2022"
                         is_completed_2022 = True
                         break
                     
                     if "completed" in l_line and "construction" not in l_line and "design" not in l_line:
                         # "Project completed March 2022"
                         is_completed_2022 = True
                         break
                     
                     if "notice of completion" in l_line:
                         # "Notice of completion filed January 2022"
                         is_completed_2022 = True
                         break

        if is_park and is_completed_2022:
            relevant_projects.add(name)

# Calculate total
total_funding = 0
found_details = []
for name in relevant_projects:
    amount = int(funding_map[name])
    total_funding += amount
    found_details.append({"name": name, "amount": amount})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": found_details}))"""

env_args = {'var_function-call-11325768186704868544': ['Funding'], 'var_function-call-11325768186704870109': ['civic_docs'], 'var_function-call-61089627249181938': 'file_storage/function-call-61089627249181938.json', 'var_function-call-61089627249180915': 'file_storage/function-call-61089627249180915.json'}

exec(code, env_args)
