code = """import re
import json

text_data = open(locals()['var_function-call-4030353850200196084'], 'r').read()
documents = json.loads(text_data)

spring_2022_projects = []

for doc in documents:
    text = doc['text']
    # Regex to find project names and their schedules
    # This pattern looks for lines starting with '(cid:190) Project Schedule:' or '(cid:190) Estimated Schedule:'
    # followed by lines containing '(cid:131) Begin Construction: Spring 2022' or similar
    # It also tries to capture the project name before these schedule lines.
    
    # Improved regex to capture project name and start date more reliably
    # It looks for a project name (often capitalized and followed by a newline)
    # then for a schedule section that contains 'Begin Construction: Spring 2022' or similar
    project_blocks = re.split(r'\n\n(?=[A-Z][A-Za-z0-9\s&,-]+(?:Project|Improvements|Plan|Study|Repairs|Facility|Park|Lane|Wall|Biofilter|Signals|Screens|Slopes|System)\n)', text)

    for block in project_blocks:
        project_name_match = re.search(r'^([A-Z][A-Za-z0-9\s&,-]+(?:Project|Improvements|Plan|Study|Repairs|Facility|Park|Lane|Wall|Biofilter|Signals|Screens|Slopes|System))\n', block)
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            # Look for "Spring 2022" as a start date within the project block
            if re.search(r'Begin Construction: (?:March|April|May|Spring) 2022', block):
                spring_2022_projects.append(project_name)
            elif re.search(r'Advertise: (?:March|April|May|Spring) 2022', block) and "Begin Construction" not in block:
                # If "Begin Construction" is not explicitly mentioned, "Advertise" might imply the start for some projects
                spring_2022_projects.append(project_name)
            elif re.search(r'st: (?:2022-Spring|2022-03|2022-04|2022-05|March 2022|April 2022|May 2022)', block):
                spring_2022_projects.append(project_name)

# Remove duplicates
spring_2022_projects = list(set(spring_2022_projects))

print('__RESULT__:')
print(json.dumps(spring_2022_projects))"""

env_args = {'var_function-call-4030353850200196084': 'file_storage/function-call-4030353850200196084.json'}

exec(code, env_args)
