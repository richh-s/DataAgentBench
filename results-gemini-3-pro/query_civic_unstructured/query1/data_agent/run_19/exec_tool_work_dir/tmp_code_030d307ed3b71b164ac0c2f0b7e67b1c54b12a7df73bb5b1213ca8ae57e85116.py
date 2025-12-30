code = """import json

with open(locals()['var_function-call-9654609134184919281'], 'r') as f:
    civic_docs = json.load(f)

text = civic_docs[0]['text']

# Find section
start_marker = "Capital Improvement Projects (Design)"
end_marker = "Capital Improvement Projects (Construction)"

start_idx = text.find(start_marker)
if start_idx == -1:
    print("__RESULT__:")
    print(json.dumps("Section not found"))
else:
    end_idx = text.find(end_marker, start_idx)
    section = text[start_idx:end_idx]
    
    # Simple split
    parts = section.split("(cid:190)")
    
    # Extract headers (last line of previous part)
    projects = []
    for i in range(len(parts)-1):
        # part i contains the project name at the end
        lines = parts[i].split('\n')
        # Filter empty
        lines = [l.strip() for l in lines if l.strip()]
        # Take last line
        if lines:
            # Filter headers
            candidate = lines[-1]
            if "Capital Improvement Projects" in candidate:
                pass # This is the header of the section
            elif "Agenda Item" in candidate or "Page" in candidate:
                if len(lines) > 1:
                    projects.append(lines[-2])
            else:
                projects.append(candidate)
    
    # Check funding
    with open(locals()['var_function-call-10318342191074584213'], 'r') as f:
        funding = json.load(f)
        
    funded_high = {x['Project_Name']: float(x['Amount']) for x in funding if float(x['Amount']) > 50000}
    
    matches = [p for p in projects if p in funded_high]
    
    print("__RESULT__:")
    print(json.dumps({"matches": matches, "count": len(matches), "extracted": projects}))"""

env_args = {'var_function-call-10318342191074584213': 'file_storage/function-call-10318342191074584213.json', 'var_function-call-9654609134184919281': 'file_storage/function-call-9654609134184919281.json'}

exec(code, env_args)
