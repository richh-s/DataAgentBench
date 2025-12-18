code = """import json

symbols = json.loads(locals()['var_function-call-17576780368704944672'])
stockinfo_data = json.load(open(locals()['var_function-call-3697019534837681094'], 'r'))

companies_data = {}
for record in stockinfo_data:
    symbol = record['Symbol']
    company_description = record['Company Description']
    companies_data[symbol] = {'name': company_description, 'count': 0}

# Process the data for AGMH (var_function-call-2435395218391636322)
if 'AGMH' in symbols:
    aghm_data = json.load(open(locals()['var_function-call-2435395218391636322'], 'r'))
    for trade_day in aghm_data:
        high = float(trade_day['High'])
        low = float(trade_day['Low'])
        if low > 0 and (high - low) > 0.20 * low:
            companies_data['AGMH']['count'] += 1

print('__RESULT__:')
print(json.dumps(companies_data))"""

env_args = {'var_function-call-3697019534837681094': 'file_storage/function-call-3697019534837681094.json', 'var_function-call-17576780368704944672': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-2435395218391636322': 'file_storage/function-call-2435395218391636322.json'}

exec(code, env_args)
