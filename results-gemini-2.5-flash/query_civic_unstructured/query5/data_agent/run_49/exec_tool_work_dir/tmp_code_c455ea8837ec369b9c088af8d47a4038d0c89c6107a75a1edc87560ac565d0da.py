code = """import json
import re

with open(locals()['var_function-call-17133822943557678886'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_2022 = []
for doc in civic_docs_data:
    text = doc['text']
    
    # Extracting "Disaster Recovery Projects" section
    disaster_section_match = re.search(r"Disaster Recovery Projects\n(.+?)(?=\nCapital Improvement Projects|\n\n|$)", text, re.DOTALL)
    if disaster_section_match:
        disaster_section_text = disaster_section_match.group(1)
        
        # Split the section into lines and process
        lines = disaster_section_text.split('\n')
        current_project_name = None
        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Project names are usually at the beginning of a line and not bullet points
            # (cid:190) or (cid:131) are bullet points
            if not line.startswith('(cid:190)') and not line.startswith('(cid:131)') and not line.startswith('Page') and ':' not in line:
                current_project_name = line
            elif current_project_name and ('Project Schedule:' in line or 'Updates:' in line or 'Estimated Schedule:' in line):
                # Check for 2022 in the schedule/updates related to the current project
                if '2022' in line:
                    disaster_projects_2022.append(current_project_name)

# Remove duplicates
disaster_projects_2022 = list(set(disaster_projects_2022))

print('__RESULT__:')
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-17133822943557678886': 'file_storage/function-call-17133822943557678886.json'}

exec(code, env_args)
