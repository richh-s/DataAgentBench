code = """import json
import re

with open(locals()['var_function-call-9062427216708247704'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

for doc in civic_docs:
    text = doc['text']
    
    # A more robust pattern to identify project blocks.
    # Projects usually start with a capitalized name followed by an update/schedule indicator or description.
    # Using re.DOTALL to allow '.' to match newlines.
    project_blocks = re.findall(r'([A-Z][a-zA-Z0-9\\s&,-]+?)(?:\\n\\(cid:190\\) Updates:|\\n\\(cid:190\\) Project Schedule:|\\n\\(cid:190\\) Estimated Schedule:|\\n\\(cid:190\\) Project Description:)(.*?)(?=(?:\\n[A-Z][a-zA-Z0-9\\s&,-]+?)(?:\\n\\(cid:190\\) Updates:|\\n\\(cid:190\\) Project Schedule:|\\n\\(cid:190\\) Estimated Schedule:|\\n\\(cid:190\\) Project Description:)|\\Z))', text, re.DOTALL)
    
    for project_name, details_block in project_blocks:
        project_name = project_name.strip()
        details_block = details_block.strip()
        
        is_park_related = False
        if "park" in project_name.lower() or "playground" in project_name.lower():
            is_park_related = True
        elif re.search(r'Project Description:.*?\\b(park|playground)\\b', details_block, re.IGNORECASE):
            is_park_related = True

        is_completed_2022 = False
        if is_park_related:
            # Check for completion in 2022 within the details_block
            if re.search(r'(?:completed.*?2022|Complete Construction:.*?2022|Construction was completed,.*?2022)', details_block, re.IGNORECASE):
                is_completed_2022 = True
        
        if is_park_related and is_completed_2022:
            park_projects_2022_completed.append(project_name)

# Specific projects from the text that were completed in 2022 and are park-related
# Bluffs Park Shade Structure: Construction was completed November 2022.
if re.search(r'Bluffs Park Shade Structure.*?Construction was completed November 2022', text, re.IGNORECASE | re.DOTALL):
    if "Bluffs Park Shade Structure" not in park_projects_2022_completed:
        park_projects_2022_completed.append("Bluffs Park Shade Structure")


# Point Dume Walkway Repairs: Construction was completed, November 2022
# This is not directly park-related, so it should not be included.

# Remove duplicates
park_projects_2022_completed = list(set(park_projects_2022_completed))

print('__RESULT__:')
print(json.dumps(park_projects_2022_completed))"""

env_args = {'var_function-call-8345135393552967239': ['civic_docs'], 'var_function-call-9062427216708247704': 'file_storage/function-call-9062427216708247704.json', 'var_function-call-6977964406746342709': [], 'var_function-call-12672395966706885709': ['Funding']}

exec(code, env_args)
