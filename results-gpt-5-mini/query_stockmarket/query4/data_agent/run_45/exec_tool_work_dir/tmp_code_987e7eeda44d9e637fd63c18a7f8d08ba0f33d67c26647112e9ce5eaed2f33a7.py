code = """import json
p1 = var_call_F7ARdSLa3CfMEqYQoQGvzIcb
p2 = var_call_nRCOIQTKtx4ukCguggXBETaj
with open(p1,'r') as f:
    data1 = json.load(f)
with open(p2,'r') as f:
    tables = json.load(f)
symbols = [rec['Symbol'] for rec in data1]
present = [s for s in symbols if s in tables]
print('__RESULT__:')
print(json.dumps({'symbols_present_count': len(present), 'sample_present': present[:20]}))"""

env_args = {'var_call_F7ARdSLa3CfMEqYQoQGvzIcb': 'file_storage/call_F7ARdSLa3CfMEqYQoQGvzIcb.json', 'var_call_nRCOIQTKtx4ukCguggXBETaj': 'file_storage/call_nRCOIQTKtx4ukCguggXBETaj.json', 'var_call_iiVxyEpARj5wqd3glSsWLWmq': {'symbols_in_stockinfo': 234, 'tables_in_stocktrade': 2753}}

exec(code, env_args)
