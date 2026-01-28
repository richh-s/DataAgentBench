code = """import json

key = 'var_function-call-2606248953050084103'
file_path = locals()[key]

with open(file_path, 'r') as f:
    docs = json.load(f)

park_projects_status = []

for doc in docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    
    # Identify projects
    project_indices = []
    for i, line in enumerate(lines):
        if 'Updates:' in line and '(cid' in line:
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
        
        block_text = " ".join(lines[start_idx:end_idx])
        block_lower = block_text.lower()
        
        # Check park
        if 'park' in name.lower() or 'playground' in name.lower() or 'recreation' in name.lower():
             park_projects_status.append({'name': name, 'text': block_text[:300]}) # limit text length

print("__RESULT__:")
print(json.dumps(park_projects_status))"""

env_args = {'var_function-call-11018828137096433112': ['civic_docs'], 'var_function-call-11018828137096433437': ['Funding'], 'var_function-call-12832671223753194442': 'file_storage/function-call-12832671223753194442.json', 'var_function-call-2606248953050084103': 'file_storage/function-call-2606248953050084103.json', 'var_function-call-2510182640991691682': 5, 'var_function-call-17108931763067660068': ['Bluffs Park Shade Structure'], 'var_function-call-10086250550960347140': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}]}

exec(code, env_args)
