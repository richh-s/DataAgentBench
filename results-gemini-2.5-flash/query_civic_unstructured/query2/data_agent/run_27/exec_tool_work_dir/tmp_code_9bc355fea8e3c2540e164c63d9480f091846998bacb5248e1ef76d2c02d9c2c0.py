code = """import json
import re

with open(locals()['var_function-call-8793161985007870018'], 'r') as f:
    civic_docs_data = json.load(f)

park_projects_completed_2022 = set()

for doc in civic_docs_data:
    text = doc['text']
    
    # Remove (cid:xxx) patterns
    cleaned_text = re.sub(r'\\(cid:\\d+\\)', '', text)

    # Split the text into potential project-level chunks. 
    # Projects are often listed with a capitalized title, followed by updates and schedule.
    # We'll look for a capitalized line that might be a project title.
    # This regex is an attempt to get blocks that look like project descriptions.
    project_chunks = re.split(r'\n(?=[A-Z][A-Za-z0-9\s,-_&/:]+(?: Project| Repairs| Improvements| Study)?(?: Phase \\d)?)', cleaned_text)
    
    for chunk in project_chunks:
        # Check if 'park' is in the chunk
        if 'park' in chunk.lower():
            # Check for 'completed' and '2022' within the same chunk
            if re.search(r'completed.*?2022', chunk, re.IGNORECASE) or \
               re.search(r'complete construction:.*?2022', chunk, re.IGNORECASE):
                
                # Now, try to extract the actual project name. It should be at the beginning of the chunk.
                project_name_match = re.search(r'^[A-Z][A-Za-z0-9\s,-_&/:]+(?: Project| Repairs| Improvements| Study)?(?: Phase \\d)?', chunk)
                if project_name_match:
                    project_name = project_name_match.group(0).strip()
                    park_projects_completed_2022.add(project_name)

print('__RESULT__:')
print(json.dumps(list(park_projects_completed_2022)))"""

env_args = {'var_function-call-11301953076737978008': ['civic_docs'], 'var_function-call-8793161985007870018': 'file_storage/function-call-8793161985007870018.json', 'var_function-call-7756715854791707326': ['Funding'], 'var_function-call-12534020772609167679': []}

exec(code, env_args)
