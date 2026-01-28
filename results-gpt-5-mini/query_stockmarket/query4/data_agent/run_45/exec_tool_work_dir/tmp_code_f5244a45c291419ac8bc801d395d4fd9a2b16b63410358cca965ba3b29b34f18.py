code = """import json
p1 = var_call_F7ARdSLa3CfMEqYQoQGvzIcb
p2 = var_call_nRCOIQTKtx4ukCguggXBETaj
with open(p1) as f:
    data1 = json.load(f)
with open(p2) as f:
    tables = json.load(f)
symbols = [rec['Symbol'] for rec in data1]
present = [s for s in symbols if s in tables]
print('__RESULT__:')
print(json.dumps(present))"""

env_args = {'var_call_F7ARdSLa3CfMEqYQoQGvzIcb': 'file_storage/call_F7ARdSLa3CfMEqYQoQGvzIcb.json', 'var_call_nRCOIQTKtx4ukCguggXBETaj': 'file_storage/call_nRCOIQTKtx4ukCguggXBETaj.json', 'var_call_iiVxyEpARj5wqd3glSsWLWmq': {'symbols_in_stockinfo': 234, 'tables_in_stocktrade': 2753}, 'var_call_cV4zh4nKX1ldk88sDJmyrQHs': {'symbols_present_count': 234, 'sample_present': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}}

exec(code, env_args)
