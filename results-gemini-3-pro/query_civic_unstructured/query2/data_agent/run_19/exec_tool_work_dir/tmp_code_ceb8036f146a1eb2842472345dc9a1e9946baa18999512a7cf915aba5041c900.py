code = """import json

path_doc = locals()['var_function-call-990771525359343970']
path_fund = locals()['var_function-call-990771525359343617']

with open(path_doc, 'r') as f:
    d_list = json.load(f)
with open(path_fund, 'r') as f:
    f_list = json.load(f)

p_dict = {}
for x in f_list:
    p_dict[x['Project_Name']] = int(x['Amount'])

p_names = list(p_dict.keys())
p_names.sort(key=len, reverse=True)

final_set = set()

for d in d_list:
    full_text = d['text']
    offsets = []
    for nm in p_names:
        idx = full_text.find(nm)
        while idx != -1:
            offsets.append((idx, nm))
            idx = full_text.find(nm, idx + 1)
    offsets.sort()

    for k in range(len(offsets)):
        start_i = offsets[k][0]
        name = offsets[k][1]
        
        if k + 1 < len(offsets):
            end_i = offsets[k+1][0]
        else:
            end_i = len(full_text)
            
        part = full_text[start_i:end_i].lower()
        
        cond_topic = 'park' in name.lower() or 'park' in part
        
        if cond_topic:
            if '2022' in part:
                lines = part.split('\n')
                for ln in lines:
                    if '2022' in ln:
                        c1 = 'complete construction' in ln
                        c2 = 'construction was completed' in ln
                        c3 = 'construction completed' in ln
                        if c1 or c2 or c3:
                            final_set.add(name)

tot = sum(p_dict[n] for n in final_set)
res = {'ans': tot, 'proj': list(final_set)}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_function-call-990771525359343970': 'file_storage/function-call-990771525359343970.json', 'var_function-call-990771525359343617': 'file_storage/function-call-990771525359343617.json'}

exec(code, env_args)
