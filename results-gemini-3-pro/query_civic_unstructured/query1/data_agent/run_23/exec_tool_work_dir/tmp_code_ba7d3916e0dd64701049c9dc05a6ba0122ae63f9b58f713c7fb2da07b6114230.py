code = """import json

funding_key = "var_function_call_14956260562366733902"
docs_key = "var_function_call_4179271317217180395"

with open(locals()[funding_key], "r") as f:
    funding = json.load(f)

with open(locals()[docs_key], "r") as f:
    docs = json.load(f)

funded_names = []
for x in funding:
    try:
        if float(x["Amount"]) > 50000:
            funded_names.append(x["Project_Name"].strip())
    except:
        pass

matches = []
for doc in docs:
    text = doc.get("text", "")
    start_marker = "Capital Improvement Projects (Design)"
    
    start_idx = text.find(start_marker)
    if start_idx == -1:
        continue
        
    # Look for end of section
    # Possible end markers
    end_markers = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]
    end_idx = -1
    
    for em in end_markers:
        idx = text.find(em, start_idx)
        if idx != -1:
            if end_idx == -1 or idx < end_idx:
                end_idx = idx
    
    if end_idx == -1:
        section_text = text[start_idx:]
    else:
        section_text = text[start_idx:end_idx]
        
    for name in funded_names:
        if name in section_text:
            matches.append(name)

unique_matches = list(set(matches))
print("__RESULT__:")
print(json.dumps({"count": len(unique_matches), "matches": unique_matches}))"""

env_args = {'var_function-call-14956260562366733902': 'file_storage/function-call-14956260562366733902.json', 'var_function-call-4179271317217180395': 'file_storage/function-call-4179271317217180395.json'}

exec(code, env_args)
