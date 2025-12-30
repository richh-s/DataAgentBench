code = """import json
import re

with open(locals()['var_function-call-7990474508499764104'], 'r') as f:
    civic_docs = json.load(f)

completed_park_projects_2022_names = []

for doc in civic_docs:
    text_lines = doc['text'].split('\n')
    current_project_name = None
    current_project_details = []

    for line in text_lines:
        line = line.strip()
        if not line:
            continue

        # Heuristic to identify a new project name line
        # Check for lines starting with an uppercase letter, potentially followed by (cid:190) or (cid:131)
        # and containing 'Project', 'Park', or 'Playground'.
        project_name_match = re.match(r'^([A-Z][a-zA-Z0-9&\\s\\-]+(?:Project|Park|Playground|Improvements)?(?:\\s\\(FEMA Project\\))?)', line)
        
        if project_name_match:
            # If a new project name is found, process the previous project's details
            if current_project_name:
                details_block = '\n'.join(current_project_details)
                
                is_park_project = False
                if 'Park' in current_project_name or 'Playground' in current_project_name:
                    is_park_project = True
                elif re.search(r'topic:\\s*.*?park|playground', details_block, re.IGNORECASE):
                    is_park_project = True

                if is_park_project:
                    if re.search(r'(completed|Construction was completed|Notice of completion filed).*?2022', details_block, re.IGNORECASE) or \
                       re.search(r'2022.*?(completed|Construction was completed|Notice of completion filed)', details_block, re.IGNORECASE) or \
                       re.search(r'(Complete Construction|Complete Design):.*?2022', details_block, re.IGNORECASE) or \
                       re.search(r'(November|December).*?2022', details_block, re.IGNORECASE):
                        cleaned_name = re.sub(r'\\(cid:190\\)|\\s\\(cid:131\\)', '', current_project_name).strip()
                        completed_park_projects_2022_names.append(cleaned_name)

            current_project_name = project_name_match.group(1).strip()
            current_project_details = []
        else:
            # Accumulate details for the current project
            current_project_details.append(line)
    
    # Process the last project in the document
    if current_project_name:
        details_block = '\n'.join(current_project_details)
        
        is_park_project = False
        if 'Park' in current_project_name or 'Playground' in current_project_name:
            is_park_project = True
        elif re.search(r'topic:\\s*.*?park|playground', details_block, re.IGNORECASE):
            is_park_project = True

        if is_park_project:
            if re.search(r'(completed|Construction was completed|Notice of completion filed).*?2022', details_block, re.IGNORECASE) or \
               re.search(r'2022.*?(completed|Construction was completed|Notice of completion filed)', details_block, re.IGNORECASE) or \
               re.search(r'(Complete Construction|Complete Design):.*?2022', details_block, re.IGNORECASE) or \
               re.search(r'(November|December).*?2022', details_block, re.IGNORECASE):
                cleaned_name = re.sub(r'\\(cid:190\\)|\\s\\(cid:131\\)', '', current_project_name).strip()
                completed_park_projects_2022_names.append(cleaned_name)

unique_completed_park_projects_2022 = list(set(completed_park_projects_2022_names))

print("__RESULT__:")
print(json.dumps(unique_completed_park_projects_2022)))"""

env_args = {'var_function-call-2531287041203044027': ['civic_docs'], 'var_function-call-7990474508499764104': 'file_storage/function-call-7990474508499764104.json', 'var_function-call-16366149949085286234': ['test'], 'var_function-call-18034137513589187498': ['Funding']}

exec(code, env_args)
