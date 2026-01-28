code = """import json

k_fund = "var_function-call-15202175332951554163"
k_docs = "var_function-call-15202175332951553736"

with open(locals()[k_fund], "r") as f:
    funds = json.load(f)

with open(locals()[k_docs], "r") as f:
    docs = json.load(f)

extracted_debug = []

for d in docs:
    txt = d.get("text", "")
    lines = txt.splitlines()
    section = "NO_SECTION"
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if "Projects" in line and ("Capital" in line or "Disaster" in line):
            section = line
            i += 1
            continue
            
        is_proj = False
        if i + 1 < len(lines):
            nxt = lines[i+1].strip()
            if "Updates:" in nxt or "Project Description:" in nxt or "Project Updates:" in nxt:
                is_proj = True
        
        if is_proj and line:
            extracted_debug.append((section, line))
            # skip block
            j = i + 1
            while j < len(lines):
                sub = lines[j].strip()
                if "Projects" in sub and ("Capital" in sub or "Disaster" in sub):
                    break
                if j + 1 < len(lines):
                    snxt = lines[j+1].strip()
                    if ("Updates:" in snxt or "Project Description:" in snxt or "Project Updates:" in snxt) and sub:
                        break
                j += 1
            i = j
        else:
            i += 1

print("__RESULT__:")
print(json.dumps({
    "extracted_count": len(extracted_debug),
    "extracted_samples": extracted_debug[:20],
    "funding_samples": [f['Project_Name'] for f in funds if 'FEMA' in f['Project_Name'] or 'Emergency' in f['Project_Name']][:10]
}))"""

env_args = {'var_function-call-8043042587493176858': ['Funding'], 'var_function-call-8043042587493178041': ['civic_docs'], 'var_function-call-15202175332951554163': 'file_storage/function-call-15202175332951554163.json', 'var_function-call-15202175332951553736': 'file_storage/function-call-15202175332951553736.json', 'var_function-call-7586344906067482996': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000', 'Status': 'Unknown'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000', 'Status': 'Unknown'}]}

exec(code, env_args)
