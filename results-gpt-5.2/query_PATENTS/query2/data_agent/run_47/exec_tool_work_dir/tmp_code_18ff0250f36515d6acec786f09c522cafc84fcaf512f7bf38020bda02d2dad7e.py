code = """import json
best = var_call_ELcCpBwqnS51TPQHPiHvyIQk
# map to corrected symbols
mapping={'F02D4100/00':'F02D41/00','F02M6500/00':'F02M65/00'}
titles = {r['symbol']: r['titleFull'] for r in var_call_NFZlDHnZyTJgrYimCizmbH7p}

out=[]
for r in best:
    sym = mapping.get(r['cpc4'], r['cpc4'])
    out.append({
        'cpc_group_code': sym,
        'titleFull': titles.get(sym),
        'best_year': r['year'],
        'ema': r['ema']
    })

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FZU99h3OjA35Qt6iUoghhjZN': ['publicationinfo'], 'var_call_rOqnuIgr3dqs27or592Xe22L': ['cpc_definition'], 'var_call_cnNoynNR4xW0vhvRiavHqmMK': 'file_storage/call_cnNoynNR4xW0vhvRiavHqmMK.json', 'var_call_ELcCpBwqnS51TPQHPiHvyIQk': [{'cpc4': 'F02D4100/00', 'year': 2010, 'ema': 1.0}, {'cpc4': 'F02M6500/00', 'year': 2010, 'ema': 1.0}], 'var_call_xldRJkxYqbXYrebofUQoexvX': [], 'var_call_NFZlDHnZyTJgrYimCizmbH7p': [{'symbol': 'F02M65/00', 'titleFull': 'Testing fuel-injection apparatus, e.g. testing injection timing ; Cleaning of fuel-injection apparatus'}, {'symbol': 'F02D41/00', 'titleFull': 'Electrical control of supply of combustible mixture or its constituents'}]}

exec(code, env_args)
