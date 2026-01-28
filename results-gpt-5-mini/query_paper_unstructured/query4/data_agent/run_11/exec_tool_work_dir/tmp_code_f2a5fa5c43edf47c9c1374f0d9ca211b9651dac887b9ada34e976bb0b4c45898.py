code = """import json
import re

with open(var_call_UiXFAWxlyIWYkqSXdENiIgwM, 'r', encoding='utf-8') as f:
    docs = json.load(f)

venue_names = ['CHI','Ubicomp','CSCW','DIS','PervasiveHealth','WWW','IUI','OzCHI','TEI','AH']

def extract_year(text):
    if not isinstance(text, str):
        return None
    years = [m for m in re.finditer(r"\b(19|20)\d{2}\b", text)]
    if not years:
        return None
    for ven in venue_names:
        for m in re.finditer(re.escape(ven), text, flags=re.IGNORECASE):
            ven_pos = m.start()
            window_start = max(0, ven_pos-120)
            window_end = ven_pos+120
            for y in years:
                if window_start <= y.start() <= window_end:
                    return int(y.group(0))
    for y in years:
        yy = int(y.group(0))
        if 1990 <= yy <= 2025:
            return yy
    return int(years[0].group(0))

def has_physical_activity(text):
    if not isinstance(text, str):
        return False
    t = text.lower()
    if 'physical activity' in t:
        return True
    if 'physical-activity' in t:
        return True
    if 'physical' in t and 'activity' in t:
        idx_p = t.find('physical')
        idx_a = t.find('activity')
        if abs(idx_p - idx_a) < 40:
            return True
    return False

out = []
for doc in docs:
    title = doc.get('filename','').replace('.txt','')
    text = doc.get('text','')
    y = extract_year(text)
    pa = has_physical_activity(text)
    out.append({'title': title, 'pub_year': y, 'has_physical_activity': pa})

# Return first 200 entries or all if fewer
out = out[:200]
import json as _json
print('__RESULT__:')
print(_json.dumps(out))"""

env_args = {'var_call_xDXDXv7O3Y8IsCnBirJ5usD6': ['paper_docs'], 'var_call_XXKoRyaVMde9ECUXLfDpTQ8d': ['Citations', 'sqlite_sequence'], 'var_call_UiXFAWxlyIWYkqSXdENiIgwM': 'file_storage/call_UiXFAWxlyIWYkqSXdENiIgwM.json', 'var_call_tAhYfbZ5ec3wGmZhugmAT3IR': 'file_storage/call_tAhYfbZ5ec3wGmZhugmAT3IR.json', 'var_call_8lOWLDZODDnFFsHeYPVcUv5P': []}

exec(code, env_args)
