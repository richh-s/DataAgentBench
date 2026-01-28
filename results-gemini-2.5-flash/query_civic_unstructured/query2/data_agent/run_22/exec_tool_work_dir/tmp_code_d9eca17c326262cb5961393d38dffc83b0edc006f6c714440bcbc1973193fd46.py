code = """import json
import re

with open(locals()['var_function-call-9062427216708247704'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = set()

for doc in civic_docs:
    text = doc['text']
    
    # Iterate through each line to find potential project names
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        # A project name is typically a capitalized phrase at the start of a line
        # followed by an optional indicator or end of line.
        project_name_match = re.match(r'([A-Z][a-zA-Z0-9\\s&,-]+?)(?:$|\\s+\\(cid:190\\)|\\s+Updates:|\\s+Project Schedule:|\\s+Estimated Schedule:|\\s+Project Description:)', line)
        
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            
            # Extract a block of text following the project name to check for details
            details_block_lines = lines[i+1 : i+1+10] # Look up to 10 lines after the project name
            details_block = '\n'.join(details_block_lines)
            
            is_park_related = False
            if "park" in project_name.lower() or "playground" in project_name.lower():
                is_park_related = True
            elif re.search(r'Project Description:.*?\\b(park|playground)\\b', details_block, re.IGNORECASE):
                is_park_related = True

            is_completed_2022 = False
            if is_park_related:
                # Check for completion in 2022 within the details block
                if re.search(r'(?:completed.*?2022|Complete Construction:\\s*(?:Spring|Summer|Fall|Winter|[A-Za-z]+)?\\s*2022|Construction was completed,\\s*(?:Spring|Summer|Fall|Winter|[A-Za-z]+)?\\s*2022)', details_block, re.IGNORECASE):
                    is_completed_2022 = True
            
            if is_park_related and is_completed_2022:
                park_projects_2022_completed.add(project_name)

# Explicitly add "Bluffs Park Shade Structure" as it is clearly completed in November 2022 and park-related.
# This handles cases where the general regex might miss specific phrasing.
if re.search(r'Bluffs Park Shade Structure.*?Construction was completed November 2022', text, re.IGNORECASE | re.DOTALL):
    park_projects_2022_completed.add("Bluffs Park Shade Structure")

print('__RESULT__:')
print(json.dumps(list(park_projects_2022_completed)))"""

env_args = {'var_function-call-8345135393552967239': ['civic_docs'], 'var_function-call-9062427216708247704': 'file_storage/function-call-9062427216708247704.json', 'var_function-call-6977964406746342709': [], 'var_function-call-12672395966706885709': ['Funding']}

exec(code, env_args)
