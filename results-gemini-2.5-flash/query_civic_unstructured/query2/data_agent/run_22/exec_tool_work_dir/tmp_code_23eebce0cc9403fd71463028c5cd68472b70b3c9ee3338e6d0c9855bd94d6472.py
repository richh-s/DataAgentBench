code = """import json
import re

with open(locals()['var_function-call-9062427216708247704'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = set() # Use a set to automatically handle duplicates

for doc in civic_docs:
    text = doc['text']
    
    # Iterate through each line to find potential project names
    # Project names are usually capitalized and at the beginning of a line
    lines = text.split('\n')
    for i, line in enumerate(lines):
        project_name_match = re.match(r'^([A-Z][a-zA-Z0-9\s&,-]+?)(?:$|\\s+\(cid:190\)|\\s+Updates:|\\s+Project Schedule:|\\s+Estimated Schedule:|\\s+Project Description:)', line)
        
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            
            is_park_related = False
            if "park" in project_name.lower() or "playground" in project_name.lower():
                is_park_related = True
            
            # Now, check for completion in 2022 in the following lines
            # Look within a window of a few lines after the project name
            completion_found = False
            for j in range(i + 1, min(i + 10, len(lines))): # Check next 9 lines
                subsequent_line = lines[j]
                if re.search(r'(?:completed|Complete Construction|Construction was completed).*?2022', subsequent_line, re.IGNORECASE):
                    completion_found = True
                    break
            
            # Also check if 'Project Description' in the following lines contains park/playground for topic match
            if not is_park_related:
                for j in range(i + 1, min(i + 5, len(lines))): # Check next 4 lines for description
                    subsequent_line = lines[j]
                    if re.search(r'Project Description:.*?\b(park|playground)\b', subsequent_line, re.IGNORECASE):
                        is_park_related = True
                        break
            
            if is_park_related and completion_found:
                park_projects_2022_completed.add(project_name)

# Special handling for "Bluffs Park Shade Structure" as it's explicitly mentioned and fits criteria.
# It might be missed by generic line-by-line parsing if the structure is very specific.
if re.search(r'Bluffs Park Shade Structure.*?Construction was completed November 2022', text, re.IGNORECASE | re.DOTALL):
    park_projects_2022_completed.add("Bluffs Park Shade Structure")

print('__RESULT__:')
print(json.dumps(list(park_projects_2022_completed)))"""

env_args = {'var_function-call-8345135393552967239': ['civic_docs'], 'var_function-call-9062427216708247704': 'file_storage/function-call-9062427216708247704.json', 'var_function-call-6977964406746342709': [], 'var_function-call-12672395966706885709': ['Funding']}

exec(code, env_args)
