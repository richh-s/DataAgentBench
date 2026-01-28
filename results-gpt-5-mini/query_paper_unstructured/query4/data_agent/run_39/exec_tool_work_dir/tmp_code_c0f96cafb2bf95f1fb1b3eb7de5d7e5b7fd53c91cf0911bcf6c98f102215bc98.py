code = """import json, re
path = var_call_ypSCdY3MpucsmohKpzfZVJau
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

results = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','')
    # attempt to detect publication year from typical header lines like 'CHI 2016' or '2016'
    year = None
    # look for lines containing '2016' near venue mentions
    if re.search(r"\b2016\b", text):
        year = 2016
    # check for domain term
    if year == 2016 and re.search(r"physical activity", text, re.IGNORECASE):
        results.append({"title": title, "year": year})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_R3Jsc9jJ2f081nEgJYmXt0we': 'file_storage/call_R3Jsc9jJ2f081nEgJYmXt0we.json', 'var_call_CRWoBTvRBnOAaxGATytfY7eg': [], 'var_call_DX5qm54njXAG3VA8Ns0XT0CT': 'file_storage/call_DX5qm54njXAG3VA8Ns0XT0CT.json', 'var_call_oa0IkubHrYmUaxkc3inyJOzE': [], 'var_call_ypSCdY3MpucsmohKpzfZVJau': 'file_storage/call_ypSCdY3MpucsmohKpzfZVJau.json'}

exec(code, env_args)
