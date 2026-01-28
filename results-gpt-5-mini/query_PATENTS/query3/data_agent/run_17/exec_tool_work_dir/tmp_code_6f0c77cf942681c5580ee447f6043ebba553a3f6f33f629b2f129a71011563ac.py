code = """import json, re
# var_call_ESyf4rKVi5PNp0DQESeG9x1t is the storage key for the query result file path
path = var_call_ESyf4rKVi5PNp0DQESeG9x1t
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
pat_nums = set()
pattern = re.compile(r"pub(?:lication)?\.?\s*(?:number)?\s*[:]?\s*([A-Z]{2}-[A-Za-z0-9\-]+)", re.IGNORECASE)
pattern2 = re.compile(r"publication number\s*[:]?\s*([A-Z]{2}-[A-Za-z0-9\-]+)", re.IGNORECASE)
for rec in data:
    pi = rec.get('Patents_info','')
    for pat in pattern.findall(pi):
        pat_nums.add(pat.strip())
    for pat in pattern2.findall(pi):
        pat_nums.add(pat.strip())
# Also try to capture patterns like 'has publication number US-11421276-B2' or 'with pub. number TW-201925402-A.'
pattern3 = re.compile(r"\b([A-Z]{2}-\d{4,}[A-Z0-9\-]*)\b")
# Limit to those that appear after words 'pub' or 'publication' in string
for rec in data:
    pi = rec.get('Patents_info','')
    for m in pattern3.findall(pi):
        if 'pub' in pi.lower() or 'publication' in pi.lower() or 'pub.' in pi.lower():
            pat_nums.add(m.strip())
pat_nums_list = sorted(pat_nums)
import json
print("__RESULT__:")
print(json.dumps(pat_nums_list))"""

env_args = {'var_call_FYCiQmyJquHDaA3DiPfaYK5x': ['publicationinfo'], 'var_call_mDH52FTLVbIZBVfcBIDocEGU': ['cpc_definition'], 'var_call_ESyf4rKVi5PNp0DQESeG9x1t': 'file_storage/call_ESyf4rKVi5PNp0DQESeG9x1t.json'}

exec(code, env_args)
