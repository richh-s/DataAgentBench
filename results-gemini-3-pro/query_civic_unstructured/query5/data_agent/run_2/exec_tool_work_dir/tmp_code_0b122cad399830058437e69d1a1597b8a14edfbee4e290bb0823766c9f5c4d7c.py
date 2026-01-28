code = """import json
import re

civic_path = locals()['var_function-call-9021704853761821384']
funding_path = locals()['var_function-call-17294341897624108968']

with open(civic_path, 'r') as f:
    civic = json.load(f)
with open(funding_path, 'r') as f:
    funding = json.load(f)

funding_map = {}
for row in funding:
    nm = row['Project_Name'].strip()
    amt = row['Amount']
    if nm in funding_map:
        funding_map[nm] += int(amt)
    else:
        funding_map[nm] = int(amt)

extracted = []

for doc in civic:
    lines = doc['text'].splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i+=1
            continue
            
        is_p = False
        if line in funding_map:
            is_p = True
        else:
            j = i + 1
            while j < len(lines):
                peek = lines[j].strip()
                if peek:
                    if '(cid:190)' in peek or peek.startswith('Updates:') or peek.startswith('Project Description:'):
                        is_p = True
                    break
                j += 1
        
        if is_p:
            p_name = line
            block = []
            k = i + 1
            while k < len(lines):
                nav = lines[k].strip()
                if 'Capital Improvement Projects' in nav and ('(Design)' in nav or '(Construction)' in nav or '(Not Started)' in nav):
                    break
                
                # Check if nav is a known project name
                if nav in funding_map and nav != p_name:
                    # Likely a new project
                    break
                    
                # Check marker lookahead
                m = k + 1
                is_next = False
                while m < len(lines):
                    pk = lines[m].strip()
                    if pk:
                        if '(cid:190)' in pk and not '(cid:190)' in nav:
                            # If nav is not a project name candidate (e.g. just text), but next is marker
                            # Then nav might be the project name.
                            # So current block ends.
                            is_next = True
                        break
                    m += 1
                if is_next:
                    break
                
                block.append(lines[k])
                k += 1
            
            blk_txt = ' '.join(block) 
            
            start_year = None
            
            # Simple substring checks for date
            # "Begin Construction: ... 2022"
            # "Start Date: ... 2022"
            # "commence during ... 2022"
            # "beginning in ... 2022"
            # "started ... 2022"
            
            check_str = blk_txt
            if "Begin Construction" in check_str:
                idx = check_str.find("Begin Construction")
                sub = check_str[idx:idx+50]
                if "2022" in sub:
                    start_year = 2022
            
            if not start_year and "Start Date" in check_str:
                idx = check_str.find("Start Date")
                sub = check_str[idx:idx+50]
                if "2022" in sub:
                    start_year = 2022
            
            if not start_year and "commence during" in check_str:
                idx = check_str.find("commence during")
                sub = check_str[idx:idx+50]
                if "2022" in sub:
                    start_year = 2022

            if not start_year and "beginning in" in check_str:
                idx = check_str.find("beginning in")
                sub = check_str[idx:idx+50]
                if "2022" in sub:
                    start_year = 2022

            if not start_year and "started" in check_str:
                # "started ... 2022"
                idx = check_str.find("started")
                sub = check_str[idx:idx+50] # Check next 50 chars
                if "2022" in sub:
                    start_year = 2022
            
            is_disaster = False
            d_kws = ['FEMA', 'CalOES', 'Woolsey', 'Disaster', 'Emergency']
            if any(kw in p_name for kw in d_kws) or any(kw in blk_txt for kw in d_kws):
                is_disaster = True
            
            extracted.append({
                'name': p_name,
                'start_year': start_year,
                'is_disaster': is_disaster
            })
            
            i = k
        else:
            i += 1

total_funding = 0
matched_projects = []

for p in extracted:
    if p['is_disaster'] and p['start_year'] == 2022:
        amt = funding_map.get(p['name'], 0)
        if amt > 0:
            total_funding += amt
            matched_projects.append(p['name'])

print('__RESULT__:')
print(json.dumps({'total_funding': total_funding, 'projects': matched_projects}))"""

env_args = {'var_function-call-4835809069730370506': ['Funding'], 'var_function-call-4835809069730370969': ['civic_docs'], 'var_function-call-17294341897624108968': 'file_storage/function-call-17294341897624108968.json', 'var_function-call-17294341897624106339': 'file_storage/function-call-17294341897624106339.json', 'var_function-call-9021704853761821384': 'file_storage/function-call-9021704853761821384.json', 'var_function-call-16225886592360458391': 'file_storage/function-call-16225886592360458391.json'}

exec(code, env_args)
