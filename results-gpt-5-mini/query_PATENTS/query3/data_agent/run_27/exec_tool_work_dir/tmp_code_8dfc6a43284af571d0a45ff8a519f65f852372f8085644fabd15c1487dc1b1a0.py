code = """import json, re
# var_call_JWwOoz2mOIB25IYurOvjgP1M is the storage key containing the JSON file path
path = var_call_JWwOoz2mOIB25IYurOvjgP1M
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
pub_nums = set()
for rec in data:
    pi = rec.get('Patents_info','')
    # look for patterns like 'pub. number X' or 'pub. number X.' or 'with pub. number X.'
    m = re.search(r'pub\. number\s+([A-Z0-9\-]+)', pi)
    if m:
        pub_nums.add(m.group(1))
    m2 = re.search(r'publication number\s+([A-Z0-9\-]+)', pi)
    if m2:
        pub_nums.add(m2.group(1))
    # also sometimes 'has publication number X' or 'has pub. number X'
    m3 = re.search(r'has (?:pub(?:lication)?\. ?number)\s+([A-Z0-9\-]+)', pi)
    if m3:
        pub_nums.add(m3.group(1))

# fallback: also check title_localized for 'pub. number' but unlikely
result = sorted(pub_nums)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_RI57H59YoXXdiFWZsUYvmLDR': ['publicationinfo'], 'var_call_pKbEylT8SZftCAfPr1MfqEdM': ['cpc_definition'], 'var_call_JWwOoz2mOIB25IYurOvjgP1M': 'file_storage/call_JWwOoz2mOIB25IYurOvjgP1M.json'}

exec(code, env_args)
