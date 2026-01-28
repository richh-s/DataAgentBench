code = """import json
import re

with open(locals()['var_function-call-9062427216708247704'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

for doc in civic_docs:
    text = doc['text']
    # Split the document text into sections, assuming project details are listed sequentially
    project_sections = re.split('\\n\\nCapital Improvement Projects \\((?:Design|Construction|Not Started)\\)|\\n\\nDisaster Recovery Projects \\((?:Active|Completed)\\)', text)
    
    # Iterate through sections and extract project details
    for section in project_sections:
        project_name_match = re.search('\\n\\n([A-Za-z0-9\\s&,-]+?)(?:\\n|\\(cid:190\\)|:)', section)
        
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            
            topic_match = re.search('Project Description:.*?\\b(park|playground)\\b', section, re.IGNORECASE)
            status_match = re.search('Updates:.*?construction was completed.*?|Updates:.*?(?:Project is currently under construction|Project is currently out to bid).*?Complete Construction: (.*?)(?:\\n|$)|Construction was completed, (.*?)(?:\\n|$)', section, re.IGNORECASE)
            
            end_time_match = re.search('(?:Complete Construction|Construction was completed|Complete Design):\\s*(.*?)(?:\\n|$)', section, re.IGNORECASE)

            is_park_related = False
            if "park" in project_name.lower() or "playground" in project_name.lower():
                is_park_related = True
            elif topic_match and ('park' in topic_match.group(0).lower() or 'playground' in topic_match.group(0).lower()):
                is_park_related = True

            is_completed_2022 = False
            if status_match:
                if "construction was completed" in status_match.group(0).lower():
                    if end_time_match:
                        end_date = end_time_match.group(1).strip()
                        if "2022" in end_date:
                            is_completed_2022 = True
                elif status_match.group(1) and "2022" in status_match.group(1):
                    is_completed_2022 = True
                elif status_match.group(2) and "2022" in status_match.group(2):
                    is_completed_2022 = True
            elif end_time_match:
                end_date = end_time_match.group(1).strip()
                if "2022" in end_date and "completed" in section.lower():
                    is_completed_2022 = True

            if is_park_related and is_completed_2022:
                park_projects_2022_completed.append(project_name)

# Remove duplicates
park_projects_2022_completed = list(set(park_projects_2022_completed))

print('__RESULT__:')
print(json.dumps(park_projects_2022_completed))"""

env_args = {'var_function-call-8345135393552967239': ['civic_docs'], 'var_function-call-9062427216708247704': 'file_storage/function-call-9062427216708247704.json'}

exec(code, env_args)
