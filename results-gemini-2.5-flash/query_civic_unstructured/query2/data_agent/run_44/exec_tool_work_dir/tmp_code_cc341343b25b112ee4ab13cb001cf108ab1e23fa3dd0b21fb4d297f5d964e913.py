code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-7381029510342299893'], 'r') as f:
    data = json.load(f)

projects = []

project_name_pattern = re.compile(
    '([A-Z][a-zA-Z0-9&,\s\\-]+(?:Project|Improvements|Repair|Plan|Structure|System|Study|Facility|Playground|Road|Drainage|Wall|Park|Station|Signals|Biofilter|Screens|Power|Walkway|Streets)\\b(?:\\s*\\(FEMA Project\\)|\\s*\\(CalJPIA Project\\)|\\s*\\(CalOES Project\\))?)',
    re.IGNORECASE
)

for doc in data:
    text = doc['text']
    for project_name_match in project_name_pattern.finditer(text):
        project_name = project_name_match.group(1).strip()
        
        search_start_index = project_name_match.end()
        search_scope = text[search_start_index : search_start_index + 500] # Adjust scope as needed

        status = 'unknown'
        et = 'unknown'
        
        status_match = re.search(
            '(?:Updates:|Project Updates:)(?:\\n\\(cid:131\\)[^\\n]*)*\\s*(construction was completed|completed|is currently under construction|is currently working on|plans have been completed|is in the preliminary design phase|is currently out to bid|City is expecting|Final Design|Complete Design|Begin construction)',
            search_scope,
            re.IGNORECASE
        )
        if status_match:
            status = status_match.group(1).lower()
        
        et_match = re.search(
            '(?:Complete Construction:|Estimated Schedule:|Project Schedule:)(?:\\n\\(cid:131\\)[^\\n]*)*\\s*([^\\n]+(?:20\\d{2}|Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))',
            search_scope,
            re.IGNORECASE
        )
        if et_match:
            et = et_match.group(1).strip()
            
        topic = []
        if 'park' in project_name.lower() or 'playground' in project_name.lower():
            topic.append('park')
        
        if topic and 'completed' in status and '2022' in et:
            projects.append({
                'Project_Name': project_name,
                'status': status,
                'et': et,
                'topic': ', '.join(topic)
            })

filtered_project_names = [p['Project_Name'] for p in projects]
unique_project_names = list(set(filtered_project_names))

print("__RESULT__:")
print(json.dumps(unique_project_names))"""

env_args = {'var_function-call-7381029510342299893': 'file_storage/function-call-7381029510342299893.json'}

exec(code, env_args)
