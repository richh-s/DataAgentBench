code = """import json

# All volatility counts from our queries
volatility_counts = {
    'IDEX': 15, 'BLFS': 0, 'CFFA': 0, 'XBIOW': 7, 'BWEN': 5, 'CBAT': 23,
    'SES': 51, 'HRTX': 1, 'PECK': 19, 'OTEL': 1, 'VTIQW': 6, 'POPE': 0,
    'BIOC': 21, 'CUBA': 0, 'OPOF': 0, 'ELSE': 0, 'ALACU': 0, 'ORSNU': 0,
    'FNCB': 1, 'MNPR': 4, 'PLIN': 1, 'TGLS': 0, 'ITI': 0, 'OPTT': 12,
    'GDYN': 0, 'ORGO': 15, 'BOTJ': 0, 'EXPC': 0, 'FSBW': 0, 'VVPR': 14,
    'MMAC': 1, 'FTFT': 21, 'VRRM': 0, 'LACQ': 0, 'WHLR': 15, 'TMSR': 40,
    'NXTD': 15, 'PBTS': 8, 'CLRB': 14, 'HQI': 2, 'EYEG': 18, 'GTEC': 0,
    'IGIC': 0, 'CDMOP': 0, 'BHAT': 10, 'CPAH': 16, 'WHLM': 0, 'MBCN': 0,
    'BKYI': 16, 'DZSI': 1, 'GLG': 42, 'SSNT': 11, 'CFBK': 0, 'MCEP': 14,
    'STKS': 0, 'VERB': 38, 'BCLI': 0, 'PCSB': 0, 'CORV': 10, 'CEMI': 3,
    'ISNS': 0, 'SNSS': 32, 'XPEL': 4, 'SHSP': 1, 'MNCLU': 0, 'AMHC': 0,
    'AGMH': 13, 'CPAAU': 0, 'PFIE': 2, 'MBNKP': 0, 'APEX': 15, 'HNNA': 0,
    'IOTS': 1, 'MLND': 3, 'GRNVU': 0, 'BOSC': 3, 'FAMI': 23, 'CVV': 0,
    'ANDA': 0, 'CCCL': 13, 'PEIX': 12, 'NVEE': 1, 'VMD': 1, 'QRHC': 3,
    'PBFS': 0, 'HCCOU': 0
}

# Sort by count descending
sorted_stocks = sorted(volatility_counts.items(), key=lambda x: x[1], reverse=True)

# Get top 10 for verification
print("Top 10 stocks by volatility days in 2019:")
for i, (symbol, count) in enumerate(sorted_stocks[:10], 1):
    print(f"{i}. {symbol}: {count} days")

# Get top 5 symbols
top_5_symbols = [symbol for symbol, count in sorted_stocks[:5]]

# Get company names for top 5
company_info_path = 'var_functions.query_db:86'
with open(company_info_path, 'r') as f:
    company_data = json.load(f)

symbol_to_company = {item['Symbol']: item['Company Description'] for item in company_data}

# Extract company names (first part of description)
company_names = []
for symbol in top_5_symbols:
    if symbol in symbol_to_company:
        desc = symbol_to_company[symbol]
        # Get first part before common verbs
        name = desc.split(' specializes')[0].split(' is ')[0].split(' engages')[0].strip()
        company_names.append(name)
    else:
        company_names.append(symbol)

print("\nTop 5 companies:")
for i, (symbol, count) in enumerate(sorted_stocks[:5], 1):
    company = company_names[i-1]
    print(f"{i}. {company} ({symbol}): {count} days")

result = {
    'top_5': list(zip(top_5_symbols, [sorted_stocks[i][1] for i in range(5)], company_names))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.query_db:18': [{'Symbol': 'AGMH'}, {'Symbol': 'ALACU'}, {'Symbol': 'AMHC'}, {'Symbol': 'ANDA'}, {'Symbol': 'APEX'}, {'Symbol': 'BCLI'}, {'Symbol': 'BHAT'}, {'Symbol': 'BIOC'}, {'Symbol': 'BKYI'}, {'Symbol': 'BLFS'}, {'Symbol': 'BOSC'}, {'Symbol': 'BOTJ'}, {'Symbol': 'BWEN'}, {'Symbol': 'CBAT'}, {'Symbol': 'CCCL'}, {'Symbol': 'CDMOP'}, {'Symbol': 'CEMI'}, {'Symbol': 'CFBK'}, {'Symbol': 'CFFA'}, {'Symbol': 'CLRB'}, {'Symbol': 'CORV'}, {'Symbol': 'CPAAU'}, {'Symbol': 'CPAH'}, {'Symbol': 'CUBA'}, {'Symbol': 'CVV'}, {'Symbol': 'DZSI'}, {'Symbol': 'ELSE'}, {'Symbol': 'EXPC'}, {'Symbol': 'EYEG'}, {'Symbol': 'FAMI'}, {'Symbol': 'FNCB'}, {'Symbol': 'FSBW'}, {'Symbol': 'FTFT'}, {'Symbol': 'GDYN'}, {'Symbol': 'GLG'}, {'Symbol': 'GRNVU'}, {'Symbol': 'GTEC'}, {'Symbol': 'HCCOU'}, {'Symbol': 'HNNA'}, {'Symbol': 'HQI'}, {'Symbol': 'HRTX'}, {'Symbol': 'IDEX'}, {'Symbol': 'IGIC'}, {'Symbol': 'IOTS'}, {'Symbol': 'ISNS'}, {'Symbol': 'ITI'}, {'Symbol': 'LACQ'}, {'Symbol': 'MBCN'}, {'Symbol': 'MBNKP'}, {'Symbol': 'MCEP'}], 'var_functions.query_db:24': [{'Symbol': 'AGMH'}, {'Symbol': 'ALACU'}, {'Symbol': 'AMHC'}, {'Symbol': 'ANDA'}, {'Symbol': 'APEX'}, {'Symbol': 'BCLI'}, {'Symbol': 'BHAT'}, {'Symbol': 'BIOC'}, {'Symbol': 'BKYI'}, {'Symbol': 'BLFS'}, {'Symbol': 'BOSC'}, {'Symbol': 'BOTJ'}, {'Symbol': 'BWEN'}, {'Symbol': 'CBAT'}, {'Symbol': 'CCCL'}, {'Symbol': 'CDMOP'}, {'Symbol': 'CEMI'}, {'Symbol': 'CFBK'}, {'Symbol': 'CFFA'}, {'Symbol': 'CLRB'}, {'Symbol': 'CORV'}, {'Symbol': 'CPAAU'}, {'Symbol': 'CPAH'}, {'Symbol': 'CUBA'}, {'Symbol': 'CVV'}, {'Symbol': 'DZSI'}, {'Symbol': 'ELSE'}, {'Symbol': 'EXPC'}, {'Symbol': 'EYEG'}, {'Symbol': 'FAMI'}, {'Symbol': 'FNCB'}, {'Symbol': 'FSBW'}, {'Symbol': 'FTFT'}, {'Symbol': 'GDYN'}, {'Symbol': 'GLG'}, {'Symbol': 'GRNVU'}, {'Symbol': 'GTEC'}, {'Symbol': 'HCCOU'}, {'Symbol': 'HNNA'}, {'Symbol': 'HQI'}, {'Symbol': 'HRTX'}, {'Symbol': 'IDEX'}, {'Symbol': 'IGIC'}, {'Symbol': 'IOTS'}, {'Symbol': 'ISNS'}, {'Symbol': 'ITI'}, {'Symbol': 'LACQ'}, {'Symbol': 'MBCN'}, {'Symbol': 'MBNKP'}, {'Symbol': 'MCEP'}, {'Symbol': 'MLND'}, {'Symbol': 'MMAC'}, {'Symbol': 'MNCLU'}, {'Symbol': 'MNPR'}, {'Symbol': 'NVEE'}, {'Symbol': 'NXTD'}, {'Symbol': 'OPOF'}, {'Symbol': 'OPTT'}, {'Symbol': 'ORGO'}, {'Symbol': 'ORSNU'}, {'Symbol': 'OTEL'}, {'Symbol': 'PBFS'}, {'Symbol': 'PBTS'}, {'Symbol': 'PCSB'}, {'Symbol': 'PECK'}, {'Symbol': 'PEIX'}, {'Symbol': 'PFIE'}, {'Symbol': 'PLIN'}, {'Symbol': 'POPE'}, {'Symbol': 'QRHC'}, {'Symbol': 'SES'}, {'Symbol': 'SHSP'}, {'Symbol': 'SNSS'}, {'Symbol': 'SSNT'}, {'Symbol': 'STKS'}, {'Symbol': 'TGLS'}, {'Symbol': 'TMSR'}, {'Symbol': 'VERB'}, {'Symbol': 'VMD'}, {'Symbol': 'VRRM'}, {'Symbol': 'VTIQW'}, {'Symbol': 'VVPR'}, {'Symbol': 'WHLM'}, {'Symbol': 'WHLR'}, {'Symbol': 'XBIOW'}, {'Symbol': 'XPEL'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'tradeable_symbols': ['IDEX', 'BLFS', 'CFFA', 'XBIOW', 'BWEN', 'CBAT', 'SES', 'HRTX', 'PECK', 'OTEL', 'VTIQW', 'POPE', 'BIOC', 'CUBA', 'OPOF', 'ELSE', 'ALACU', 'ORSNU', 'FNCB', 'MNPR', 'PLIN', 'TGLS', 'ITI', 'OPTT', 'GDYN', 'ORGO', 'BOTJ', 'EXPC', 'FSBW', 'VVPR', 'MMAC', 'FTFT', 'VRRM', 'LACQ', 'WHLR', 'TMSR', 'NXTD', 'PBTS', 'CLRB', 'HQI', 'EYEG', 'GTEC', 'IGIC', 'CDMOP', 'BHAT', 'CPAH', 'WHLM', 'MBCN', 'BKYI', 'DZSI', 'GLG', 'SSNT', 'CFBK', 'MCEP', 'STKS', 'VERB', 'BCLI', 'PCSB', 'CORV', 'CEMI', 'ISNS', 'SNSS', 'XPEL', 'SHSP', 'MNCLU', 'AMHC', 'AGMH', 'CPAAU', 'PFIE', 'MBNKP', 'APEX', 'HNNA', 'IOTS', 'MLND', 'GRNVU', 'BOSC', 'FAMI', 'CVV', 'ANDA', 'CCCL', 'PEIX', 'NVEE', 'VMD', 'QRHC', 'PBFS', 'HCCOU'], 'count': 86}, 'var_functions.execute_python:38': {'count': 86, 'symbols': ['IDEX', 'BLFS', 'CFFA', 'XBIOW', 'BWEN', 'CBAT', 'SES', 'HRTX', 'PECK', 'OTEL', 'VTIQW', 'POPE', 'BIOC', 'CUBA', 'OPOF', 'ELSE', 'ALACU', 'ORSNU', 'FNCB', 'MNPR', 'PLIN', 'TGLS', 'ITI', 'OPTT', 'GDYN', 'ORGO', 'BOTJ', 'EXPC', 'FSBW', 'VVPR', 'MMAC', 'FTFT', 'VRRM', 'LACQ', 'WHLR', 'TMSR', 'NXTD', 'PBTS', 'CLRB', 'HQI', 'EYEG', 'GTEC', 'IGIC', 'CDMOP', 'BHAT', 'CPAH', 'WHLM', 'MBCN', 'BKYI', 'DZSI', 'GLG', 'SSNT', 'CFBK', 'MCEP', 'STKS', 'VERB', 'BCLI', 'PCSB', 'CORV', 'CEMI', 'ISNS', 'SNSS', 'XPEL', 'SHSP', 'MNCLU', 'AMHC', 'AGMH', 'CPAAU', 'PFIE', 'MBNKP', 'APEX', 'HNNA', 'IOTS', 'MLND', 'GRNVU', 'BOSC', 'FAMI', 'CVV', 'ANDA', 'CCCL', 'PEIX', 'NVEE', 'VMD', 'QRHC', 'PBFS', 'HCCOU'], 'symbols_for_query': "IDEX','BLFS','CFFA','XBIOW','BWEN','CBAT','SES','HRTX','PECK','OTEL','VTIQW','POPE','BIOC','CUBA','OPOF','ELSE','ALACU','ORSNU','FNCB','MNPR','PLIN','TGLS','ITI','OPTT','GDYN','ORGO','BOTJ','EXPC','FSBW','VVPR','MMAC','FTFT','VRRM','LACQ','WHLR','TMSR','NXTD','PBTS','CLRB','HQI','EYEG','GTEC','IGIC','CDMOP','BHAT','CPAH','WHLM','MBCN','BKYI','DZSI','GLG','SSNT','CFBK','MCEP','STKS','VERB','BCLI','PCSB','CORV','CEMI','ISNS','SNSS','XPEL','SHSP','MNCLU','AMHC','AGMH','CPAAU','PFIE','MBNKP','APEX','HNNA','IOTS','MLND','GRNVU','BOSC','FAMI','CVV','ANDA','CCCL','PEIX','NVEE','VMD','QRHC','PBFS','HCCOU"}, 'var_functions.query_db:40': [{'high_volatility_days': '15'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:50': [{'count': '15'}], 'var_functions.query_db:52': [{'symbol': 'BLFS', 'count': '0'}, {'symbol': 'CFFA', 'count': '0'}, {'symbol': 'XBIOW', 'count': '7'}, {'symbol': 'BWEN', 'count': '5'}, {'symbol': 'CBAT', 'count': '23'}], 'var_functions.query_db:54': [{'symbol': 'SES', 'count': '51'}, {'symbol': 'HRTX', 'count': '1'}, {'symbol': 'PECK', 'count': '19'}, {'symbol': 'OTEL', 'count': '1'}, {'symbol': 'VTIQW', 'count': '6'}], 'var_functions.query_db:56': [{'symbol': 'POPE', 'count': '0'}, {'symbol': 'BIOC', 'count': '21'}, {'symbol': 'CUBA', 'count': '0'}, {'symbol': 'OPOF', 'count': '0'}, {'symbol': 'ELSE', 'count': '0'}], 'var_functions.query_db:58': [{'symbol': 'ALACU', 'count': '0'}, {'symbol': 'ORSNU', 'count': '0'}, {'symbol': 'FNCB', 'count': '1'}, {'symbol': 'MNPR', 'count': '4'}, {'symbol': 'PLIN', 'count': '1'}], 'var_functions.query_db:60': [{'symbol': 'TGLS', 'count': '0'}, {'symbol': 'ITI', 'count': '0'}, {'symbol': 'OPTT', 'count': '12'}, {'symbol': 'GDYN', 'count': '0'}, {'symbol': 'ORGO', 'count': '15'}], 'var_functions.query_db:62': [{'symbol': 'BOTJ', 'count': '0'}, {'symbol': 'EXPC', 'count': '0'}, {'symbol': 'FSBW', 'count': '0'}, {'symbol': 'VVPR', 'count': '14'}, {'symbol': 'MMAC', 'count': '1'}], 'var_functions.query_db:64': [{'symbol': 'FTFT', 'count': '21'}, {'symbol': 'VRRM', 'count': '0'}, {'symbol': 'LACQ', 'count': '0'}, {'symbol': 'WHLR', 'count': '15'}, {'symbol': 'TMSR', 'count': '40'}], 'var_functions.query_db:66': [{'symbol': 'NXTD', 'count': '15'}, {'symbol': 'PBTS', 'count': '8'}, {'symbol': 'CLRB', 'count': '14'}, {'symbol': 'HQI', 'count': '2'}, {'symbol': 'EYEG', 'count': '18'}], 'var_functions.query_db:68': [{'symbol': 'GTEC', 'count': '0'}, {'symbol': 'IGIC', 'count': '0'}, {'symbol': 'CDMOP', 'count': '0'}, {'symbol': 'BHAT', 'count': '10'}, {'symbol': 'CPAH', 'count': '16'}], 'var_functions.execute_python:70': [['IDEX', 15]], 'var_functions.query_db:72': [{'symbol': 'WHLM', 'count': '0'}, {'symbol': 'MBCN', 'count': '0'}, {'symbol': 'BKYI', 'count': '16'}, {'symbol': 'DZSI', 'count': '1'}, {'symbol': 'GLG', 'count': '42'}], 'var_functions.query_db:74': [{'symbol': 'SSNT', 'count': '11'}, {'symbol': 'CFBK', 'count': '0'}, {'symbol': 'MCEP', 'count': '14'}, {'symbol': 'STKS', 'count': '0'}, {'symbol': 'VERB', 'count': '38'}], 'var_functions.query_db:76': [{'symbol': 'BCLI', 'count': '0'}, {'symbol': 'PCSB', 'count': '0'}, {'symbol': 'CORV', 'count': '10'}, {'symbol': 'CEMI', 'count': '3'}, {'symbol': 'ISNS', 'count': '0'}], 'var_functions.query_db:78': [{'symbol': 'SNSS', 'count': '32'}, {'symbol': 'XPEL', 'count': '4'}, {'symbol': 'SHSP', 'count': '1'}, {'symbol': 'MNCLU', 'count': '0'}, {'symbol': 'AMHC', 'count': '0'}], 'var_functions.query_db:80': [{'symbol': 'AGMH', 'count': '13'}, {'symbol': 'CPAAU', 'count': '0'}, {'symbol': 'PFIE', 'count': '2'}, {'symbol': 'MBNKP', 'count': '0'}, {'symbol': 'APEX', 'count': '15'}, {'symbol': 'HNNA', 'count': '0'}, {'symbol': 'IOTS', 'count': '1'}, {'symbol': 'MLND', 'count': '3'}, {'symbol': 'GRNVU', 'count': '0'}, {'symbol': 'BOSC', 'count': '3'}], 'var_functions.query_db:82': [{'symbol': 'FAMI', 'count': '23'}, {'symbol': 'CVV', 'count': '0'}, {'symbol': 'ANDA', 'count': '0'}, {'symbol': 'CCCL', 'count': '13'}, {'symbol': 'PEIX', 'count': '12'}, {'symbol': 'NVEE', 'count': '1'}, {'symbol': 'VMD', 'count': '1'}, {'symbol': 'QRHC', 'count': '3'}, {'symbol': 'PBFS', 'count': '0'}, {'symbol': 'HCCOU', 'count': '0'}], 'var_functions.query_db:86': [{'Symbol': 'GLG', 'Company Description': 'TD Holdings, Inc. is involved in commodity trading and supply chain management, specializing in the distribution of non-ferrous metals and other industrial materials.'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Symbol': 'TMSR', 'Company Description': 'TMSR Holding Company Limited engages in the development and distribution of advanced industrial materials, focusing on enhancing efficiency and sustainability in various manufacturing processes.'}, {'Symbol': 'VERB', 'Company Description': 'Verb Technology Company, Inc. specializes in developing interactive video-based sales and marketing applications designed to enhance customer engagement and drive business growth.'}]}

exec(code, env_args)
