code = """import json
# Read results from parallel calls
r1 = var_call_lEsEuqCelCzur3QufKzJgYVm
r2 = var_call_NOwPCuYiuqpY6hWnjJLXASaQ
r3 = var_call_YHU1bQLZbtAvwIkjYbYiF1Uw
r4 = var_call_e4OSFY70qwH7bwuSKMkqbsk6
r5 = var_call_VNI9OFRxM69zhjNPveSUKlfS
r6 = var_call_yYkdiuhBsVvmtzUN0IpiC84m

# Each var is a list (possibly empty). Collect non-empty symbols.
symbols = []
for r in (r1,r2,r3,r4,r5,r6):
    if isinstance(r, list) and len(r)>0:
        symbols.append(r[0]['Symbol'])

out = {'symbols_over_200_in_2015': symbols, 'count': len(symbols)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_d6OF5lNHFpCkdROe3WXhSEIn': 'file_storage/call_d6OF5lNHFpCkdROe3WXhSEIn.json', 'var_call_pWaf7Rt5WZqXxRrWb0Xhaa1p': 'file_storage/call_pWaf7Rt5WZqXxRrWb0Xhaa1p.json', 'var_call_sPUq8PJYpCCHgVos6fsyIewx': 'file_storage/call_sPUq8PJYpCCHgVos6fsyIewx.json', 'var_call_CxPrelKYGz4fmA9wX1r6Nnjf': [{'Symbol': 'DIA', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'GLD', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'IVV', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'IWM', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'QQQ', 'ETF': 'Y', 'Listing Exchange': 'Q'}, {'Symbol': 'SPY', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'VOO', 'ETF': 'Y', 'Listing Exchange': 'P'}], 'var_call_lEsEuqCelCzur3QufKzJgYVm': [], 'var_call_NOwPCuYiuqpY6hWnjJLXASaQ': [], 'var_call_YHU1bQLZbtAvwIkjYbYiF1Uw': [], 'var_call_e4OSFY70qwH7bwuSKMkqbsk6': [], 'var_call_VNI9OFRxM69zhjNPveSUKlfS': [], 'var_call_yYkdiuhBsVvmtzUN0IpiC84m': []}

exec(code, env_args)
