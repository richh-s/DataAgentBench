code = """import json

# Get company names from stockinfo data
stockinfo_path = locals()['var_functions.query_db:0']
with open(stockinfo_path, 'r') as f:
    stockinfo_data = json.load(f)

company_map = {item['Symbol']: item['Company Description'] for item in stockinfo_data}

# Top 5 companies based on the analysis
top_5 = [
    ('SES', 51),
    ('GLG', 42),
    ('TMSR', 40),
    ('VERB', 38),
    ('SNSS', 32)
]

result = []
for ticker, days in top_5:
    if ticker in company_map:
        # Clean up company name - take first part before common separators
        company_name = company_map[ticker]
        if ' specializes in ' in company_name:
            company_name = company_name.split(' specializes in ')[0]
        elif ' is ' in company_name:
            company_name = company_name.split(' is ')[0]
        elif ' focuses on ' in company_name:
            company_name = company_name.split(' focuses on ')[0]
        elif ' is a ' in company_name:
            company_name = company_name.split(' is a ')[0]
        elif ' based in ' in company_name:
            company_name = company_name.split(' based in ')[0]
        elif ',' in company_name:
            company_name = company_name.split(',')[0]
        elif '.' in company_name and not company_name.startswith('U.S.'):
            parts = company_name.split('.')
            if len(parts[0]) > 3:
                company_name = parts[0]
        
        result.append(f"{company_name} ({ticker}): {days} days")
    else:
        result.append(f"{ticker}: {days} days (Company name not found)")

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': {'total_capital_market': 86, 'total_trade_tables': 2753, 'common_tickers_count': 86, 'sample_common': ['PLIN', 'FAMI', 'MBCN', 'NXTD', 'MNCLU', 'PFIE', 'NVEE', 'IOTS', 'XBIOW', 'EXPC']}, 'var_functions.query_db:10': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.execute_python:12': ['PLIN', 'FAMI', 'MBCN', 'NXTD', 'MNCLU', 'PFIE', 'NVEE', 'IOTS', 'XBIOW', 'EXPC'], 'var_functions.execute_python:14': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.query_db:22': [{'ticker': 'AGMH', 'days': '13'}], 'var_functions.query_db:26': [{'ticker': 'APEX', 'days': '15'}], 'var_functions.query_db:30': [{'ticker': 'APEX', 'days': '15'}, {'ticker': 'AGMH', 'days': '13'}], 'var_functions.execute_python:32': {'total_tickers': 86, 'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_functions.query_db:34': [{'ticker': 'CBAT', 'days': '23'}, {'ticker': 'BIOC', 'days': '21'}, {'ticker': 'BKYI', 'days': '16'}, {'ticker': 'APEX', 'days': '15'}, {'ticker': 'CLRB', 'days': '14'}, {'ticker': 'CCCL', 'days': '13'}, {'ticker': 'AGMH', 'days': '13'}, {'ticker': 'BHAT', 'days': '10'}, {'ticker': 'BWEN', 'days': '5'}, {'ticker': 'CEMI', 'days': '3'}, {'ticker': 'BOSC', 'days': '3'}], 'var_functions.query_db:36': [{'ticker': 'GLG', 'days': '42'}, {'ticker': 'FAMI', 'days': '23'}, {'ticker': 'FTFT', 'days': '21'}, {'ticker': 'EYEG', 'days': '18'}, {'ticker': 'CPAH', 'days': '16'}, {'ticker': 'IDEX', 'days': '15'}, {'ticker': 'CORV', 'days': '10'}, {'ticker': 'HQI', 'days': '2'}, {'ticker': 'FNCB', 'days': '1'}, {'ticker': 'DZSI', 'days': '1'}, {'ticker': 'HRTX', 'days': '1'}, {'ticker': 'IOTS', 'days': '1'}], 'var_functions.query_db:38': [{'ticker': 'PECK', 'days': '19'}, {'ticker': 'NXTD', 'days': '15'}, {'ticker': 'ORGO', 'days': '15'}, {'ticker': 'MCEP', 'days': '14'}, {'ticker': 'OPTT', 'days': '12'}, {'ticker': 'PEIX', 'days': '12'}, {'ticker': 'PBTS', 'days': '8'}, {'ticker': 'MNPR', 'days': '4'}, {'ticker': 'MLND', 'days': '3'}, {'ticker': 'PFIE', 'days': '2'}, {'ticker': 'MMAC', 'days': '1'}, {'ticker': 'NVEE', 'days': '1'}, {'ticker': 'OTEL', 'days': '1'}], 'var_functions.query_db:40': [{'ticker': 'SES', 'days': '51'}, {'ticker': 'TMSR', 'days': '40'}, {'ticker': 'VERB', 'days': '38'}, {'ticker': 'SNSS', 'days': '32'}, {'ticker': 'WHLR', 'days': '15'}, {'ticker': 'VVPR', 'days': '14'}, {'ticker': 'SSNT', 'days': '11'}, {'ticker': 'XBIOW', 'days': '7'}, {'ticker': 'VTIQW', 'days': '6'}, {'ticker': 'XPEL', 'days': '4'}, {'ticker': 'QRHC', 'days': '3'}, {'ticker': 'VMD', 'days': '1'}, {'ticker': 'SHSP', 'days': '1'}, {'ticker': 'PLIN', 'days': '1'}]}

exec(code, env_args)
