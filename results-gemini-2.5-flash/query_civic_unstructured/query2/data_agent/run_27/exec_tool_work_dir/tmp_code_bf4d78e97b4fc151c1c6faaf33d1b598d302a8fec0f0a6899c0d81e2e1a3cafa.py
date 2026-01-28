code = """import json
import re

# Load the full result from the file
with open(locals()['var_function-call-8793161985007870018'], 'r') as f:
    civic_docs_data = json.load(f)

park_projects_completed_2022 = []

for doc in civic_docs_data:
    text = doc['text']
    
    # Regex to find projects and their details. This is a simplified regex and might need refinement.
    # It looks for a project name, followed by updates and a schedule, until another project or section title.
    # The pattern looks for a line starting with a capital letter (Project Name), then captures everything until
    # another similar line or a section title.
    
    # More refined regex to capture Project Name, Updates, and Schedule
    # This regex attempts to capture blocks for Capital Improvement Projects (Design), (Construction), (Not Started)
    # and then within those blocks, individual projects.

    # This approach attempts to parse individual project blocks based on common patterns
    project_blocks = re.split(r'\n(?=[A-Z][a-zA-Z0-9\s,-_&/]+(?: Project)?(?: Repair)?(?: Improvements)?(?: Study)?(?: Phase \d)?)', text)
    
    for block in project_blocks:
        project_name_match = re.match(r'\n([A-Z][a-zA-Z0-9\s,-_&/]+(?: Project)?(?: Repair)?(?: Improvements)?(?: Study)?(?: Phase \d)?)', block)
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            
            # Check for 'park' in project name or description (which is the rest of the block)
            if 'park' in project_name.lower() or 'park' in block.lower():
                
                # Check for 'completed' status
                if 'completed' in block.lower():
                    
                    # Check for completion in 2022
                    # Looking for "Complete Construction: [Date with 2022]" or "Construction was completed, [Date with 2022]"
                    completion_date_match = re.search(r'(?:Complete Construction:|Construction was completed,)\s*(.*?2022.*?)(\n|$)', block, re.IGNORECASE)
                    if completion_date_match:
                        # Add to our list
                        park_projects_completed_2022.append(project_name)

# Remove duplicates
park_projects_completed_2022 = list(set(park_projects_completed_2022))

print('__RESULT__:')
print(json.dumps(park_projects_completed_2022))"""

env_args = {'var_function-call-11301953076737978008': ['civic_docs'], 'var_function-call-8793161985007870018': 'file_storage/function-call-8793161985007870018.json'}

exec(code, env_args)
