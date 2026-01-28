code = """import json
# Collect the known max results we queried
keys = [
    var_call_dWfvT0luf7T0VujqftWJv4dN, var_call_GFwSComURS3CZBJ1PAqc4Bqg, var_call_IscIXh2sqEzpc12Hy2DATz6M,
    var_call_cVSozzSQ8a74CYM7tw3aJpw9, var_call_ujKq5ibmuF0nKDXf8FMQRiUf, var_call_2atnP8DTdzKf5XPJpgswVjhF,
    var_call_LCRXcZcGuwgdTWH6r6tt1gRY, var_call_t9plJfG2b0gYbjXM2lCeitVh, var_call_jLMkYZPhZ4ztLN40JiNmg8SW,
    var_call_mjlSrtk7unqAtXDijwe4NIpp, var_call_xLTjLoSus1MXQPvIWCPaoKyU, var_call_MXmdqHqneO3Z7AKSRr6J2S7i,
    var_call_4QO5nCzFsFxeva5oROWc8T1Z, var_call_QMui07hvdefDQuFpndxFXpZS, var_call_2oMOmlZNivM6PlBm9Di2B1Cz, var_call_vnuNeODHxnkNI6xdxOSx0DKI, var_call_HiWhFUYaZohyi9jYRXRMEujh
]
res = []
for k in keys:
    try:
        with open(k, 'r') as f:
            data = json.load(f)
        # data could be list of dicts
        if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            for item in data:
                res.append(item)
        else:
            res.append({'raw': data})
    except Exception as e:
        res.append({'error_loading': str(e), 'key': str(k)})
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_sivacHuiSgcyyLES4JY2Pmbh': 'file_storage/call_sivacHuiSgcyyLES4JY2Pmbh.json', 'var_call_8wxgRA4ankapzlMw4DhePGJj': 'file_storage/call_8wxgRA4ankapzlMw4DhePGJj.json', 'var_call_GM4b9XWbZdjPKEghYXIfgFyD': {'has_SPY': True, 'total_etfs': 1435}, 'var_call_svQsBvucK6HUwI89ycJ6EqMt': 'file_storage/call_svQsBvucK6HUwI89ycJ6EqMt.json', 'var_call_2oMOmlZNivM6PlBm9Di2B1Cz': [], 'var_call_vnuNeODHxnkNI6xdxOSx0DKI': [{'max_adj': '193.3121490478516'}], 'var_call_GvKoHGUrw88alYqSONJgoBfz': ['SELECT "SPY" FROM "SPY";'], 'var_call_HiWhFUYaZohyi9jYRXRMEujh': [{'max_adj': '177.17626953125'}], 'var_call_dWfvT0luf7T0VujqftWJv4dN': [{'Symbol': 'SPY', 'max_adj': '193.3121490478516'}], 'var_call_GFwSComURS3CZBJ1PAqc4Bqg': [{'Symbol': 'VOO', 'max_adj': '177.17626953125'}], 'var_call_IscIXh2sqEzpc12Hy2DATz6M': [{'Symbol': 'IVV', 'max_adj': '193.5270538330078'}], 'var_call_Y2oorkNc2A9lPdwSpsrjN10H': {'error': 'unable to assemble results due to storage format differences'}, 'var_call_m47ceqG6QQQqcaWz7MiLOxwb': [{'Symbol': 'SPY', 'max_adj': 193.3121490478516}, {'Symbol': 'VOO', 'max_adj': 177.17626953125}, {'Symbol': 'IVV', 'max_adj': 193.5270538330078}], 'var_call_cVSozzSQ8a74CYM7tw3aJpw9': [{'Symbol': 'GLD', 'max_adj': '125.2300033569336'}], 'var_call_ujKq5ibmuF0nKDXf8FMQRiUf': [{'Symbol': 'GDX', 'max_adj': '22.22186088562012'}], 'var_call_2atnP8DTdzKf5XPJpgswVjhF': [{'Symbol': 'QQQ', 'max_adj': '110.42893981933594'}], 'var_call_LCRXcZcGuwgdTWH6r6tt1gRY': [{'Symbol': 'DIA', 'max_adj': '163.6190185546875'}], 'var_call_t9plJfG2b0gYbjXM2lCeitVh': [{'Symbol': 'IWM', 'max_adj': '120.37349700927734'}], 'var_call_jLMkYZPhZ4ztLN40JiNmg8SW': [{'Symbol': 'XLK', 'max_adj': '41.50289535522461'}], 'var_call_mjlSrtk7unqAtXDijwe4NIpp': [{'Symbol': 'XLF', 'max_adj': '14.538848876953123'}], 'var_call_xLTjLoSus1MXQPvIWCPaoKyU': [{'Symbol': 'VTI', 'max_adj': '100.54161834716795'}], 'var_call_MXmdqHqneO3Z7AKSRr6J2S7i': [{'Symbol': 'XLE', 'max_adj': '68.05343627929688'}], 'var_call_4QO5nCzFsFxeva5oROWc8T1Z': [{'Symbol': 'XLB', 'max_adj': '46.816436767578125'}], 'var_call_QMui07hvdefDQuFpndxFXpZS': [{'Symbol': 'XLV', 'max_adj': '71.13082122802734'}]}

exec(code, env_args)
