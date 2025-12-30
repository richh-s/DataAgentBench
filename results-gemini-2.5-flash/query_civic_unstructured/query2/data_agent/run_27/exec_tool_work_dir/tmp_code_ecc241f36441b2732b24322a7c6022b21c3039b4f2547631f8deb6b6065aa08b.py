code = """import json
import re

with open(locals()['var_function-call-8793161985007870018'], 'r') as f:
    civic_docs_data = json.load(f)

park_projects_completed_2022 = set()

for doc in civic_docs_data:
    text = doc['text']

    # Manually replace (cid:xxx) as regex for it seems to be problematic
    cleaned_text = text.replace('(cid:190)', '').replace('(cid:131)', '')

    lines = cleaned_text.split('\n')
    
    for i, line in enumerate(lines):
        if 'park' in line.lower():
            # Consider a window of 3 lines before and 4 lines after the line containing 'park'
            context_lines = lines[max(0, i-3):min(len(lines), i+4)]
            context_text = '\n'.join(context_lines)

            # Simplified regex for project name: starts with a capital, followed by words/numbers/some symbols
            project_name_match = re.search(r'([A-Z][a-zA-Z0-9 ,-_&/]+(?: Project)?(?: Repair)?(?: Improvements)?(?: Study)?(?: Phase [0-9])?)', context_text)
            
            if project_name_match:
                project_name = project_name_match.group(1).strip()
                
                if 'park' in project_name.lower():
                    # Check for completion in 2022 within the context
                    if (re.search(r'completed', context_text, re.IGNORECASE) or
                        re.search(r'complete construction:', context_text, re.IGNORECASE)) and \
                       re.search(r'2022', context_text):
                        park_projects_completed_2022.add(project_name)

print('__RESULT__:')
print(json.dumps(list(park_projects_completed_2022)))"""

env_args = {'var_function-call-11301953076737978008': ['civic_docs'], 'var_function-call-8793161985007870018': 'file_storage/function-call-8793161985007870018.json'}

exec(code, env_args)
