code = """import json
p1 = var_call_F7ARdSLa3CfMEqYQoQGvzIcb
p2 = var_call_nRCOIQTKtx4ukCguggXBETaj
with open(p1,'r') as f:
    data1 = json.load(f)
with open(p2,'r') as f:
    tables = json.load(f)
print('__RESULT__:')
print(json.dumps({'symbols_in_stockinfo': len(data1), 'tables_in_stocktrade': len(tables)}))"""

env_args = {'var_call_F7ARdSLa3CfMEqYQoQGvzIcb': 'file_storage/call_F7ARdSLa3CfMEqYQoQGvzIcb.json', 'var_call_nRCOIQTKtx4ukCguggXBETaj': 'file_storage/call_nRCOIQTKtx4ukCguggXBETaj.json'}

exec(code, env_args)
