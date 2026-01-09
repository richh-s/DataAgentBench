code = """import json, re
import pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

papers = load_json_maybe(var_call_0OfMBdbV5cVzriuY9i6t6L8u)
cites = load_json_maybe(var_call_VBinrQYEv9PVOnmqCxt1kkuV)

# Extract publication year from text
year_pat = re.compile(r"\b(19|20)\d{2}\b")

def extract_pub_year(text):
    # prefer explicit copyright year or venue year patterns
    m = re.search(r"Copyright\s+(?:\D{0,10})?((?:19|20)\d{2})", text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r"\b(?:CHI|UbiComp|UBICOMP|CSCW|DIS|IUI|WWW|TEI|AH)\s*'?\s*(\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy < 50 else 1900 + yy
    # fallback: first year-like token in header portion
    header = text[:2000]
    yrs = [int(x) for x in year_pat.findall(header)]
    # year_pat.findall returns tuples due to group; fix
    return None

# Fix year extraction: use finditer

def extract_pub_year(text):
    m = re.search(r"Copyright\s+\D{0,20}((?:19|20)\d{2})", text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r"\b(?:CHI|UbiComp|UBICOMP|CSCW|DIS|IUI|WWW|TEI|AH)\s*'?\s*(\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy < 50 else 1900 + yy
    header = text[:2500]
    years = [int(mi.group(0)) for mi in year_pat.finditer(header)]
    if years:
        # choose most frequent in header; else first
        ser = pd.Series(years)
        return int(ser.mode().iloc[0])
    return None

# Determine domain physical activity via keyword
pa_pat = re.compile(r"physical activity", flags=re.IGNORECASE)

def is_physical_activity_domain(text):
    # Heuristic: check for 'Physical Activity' in keywords/author keywords section, or repeated mention
    if re.search(r"Author Keywords[\s\S]{0,400}physical activity", text, flags=re.IGNORECASE):
        return True
    if re.search(r"Keywords[\s\S]{0,400}physical activity", text, flags=re.IGNORECASE):
        return True
    # otherwise require multiple mentions
    return len(pa_pat.findall(text[:5000])) >= 2 or len(pa_pat.findall(text)) >= 5

rows=[]
for d in papers:
    title = d['filename'][:-4] if d.get('filename','').lower().endswith('.txt') else d.get('filename')
    text = d.get('text','') or ''
    if not is_physical_activity_domain(text):
        continue
    yr = extract_pub_year(text)
    if yr == 2016:
        rows.append({'title': title})

pa2016 = pd.DataFrame(rows).drop_duplicates()

citedf = pd.DataFrame(cites)
if not citedf.empty:
    citedf['total_citations'] = pd.to_numeric(citedf['total_citations'], errors='coerce')

out = pa2016.merge(citedf, on='title', how='left').fillna({'total_citations':0})
out['total_citations'] = out['total_citations'].astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_VBinrQYEv9PVOnmqCxt1kkuV': 'file_storage/call_VBinrQYEv9PVOnmqCxt1kkuV.json', 'var_call_0OfMBdbV5cVzriuY9i6t6L8u': 'file_storage/call_0OfMBdbV5cVzriuY9i6t6L8u.json'}

exec(code, env_args)
