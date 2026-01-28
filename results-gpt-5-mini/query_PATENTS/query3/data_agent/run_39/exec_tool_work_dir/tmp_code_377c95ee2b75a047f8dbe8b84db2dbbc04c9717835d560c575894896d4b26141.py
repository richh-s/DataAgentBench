code = """import json, re
# var_call_teNtoCHZkRPcqi3NXSIAqDMd is a path to the JSON file with UC-owned patent records
p = var_call_teNtoCHZkRPcqi3NXSIAqDMd
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)
# Extract publication numbers from Patents_info using regex
pub_nums = set()
pat = re.compile(r"\b[A-Z]{2}-\d{4,}[A-Z0-9\-]*\b")
for rec in data:
    info = rec.get('Patents_info','')
    for m in pat.findall(info):
        pub_nums.add(m)
# Fallback: also look for patterns like 'pub. number ' followed by token
pat2 = re.compile(r"pub\. number\s+([A-Za-z0-9\-]+)", re.IGNORECASE)
for rec in data:
    info = rec.get('Patents_info','')
    for m in pat2.findall(info):
        pub_nums.add(m)
# Prepare JSON serializable list
pub_list = sorted(pub_nums)
print("__RESULT__:")
print(json.dumps(pub_list))"""

env_args = {'var_call_uDiYoolU3jAQpH2wMff8iPIt': ['publicationinfo'], 'var_call_GlGC2BtHSHcOnyHn5dstNfTH': ['cpc_definition'], 'var_call_teNtoCHZkRPcqi3NXSIAqDMd': 'file_storage/call_teNtoCHZkRPcqi3NXSIAqDMd.json'}

exec(code, env_args)
