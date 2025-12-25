code = """import json

# Load UC Patents Info
uc_f = locals()["var_function-call-163982095095483053"]
with open(uc_f, "r") as f:
    uc_data = json.load(f)

uc_pubs = set()
for row in uc_data:
    words = row["Patents_info"].replace(".", " ").replace(",", " ").split()
    for i, w in enumerate(words):
        if "-" in w and len(w)>5 and w[0].isupper():
            if i>0 and words[i-1].lower() in ["number", "no"]:
                uc_pubs.add(w)

all_f = locals()["var_function-call-12118947113934152352"]
with open(all_f, "r") as f:
    all_data = json.load(f)

citing = {} 

def get_assignee(text):
    text = text.replace(chr(10), " ")
    if " holds the " in text: return text.split(" holds the ")[0].strip()
    if " owned by " in text: return text.split(" owned by ")[1].split(" and ")[0].split(" with ")[0].strip()
    if " assigned to " in text: return text.split(" assigned to ")[1].split(" and ")[0].split(" with ")[0].strip()
    if " belonging to " in text: return text.split(" belonging to ")[1].split(" and ")[0].split(" with ")[0].strip()
    if " held by " in text: return text.split(" held by ")[1].split(" and ")[0].split(",")[0].strip()
    return None

def get_sub(cpc_str):
    try:
        cpc = json.loads(cpc_str)
        if not cpc: return []
        codes = set()
        prims = [x for x in cpc if x.get("first")==True]
        if not prims: prims = [cpc[0]]
        for p in prims:
            if "code" in p: codes.add(p["code"][:4])
        return list(codes)
    except: return []

for row in all_data:
    try:
        cits = json.loads(row["citation"])
    except: continue
    
    cited = False
    for c in cits:
        if c.get("publication_number") in uc_pubs:
            cited = True
            break
            
    if cited:
        ass = get_assignee(row["Patents_info"])
        if ass:
            ass = ass.strip()
            if "UNIV CALIFORNIA" in ass: continue
            subs = get_sub(row["cpc"])
            if subs:
                if ass not in citing: citing[ass] = set()
                for s in subs: citing[ass].add(s)

res = []
all_subs = set()
for k, v in citing.items():
    res.append({"assignee": k, "subclasses": list(v)})
    all_subs.update(v)

print("__RESULT__:")
print(json.dumps({"assignees": res, "all_subclasses": list(all_subs)}))"""

env_args = {'var_function-call-3523691000772885977': 'file_storage/function-call-3523691000772885977.json', 'var_function-call-163982095095483053': 'file_storage/function-call-163982095095483053.json', 'var_function-call-7359064648347536263': ['AU-2898989-A', 'US-2023279470-A1', 'CN-101584047-A', 'US-2020025859-A1', 'US-7745569-B2', 'CN-102584712-A', 'KR-20200041324-A', 'US-2018304537-A1', 'KR-20180041236-A', 'US-2021282642-A1'], 'var_function-call-8038203737880887453': [{'cnt': '277813'}], 'var_function-call-12118947113934152352': 'file_storage/function-call-12118947113934152352.json', 'var_function-call-18096850190734713902': [{'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B35/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0565', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0562', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01G45/006', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0566', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/052', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01P2002/76', 'first': False, 'inventive': False, 'tree': []}, {'code': 'C01G45/006', 'first': False, 'inventive': True, 'tree': []}, {'code': 'Y02E60/10', 'first': False, 'inventive': False, 'tree': []}, {'code': 'C01P2002/76', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M10/0525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M2004/028', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M4/1315', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M2004/021', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M4/525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B33/00', 'first': True, 'inventive': True, 'tree': []}, {'code': 'H01M4/1315', 'first': True, 'inventive': True, 'tree': []}, {'code': 'H01M4/525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M4/505', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M4/505', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B35/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M4/582', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B35/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M4/525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01P2002/76', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M4/1315', 'first': True, 'inventive': True, 'tree': []}, {'code': 'H01M10/0562', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M2004/028', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M4/505', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0565', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M2004/021', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M10/0525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0566', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/052', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01G45/006', 'first': False, 'inventive': True, 'tree': []}], 'var_function-call-5526764884293808686': 'test'}

exec(code, env_args)
