code = """import json
res = var_call_m0zfM15HvepS7eBin0EYojKZ
defs = var_call_IKDqTvkevF0f6i4Zzbb47ltd
# build title map
title_map = {}
for d in defs:
    sym = d.get('symbol')
    t = d.get('titleFull')
    if sym:
        title_map[sym] = t or ''
# sort groups
groups = sorted(res.get('groups', []), key=lambda x: (-x.get('best_ema', 0), x.get('level4','')))
output = []
for g in groups:
    code = g.get('level4','')
    title = title_map.get(code, '')
    best_year = g.get('best_year')
    output.append({'titleFull': title, 'cpc_group': code, 'best_year': best_year})
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_EG3jYgEy7mbMHgDYp7xJmNPY': 'file_storage/call_EG3jYgEy7mbMHgDYp7xJmNPY.json', 'var_call_C1mviJjloTwFfejDEpxwxHRn': 'file_storage/call_C1mviJjloTwFfejDEpxwxHRn.json', 'var_call_m0zfM15HvepS7eBin0EYojKZ': {'groups': [{'level4': 'H01R', 'counts': {'2016': 18}, 'ema': {'2016': 18}, 'best_year': 2016, 'best_ema': 18.0}, {'level4': 'B01J', 'counts': {'2018': 57}, 'ema': {'2018': 57}, 'best_year': 2018, 'best_ema': 57.0}, {'level4': 'B01D', 'counts': {'2018': 28}, 'ema': {'2018': 28}, 'best_year': 2018, 'best_ema': 28.0}, {'level4': 'Y02C', 'counts': {'2018': 3}, 'ema': {'2018': 3}, 'best_year': 2018, 'best_ema': 3.0}, {'level4': 'C07C', 'counts': {'2018': 4}, 'ema': {'2018': 4}, 'best_year': 2018, 'best_ema': 4.0}, {'level4': 'F01N', 'counts': {'2018': 15}, 'ema': {'2018': 15}, 'best_year': 2018, 'best_ema': 15.0}, {'level4': 'Y02A', 'counts': {'2018': 1}, 'ema': {'2018': 1}, 'best_year': 2018, 'best_ema': 1.0}], 'level4_list': ['B01D', 'B01J', 'C07C', 'F01N', 'H01R', 'Y02A', 'Y02C']}, 'var_call_OoY3UoYo3PbCVbGMTcxsOISB': [], 'var_call_IKDqTvkevF0f6i4Zzbb47ltd': [{'symbol': 'C07C', 'titleFull': 'ACYCLIC OR CARBOCYCLIC COMPOUNDS', 'level': '5.0'}, {'symbol': 'F01N', 'titleFull': 'GAS-FLOW SILENCERS OR EXHAUST APPARATUS FOR MACHINES OR ENGINES IN GENERAL; GAS-FLOW SILENCERS OR EXHAUST APPARATUS FOR INTERNAL COMBUSTION ENGINES', 'level': '5.0'}, {'symbol': 'H01R', 'titleFull': 'ELECTRICALLY-CONDUCTIVE CONNECTIONS; STRUCTURAL ASSOCIATIONS OF A PLURALITY OF MUTUALLY-INSULATED ELECTRICAL CONNECTING ELEMENTS; COUPLING DEVICES; CURRENT COLLECTORS', 'level': '5.0'}, {'symbol': 'B01J', 'titleFull': 'CHEMICAL OR PHYSICAL PROCESSES, e.g. CATALYSIS OR COLLOID CHEMISTRY; THEIR RELEVANT APPARATUS', 'level': '5.0'}, {'symbol': 'B01D', 'titleFull': 'SEPARATION', 'level': '5.0'}, {'symbol': 'Y02C', 'titleFull': 'CAPTURE, STORAGE, SEQUESTRATION OR DISPOSAL OF GREENHOUSE GASES [GHG]', 'level': '5.0'}, {'symbol': 'Y02A', 'titleFull': 'TECHNOLOGIES FOR ADAPTATION TO CLIMATE CHANGE', 'level': '5.0'}]}

exec(code, env_args)
