code = """import json

# Load tickers from stockinfo
stockinfo_path = locals()['var_functions.query_db:0']
with open(stockinfo_path, 'r') as f:
    stockinfo_data = json.load(f)

tickers = [item['Symbol'] for item in stockinfo_data]
company_names = {item['Symbol']: item['Company Description'] for item in stockinfo_data}

# Build a single comprehensive query
subqueries = []
for ticker in tickers:
    subquery = f"(SELECT '{ticker}' as ticker, COUNT(*) as days FROM \"{ticker}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.20 * Low))"
    subqueries.append(subquery)

union_query = " UNION ALL ".join(subqueries)
final_query = f"SELECT ticker, days FROM ({union_query}) AS results WHERE days > 0 ORDER BY days DESC LIMIT 5"

print('__RESULT__:')
print(json.dumps({
    'num_tickers': len(tickers),
    'query_length': len(final_query),
    'first_subquery': subqueries[0] if subqueries else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': {'total_capital_market': 86, 'total_trade_tables': 2753, 'common_tickers_count': 86, 'sample_common': ['PLIN', 'FAMI', 'MBCN', 'NXTD', 'MNCLU', 'PFIE', 'NVEE', 'IOTS', 'XBIOW', 'EXPC']}, 'var_functions.query_db:10': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.execute_python:12': ['PLIN', 'FAMI', 'MBCN', 'NXTD', 'MNCLU', 'PFIE', 'NVEE', 'IOTS', 'XBIOW', 'EXPC'], 'var_functions.execute_python:14': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.query_db:22': [{'ticker': 'AGMH', 'days': '13'}], 'var_functions.query_db:26': [{'ticker': 'APEX', 'days': '15'}]}

exec(code, env_args)
