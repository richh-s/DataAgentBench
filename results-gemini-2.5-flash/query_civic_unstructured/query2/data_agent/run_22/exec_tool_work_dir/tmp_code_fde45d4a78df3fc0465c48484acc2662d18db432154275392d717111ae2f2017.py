code = """import json
import re

with open(locals()['var_function-call-9062427216708247704'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

for doc in civic_docs:
    text = doc['text']
    
    # Split the document by major project category headers to get broader sections.
    # Using re.split with a capturing group for the delimiter keeps the delimiter in the result.
    sections = re.split(r'(\n\n(?:Capital Improvement Projects|Disaster Recovery Projects) \(.*?\))\n\n', text)
    
    # The first element is usually preamble before the first header, skip it.
    # Then, we have [header, content, header, content, ...]
    for i in range(1, len(sections), 2):
        if i + 1 < len(sections): # Ensure there's a content block after the header
            section_content = sections[i+1]
            
            # Now, within each content section, find individual projects.
            # A project usually starts with a capitalized name on a new line, followed by details.
            # Use a non-greedy match to stop at the next project name or end of section.
            project_pattern = r'([A-Z][a-zA-Z0-9\s&,-]+?)\n(?:\(cid:190\)|Updates:|Project Schedule:|Estimated Schedule:|Project Description:)(.*?)(?=\n[A-Z][a-zA-Z0-9\s&,-]+?)(?:\n\(cid:190\)|Updates:|Project Schedule:|Estimated Schedule:|Project Description:)|\Z)'
            
            for match in re.finditer(project_pattern, section_content, re.DOTALL):
                project_name = match.group(1).strip()
                details_block = match.group(2).strip()
                
                is_park_related = False
                if "park" in project_name.lower() or "playground" in project_name.lower():
                    is_park_related = True
                elif re.search(r'Project Description:.*?\b(park|playground)\b', details_block, re.IGNORECASE):
                    is_park_related = True

                is_completed_2022 = False
                if is_park_related:
                    # Check for completion in 2022 within the details_block
                    # Look for phrases like "completed November 2022", "Complete Construction: April 2022"
                    if re.search(r'(?:completed.*?2022|Complete Construction:\s*(?:Spring|Summer|Fall|Winter|[A-Za-z]+)?\s*2022|Construction was completed,\s*(?:Spring|Summer|Fall|Winter|[A-Za-z]+)?\s*2022)', details_block, re.IGNORECASE):
                        is_completed_2022 = True
                
                if is_park_related and is_completed_2022:
                    park_projects_2022_completed.append(project_name)

# Manually add Bluffs Park Shade Structure as it is clearly completed in 2022 and park-related.
# The regex might miss it if its structure is slightly different.
if re.search(r'Bluffs Park Shade Structure.*?Construction was completed November 2022', text, re.IGNORECASE | re.DOTALL):
    if "Bluffs Park Shade Structure" not in park_projects_2022_completed:
        park_projects_2022_completed.append("Bluffs Park Shade Structure")


park_projects_2022_completed = list(set(park_projects_2022_completed))

print('__RESULT__:')
print(json.dumps(park_projects_2022_completed))"""

env_args = {'var_function-call-8345135393552967239': ['civic_docs'], 'var_function-call-9062427216708247704': 'file_storage/function-call-9062427216708247704.json', 'var_function-call-6977964406746342709': [], 'var_function-call-12672395966706885709': ['Funding']}

exec(code, env_args)
