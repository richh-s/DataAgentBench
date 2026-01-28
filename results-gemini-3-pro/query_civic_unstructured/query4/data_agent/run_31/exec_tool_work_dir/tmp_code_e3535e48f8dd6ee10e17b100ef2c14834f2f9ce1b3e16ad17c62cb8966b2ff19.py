code = """import json

path_funding = locals()['var_function-call-8803859908455603463']
path_docs = locals()['var_function-call-8587075472335102739']

with open(path_funding, 'r') as f:
    funding_data = json.load(f)

with open(path_docs, 'r') as f:
    docs = json.load(f)

valid_names = set(x['Project_Name'] for x in funding_data)
identified = []
marker = 'cid:190'

for doc in docs:
    lines = doc['text'].splitlines()
    curr_name = None
    buf = []
    
    for line in lines:
        s = line.strip()
        if not s: continue
        
        if marker in s:
            clean_buf = []
            for b in buf:
                if 'Agenda' not in b and 'Page' not in b and 'Public Works' not in b:
                    clean_buf.append(b)
            
            if clean_buf:
                cand = clean_buf[-1]
                # Try to map to valid_names
                if cand in valid_names:
                    curr_name = cand
                else:
                    # check if it matches roughly
                    found = False
                    for vn in valid_names:
                        if cand == vn or cand in vn or vn in cand:
                            curr_name = vn
                            found = True
                            break
                    if not found:
                        curr_name = cand
            buf = []
        else:
            buf.append(s)
            if curr_name:
                low = s.lower()
                match = False
                if 'spring 2022' in low: match = True
                if 'march 2022' in low: match = True
                if 'april 2022' in low: match = True
                if 'may 2022' in low: match = True
                
                if match:
                    # check start
                    if 'begin' in low or 'start' in low:
                        identified.append(curr_name)

final_projects = list(set(identified))
print('__RESULT__:')
print(json.dumps(final_projects))"""

env_args = {'var_function-call-6062983773300407174': ['civic_docs'], 'var_function-call-8587075472335102739': 'file_storage/function-call-8587075472335102739.json', 'var_function-call-4603789047444994898': ['Funding'], 'var_function-call-8803859908455603463': 'file_storage/function-call-8803859908455603463.json'}

exec(code, env_args)
