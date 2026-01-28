code = """import json, re
# var_call_MuJAaiO2PzoIYGskQYaoTn64 is the storage key for the initial query result file path
fp = var_call_MuJAaiO2PzoIYGskQYaoTn64
with open(fp, 'r', encoding='utf-8') as f:
    data = json.load(f)
pub_nums = set()
for rec in data:
    pi = rec.get('Patents_info','')
    # look for patterns like 'pub. number XXXX', 'pub. number: XXXX', 'publication number XXXX', 'publication number: XXXX'
    m = re.search(r'pub(?:\.|lication)?\s*(?:number)?[:\s]*([A-Z0-9-]+)', pi, flags=re.IGNORECASE)
    if m:
        pub_nums.add(m.group(1))
    else:
        # fallback: look for patterns like 'pub. number <id>' repeated
        for m2 in re.finditer(r'pub\. number\s*([A-Z0-9-]+)', pi, flags=re.IGNORECASE):
            pub_nums.add(m2.group(1))
# also check citation fields in these UNIV CA records to capture their publication_numbers if present
for rec in data:
    cit = rec.get('citation')
    if cit:
        try:
            c = json.loads(cit)
            for item in c:
                pn = item.get('publication_number')
                if pn:
                    pub_nums.add(pn)
        except Exception:
            # if citation not json, try regex
            for m in re.finditer(r'([A-Z]{2}-?\d+[A-Z0-9\-]*)', str(cit)):
                pub_nums.add(m.group(1))

pub_nums = sorted(x for x in pub_nums if x)
out = {'publication_numbers': pub_nums}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_MuJAaiO2PzoIYGskQYaoTn64': 'file_storage/call_MuJAaiO2PzoIYGskQYaoTn64.json'}

exec(code, env_args)
