code = """import json

# Get all tickers from the previous query
tickers_data = locals().get('var_functions.query_db:2', [])
if isinstance(tickers_data, str) and tickers_data.endswith('.json'):
    with open(tickers_data, 'r') as f:
        tickers_data = json.load(f)

tickers = [item['Symbol'] for item in tickers_data]
print(f"Processing {len(tickers)} tickers")

# Build batch queries - process in chunks to avoid query size issues
batch_size = 20
batches = []

for i in range(0, len(tickers), batch_size):
    batch = tickers[i:i+batch_size]
    query_parts = []
    
    for ticker in batch:
        query_parts.append(f"SELECT '{ticker}' as ticker, COUNT(*) as days_with_high_volatility FROM \"{ticker}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) / Low > 0.20")
    
    batch_query = " UNION ALL ".join(query_parts)
    batches.append(batch_query)

print(f"Created {len(batches)} batches")
print('__RESULT__:')
print(json.dumps({'batches_count': len(batches), 'batch_size': batch_size, 'total_tickers': len(tickers)}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': [{'Symbol': 'AGMH'}, {'Symbol': 'ALACU'}, {'Symbol': 'AMHC'}, {'Symbol': 'ANDA'}, {'Symbol': 'APEX'}, {'Symbol': 'BCLI'}, {'Symbol': 'BHAT'}, {'Symbol': 'BIOC'}, {'Symbol': 'BKYI'}, {'Symbol': 'BLFS'}, {'Symbol': 'BOSC'}, {'Symbol': 'BOTJ'}, {'Symbol': 'BWEN'}, {'Symbol': 'CBAT'}, {'Symbol': 'CCCL'}, {'Symbol': 'CDMOP'}, {'Symbol': 'CEMI'}, {'Symbol': 'CFBK'}, {'Symbol': 'CFFA'}, {'Symbol': 'CLRB'}, {'Symbol': 'CORV'}, {'Symbol': 'CPAAU'}, {'Symbol': 'CPAH'}, {'Symbol': 'CUBA'}, {'Symbol': 'CVV'}, {'Symbol': 'DZSI'}, {'Symbol': 'ELSE'}, {'Symbol': 'EXPC'}, {'Symbol': 'EYEG'}, {'Symbol': 'FAMI'}, {'Symbol': 'FNCB'}, {'Symbol': 'FSBW'}, {'Symbol': 'FTFT'}, {'Symbol': 'GDYN'}, {'Symbol': 'GLG'}, {'Symbol': 'GRNVU'}, {'Symbol': 'GTEC'}, {'Symbol': 'HCCOU'}, {'Symbol': 'HNNA'}, {'Symbol': 'HQI'}, {'Symbol': 'HRTX'}, {'Symbol': 'IDEX'}, {'Symbol': 'IGIC'}, {'Symbol': 'IOTS'}, {'Symbol': 'ISNS'}, {'Symbol': 'ITI'}, {'Symbol': 'LACQ'}, {'Symbol': 'MBCN'}, {'Symbol': 'MBNKP'}, {'Symbol': 'MCEP'}, {'Symbol': 'MLND'}, {'Symbol': 'MMAC'}, {'Symbol': 'MNCLU'}, {'Symbol': 'MNPR'}, {'Symbol': 'NVEE'}, {'Symbol': 'NXTD'}, {'Symbol': 'OPOF'}, {'Symbol': 'OPTT'}, {'Symbol': 'ORGO'}, {'Symbol': 'ORSNU'}, {'Symbol': 'OTEL'}, {'Symbol': 'PBFS'}, {'Symbol': 'PBTS'}, {'Symbol': 'PCSB'}, {'Symbol': 'PECK'}, {'Symbol': 'PEIX'}, {'Symbol': 'PFIE'}, {'Symbol': 'PLIN'}, {'Symbol': 'POPE'}, {'Symbol': 'QRHC'}, {'Symbol': 'SES'}, {'Symbol': 'SHSP'}, {'Symbol': 'SNSS'}, {'Symbol': 'SSNT'}, {'Symbol': 'STKS'}, {'Symbol': 'TGLS'}, {'Symbol': 'TMSR'}, {'Symbol': 'VERB'}, {'Symbol': 'VMD'}, {'Symbol': 'VRRM'}, {'Symbol': 'VTIQW'}, {'Symbol': 'VVPR'}, {'Symbol': 'WHLM'}, {'Symbol': 'WHLR'}, {'Symbol': 'XBIOW'}, {'Symbol': 'XPEL'}], 'var_functions.execute_python:5': {'status': 'setup_complete', 'tickers_count': 86, 'examples': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.query_db:7': [{'days_with_high_volatility': '13'}], 'var_functions.query_db:8': [{'days_with_high_volatility': '0'}], 'var_functions.query_db:12': [{'ticker': 'AMHC', 'days_with_high_volatility': '0'}, {'ticker': 'ANDA', 'days_with_high_volatility': '0'}, {'ticker': 'APEX', 'days_with_high_volatility': '15'}, {'ticker': 'BCLI', 'days_with_high_volatility': '0'}, {'ticker': 'BHAT', 'days_with_high_volatility': '10'}]}

exec(code, env_args)
