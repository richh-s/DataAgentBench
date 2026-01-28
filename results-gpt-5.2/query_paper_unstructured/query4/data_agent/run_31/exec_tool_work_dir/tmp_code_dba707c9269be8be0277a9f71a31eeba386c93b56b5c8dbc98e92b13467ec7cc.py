code = """import json, re
import pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

papers = load_json_maybe(var_call_vLIdXE2BTcOmkjKEYDPomsPy)
cits = load_json_maybe(var_call_yK1pviTcsmJkeBtrsfSWIxc6)

cit_df = pd.DataFrame(cits)
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)
cit_map = dict(zip(cit_df['title'], cit_df['total_citations']))

copyright_re = re.compile(r'Copyright\s+(?:\(c\)\s*)?(20\d{2})', re.IGNORECASE)
venue_year_re = re.compile(r'\b(?:CHI|CSCW|UbiComp|UBICOMP|DIS|IUI|WWW|TEI|AH|PervasiveHealth)[^\n\r]{0,40}?(\b\d{2}\b)')

def is_physical_activity(text):
    return re.search(r'physical\s+activity', text, flags=re.IGNORECASE) is not None

def extract_year(text):
    m = copyright_re.search(text)
    if m:
        return int(m.group(1))
    m = venue_year_re.search(text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy
    for m in re.finditer(r'\b(20\d{2})\b', text[:3000]):
        y = int(m.group(1))
        if 2000 <= y <= 2026:
            return y
    return None

rows = []
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','') or ''
    if not is_physical_activity(text):
        continue
    y = extract_year(text)
    if y != 2016:
        continue
    total_cit = int(cit_map.get(title, 0))
    rows.append({'title': title, 'total_citations': total_cit})

res_df = pd.DataFrame(rows).drop_duplicates(subset=['title'])
if len(res_df):
    res_df = res_df.sort_values(['total_citations','title'], ascending=[False, True])
result = res_df.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_vLIdXE2BTcOmkjKEYDPomsPy': 'file_storage/call_vLIdXE2BTcOmkjKEYDPomsPy.json', 'var_call_yK1pviTcsmJkeBtrsfSWIxc6': 'file_storage/call_yK1pviTcsmJkeBtrsfSWIxc6.json'}

exec(code, env_args)
