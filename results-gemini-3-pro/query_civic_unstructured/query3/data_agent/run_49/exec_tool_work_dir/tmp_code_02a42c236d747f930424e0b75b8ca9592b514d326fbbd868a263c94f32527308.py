code = """import json
import pandas as pd

# Load extracted data
civic_path = locals()['var_function-call-17911160366985572279']
funding_path = locals()['var_function-call-5314689848264008089']

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

results = []
seen = set()

# Process
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
        is_project = False
        while j < len(lines):
            nxt = lines[j].strip()
            if nxt:
                # Check for (cid:
                if nxt.startswith('(' + 'cid:'):
                    is_project = True
                break
            j += 1
            
        if is_project:
            p_name = line
            # Extract block
            block = [line]
            k = i + 1
            while k < len(lines):
                ls = lines[k].strip()
                # Stop conditions
                if 'Capital Improvement Projects (' in ls:
                    break
                
                # Check next project
                m = k + 1
                nxt_ls = ''
                while m < len(lines):
                    if lines[m].strip():
                        nxt_ls = lines[m].strip()
                        break
                    m += 1
                
                if nxt_ls.startswith('(' + 'cid:') and ls:
                    break
                
                block.append(lines[k])
                k += 1
            
            full_text = '\n'.join(block)
            lower_text = full_text.lower()
            
            status = current_status
            if status == 'construction':
                if 'construction was completed' in lower_text or 'notice of completion' in lower_text:
                    status = 'completed'
            
            # Check related
            is_related_text = 'emergency' in lower_text or 'fema' in lower_text
            
            # Match Funding
            p_name_clean = p_name.strip()
            matched_funding = []
            for f in funding_data:
                fn = f['Project_Name'].strip()
                if fn == p_name_clean:
                    matched_funding.append(f)
                elif fn.startswith(p_name_clean) and ('(FEMA' in fn or '(CalOES' in fn or '(CalJPIA' in fn):
                    matched_funding.append(f)
            
            is_related_funding = any('FEMA' in f['Project_Name'] for f in matched_funding)
            
            if is_related_text or is_related_funding:
                for f in matched_funding:
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
