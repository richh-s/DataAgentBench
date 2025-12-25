code = """import json, re, pandas as pd
from datetime import datetime

# load large results
with open(var_call_UEoqViEfn6TO0tMYSyhmsByh, 'r') as f:
    pubs = json.load(f)
with open(var_call_tPObFac4aRP32NJiUPqVvtSb, 'r') as f:
    cpc_defs = json.load(f)

# helper to extract country code "country_code XX" or "country code: XX" or "country code XX" from Patents_info
cc_re = re.compile(r"country[_ ]code[: ]\s*([A-Z]{2})")

def get_country(info):
    if not info:
        return None
    m = cc_re.search(info)
    return m.group(1) if m else None

# parse natural language date, expect formats like "3rd August 2021", "dated 6th October 2020", "21st of September, 2021"
months = {m: i for i, m in enumerate(["January","February","March","April","May","June","July","August","September","October","November","December"], 1)}

ord_re = re.compile(r"(\d+)(st|nd|rd|th)?")


def parse_date(s):
    if not s:
        return None
    s = s.strip()
    s = re.sub(r"^dated ", "", s, flags=re.IGNORECASE)
    s = s.replace(",", "")
    parts = s.split()
    if len(parts) < 3:
        return None
    # find day
    day_m = ord_re.match(parts[0])
    if not day_m:
        return None
    day = int(day_m.group(1))
    # month is next or skipping 'of'
    if parts[1].lower() == 'of' and len(parts) >= 4:
        month_name = parts[2]
        year = int(parts[3])
    else:
        month_name = parts[1]
        year = int(parts[2])
    month = months.get(month_name)
    if not month:
        return None
    try:
        return datetime(year, month, day)
    except Exception:
        return None

# filter to Germany, granted in H2 2019
filtered = []
for r in pubs:
    cc = get_country(r.get('Patents_info',''))
    if cc != 'DE':
        continue
    gd = parse_date(r.get('grant_date'))
    if not gd:
        continue
    if not (gd.year == 2019 and gd.month >= 7):
        continue
    filtered.append({'grant_date': gd, 'cpc': r.get('cpc')})

# if no filtered patents, return message
if not filtered:
    result = {"error": "No German patents granted in H2 2019 found in dataset given available fields."}
else:
    # explode CPC codes
    rows = []
    for r in filtered:
        cpc_list_str = r['cpc']
        try:
            cpc_list = json.loads(cpc_list_str)
        except Exception:
            continue
        for entry in cpc_list:
            code = entry.get('code')
            if not code:
                continue
            # level-4 group code is first 3 characters (like B29, H04, etc.)
            group4 = code[:3]
            rows.append({'year': r['grant_date'].year, 'group4': group4})

    if not rows:
        result = {"error": "No CPC codes parsed for German patents in H2 2019."}
    else:
        df = pd.DataFrame(rows)
        counts = df.groupby(['group4','year']).size().reset_index(name='count')
        # compute EMA over years per group with alpha=0.1, sorted by year
        alpha = 0.1
        ema_records = []
        for g, sub in counts.groupby('group4'):
            sub = sub.sort_values('year')
            ema = None
            for _, row in sub.iterrows():
                c = row['count']
                if ema is None:
                    ema = c
                else:
                    ema = alpha * c + (1-alpha) * ema
                ema_records.append({'group4': g, 'year': int(row['year']), 'ema': float(ema)})
        ema_df = pd.DataFrame(ema_records)
        # get best year per group (max ema)
        idx = ema_df.groupby('group4')['ema'].idxmax()
        best = ema_df.loc[idx]
        # map titles from cpc_defs
        defs_df = pd.DataFrame(cpc_defs)
        defs_df['level'] = defs_df['level'].astype(float)
        defs4 = defs_df[defs_df['level'] == 4.0][['symbol','titleFull']].drop_duplicates()
        merged = best.merge(defs4, left_on='group4', right_on='symbol', how='left')
        merged = merged.sort_values('ema', ascending=False)
        result = []
        for _, row in merged.iterrows():
            result.append({
                'cpc_group_code': row['group4'],
                'titleFull': row.get('titleFull'),
                'best_year': int(row['year']),
                'ema_patent_filings': row['ema']
            })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_UEoqViEfn6TO0tMYSyhmsByh': 'file_storage/call_UEoqViEfn6TO0tMYSyhmsByh.json', 'var_call_tPObFac4aRP32NJiUPqVvtSb': 'file_storage/call_tPObFac4aRP32NJiUPqVvtSb.json'}

exec(code, env_args)
