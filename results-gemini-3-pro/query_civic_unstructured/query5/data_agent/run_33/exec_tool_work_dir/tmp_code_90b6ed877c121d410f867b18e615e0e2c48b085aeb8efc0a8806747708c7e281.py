code = """import json
import re

# Load the civic docs
with open(locals()['var_function-call-12317361831468384519'], 'r') as f:
    docs = json.load(f)

extracted_projects = []

for doc in docs:
    text = doc['text']
    # Split text to isolate potential project sections
    # The pattern seems to be: Project Name \n\n (cid:190) Updates:
    # We can split by "(cid:190) Updates:"
    # The name of the project is at the end of the *previous* chunk.
    # The details of the project are at the beginning of the *current* chunk.
    
    chunks = text.split('(cid:190) Updates:')
    
    # The first chunk is header/intro material, but its end *might* contain the name of the first project.
    # The last chunk contains the details of the last project, but no new project name at the end (unless there is one that didn't have updates?)
    # Wait, every project in the list seems to have "Updates:"
    
    # Let's iterate from 1 to len(chunks)-1
    # chunk[i] contains the DETAILS of project [i]
    # chunk[i-1] ends with the NAME of project [i]
    
    # We need to process chunks 1 to end
    for i in range(1, len(chunks)):
        details_chunk = chunks[i]
        prev_chunk = chunks[i-1]
        
        # Extract Name from end of prev_chunk
        # Look for the last non-empty lines in prev_chunk
        prev_lines = [line.strip() for line in prev_chunk.strip().split('\n') if line.strip()]
        if not prev_lines:
            continue
            
        # The project name is likely the last line or last few lines if it wraps. 
        # But looking at the snippet: "Capital Improvement Projects (Design)\n\n2022 Morning View..."
        # It seems the headers like "Capital Improvement Projects (Design)" might interfere.
        # But the headers are usually separated.
        # Let's assume the last non-empty line is the project name.
        project_name = prev_lines[-1]
        
        # Sometimes the header is immediately before.
        # E.g. "Capital Improvement Projects (Design)\n\n2022 Morning View..."
        # If project_name is a category header, we might have an issue.
        # But category headers usually don't have "Updates:" following them immediately.
        # The "Updates:" follows the project name.
        
        # Parse Details for Start Date and Type info
        # Look for "Begin Construction: <date>" or "Start: <date>"
        # Also "Project Schedule" section.
        
        # Start Date
        st = None
        st_match = re.search(r'Begin Construction:\s*(.*)', details_chunk, re.IGNORECASE)
        if st_match:
            st = st_match.group(1).strip()
        
        # Type
        p_type = 'capital' # default
        name_lower = project_name.lower()
        if 'fema' in name_lower or 'caljpia' in name_lower or 'caloes' in name_lower or 'disaster' in name_lower or 'woolsey' in name_lower:
            p_type = 'disaster'
        # Also check suffixes in name specifically if needed, but the keyword search is robust.
        
        extracted_projects.append({
            'name': project_name,
            'st': st,
            'type': p_type,
            'raw_details': details_chunk[:200] # for debugging
        })

print("__RESULT__:")
print(json.dumps(extracted_projects))"""

env_args = {'var_function-call-12317361831468384519': 'file_storage/function-call-12317361831468384519.json'}

exec(code, env_args)
