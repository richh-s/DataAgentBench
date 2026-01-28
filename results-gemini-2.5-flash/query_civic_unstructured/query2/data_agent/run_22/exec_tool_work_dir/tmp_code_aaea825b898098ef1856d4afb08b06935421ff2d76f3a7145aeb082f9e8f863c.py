code = """import json
import re

with open(locals()['var_function-call-9062427216708247704'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

for doc in civic_docs:
    text = doc['text']
    
    # Split the document into sections based on project type headers.
    # This creates a list where alternating elements are headers and their content.
    sections = re.split(r'\n\n(Capital Improvement Projects \((?:Design|Construction|Not Started)\)|Disaster Recovery Projects \((?:Active|Completed)\))\n\n', text)
    
    # Iterate through the content sections (skipping the headers and initial preamble).
    for i in range(1, len(sections), 2):
        section_content = sections[i] if i < len(sections) else ''
        
        # Within each section_content, find individual project blocks.
        # A project block starts with a capitalized name on a new line and continues until the next capitalized name or end of section.
        project_blocks = re.findall(r'([A-Z][a-zA-Z0-9\s&,-]+?)\n(.*?)(?=\n[A-Z][a-zA-Z0-9\s&,-]+?|\Z)', section_content, re.DOTALL)
        
        for project_name, details_block in project_blocks:
            project_name = project_name.strip()
            details_block = details_block.strip()
            
            is_park_related = False
            if "park" in project_name.lower() or "playground" in project_name.lower():
                is_park_related = True
            elif re.search(r'Project Description:.*?\b(park|playground)\b', details_block, re.IGNORECASE):
                is_park_related = True

            is_completed_2022 = False
            if is_park_related:
                # Check for completion in 2022 within the details_block
                if re.search(r'(?:completed|Complete Construction|Construction was completed|Complete Construction:).*?2022', details_block, re.IGNORECASE):
                    is_completed_2022 = True
            
            if is_park_related and is_completed_2022:
                park_projects_2022_completed.append(project_name)

# Handle projects that might not be under a specific header (e.g., if the regex split misses them)
# This is a fallback and might duplicate if the primary split was partially successful.
# For now, stick to the structured split to avoid re-introducing previous errors.

# The Bluffs Park Shade Structure and Broad Beach Road Water Quality Repair are explicitly listed as completed November 2022.
# Let's add them directly if they are not picked up by the regex.
if "Bluffs Park Shade Structure" not in park_projects_2022_completed:
    # Verify from the raw text if it meets criteria
    if re.search(r'Bluffs Park Shade Structure.*?completed.*?2022', text, re.IGNORECASE | re.DOTALL):
        if re.search(r'park', 'Bluffs Park Shade Structure', re.IGNORECASE):
            park_projects_2022_completed.append("Bluffs Park Shade Structure")

if "Broad Beach Road Water Quality Repair" not in park_projects_2022_completed:
    if re.search(r'Broad Beach Road Water Quality Repair.*?completed.*?2022', text, re.IGNORECASE | re.DOTALL):
        # This project is not directly park-related, so it should not be added.
        pass # Do nothing, this is not a park project

# Marie Canyon Green Streets, also completed 2023. Not 2022.

# Point Dume Walkway Repairs, completed November 2022, check for park relation
if "Point Dume Walkway Repairs" not in park_projects_2022_completed:
    if re.search(r'Point Dume Walkway Repairs.*?completed.*?2022', text, re.IGNORECASE | re.DOTALL):
        if re.search(r'park|playground', 'Point Dume Walkway Repairs', re.IGNORECASE):
            park_projects_2022_completed.append("Point Dume Walkway Repairs")


park_projects_2022_completed = list(set(park_projects_2022_completed))

print('__RESULT__:')
print(json.dumps(park_projects_2022_completed))"""

env_args = {'var_function-call-8345135393552967239': ['civic_docs'], 'var_function-call-9062427216708247704': 'file_storage/function-call-9062427216708247704.json', 'var_function-call-6977964406746342709': [], 'var_function-call-12672395966706885709': ['Funding']}

exec(code, env_args)
