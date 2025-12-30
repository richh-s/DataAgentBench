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
    
    # Split the document into sections based on major headers
    sections = re.split(r'(Capital Improvement Projects \(Design\)|Disaster Recovery Projects Status Report|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\))', text)
    
    current_context_type = "unknown"
    
    for i in range(len(sections)):
        section_content = sections[i]
        if "Disaster Recovery Projects" in section_content:
            current_context_type = "disaster"
        elif "Capital Improvement Projects" in section_content:
            current_context_type = "capital"

        # Process project details within each section
        # Find project names and their associated details using a more general regex
        # Project Name: Starts with a capital letter, not a bullet, followed by bulleted details.
        # This regex looks for a line that might be a project name followed by details.
        projects_in_section = re.findall(r'([A-Z][^\n]*(?:Project)?(?:\s*\(.*?\))?)\n(?:\s*\(cid:\d+\).*?(?=\n[A-Z][^\n]*(?:Project)?(?:\s*\(.*?\))?|\Z))?', section_content, re.DOTALL)

        for project_block in projects_in_section:
            project_name_match = re.match(r'([A-Z][^\n]*(?:Project)?(?:\s*\(.*?\))?)', project_block)
            if not project_name_match:
                continue
            
            project_name = project_name_match.group(1).strip()
            project_detail_text = project_block # Use the whole block for detail searching

            is_disaster_project = False
            if current_context_type == "disaster":
                is_disaster_project = True
            elif disaster_keywords_pattern.search(project_name):
                is_disaster_project = True
                
            if is_disaster_project:
                if start_date_2022_pattern.search(project_detail_text):
                    disaster_projects_2022_start_names.add(project_name)


project_names_list = list(disaster_projects_2022_start_names)

print("__RESULT__:")
print(json.dumps(project_names_list))"""

env_args = {'var_function-call-7673823113563948285': ['civic_docs'], 'var_function-call-4723927449613075700': 'file_storage/function-call-4723927449613075700.json', 'var_function-call-6314443807874731014': ['Funding']}

exec(code, env_args)
