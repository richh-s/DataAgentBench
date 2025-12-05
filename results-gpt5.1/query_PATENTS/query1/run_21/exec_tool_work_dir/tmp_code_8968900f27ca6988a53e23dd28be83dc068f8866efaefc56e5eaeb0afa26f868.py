code = """import json, pandas as pd, re

pub_path = var_call_rsLR4inHjlZynKAipYdpmjRT
cpcdef_path = var_call_aIEDwcrdwiNPeICQgcADbBR0

with open(pub_path, 'r') as f:
    pub_data = json.load(f)
with open(cpcdef_path, 'r') as f:
    cpcdef_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

# year
pub_df['year'] = pub_df['publication_date'].str.extract(r'(\d{4})').astype(float).astype('Int64')
pub_df = pub_df.dropna(subset=['year'])
pub_df['year'] = pub_df['year'].astype(int)

# explode cpc
recs = []
for _, row in pub_df.iterrows():
    y = row['year']
    cpc_raw = row['cpc']
    if not isinstance(cpc_raw, str) or not cpc_raw.strip():
        continue
    try:
        codes = json.loads(cpc_raw)
    except Exception:
        continue
    for ent in codes:
        code = ent.get('code') if isinstance(ent, dict) else None
        if not code:
            continue
        recs.append({'symbol': code, 'year': y})

cpc_year = pd.DataFrame(recs)

cpcdef_df = pd.DataFrame(cpcdef_data)
level5_syms = set(cpcdef_df['symbol'].astype(str))

cpc_year = cpc_year[cpc_year['symbol'].isin(level5_syms)]

if cpc_year.empty:
    result = []
else:
    counts = cpc_year.groupby(['symbol','year']).size().reset_index(name='filings')
    alpha = 0.2
    ema_rows = []
    for sym, grp in counts.groupby('symbol'):
        grp = grp.sort_values('year')
        ema = None
        for _, r in grp.iterrows():
            y = r['year']; f = r['filings']
            ema = f if ema is None else alpha*f + (1-alpha)*ema
            ema_rows.append({'symbol': sym, 'year': y, 'ema': ema})
    ema_df = pd.DataFrame(ema_rows)
    idx = ema_df.groupby('symbol')['ema'].idxmax()
    best = ema_df.loc[idx].reset_index(drop=True)
    best_2022 = best[best['year'] == 2022]
    result = sorted(best_2022['symbol'].unique().tolist())

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_rsLR4inHjlZynKAipYdpmjRT': 'file_storage/call_rsLR4inHjlZynKAipYdpmjRT.json', 'var_call_aIEDwcrdwiNPeICQgcADbBR0': 'file_storage/call_aIEDwcrdwiNPeICQgcADbBR0.json', 'var_call_Wv3EauzuDayJeCTsVQKuglM4': ['symbol', 'level'], 'var_call_Gajww71rm9Y62hldEHFbtnDu': {'columns': ['symbol', 'level'], 'sample': [{'symbol': 'A41D', 'level': '5.0'}, {'symbol': 'A41C', 'level': '5.0'}, {'symbol': 'A41H', 'level': '5.0'}, {'symbol': 'A42B', 'level': '5.0'}, {'symbol': 'A42C', 'level': '5.0'}]}, 'var_call_boGrU18qKSa5CxRCo9gQucvQ': {'columns': ['publication_date', 'cpc'], 'sample': [{'publication_date': 'Aug 3rd, 2021', 'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'publication_date': 'Oct 6th, 2020', 'cpc': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H2037/0893",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/2007",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H37/084",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/0043",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2037/0873",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/2041",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2037/0886",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H3/62",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/084",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H3/76",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H2037/0873",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2037/0873",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/2007",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H3/62",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/084",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/0043",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/2041",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}]}}

exec(code, env_args)
