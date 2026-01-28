code = """import json, pandas as pd, re
from pathlib import Path

path = Path(var_call_qxJzcYGvhXCQwmx3BhhJM4sv)
recs = json.loads(path.read_text())

def infer_domain(text):
    m = re.search(r"(?im)^\s*domain\s*[:=]\s*(.+)$", text)
    if m:
        dom_line = m.group(1).strip().lower()
        if 'food' in dom_line:
            return True
    # fallback: look for keyword list style
    if re.search(r"(?i)\bfood\b", text):
        # but require it's in a domains/topics context to reduce false positives
        if re.search(r"(?i)domains?\b.*\bfood\b|\bfood\b.*domains?\b", text):
            return True
    return False

food_titles = []
for r in recs:
    txt = r.get('text','')
    if infer_domain(txt):
        fn = r.get('filename','')
        title = fn[:-4] if fn.lower().endswith('.txt') else fn
        food_titles.append(title)

food_titles = sorted(set(food_titles))
print('__RESULT__:')
print(json.dumps({'food_titles': food_titles, 'n_food': len(food_titles)}))"""

env_args = {'var_call_AoxZZ8XBJHoNbaSw5leq6Tzq': ['paper_docs'], 'var_call_qxJzcYGvhXCQwmx3BhhJM4sv': 'file_storage/call_qxJzcYGvhXCQwmx3BhhJM4sv.json'}

exec(code, env_args)
