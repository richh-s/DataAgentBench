code = """import json
import re

with open(locals()['var_function-call-9062427216708247704'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

for doc in civic_docs:
    text = doc['text']
    
    # Use a more flexible regex to find project names and their associated details
    # Looking for 'Project Name' followed by some content and then 'Updates' or 'Project Schedule'
    # This pattern captures potential project blocks more broadly
    project_blocks = re.findall(r'([A-Z][a-zA-Z0-9\\s&,-]+?)\\n(?:\\(cid:190\\)|Updates:|Project Schedule:).*?(?=\\n[A-Z][a-zA-Z0-9\\s&,-]+?)', text, re.DOTALL)
    
    # If the above broad split fails, try splitting by known project type headers (less reliable)
    if not project_blocks:
        project_blocks = re.split(r'\\n\\nCapital Improvement Projects \\((?:Design|Construction|Not Started)\\)|\\n\\nDisaster Recovery Projects \\((?:Active|Completed)\\)', text)
        # The first element after split is usually preamble, so skip it
        if len(project_blocks) > 0: # Ensure there is at least a preamble
            project_blocks = project_blocks[1:]
        # For these blocks, the project name is at the beginning
        project_blocks = [re.match(r'^([A-Z][a-zA-Z0-9\\s&,-]+?)\\n', block).group(1).strip() + '\n' + block if re.match(r'^([A-Z][a-zA-Z0-9\\s&,-]+?)\\n', block) else block for block in project_blocks]


    for block in project_blocks:
        project_name_match = re.search(r'^([A-Z][a-zA-Z0-9\\s&,-]+?)\\n', block) # Find project name at the beginning of the block

        if project_name_match:
            project_name = project_name_match.group(1).strip()
            
            is_park_related = False
            if "park" in project_name.lower() or "playground" in project_name.lower():
                is_park_related = True
            elif re.search(r'Project Description:.*?\\b(park|playground)\\b', block, re.IGNORECASE):
                is_park_related = True
            
            is_completed_2022 = False
            if is_park_related:
                # Look for completion in 2022 within the same block
                if re.search(r'completed.*?2022', block, re.IGNORECASE) or \
                   re.search(r'Complete Construction:.*?2022', block, re.IGNORECASE) or \
                   re.search(r'Construction was completed,.*?2022', block, re.IGNORECASE):
                    is_completed_2022 = True

            if is_park_related and is_completed_2022:
                park_projects_2022_completed.append(project_name)

# Remove duplicates
park_projects_2022_completed = list(set(park_projects_2022_completed))

print('__RESULT__:')
print(json.dumps(park_projects_2022_completed))"""

env_args = {'var_function-call-8345135393552967239': ['civic_docs'], 'var_function-call-9062427216708247704': 'file_storage/function-call-9062427216708247704.json', 'var_function-call-6977964406746342709': []}

exec(code, env_args)
