code = """import json
import re

file_path = locals()['var_function-call-4723927449613075700']

with open(file_path, 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022_start_names = set()

for doc in civic_docs:
    text = doc['text']
    
    lines = text.split('\n')
    
    current_context_type = "unknown"
    current_project_name_candidate = None
    project_start_line_index = -1
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        if "Disaster Recovery Projects" in line:
            current_context_type = "disaster"
            current_project_name_candidate = None
            project_start_line_index = -1
            continue
        elif "Capital Improvement Projects" in line:
            current_context_type = "capital"
            current_project_name_candidate = None
            project_start_line_index = -1
            continue
        
        if any(keyword in line for keyword in ["Page", "Item", "Agenda Report", "To:", "Prepared by:", "Approved by:", "Date prepared:", "Meeting date:", "Subject:", "RECOMMENDED ACTION:", "DISCUSSION:"]) or not line:
            continue
        
        is_potential_new_project_header = (
            not line.startswith('(cid:') and
            len(line) > 10 and
            line[0].isupper()
        )
        
        if is_potential_new_project_header:
            future_lines_segment = "\n".join(lines[i+1:min(i+5, len(lines))])
            if re.search(r'\(cid:\d+\)\s*(?:Updates:|Project Schedule:|Estimated Schedule:|Project Description:)', future_lines_segment):
                if current_project_name_candidate and project_start_line_index != -1:
                    project_detail_block_lines = lines[project_start_line_index:i]
                    project_detail_text = "\n".join(project_detail_block_lines)
                    
                    is_disaster_project = False
                    if current_context_type == "disaster":
                        is_disaster_project = True
                    elif "FEMA Project" in current_project_name_candidate or "CalOES Project" in current_project_name_candidate or "CalJPIA Project" in current_project_name_candidate or "disaster" in current_project_name_candidate.lower() or "emergency" in current_project_name_candidate.lower() or "fire" in current_project_name_candidate.lower():
                        is_disaster_project = True
                        
                    if is_disaster_project:
                        start_date_match = re.search(r'(?:Begin Construction|Project Schedule|Estimated Schedule):\s*.*?(2022(?:-|\s*(?:Spring|Summer|Fall|January|February|March|April|May|June|July|August|September|October|November|December))?)', project_detail_text, re.IGNORECASE)
                        if start_date_match:
                            disaster_projects_2022_start_names.add(current_project_name_candidate)
                
                current_project_name_candidate = line
                project_start_line_index = i
        
    if current_project_name_candidate and project_start_line_index != -1:
        project_detail_block_lines = lines[project_start_line_index:]
        project_detail_text = "\n".join(project_detail_block_lines)
        
        is_disaster_project = False
        if current_context_type == "disaster":
            is_disaster_project = True
        elif "FEMA Project" in current_project_name_candidate or "CalOES Project" in current_project_name_candidate or "CalJPIA Project" in current_project_name_candidate or "disaster" in current_project_name_candidate.lower() or "emergency" in current_project_name_candidate.lower() or "fire" in current_project_name_candidate.lower():
            is_disaster_project = True
            
        if is_disaster_project:
            start_date_match = re.search(r'(?:Begin Construction|Project Schedule|Estimated Schedule):\s*.*?(2022(?:-|\s*(?:Spring|Summer|Fall|January|February|March|April|May|June|July|August|September|October|November|December))?)', project_detail_text, re.IGNORECASE)
            if start_date_match:
                disaster_projects_2022_start_names.add(current_project_name_candidate)

project_names_list = list(disaster_projects_2022_start_names)

print("__RESULT__:")
print(json.dumps(project_names_list))"""

env_args = {'var_function-call-7673823113563948285': ['civic_docs'], 'var_function-call-4723927449613075700': 'file_storage/function-call-4723927449613075700.json', 'var_function-call-6314443807874731014': ['Funding']}

exec(code, env_args)
