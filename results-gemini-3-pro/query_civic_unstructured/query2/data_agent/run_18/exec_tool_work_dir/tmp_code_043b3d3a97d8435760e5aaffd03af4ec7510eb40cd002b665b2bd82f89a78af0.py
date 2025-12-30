code = """import json
import re

file_path = locals()['var_function-call-2606248953050084103']

with open(file_path, 'r') as f:
    docs = json.load(f)

projects = []

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    project_indices = []
    # Identify project starts
    for i, line in enumerate(lines):
        if '(cid:190) Updates:' in line or '(cid:190) Project Description:' in line:
            # Title is likely the previous non-empty line
            idx = i - 1
            while idx >= 0 and not lines[idx].strip():
                idx -= 1
            if idx >= 0:
                name = lines[idx].strip()
                project_indices.append((idx, name))
    
    # Process blocks
    for k in range(len(project_indices)):
        start_idx, name = project_indices[k]
        if k < len(project_indices) - 1:
            end_idx = project_indices[k+1][0]
        else:
            end_idx = len(lines)
        
        block_text = "\n".join(lines[start_idx:end_idx])
        
        # Check conditions
        # 1. Park related
        name_lower = name.lower()
        # Look for park keywords in name
        if 'park' in name_lower or 'playground' in name_lower or 'recreation' in name_lower:
            is_park = True
        else:
            is_park = False
            
        # 2. Completed in 2022
        is_completed_2022 = False
        # Split block into sentences or lines to be more specific
        block_lines = block_text.split('\n')
        for line in block_lines:
            l_lower = line.lower()
            # Check for "completed" and "2022"
            if 'completed' in l_lower and '2022' in l_lower:
                # Exclude "expected to be completed" if possible?
                # The snippets were "Construction was completed November 2022"
                if 'construction was completed' in l_lower or 'project was completed' in l_lower or 'completed, november 2022' in l_lower or 'completed november 2022' in l_lower:
                     is_completed_2022 = True
        
        if is_park and is_completed_2022:
            projects.append(name)

print("__RESULT__:")
print(json.dumps(projects))"""

env_args = {'var_function-call-11018828137096433112': ['civic_docs'], 'var_function-call-11018828137096433437': ['Funding'], 'var_function-call-12832671223753194442': 'file_storage/function-call-12832671223753194442.json', 'var_function-call-2606248953050084103': 'file_storage/function-call-2606248953050084103.json'}

exec(code, env_args)
