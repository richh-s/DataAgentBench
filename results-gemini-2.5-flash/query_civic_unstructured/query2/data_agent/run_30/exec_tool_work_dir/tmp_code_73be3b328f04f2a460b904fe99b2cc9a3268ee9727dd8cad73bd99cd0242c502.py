code = """import json
import re

with open(locals()['var_function-call-7990474508499764104'], 'r') as f:
    civic_docs = json.load(f)

park_projects_found = []

for doc in civic_docs:
    text = doc['text']
    
    # Split the document text into potential project blocks based on capitalized lines followed by details
    # This pattern attempts to capture a project name (often capitalized on its own line)
    # and all subsequent details until the next similar project name or end of document.
    project_blocks = re.findall(r'(?m)^([A-Z][a-zA-Z0-9&\s\-]+(?:Park|Playground|Project)(?: \\(FEMA Project\\))?)\n(?:\\(cid:190\\)|\n)*?((?:.|\n)(?!^[A-Z][a-zA-Z0-9&\s\-]+(?:Park|Playground|Project)(?: \\(FEMA Project\\))?))*', text)

    for project_name, details_block in project_blocks:
        project_name = project_name.strip()
        details_block = details_block.strip()
        
        # Check if it's a park-related project based on name keywords
        is_park_project = False
        if 'Park' in project_name or 'Playground' in project_name:
            is_park_project = True

        if is_park_project:
            status = 'N/A'
            end_year = 'N/A'
            
            # Try to find completion status within the details block
            completed_match = re.search(r'(completed|Construction was completed|filed January 2023|Notice of completion filed January 2023)', details_block, re.IGNORECASE)
            if completed_match:
                status = 'completed'
                
                # Look for the year 2022 in the completion context or schedule
                year_match = re.search(r'(?:completed|Construction was completed|Complete Construction:|Complete Design:).*?(\d{4})', details_block)
                if year_match:
                    end_year = year_match.group(1)
                elif 'November 2022' in details_block or 'December 2022' in details_block:
                    end_year = '2022'

            if status == 'completed' and end_year == '2022':
                park_projects_found.append(project_name)

unique_park_projects = list(set(park_projects_found))

print("__RESULT__:")
print(json.dumps(unique_park_projects)))"""

env_args = {'var_function-call-2531287041203044027': ['civic_docs'], 'var_function-call-7990474508499764104': 'file_storage/function-call-7990474508499764104.json'}

exec(code, env_args)
