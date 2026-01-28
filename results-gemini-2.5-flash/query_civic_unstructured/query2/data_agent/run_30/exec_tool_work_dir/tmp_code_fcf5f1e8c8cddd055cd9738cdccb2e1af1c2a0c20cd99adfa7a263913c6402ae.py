code = """import json
import re

with open(locals()['var_function-call-7990474508499764104'], 'r') as f:
    civic_docs = json.load(f)

completed_park_projects_2022_names = set()

for doc in civic_docs:
    text_lines = doc['text'].split('\n')
    current_project_name = None
    current_project_details = []

    for line in text_lines:
        cleaned_line = line.strip()
        if not cleaned_line:
            continue

        # Regex for project name detection (case-insensitive for keywords like 'Project', 'Park')
        # The regex specifically avoids matching lines that are clearly sub-bullets or minor details.
        # This pattern looks for lines starting with a capital letter or digit, and containing key project words.
        # It's made more robust by checking if the line is not just (cid:XXX) or similar markers.
        is_project_name_line = False
        if re.match(r'^[A-Z0-9][a-zA-Z0-9&\\s\\-]+(?:Project|Park|Playground|Improvements|Repairs)?(?:\\s\\(FEMA Project\\))?$', cleaned_line):
            if not re.match(r'^\\(cid:(?:190|131)\\)', cleaned_line):
                is_project_name_line = True
        
        if is_project_name_line:
            # If a new project name is found, process the previous project's details
            if current_project_name:
                details_block = '\n'.join(current_project_details)
                
                is_park_project = False
                if 'Park' in current_project_name or 'Playground' in current_project_name:
                    is_park_project = True
                elif re.search(r'topic:\\s*.*?park|playground', details_block, re.IGNORECASE):
                    is_park_project = True

                if is_park_project:
                    # Check for completion and 2022. Looking for specific completion phrases near '2022'
                    if (re.search(r'completed.*?2022', details_block, re.IGNORECASE) or
                        re.search(r'2022.*?completed', details_block, re.IGNORECASE) or
                        re.search(r'(Complete Construction|Complete Design):.*?2022', details_block, re.IGNORECASE) or
                        re.search(r'(?:November|December)\\s+2022', details_block, re.IGNORECASE)):
                        
                        cleaned_name = re.sub(r'\\(cid:190\\)|\\s\\(cid:131\\)', '', current_project_name).strip()
                        completed_park_projects_2022_names.add(cleaned_name)

            # Start new project
            current_project_name = cleaned_line
            current_project_details = []
        elif current_project_name is not None: # Accumulate details for the current project
            current_project_details.append(cleaned_line)

    # Process the last project in the document after the loop finishes
    if current_project_name:
        details_block = '\n'.join(current_project_details)
        
        is_park_project = False
        if 'Park' in current_project_name or 'Playground' in current_project_name:
            is_park_project = True
        elif re.search(r'topic:\\s*.*?park|playground', details_block, re.IGNORECASE):
            is_park_project = True

        if is_park_project:
            if (re.search(r'completed.*?2022', details_block, re.IGNORECASE) or
                re.search(r'2022.*?completed', details_block, re.IGNORECASE) or
                re.search(r'(Complete Construction|Complete Design):.*?2022', details_block, re.IGNORECASE) or
                re.search(r'(?:November|December)\\s+2022', details_block, re.IGNORECASE)):
                
                cleaned_name = re.sub(r'\\(cid:190\\)|\\s\\(cid:131\\)', '', current_project_name).strip()
                completed_park_projects_2022_names.add(cleaned_name)

print("__RESULT__:")
print(json.dumps(list(completed_park_projects_2022_names))))"""

env_args = {'var_function-call-2531287041203044027': ['civic_docs'], 'var_function-call-7990474508499764104': 'file_storage/function-call-7990474508499764104.json', 'var_function-call-16366149949085286234': ['test'], 'var_function-call-18034137513589187498': ['Funding']}

exec(code, env_args)
