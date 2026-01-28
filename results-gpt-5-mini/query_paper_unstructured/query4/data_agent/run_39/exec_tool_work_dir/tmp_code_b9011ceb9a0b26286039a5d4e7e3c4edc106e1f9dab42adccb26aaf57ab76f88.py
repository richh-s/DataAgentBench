code = """import json, re
path = var_call_DX5qm54njXAG3VA8Ns0XT0CT
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

results = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','')
    # find years in text
    years = re.findall(r"\b(?:19|20)\d{2}\b", text)
    year = None
    if years:
        # try to find '2016' specifically; otherwise take first occurrence
        if '2016' in years:
            year = 2016
        else:
            year = int(years[0])
    # check domain mention
    if year == 2016 and re.search(r"physical activity", text, re.IGNORECASE):
        results.append({"title": title, "year": year})

# deduplicate
unique = {r['title']: r for r in results}
out = list(unique.values())
import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_R3Jsc9jJ2f081nEgJYmXt0we': 'file_storage/call_R3Jsc9jJ2f081nEgJYmXt0we.json', 'var_call_CRWoBTvRBnOAaxGATytfY7eg': [], 'var_call_DX5qm54njXAG3VA8Ns0XT0CT': 'file_storage/call_DX5qm54njXAG3VA8Ns0XT0CT.json'}

exec(code, env_args)
