code = """import json
import re

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
    lines = doc['text'].split('\n')
    curr_name = None
    buf = []
    
    for line in lines:
        s = line.strip()
        if not s: continue
        
        if marker in s:
            # check buf for name
            clean_buf = [b for b in buf if 'Agenda' not in b and 'Page' not in b and 'Public Works' not in b]
            if clean_buf:
                cand = clean_buf[-1]
                if cand in valid_names:
                    curr_name = cand
                else:
                    # fuzzy check? 
                    # If valid_names contains cand
                    if cand in valid_names:
                         curr_name = cand
                    else:
                         # Check if cand is superstring of a valid name?
                         # or substring?
                         # Assume cand is the name
                         curr_name = cand
            buf = []
        else:
            buf.append(s)
            if curr_name:
                low = s.lower()
                # Check for Spring 2022
                match = False
                if 'spring 2022' in low: match = True
                if 'march 2022' in low: match = True
                if 'april 2022' in low: match = True
                if 'may 2022' in low: match = True
                
                if match:
                    # Check for start keywords
                    if 'begin' in low or 'start' in low or 'commence' in low:
                        identified.append(curr_name)
                    # if 'advertise' in low: identified.append(curr_name) # debatable

final_projects = list(set(identified))
print('__RESULT__:')
print(json.dumps(final_projects))"""

env_args = {'var_function-call-6062983773300407174': ['civic_docs'], 'var_function-call-8587075472335102739': 'file_storage/function-call-8587075472335102739.json', 'var_function-call-4603789047444994898': ['Funding'], 'var_function-call-8803859908455603463': 'file_storage/function-call-8803859908455603463.json'}

exec(code, env_args)
