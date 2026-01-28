code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub = load_records(var_call_Ci7QE5Ao8guCBeLVQnOZGbwF)
defs = load_records(var_call_lwUd1tCAYUIMf5mAUJQnpbBx)

df_pub = pd.DataFrame(pub)

def parse_year(s):
    if s is None:
        return None
    m = re.search(r'(19|20)\d{2}', str(s))
    return int(m.group(0)) if m else None

def parse_cpc_list(s):
    if not s:
        return []
    try:
        arr = json.loads(s)
        codes = []
        for o in arr:
            c = o.get('code')
            if c:
                codes.append(c)
        return codes
    except Exception:
        return []

df_pub['filing_year'] = df_pub['filing_date'].apply(parse_year)
df_pub['cpc_codes'] = df_pub['cpc'].apply(parse_cpc_list)

# explode to codes
rows = []
for _, r in df_pub.iterrows():
    y = r['filing_year']
    if y is None:
        continue
    for code in r['cpc_codes']:
        # level 4 group: first 4 chars like H04W
        g = re.match(r'^([A-HY]\d{2}[A-Z])', code)
        if g:
            rows.append((g.group(1), y))

d = pd.DataFrame(rows, columns=['cpc4','year'])

# yearly counts
counts = d.groupby(['cpc4','year']).size().reset_index(name='n').sort_values(['cpc4','year'])

alpha = 0.1

def ema_for_group(gdf):
    gdf = gdf.sort_values('year').copy()
    ema = None
    emas = []
    for n in gdf['n'].tolist():
        ema = n if ema is None else alpha*n + (1-alpha)*ema
        emas.append(ema)
    gdf['ema'] = emas
    return gdf

counts2 = counts.groupby('cpc4', group_keys=False).apply(ema_for_group)

# for each group, find best year (max ema); tie -> earliest year
idx = counts2.sort_values(['cpc4','ema','year'], ascending=[True,False,True]).groupby('cpc4').head(1)

# highest ema groups overall
idx_top = idx.sort_values('ema', ascending=False)
max_ema = idx_top['ema'].max() if len(idx_top) else None
if max_ema is None:
    out = []
else:
    top = idx_top[idx_top['ema'] == max_ema].copy()
    # join titles
    df_defs = pd.DataFrame(defs)
    df_defs['symbol'] = df_defs['symbol'].astype(str)
    title_map = dict(zip(df_defs['symbol'], df_defs['titleFull']))
    top['titleFull'] = top['cpc4'].map(title_map)
    out = top[['cpc4','titleFull','year','ema']].rename(columns={'cpc4':'cpc_group_code','year':'best_year','ema':'best_year_ema'}).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_mxjoTsMb7lrEqskrvgMNVOYx': [], 'var_call_0mxLeh7cvsl3OE0fOzPkBWve': [], 'var_call_dVpHQdCfSXuPsGrrFeL6sRnV': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_call_3eBieL8l9gwZ8lHwCAgwtHiU': [{'grant_date': 'None Date', 'n': '172069'}, {'grant_date': 'May 23rd, 2023', 'n': '28'}, {'grant_date': 'May 17th, 2022', 'n': '26'}, {'grant_date': '19th May 2020', 'n': '24'}, {'grant_date': 'October 27th, 2020', 'n': '22'}], 'var_call_g4QiVSl0jDaGxsVvrMr85eos': [{'grant_date': '14th Mar 2019', 'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.'}, {'grant_date': 'Mar 19th, 2019', 'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.'}, {'grant_date': 'Mar 12th, 2019', 'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.'}, {'grant_date': '2019 on Jul 12th', 'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.'}, {'grant_date': 'on March 14th, 2019', 'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.'}], 'var_call_Ci7QE5Ao8guCBeLVQnOZGbwF': 'file_storage/call_Ci7QE5Ao8guCBeLVQnOZGbwF.json', 'var_call_lwUd1tCAYUIMf5mAUJQnpbBx': 'file_storage/call_lwUd1tCAYUIMf5mAUJQnpbBx.json'}

exec(code, env_args)
