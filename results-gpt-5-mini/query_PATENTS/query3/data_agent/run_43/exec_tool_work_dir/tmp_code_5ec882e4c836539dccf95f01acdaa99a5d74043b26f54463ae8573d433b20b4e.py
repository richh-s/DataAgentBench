code = """import json, re
# var_call_TbqAJZFKU2tYJY3RZLuEn1w5 is provided by storage
path = var_call_TbqAJZFKU2tYJY3RZLuEn1w5
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
pub_nums = set()
pat = re.compile(r'\b[A-Z]{2}-[0-9A-Za-z\-/]+[A-Z0-9]\b')
# Also capture patterns like 'US11466906B2' without dashes? but examples have dashes.
for rec in data:
    pi = rec.get('Patents_info','')
    if pi:
        for m in pat.findall(pi):
            pub_nums.add(m)
# Also search in title_localized or other fields for publication numbers
# Convert to sorted list
pub_list = sorted(pub_nums)
import json
print("__RESULT__:")
print(json.dumps(pub_list))"""

env_args = {'var_call_TbqAJZFKU2tYJY3RZLuEn1w5': 'file_storage/call_TbqAJZFKU2tYJY3RZLuEn1w5.json'}

exec(code, env_args)
