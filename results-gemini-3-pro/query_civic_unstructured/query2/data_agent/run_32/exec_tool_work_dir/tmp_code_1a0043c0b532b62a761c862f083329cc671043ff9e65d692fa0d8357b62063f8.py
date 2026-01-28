code = """import json

funding_key = "var_function-call-4014968237340428108"
docs_key = "var_function-call-4014968237340429633"

with open(locals()[docs_key], "r") as f:
    docs_data = json.load(f)

# Hardcoded matches to check
targets = ['Malibu Park Drainage Improvements', 'Permanent Skate Park', 'Bluffs Park Shade Structure']

snippets = {}

for d in docs_data:
    txt = d["text"]
    lines = txt.splitlines()
    
    current_proj = None
    chunk = []
    
    for line in lines:
        l = line.strip()
        if not l: continue
        
        # Check targets
        found = None
        for t in targets:
            if t.lower() == l.lower():
                found = t
                break
        
        if found:
            if current_proj:
                # Save previous if it was a target
                if current_proj in targets:
                    snippets[current_proj] = snippets.get(current_proj, "") + "\n---DOC---\n" + "\n".join(chunk)
            current_proj = found
            chunk = []
        elif current_proj:
            chunk.append(l)
            
    if current_proj and current_proj in targets:
        snippets[current_proj] = snippets.get(current_proj, "") + "\n---DOC---\n" + "\n".join(chunk)

print("__RESULT__:")
print(json.dumps(snippets))"""

env_args = {'var_function-call-1448852997668966591': ['civic_docs'], 'var_function-call-1448852997668967958': ['Funding'], 'var_function-call-4014968237340428108': 'file_storage/function-call-4014968237340428108.json', 'var_function-call-4014968237340429633': 'file_storage/function-call-4014968237340429633.json', 'var_function-call-2811947825801822237': {'matches': ['Malibu Park Drainage Improvements', 'Permanent Skate Park', 'Bluffs Park Shade Structure'], 'total': 135000}}

exec(code, env_args)
