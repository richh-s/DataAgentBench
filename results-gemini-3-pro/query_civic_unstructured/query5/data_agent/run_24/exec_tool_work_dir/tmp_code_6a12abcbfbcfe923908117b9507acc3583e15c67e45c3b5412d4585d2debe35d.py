code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-2498552123289550299'], 'r') as f:
    docs = json.load(f)

projects = []

for doc in docs:
    text = doc['text']
    # Safer regex. Matches a line of text, followed by newlines, optional bullet-like chars, and "Updates:"
    # We use [\s\S] to match anything if needed, but here we want the line before.
    # We'll look for "Updates:" and go backwards to find the header.
    
    # Iterate over all "Updates:" occurrences
    # Pattern: \n <Title> \n <(cid:190) or similar> Updates:
    # We assume Title is on a separate line.
    
    # Regex:
    # Group 1: Title (non-newlines)
    # Followed by newline(s)
    # Followed by optional (cid:190) or punctuation
    # Followed by Updates:
    pattern = r'([^\n]+)\n+(?:(?:\(cid:190\)|[^\w\s])\s*)?Updates:'
    
    matches = list(re.finditer(pattern, text))
    
    if not matches:
         matches = list(re.finditer(r'([^\n]+)\n+\s*Updates:', text))

    for i in range(len(matches)):
        name = matches[i].group(1).strip()
        
        # content range
        content_start = matches[i].end()
        if i < len(matches) - 1:
            content_end = matches[i+1].start()
        else:
            content_end = len(text)
            
        content = text[content_start:content_end]
        
        # Start Date
        st = None
        # Begin Construction
        m_st = re.search(r'Begin Construction:?\s*([^\n]*)', content, re.IGNORECASE)
        if m_st:
            st = m_st.group(1).strip()
            
        # Is Disaster?
        is_disaster = False
        upper_content = content.upper()
        upper_name = name.upper()
        
        if any(x in upper_name or x in upper_content for x in ["FEMA", "CALOES", "CALJPIA", "DISASTER"]):
            is_disaster = True
            
        projects.append({
            "Project_Name": name,
            "st": st,
            "is_disaster": is_disaster
        })

print("__RESULT__:")
print(json.dumps(projects))"""

env_args = {'var_function-call-2498552123289550299': 'file_storage/function-call-2498552123289550299.json', 'var_function-call-4052442815910590834': 'file_storage/function-call-4052442815910590834.json'}

exec(code, env_args)
