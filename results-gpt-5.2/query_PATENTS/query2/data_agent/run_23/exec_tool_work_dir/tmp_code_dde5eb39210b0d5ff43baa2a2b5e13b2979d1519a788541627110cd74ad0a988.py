code = """import json, pandas as pd, re

leaders = var_call_sHe6lMYcoLrggT5MfqXU8JkP['leaders']
leader_syms = sorted({d['symbol'] for d in leaders})

path = var_call_6E8JdAnzLdtly5XQKALd1Ltq
with open(path, 'r', encoding='utf-8') as f:
    defs = json.load(f)

df_defs = pd.DataFrame(defs)
# build mapping for exact symbol
map_title = dict(zip(df_defs['symbol'], df_defs['titleFull']))

out=[]
for d in leaders:
    sym=d['symbol']
    title = map_title.get(sym)
    if title is None:
        # fallback: use first 3 chars (e.g., A24) if only section-class exists
        title = map_title.get(sym[:3]) or map_title.get(sym[:2])
    out.append({'cpc_group_code_level4': sym, 'titleFull': title, 'best_year': int(d['best_year']), 'best_ema': float(d['best_ema'])})

out = sorted(out, key=lambda x: (-(x['best_ema']), x['cpc_group_code_level4']))
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_LGNwoYwFNT3vbRKKf6jzBG90': ['publicationinfo'], 'var_call_PaD7spDALVHLONxPexljNovY': ['cpc_definition'], 'var_call_vcOVAgHoyxakz68g1MceCiu1': 'file_storage/call_vcOVAgHoyxakz68g1MceCiu1.json', 'var_call_sHe6lMYcoLrggT5MfqXU8JkP': {'max_ema': 1.0, 'leaders': [{'symbol': 'A24C5', 'best_year': 2018, 'best_ema': 1.0}, {'symbol': 'A43B13', 'best_year': 2016, 'best_ema': 1.0}, {'symbol': 'A43B17', 'best_year': 2016, 'best_ema': 1.0}, {'symbol': 'A43B7', 'best_year': 2016, 'best_ema': 1.0}, {'symbol': 'A61B1', 'best_year': 2016, 'best_ema': 1.0}, {'symbol': 'A61F5', 'best_year': 2016, 'best_ema': 1.0}, {'symbol': 'B29C2049', 'best_year': 2007, 'best_ema': 1.0}, {'symbol': 'B29C2949', 'best_year': 2007, 'best_ema': 1.0}, {'symbol': 'B29C49', 'best_year': 2007, 'best_ema': 1.0}, {'symbol': 'B60S9', 'best_year': 2016, 'best_ema': 1.0}, {'symbol': 'B63B21', 'best_year': 2014, 'best_ema': 1.0}, {'symbol': 'B66C23', 'best_year': 2016, 'best_ema': 1.0}, {'symbol': 'C04B2235', 'best_year': 2015, 'best_ema': 1.0}, {'symbol': 'C04B35', 'best_year': 2015, 'best_ema': 1.0}, {'symbol': 'C04B40', 'best_year': 2015, 'best_ema': 1.0}, {'symbol': 'C09K11', 'best_year': 2015, 'best_ema': 1.0}, {'symbol': 'E02F3', 'best_year': 2012, 'best_ema': 1.0}, {'symbol': 'E02F9', 'best_year': 2012, 'best_ema': 1.0}, {'symbol': 'E21B43', 'best_year': 2013, 'best_ema': 1.0}, {'symbol': 'F01C1', 'best_year': 2013, 'best_ema': 1.0}, {'symbol': 'F02D13', 'best_year': 2018, 'best_ema': 1.0}, {'symbol': 'F02D15', 'best_year': 2018, 'best_ema': 1.0}, {'symbol': 'F02D41', 'best_year': 2010, 'best_ema': 1.0}, {'symbol': 'F02M65', 'best_year': 2010, 'best_ema': 1.0}, {'symbol': 'F04C11', 'best_year': 2013, 'best_ema': 1.0}, {'symbol': 'F04C13', 'best_year': 2013, 'best_ema': 1.0}, {'symbol': 'F04C15', 'best_year': 2013, 'best_ema': 1.0}, {'symbol': 'F04C2', 'best_year': 2013, 'best_ema': 1.0}, {'symbol': 'F16H2200', 'best_year': 2009, 'best_ema': 1.0}, {'symbol': 'F16H3', 'best_year': 2009, 'best_ema': 1.0}, {'symbol': 'F16H37', 'best_year': 2009, 'best_ema': 1.0}, {'symbol': 'F23B50', 'best_year': 2018, 'best_ema': 1.0}, {'symbol': 'F23B60', 'best_year': 2018, 'best_ema': 1.0}, {'symbol': 'F23L1', 'best_year': 2018, 'best_ema': 1.0}, {'symbol': 'F23L15', 'best_year': 2018, 'best_ema': 1.0}, {'symbol': 'F23N1', 'best_year': 2018, 'best_ema': 1.0}, {'symbol': 'F24B5', 'best_year': 2018, 'best_ema': 1.0}, {'symbol': 'F41H11', 'best_year': 2012, 'best_ema': 1.0}, {'symbol': 'F42B3', 'best_year': 2012, 'best_ema': 1.0}, {'symbol': 'G02B13', 'best_year': 2016, 'best_ema': 1.0}, {'symbol': 'G02B15', 'best_year': 2016, 'best_ema': 1.0}, {'symbol': 'G02B23', 'best_year': 2016, 'best_ema': 1.0}, {'symbol': 'H01L23', 'best_year': 2008, 'best_ema': 1.0}, {'symbol': 'H01L25', 'best_year': 2008, 'best_ema': 1.0}, {'symbol': 'H01L2924', 'best_year': 2008, 'best_ema': 1.0}, {'symbol': 'H04L1', 'best_year': 2015, 'best_ema': 1.0}, {'symbol': 'H04L5', 'best_year': 2015, 'best_ema': 1.0}, {'symbol': 'H04W52', 'best_year': 2015, 'best_ema': 1.0}, {'symbol': 'H04W72', 'best_year': 2015, 'best_ema': 1.0}, {'symbol': 'H04W76', 'best_year': 2015, 'best_ema': 1.0}, {'symbol': 'Y02D30', 'best_year': 2015, 'best_ema': 1.0}, {'symbol': 'Y02E20', 'best_year': 2018, 'best_ema': 1.0}, {'symbol': 'Y02T10', 'best_year': 2018, 'best_ema': 1.0}]}, 'var_call_6E8JdAnzLdtly5XQKALd1Ltq': 'file_storage/call_6E8JdAnzLdtly5XQKALd1Ltq.json'}

exec(code, env_args)
