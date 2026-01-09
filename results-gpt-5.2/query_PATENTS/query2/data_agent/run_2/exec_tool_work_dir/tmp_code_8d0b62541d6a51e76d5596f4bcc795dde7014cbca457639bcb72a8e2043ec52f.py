code = """import json, re

# top groups
top = var_call_IVrop28g4upplnofQkBPHuH7

# load cpc definitions level4
path = var_call_ctQJ2KMH8FuxLNtw8rdlkRMb
with open(path,'r',encoding='utf-8') as f:
    defs = json.load(f)

# build mapping from symbol to titleFull
m = {d['symbol'].replace(' ',''): d.get('titleFull') for d in defs if d.get('symbol')}

def title_for(cpc4):
    # try exact match
    if cpc4 in m:
        return m[cpc4]
    # try first 3 chars? Actually level-4 in CPCDefinition seems be section-class (e.g., B60), so map by first 3
    pref = cpc4[:3]
    return m.get(pref)

out=[]
for r in top:
    c=r['cpc_group_code']
    out.append({
        'CPC group code (level 4)': c,
        'Full title': title_for(c) or None,
        'Best year (by EMA of filings)': r['best_year'],
        'Max EMA (alpha=0.1)': r['best_ema'],
    })

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_vZrDOLIHfW9dlOdw3MYzm4C2': ['publicationinfo'], 'var_call_jO4ZMQloc2z16UQOYwgNqPEk': ['cpc_definition'], 'var_call_UCf7Z4QIMTSExuLabWT4eoX8': [], 'var_call_raMtB9lmUWv0ZwZf1IcnvP6F': 'file_storage/call_raMtB9lmUWv0ZwZf1IcnvP6F.json', 'var_call_yfmgTYsGCSf4u0WA7OJevGvX': 'file_storage/call_yfmgTYsGCSf4u0WA7OJevGvX.json', 'var_call_IVrop28g4upplnofQkBPHuH7': [{'cpc_group_code': 'B23K1', 'best_year': 2015, 'best_ema': 1.0}, {'cpc_group_code': 'B29C2045', 'best_year': 2012, 'best_ema': 1.0}, {'cpc_group_code': 'B29C45', 'best_year': 2012, 'best_ema': 1.0}, {'cpc_group_code': 'B29D99', 'best_year': 2012, 'best_ema': 1.0}, {'cpc_group_code': 'B41F21', 'best_year': 2007, 'best_ema': 1.0}, {'cpc_group_code': 'B41F22', 'best_year': 2007, 'best_ema': 1.0}, {'cpc_group_code': 'B60K6', 'best_year': 2013, 'best_ema': 1.0}, {'cpc_group_code': 'B60R16', 'best_year': 2018, 'best_ema': 1.0}, {'cpc_group_code': 'B60W30', 'best_year': 2013, 'best_ema': 1.0}, {'cpc_group_code': 'B64D11', 'best_year': 2018, 'best_ema': 1.0}, {'cpc_group_code': 'E02F3', 'best_year': 2012, 'best_ema': 1.0}, {'cpc_group_code': 'E02F9', 'best_year': 2012, 'best_ema': 1.0}, {'cpc_group_code': 'E05B19', 'best_year': 2012, 'best_ema': 1.0}, {'cpc_group_code': 'F02D41', 'best_year': 2010, 'best_ema': 1.0}, {'cpc_group_code': 'F02M55', 'best_year': 2014, 'best_ema': 1.0}, {'cpc_group_code': 'F02M59', 'best_year': 2014, 'best_ema': 1.0}, {'cpc_group_code': 'F02M65', 'best_year': 2010, 'best_ema': 1.0}, {'cpc_group_code': 'F02N11', 'best_year': 2013, 'best_ema': 1.0}, {'cpc_group_code': 'F02N2200', 'best_year': 2013, 'best_ema': 1.0}, {'cpc_group_code': 'F02N2300', 'best_year': 2013, 'best_ema': 1.0}], 'var_call_ctQJ2KMH8FuxLNtw8rdlkRMb': 'file_storage/call_ctQJ2KMH8FuxLNtw8rdlkRMb.json'}

exec(code, env_args)
