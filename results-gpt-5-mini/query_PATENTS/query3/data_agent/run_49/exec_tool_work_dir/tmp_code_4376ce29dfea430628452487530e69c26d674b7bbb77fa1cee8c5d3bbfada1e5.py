code = """import json, re
# var_call_npUMUKEmpDiHTFu2GVHD1Vg3 is the storage key for the previous query_db result file path
path = var_call_npUMUKEmpDiHTFu2GVHD1Vg3
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
pub_nums = set()
pat = re.compile(r'(?:pub(?:\.|lication)? number|publication number|pub\. number|publication no\.|pub no\.)\s*([A-Z0-9\-]+)', re.IGNORECASE)
for rec in data:
    txt = rec.get('Patents_info','')
    m = pat.search(txt)
    if m:
        pub_nums.add(m.group(1).strip())
# Also try to capture patterns like 'publication number US-11421276-B2' without the leading label
# and patterns like 'publication number US-11421276-B2.' already covered. If none found, try to find tokens like 'pub. number' variations already done.
# Convert to sorted list
pub_list = sorted(pub_nums)
import json
print("__RESULT__:")
print(json.dumps(pub_list))"""

env_args = {'var_call_npUMUKEmpDiHTFu2GVHD1Vg3': 'file_storage/call_npUMUKEmpDiHTFu2GVHD1Vg3.json'}

exec(code, env_args)
