code = """import json

file_docs = locals()['var_function-call-990771525359343970']
file_fund = locals()['var_function-call-990771525359343617']

with open(file_docs, 'r') as f:
    docs = json.load(f)
with open(file_fund, 'r') as f:
    funds = json.load(f)

p_map = {x['Project_Name']: int(x['Amount']) for x in funds}
p_names = sorted(list(p_map.keys()), key=len, reverse=True)

found_projects = set()

for d in docs:
    txt = d['text']
    # Find positions
    locs = []
    for p in p_names:
        idx = txt.find(p)
        while idx != -1:
            locs.append((idx, p))
            idx = txt.find(p, idx + 1)
    locs.sort()
    
    for i in range(len(locs)):
        idx, name = locs[i]
        # End at next project or end of text
        end = locs[i+1][0] if i+1 < len(locs) else len(txt)
        # Limit segment length to avoid reading too much if next project is far
        # But here projects are listed sequentially.
        chunk = txt[idx:end].lower()
        
        # Check topic
        if 'park' in name.lower() or 'park' in chunk:
            # Check completion in 2022
            # Indicators: "construction was completed" or "complete construction"
            # And year 2022
            if '2022' in chunk:
                # Check specific phrases
                lines = chunk.split('\n')
                for line in lines:
                    if '2022' in line:
                        if 'complete construction' in line or 'construction was completed' in line or 'construction completed' in line:
                             found_projects.add(name)

total = sum(p_map[n] for n in found_projects)
print('__RESULT__:')
print(json.dumps({'projects': list(found_projects), 'total': total}))"""

env_args = {'var_function-call-990771525359343970': 'file_storage/function-call-990771525359343970.json', 'var_function-call-990771525359343617': 'file_storage/function-call-990771525359343617.json'}

exec(code, env_args)
