code = """import json

keys = [k for k in locals().keys() if k.startswith('var_function_call') or k.startswith('var_function-call')]

civic_docs = []
funding_data = []

for k in keys:
    val = locals()[k]
    if isinstance(val, str) and val.endswith('.json'):
        try:
            with open(val, 'r') as f:
                data = json.load(f)
                if isinstance(data, list) and len(data) > 0:
                    if 'text' in data[0]:
                        civic_docs = data
                    elif 'Project_Name' in data[0]:
                        funding_data = data
        except:
            continue

results = []
seen = set()

for doc in civic_docs:
    lines = doc.get('text', '').split('\n')
    current_status = 'Unknown'
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        if 'Capital Improvement Projects (Design)' in line:
            current_status = 'design'
            i += 1
            continue
        elif 'Capital Improvement Projects (Construction)' in line:
            current_status = 'construction'
            i += 1
            continue
        elif 'Capital Improvement Projects (Not Started)' in line:
            current_status = 'not started'
            i += 1
            continue
            
        j = i + 1
        is_p = False
        while j < len(lines):
            nxt = lines[j].strip()
            if nxt:
                if 'cid:' in nxt:
                    is_p = True
                break
            j += 1
            
        if is_p:
            p_name = line
            block = [line]
            k = i + 1
            while k < len(lines):
                ls = lines[k].strip()
                if 'Capital Improvement Projects (' in ls:
                    break
                m = k + 1
                nl = ''
                while m < len(lines):
                    if lines[m].strip():
                        nl = lines[m].strip()
                        break
                    m += 1
                if 'cid:' in nl and ls:
                    break
                block.append(lines[k])
                k += 1
            
            full_text = ' '.join(block).lower()
            status = current_status
            if status == 'construction':
                if 'construction was completed' in full_text or 'notice of completion' in full_text:
                    status = 'completed'
            
            is_rel_txt = 'emergency' in full_text or 'fema' in full_text
            
            matched = []
            p_clean = p_name.strip()
            for f in funding_data:
                fn = f.get('Project_Name', '').strip()
                if fn == p_clean:
                    matched.append(f)
                elif fn.startswith(p_clean) and ('(FEMA' in fn or '(CalOES' in fn):
                    matched.append(f)
            
            is_rel_fund = any('FEMA' in f.get('Project_Name', '') for f in matched)
            
            if is_rel_txt or is_rel_fund:
                for f in matched:
                    key = (f['Project_Name'], f['Funding_Source'], f['Amount'], status)
                    if key not in seen:
                        results.append({
                            "Project_Name": f['Project_Name'],
                            "Funding_Source": f['Funding_Source'],
                            "Amount": f['Amount'],
                            "Status": status
                        })
                        seen.add(key)
            i = k
        else:
            i += 1

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5314689848264011546': 'file_storage/function-call-5314689848264011546.json', 'var_function-call-5314689848264008089': 'file_storage/function-call-5314689848264008089.json', 'var_function-call-17911160366985572279': 'file_storage/function-call-17911160366985572279.json'}

exec(code, env_args)
