code = """import json, pandas as pd, re

biz_src = var_call_B8LCcXU6KbW3JWTPMcvjlQai
if isinstance(biz_src, str):
    with open(biz_src, 'r', encoding='utf-8') as f:
        biz = json.load(f)
else:
    biz = biz_src

rev_src = var_call_ld23lZb7UmVdFsh1vdKAqxw0
if isinstance(rev_src, str):
    with open(rev_src, 'r', encoding='utf-8') as f:
        rev = json.load(f)
else:
    rev = rev_src

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
avg_df = rev_df.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})

weekday_set = {'monday','tuesday','wednesday','thursday','friday'}

def parse_close_after_6(hours_str):
    if hours_str is None:
        return False
    if isinstance(hours_str, str) and hours_str.strip().lower() == 'none':
        return False
    try:
        arr = json.loads(hours_str) if isinstance(hours_str, str) else hours_str
    except Exception:
        return False
    if not isinstance(arr, list):
        return False
    for item in arr:
        if not (isinstance(item, list) and len(item) >= 2):
            continue
        day = str(item[0]).strip().lower()
        if day not in weekday_set:
            continue
        times = str(item[1])
        t = times.lower()
        if 'open 24 hours' in t:
            return True
        if 'closed' in t:
            continue
        ranges = re.split(r'\s*,\s*', times)
        for rr in ranges:
            if '–' in rr:
                parts = rr.split('–')
            elif '-' in rr:
                parts = rr.split('-')
            else:
                continue
            end = parts[-1].strip()
            m = re.match(r'^(\d{1,2})(?::(\d{2}))?\s*(AM|PM)$', end, re.IGNORECASE)
            if not m:
                continue
            hh = int(m.group(1))
            mm = int(m.group(2) or 0)
            ap = m.group(3).upper()
            if ap == 'PM' and hh != 12:
                hh += 12
            if ap == 'AM' and hh == 12:
                hh = 0
            minutes = hh*60 + mm
            if minutes > 18*60:
                return True
    return False

biz_df['open_after_6_weekday'] = biz_df['hours'].apply(parse_close_after_6)
filtered = biz_df[biz_df['open_after_6_weekday']].copy()

merged = filtered.merge(avg_df, on='gmap_id', how='left')
merged = merged.dropna(subset=['avg_rating'])
merged = merged.sort_values(['avg_rating','name'], ascending=[False, True]).head(5)

out_lines = []
for _, row in merged.iterrows():
    out_lines.append(f"{row['name']} | Avg rating: {row['avg_rating']:.2f} | Hours: {row['hours']}")

result = "\n".join(out_lines) if out_lines else "No matching businesses found."
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_8dkAC9TO6HNMZWO3MspMoqfI': [], 'var_call_ld23lZb7UmVdFsh1vdKAqxw0': 'file_storage/call_ld23lZb7UmVdFsh1vdKAqxw0.json', 'var_call_N5i5v8D8wI1sirgR4x3bIWlX': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'state': 'Open now'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_call_B8LCcXU6KbW3JWTPMcvjlQai': 'file_storage/call_B8LCcXU6KbW3JWTPMcvjlQai.json'}

exec(code, env_args)
