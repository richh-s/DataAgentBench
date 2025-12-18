code = """import json

with open(locals()['var_function-call-7512712772181424858'], 'r') as f:
    nasdaq_capital_market_companies = json.load(f)

company_data = []
for company in nasdaq_capital_market_companies:
    company_data.append({'Symbol': company['Symbol'], 'Company Description': company['Company Description']})

print("__RESULT__:")
print(json.dumps(company_data))"""

env_args = {'var_function-call-10635938268862818382': 'file_storage/function-call-10635938268862818382.json', 'var_function-call-7512712772181424858': 'file_storage/function-call-7512712772181424858.json', 'var_function-call-14575303271704160794': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-7698664705107236352': 'file_storage/function-call-7698664705107236352.json'}

exec(code, env_args)
