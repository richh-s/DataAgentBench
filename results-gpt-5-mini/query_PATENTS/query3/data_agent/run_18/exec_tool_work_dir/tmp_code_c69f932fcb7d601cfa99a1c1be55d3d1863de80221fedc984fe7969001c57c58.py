code = """import json
path = var_call_VJd2BQjoEG4GoMrradXkpv3s
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
# extract publication_number from Patents_info where pattern like pub. number XXX
import re
pub_nums = []
for rec in data:
    pi = rec.get('Patents_info','')
    # look for patterns like pub. number US-2022074631-A1 or publication number US-11421276-B2
    m = re.findall(r'pub(?:\.lic|lication)?(?:\snumber)?\s*[:]?\s*([A-Z]{2}-[0-9A-Za-z-]+)', pi, flags=re.IGNORECASE)
    if not m:
        # try find US-...-A1 or B2 generally
        m = re.findall(r'(US-[0-9A-Za-z-]+)', pi)
    for mm in m:
        pub_nums.append(mm)
# Also sometimes include pub. number in any case; also look for pub. number pattern with country code
m_all = []
# fallback: try any pattern like [A-Z]{2}-\d{4,}
for rec in data:
    pi = rec.get('Patents_info','')
    found = re.findall(r'([A-Z]{2}-\d{4,}[0-9A-Za-z-]*)', pi)
    for mm in found:
        m_all.append(mm)
for mm in m_all:
    if mm not in pub_nums:
        pub_nums.append(mm)
# dedupe
pub_nums = list(dict.fromkeys(pub_nums))
# limit to first 60 to keep manageable
pub_nums = pub_nums[:60]
print("__RESULT__:")
print(json.dumps(pub_nums))"""

env_args = {'var_call_VJd2BQjoEG4GoMrradXkpv3s': 'file_storage/call_VJd2BQjoEG4GoMrradXkpv3s.json'}

exec(code, env_args)
