code = """import json
# load max_adj results
r_spy = var_call_nXcH62ruwbrKNsijp3K4K9Oj
r_ivv = var_call_ofGeKpF3TQSqwZdtKR60v9t8
r_voo = var_call_mXwhcPCVTxYY7O4hEyWoWaSr
r_gld = var_call_oOlnFpapQjKZvQH391N62KjS
r_iwm = var_call_putQS22LQu6cdwGr1yq1oJGO
r_dia = var_call_mzADtnkxr5iwzmv9uJkwQu17

results = {
    'SPY': float(r_spy[0]['max_adj']),
    'IVV': float(r_ivv[0]['max_adj']),
    'VOO': float(r_voo[0]['max_adj']),
    'GLD': float(r_gld[0]['max_adj']),
    'IWM': float(r_iwm[0]['max_adj']),
    'DIA': float(r_dia[0]['max_adj'])
}
# Determine which exceeded 200
exceeded = [s for s,v in results.items() if v>200]
out = {'max_adj_by_symbol': results, 'exceeded_200_in_2015': exceeded, 'count': len(exceeded)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_d6OF5lNHFpCkdROe3WXhSEIn': 'file_storage/call_d6OF5lNHFpCkdROe3WXhSEIn.json', 'var_call_pWaf7Rt5WZqXxRrWb0Xhaa1p': 'file_storage/call_pWaf7Rt5WZqXxRrWb0Xhaa1p.json', 'var_call_sPUq8PJYpCCHgVos6fsyIewx': 'file_storage/call_sPUq8PJYpCCHgVos6fsyIewx.json', 'var_call_CxPrelKYGz4fmA9wX1r6Nnjf': [{'Symbol': 'DIA', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'GLD', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'IVV', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'IWM', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'QQQ', 'ETF': 'Y', 'Listing Exchange': 'Q'}, {'Symbol': 'SPY', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'VOO', 'ETF': 'Y', 'Listing Exchange': 'P'}], 'var_call_lEsEuqCelCzur3QufKzJgYVm': [], 'var_call_NOwPCuYiuqpY6hWnjJLXASaQ': [], 'var_call_YHU1bQLZbtAvwIkjYbYiF1Uw': [], 'var_call_e4OSFY70qwH7bwuSKMkqbsk6': [], 'var_call_VNI9OFRxM69zhjNPveSUKlfS': [], 'var_call_yYkdiuhBsVvmtzUN0IpiC84m': [], 'var_call_C20eWm3QGrTb3A4XdNDdDVbh': {'symbols_over_200_in_2015': [], 'count': 0}, 'var_call_nXcH62ruwbrKNsijp3K4K9Oj': [{'max_adj': '193.3121490478516'}], 'var_call_oOlnFpapQjKZvQH391N62KjS': [{'max_adj': '125.2300033569336'}], 'var_call_ofGeKpF3TQSqwZdtKR60v9t8': [{'max_adj': '193.5270538330078'}], 'var_call_mXwhcPCVTxYY7O4hEyWoWaSr': [{'max_adj': '177.17626953125'}], 'var_call_putQS22LQu6cdwGr1yq1oJGO': [{'max_adj': '120.37349700927734'}], 'var_call_mzADtnkxr5iwzmv9uJkwQu17': [{'max_adj': '163.6190185546875'}]}

exec(code, env_args)
