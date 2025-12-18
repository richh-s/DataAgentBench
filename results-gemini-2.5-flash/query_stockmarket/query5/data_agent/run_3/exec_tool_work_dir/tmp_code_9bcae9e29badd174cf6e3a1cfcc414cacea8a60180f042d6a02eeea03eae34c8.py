code = """import json

with open(locals()['var_function-call-2253693256509417702'], 'r') as f:
    nasdaq_capital_market_stocks = json.load(f)

symbol_company_map = {item["Symbol"]: item["Company Description"] for item in nasdaq_capital_market_stocks}
symbols_to_process = list(symbol_company_map.keys())

initial_state = {
    "symbol_company_map": symbol_company_map,
    "company_day_counts": {},
    "symbols_to_process": symbols_to_process
}

print("__RESULT__:")
print(json.dumps(initial_state))"""

env_args = {'var_function-call-2253693256509417702': 'file_storage/function-call-2253693256509417702.json', 'var_function-call-9377614823541614527': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX'], 'var_function-call-18434627271801569945': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP'], 'var_function-call-9482372077361508182': 'file_storage/function-call-9482372077361508182.json'}

exec(code, env_args)
