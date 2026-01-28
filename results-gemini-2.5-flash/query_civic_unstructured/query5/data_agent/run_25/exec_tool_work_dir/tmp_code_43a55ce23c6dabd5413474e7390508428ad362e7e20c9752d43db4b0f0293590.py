code = """import json
import re

file_path = locals()['var_function-call-4723927449613075700']

with open(file_path, 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022_start_names = set()

disaster_keywords_pattern = re.compile(r"(FEMA Project|CalOES Project|CalJPIA Project|disaster|emergency|fire)", re.IGNORECASE)
start_date_2022_pattern = re.compile(r"(?:Begin Construction|Project Schedule|Estimated Schedule):.*?2022", re.IGNORECASE)

for doc in civic_docs:
    text = doc['text']
    
    # Split document into potential project blocks, using common section headers or new project names as delimiters
    # This regex attempts to find a capitalized line (project name) followed by details, up until another capitalized line or section header.
    # It tries to capture the project name and its associated details.
    project_blocks = re.findall(r'([A-Z][^\n]*(?:Project|Improvements|Repair|Plan|Facility|Park|Study|System|Screens)?(?:\s*\(.*?\))?)\n((?:\s*\(cid:\d+\).*|\s*(?:Updates:|Project Schedule:|Estimated Schedule:|Project Description:).*|\s*[^\(cid:]+?)*)(?=\n[A-Z][^\n]*(?:Project|Improvements|Repair|Plan|Facility|Park|Study|System|Screens)?(?:\s*\(.*?\))?|\n(?:Capital Improvement Projects|Disaster Recovery Projects)|\Z)', text, re.DOTALL)


    for project_name, details_block in project_blocks:
        project_name = project_name.strip()
        details_block = details_block.strip()

        is_disaster_project = False
        # Check if project name or its details contain disaster-related keywords
        if disaster_keywords_pattern.search(project_name) or disaster_keywords_pattern.search(details_block):
            is_disaster_project = True
                
        if is_disaster_project:
            if start_date_2022_pattern.search(details_block):
                disaster_projects_2022_start_names.add(project_name)

project_names_list = list(disaster_projects_2022_start_names)

print("__RESULT__:")
print(json.dumps(project_names_list))"""

env_args = {'var_function-call-7673823113563948285': ['civic_docs'], 'var_function-call-4723927449613075700': 'file_storage/function-call-4723927449613075700.json', 'var_function-call-6314443807874731014': ['Funding']}

exec(code, env_args)
