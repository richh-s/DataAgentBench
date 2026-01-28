code = """import json
s = "FROM '{0}' WHERE Date >= '2017-01-01'"
print('__RESULT__:')
print(json.dumps({'s': s}))"""

env_args = {'var_call_W9DknPtITkO5E8fVFyGGCP1i': 'file_storage/call_W9DknPtITkO5E8fVFyGGCP1i.json', 'var_call_IkdZGIDgN5BwsY28UnCmseZJ': 'file_storage/call_IkdZGIDgN5BwsY28UnCmseZJ.json', 'var_call_UsFARjzhRdUpjRMozyesZDyT': {'a': 1}, 'var_call_0Tl5rumVClCnuwCs6jSI49Ox': {'n_symbols': 234, 'first10': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_call_fYerQF0UCfobeIErd7qXjARo': [{'Symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_M7EGmETCBvxPGIMKeYmUothi': {'q': "SELECT 'AIN' AS Symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days"}, 'var_call_FDruDVhtF9CeIMWNfQYa0s66': {'pd_version': '2.3.3'}}

exec(code, env_args)
