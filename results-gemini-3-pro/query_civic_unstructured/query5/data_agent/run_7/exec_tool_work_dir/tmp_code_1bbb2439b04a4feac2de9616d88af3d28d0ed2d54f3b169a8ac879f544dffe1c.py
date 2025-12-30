code = """import json

fp = locals()['var_function-call-12062815889619764856']
cp = locals()['var_function-call-9916471758806846480']

with open(fp, 'r') as f:
    funding = json.load(f)
with open(cp, 'r') as f:
    docs = json.load(f)

extracted = {}

for d in docs:
    lines = d['text'].split(chr(10))
    is_disaster_section = False
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if "Disaster Recovery Projects" in line:
            is_disaster_section = True
        elif "Capital Improvement Projects" in line:
            is_disaster_section = False
            
        is_proj = False
        if i+1 < len(lines):
            nxt = lines[i+1].strip()
            if "Updates:" in nxt or "Project Description:" in nxt:
                is_proj = True
        
        if is_proj and line and len(line) > 3 and "Agenda" not in line:
            name = line.strip()
            block = []
            j = i + 1
            while j < len(lines):
                nxt = lines[j].strip()
                if j+1 < len(lines):
                    nnxt = lines[j+1].strip()
                    if ("Updates:" in nnxt or "Project Description:" in nnxt) and nxt and len(nxt) > 3:
                        break
                if "Capital Improvement Projects" in nxt or "Disaster Recovery Projects" in nxt:
                    break
                block.append(nxt)
                j += 1
            
            full_text = " ".join(block)
            
            is_dis = is_disaster_section
            if "FEMA" in name or "CalOES" in name or "Disaster" in name:
                is_dis = True
            if "FEMA" in full_text or "CalOES" in full_text or "Disaster" in full_text:
                is_dis = True
                
            start_2022 = False
            lt = full_text.lower()
            if "begin construction" in lt:
                idx = lt.find("begin construction")
                if idx != -1:
                    sub = lt[idx:idx+50]
                    if "2022" in sub:
                        start_2022 = True
            if "construction started" in lt:
                idx = lt.find("construction started")
                if idx != -1:
                    sub = lt[idx:idx+50]
                    if "2022" in sub:
                        start_2022 = True
            if "start date" in lt:
                idx = lt.find("start date")
                if idx != -1:
                    sub = lt[idx:idx+50]
                    if "2022" in sub:
                        start_2022 = True

            if name not in extracted:
                extracted[name] = {'disaster': False, 'start_2022': False}
            if is_dis:
                extracted[name]['disaster'] = True
            if start_2022:
                extracted[name]['start_2022'] = True
            
            i = j - 1
        i += 1

print("__RESULT__:")
# Filter for 2022 projects
projs_2022 = {k:v for k,v in extracted.items() if v['start_2022']}
print(json.dumps(projs_2022))"""

env_args = {'var_function-call-1624468200300741529': ['Funding'], 'var_function-call-1624468200300743390': ['civic_docs'], 'var_function-call-12062815889619764856': 'file_storage/function-call-12062815889619764856.json', 'var_function-call-12062815889619765571': 'file_storage/function-call-12062815889619765571.json', 'var_function-call-9916471758806846480': 'file_storage/function-call-9916471758806846480.json', 'var_function-call-4000825610634177752': 1, 'var_function-call-3548741773623952948': 5, 'var_function-call-14645956101739205589': {'total': 85000.0, 'matches': ['Birdview Avenue Improvements (CalOES Project)']}, 'var_function-call-14596813845231011609': {'Birdview Avenue Improvements (CalOES Project)': {'disaster': True, 'start_2022': True}, 'Malibu Park Storm Drain Repairs': {'disaster': True, 'start_2022': False}}}

exec(code, env_args)
