code = """import json
import re

with open(locals()['var_function-call-13284801232826476662'], 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022 = set()

for doc in civic_docs:
    text = doc['text']
    
    # Identify sections. The document often has 'Capital Improvement Projects' and 'Disaster Recovery Projects' as main headings.
    # We need to consider both patterns for finding project types and their schedules.
    
    # Split the document into logical blocks based on major project type headings
    # This regex splits by either 'Capital Improvement Projects' or 'Disaster Recovery Projects'
    # and keeps the delimiters, so we can identify the type of the block.
    sections = re.split(r'(Capital Improvement Projects|Disaster Recovery Projects)\s*(\(.*?\))?\n\n', text, flags=re.IGNORECASE)

    current_project_type = None
    for i in range(len(sections)): # Iterate through the split parts
        part = sections[i]
        if "Disaster Recovery Projects" in part:
            current_project_type = "disaster"
            continue # Move to the next part which is the content of this section
        elif "Capital Improvement Projects" in part:
            current_project_type = "capital"
            continue

        if current_project_type == "disaster":
            # Now, within the disaster section, find project names and their schedules.
            # Project name followed by details, especially the 'Begin Construction' date.
            # Project name is usually on a line by itself before '(cid:190) Updates:'
            # We are looking for Project Schedule -> Begin Construction

            # This regex looks for a project name (captured in group 1)
            # and then tries to find 'Begin Construction' followed by a date (captured in group 2)
            project_details_matches = re.finditer(
                r'([A-Za-z0-9\s&\-_/]+?)\n\n\\(cid:190\\) Updates:.*?\\(cid:190\\) Project Schedule:\\n\\n\\(cid:131\\) Begin Construction: (.*?)\n',
                part, re.DOTALL
            )
            
            for match in project_details_matches:
                project_name = match.group(1).strip()
                begin_construction_date = match.group(2).strip()

                # Check if the project began in 2022
                if "2022" in begin_construction_date:
                    disaster_projects_2022.add(project_name)

print("__RESULT__:")
print(json.dumps(list(disaster_projects_2022)))"""

env_args = {'var_function-call-10152952571518250078': ['civic_docs'], 'var_function-call-13284801232826476662': 'file_storage/function-call-13284801232826476662.json', 'var_function-call-14885524129273062117': []}

exec(code, env_args)
