code = """import json, re
from statistics import mean

with open(var_call_Xhb32TnSssbYltGVfMFXepD9, 'r') as f:
    citations = json.load(f)
with open(var_call_uRzir7brgVXNmmgbU8QXkL6s, 'r') as f:
    docs = json.load(f)

acm_titles = set()
for d in docs:
    filename = d.get('filename', '')
    title = filename.rsplit('.txt', 1)[0]
    text = d.get('text', '')
    pattern = r'Copyright\s+\d{4}[^\n]*ACM'
    if re.search(pattern, text, re.IGNORECASE) or 'Association for Computing Machinery' in text or 'ACM 978' in text:
        acm_titles.add(title)

vals = []
for c in citations:
    title = c.get('title')
    if title in acm_titles:
        try:
            vals.append(int(c.get('citation_count', 0)))
        except Exception:
            pass

avg = mean(vals) if vals else 0

res = json.dumps(avg)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_Xhb32TnSssbYltGVfMFXepD9': 'file_storage/call_Xhb32TnSssbYltGVfMFXepD9.json', 'var_call_uRzir7brgVXNmmgbU8QXkL6s': 'file_storage/call_uRzir7brgVXNmmgbU8QXkL6s.json'}

exec(code, env_args)
