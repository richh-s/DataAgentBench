code = """import json

path_d = locals()["var_function-call-990771525359343970"]
path_f = locals()["var_function-call-990771525359343617"]

with open(path_d, "r") as f:
    docs = json.load(f)
with open(path_f, "r") as f:
    funds = json.load(f)

p_map = {x["Project_Name"]: int(x["Amount"]) for x in funds}
p_list = sorted(p_map.keys(), key=len, reverse=True)

found = set()

for doc in docs:
    txt = doc["text"]
    starts = []
    for p in p_list:
        i = txt.find(p)
        while i != -1:
            starts.append((i, p))
            i = txt.find(p, i+1)
    starts.sort()
    
    for k in range(len(starts)):
        idx, name = starts[k]
        end = starts[k+1][0] if k+1 < len(starts) else len(txt)
        chunk = txt[idx:end].lower()
        
        is_park = "park" in name.lower() or "park" in chunk
        if is_park:
            lines = chunk.split("\n")
            for line in lines:
                if "2022" in line:
                    if "construction" in line and "completed" in line:
                         found.add(name)

total = sum(p_map[n] for n in found)
res = {"t": total, "p": list(found)}
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-990771525359343970': 'file_storage/function-call-990771525359343970.json', 'var_function-call-990771525359343617': 'file_storage/function-call-990771525359343617.json'}

exec(code, env_args)
