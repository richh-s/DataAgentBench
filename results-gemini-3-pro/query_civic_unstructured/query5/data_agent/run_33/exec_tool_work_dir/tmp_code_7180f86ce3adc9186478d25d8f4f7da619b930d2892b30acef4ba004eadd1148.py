code = """import json
import re

with open(locals()['var_function-call-12317361831468384519'], 'r') as f:
    docs = json.load(f)

extracted_projects = []

for doc in docs:
    text = doc['text']
    # Split by "Updates:" which seems consistent
    chunks = text.split('Updates:')
    
    for i in range(1, len(chunks)):
        details_chunk = chunks[i]
        prev_chunk = chunks[i-1]
        
        # Helper to clean lines
        lines = [line.strip() for line in prev_chunk.strip().split('\n') if line.strip()]
        if not lines:
            continue
            
        # The last line should be the bullet + Project Name or just Project Name + bullet
        # In snippet: "Project Name \n\n (cid:190) Updates:"
        # So splitting by "Updates:", the prev_chunk ends with "(cid:190) "
        # We need to remove that bullet line to get to the project name.
        
        # Remove lines that are just bullets or empty
        # Common bullets: (cid:190), (cid:131), etc.
        valid_lines = [l for l in lines if not l.startswith('(cid:') and len(l) > 3]
        
        if not valid_lines:
            continue
            
        project_name = valid_lines[-1]
        
        # Check start date
        st = None
        # Look for "Begin Construction: <date>"
        # or "Start Date: <date>"
        # Using a regex
        st_match = re.search(r'Begin Construction:([^\n]*)', details_chunk, re.IGNORECASE)
        if st_match:
            st = st_match.group(1).strip()
            
        # Check type
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
