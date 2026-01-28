code = """import json
import re

# Load the civic docs
with open(locals()['var_function-call-12317361831468384519'], 'r') as f:
    docs = json.load(f)

extracted_projects = []

for doc in docs:
    text = doc['text']
    chunks = text.split('(cid:190) Updates:')
    
    for i in range(1, len(chunks)):
        details_chunk = chunks[i]
        prev_chunk = chunks[i-1]
        
        prev_lines = [line.strip() for line in prev_chunk.strip().split('\n') if line.strip()]
        if not prev_lines:
            continue
            
        project_name = prev_lines[-1]
        
        st = None
        st_match = re.search(r'Begin Construction:\s*(.*)', details_chunk, re.IGNORECASE)
        if st_match:
            st = st_match.group(1).strip()
        
        p_type = 'capital'
        name_lower = project_name.lower()
        if 'fema' in name_lower or 'caljpia' in name_lower or 'caloes' in name_lower or 'disaster' in name_lower or 'woolsey' in name_lower:
            p_type = 'disaster'
        
        extracted_projects.append({
            'name': project_name,
            'st': st,
            'type': p_type
        })

print("__RESULT__:")
print(json.dumps(extracted_projects))"""

env_args = {'var_function-call-12317361831468384519': 'file_storage/function-call-12317361831468384519.json'}

exec(code, env_args)
