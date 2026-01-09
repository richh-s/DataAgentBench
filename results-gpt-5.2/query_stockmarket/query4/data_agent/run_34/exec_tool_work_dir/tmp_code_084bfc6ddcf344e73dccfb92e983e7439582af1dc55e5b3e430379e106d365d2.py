code = """import json
q = "SELECT '{sym}' AS Symbol, * FROM \"{sym}\" WHERE Date >= '2017-01-01'".format(sym='AIN')
print('__RESULT__:')
print(json.dumps({'q': q}))"""

env_args = {'var_call_W9DknPtITkO5E8fVFyGGCP1i': 'file_storage/call_W9DknPtITkO5E8fVFyGGCP1i.json', 'var_call_IkdZGIDgN5BwsY28UnCmseZJ': 'file_storage/call_IkdZGIDgN5BwsY28UnCmseZJ.json', 'var_call_UsFARjzhRdUpjRMozyesZDyT': {'a': 1}, 'var_call_0Tl5rumVClCnuwCs6jSI49Ox': {'n_symbols': 234, 'first10': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_call_fYerQF0UCfobeIErd7qXjARo': [{'Symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_M7EGmETCBvxPGIMKeYmUothi': {'q': "SELECT 'AIN' AS Symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days"}, 'var_call_FDruDVhtF9CeIMWNfQYa0s66': {'pd_version': '2.3.3'}, 'var_call_3d0DpwYc7Ba9NHoC0ocaDbTv': {'s': "FROM '{0}' WHERE Date >= '2017-01-01'"}, 'var_call_MFQkdAqAFU34u03iO5S7SHac': {'s': 'FROM "X"'}, 'var_call_px2hcmt89gIE9RUG0CVEnTfo': {'s': 'SELECT 1 FROM "AEFC"'}, 'var_call_8VMqQFONQ2E74KmlBubo21Y2': 'file_storage/call_8VMqQFONQ2E74KmlBubo21Y2.json', 'var_call_f8ECKv8oOcLzwD2GwoA2oXlP': [{'Symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'Symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}]}

exec(code, env_args)
