code = """import json

# Get tickers data
tickers_info = locals().get('var_functions.query_db:2', [])
if isinstance(tickers_info, str) and tickers_info.endswith('.json'):
    with open(tickers_info, 'r') as f:
        tickers_info = json.load(f)

tickers_list = [item['Symbol'] for item in tickers_info]
print('Total tickers to process:', len(tickers_list))

# Create batches for querying
def create_batch_query(ticker_batch):
    parts = []
    for ticker in ticker_batch:
        part = "SELECT " + "'" + ticker + "'" + " as ticker, COUNT(*) as days_with_high_volatility FROM " + '"' + ticker + '"' + " WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) / Low > 0.20"
        parts.append(part)
    return " UNION ALL ".join(parts)

# Create all batch queries
all_batches = []
batch_size = 15

for i in range(0, len(tickers_list), batch_size):
    batch = tickers_list[i:i+batch_size]
    batch_query = create_batch_query(batch)
    all_batches.append(batch_query)

print('Created', len(all_batches), 'batches')
print('__RESULT__:')
result = json.dumps({'batch_count': len(all_batches), 'first_batch_sample': all_batches[0][:200] if all_batches else ''})
print(result)"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': [{'Symbol': 'AGMH'}, {'Symbol': 'ALACU'}, {'Symbol': 'AMHC'}, {'Symbol': 'ANDA'}, {'Symbol': 'APEX'}, {'Symbol': 'BCLI'}, {'Symbol': 'BHAT'}, {'Symbol': 'BIOC'}, {'Symbol': 'BKYI'}, {'Symbol': 'BLFS'}, {'Symbol': 'BOSC'}, {'Symbol': 'BOTJ'}, {'Symbol': 'BWEN'}, {'Symbol': 'CBAT'}, {'Symbol': 'CCCL'}, {'Symbol': 'CDMOP'}, {'Symbol': 'CEMI'}, {'Symbol': 'CFBK'}, {'Symbol': 'CFFA'}, {'Symbol': 'CLRB'}, {'Symbol': 'CORV'}, {'Symbol': 'CPAAU'}, {'Symbol': 'CPAH'}, {'Symbol': 'CUBA'}, {'Symbol': 'CVV'}, {'Symbol': 'DZSI'}, {'Symbol': 'ELSE'}, {'Symbol': 'EXPC'}, {'Symbol': 'EYEG'}, {'Symbol': 'FAMI'}, {'Symbol': 'FNCB'}, {'Symbol': 'FSBW'}, {'Symbol': 'FTFT'}, {'Symbol': 'GDYN'}, {'Symbol': 'GLG'}, {'Symbol': 'GRNVU'}, {'Symbol': 'GTEC'}, {'Symbol': 'HCCOU'}, {'Symbol': 'HNNA'}, {'Symbol': 'HQI'}, {'Symbol': 'HRTX'}, {'Symbol': 'IDEX'}, {'Symbol': 'IGIC'}, {'Symbol': 'IOTS'}, {'Symbol': 'ISNS'}, {'Symbol': 'ITI'}, {'Symbol': 'LACQ'}, {'Symbol': 'MBCN'}, {'Symbol': 'MBNKP'}, {'Symbol': 'MCEP'}, {'Symbol': 'MLND'}, {'Symbol': 'MMAC'}, {'Symbol': 'MNCLU'}, {'Symbol': 'MNPR'}, {'Symbol': 'NVEE'}, {'Symbol': 'NXTD'}, {'Symbol': 'OPOF'}, {'Symbol': 'OPTT'}, {'Symbol': 'ORGO'}, {'Symbol': 'ORSNU'}, {'Symbol': 'OTEL'}, {'Symbol': 'PBFS'}, {'Symbol': 'PBTS'}, {'Symbol': 'PCSB'}, {'Symbol': 'PECK'}, {'Symbol': 'PEIX'}, {'Symbol': 'PFIE'}, {'Symbol': 'PLIN'}, {'Symbol': 'POPE'}, {'Symbol': 'QRHC'}, {'Symbol': 'SES'}, {'Symbol': 'SHSP'}, {'Symbol': 'SNSS'}, {'Symbol': 'SSNT'}, {'Symbol': 'STKS'}, {'Symbol': 'TGLS'}, {'Symbol': 'TMSR'}, {'Symbol': 'VERB'}, {'Symbol': 'VMD'}, {'Symbol': 'VRRM'}, {'Symbol': 'VTIQW'}, {'Symbol': 'VVPR'}, {'Symbol': 'WHLM'}, {'Symbol': 'WHLR'}, {'Symbol': 'XBIOW'}, {'Symbol': 'XPEL'}], 'var_functions.execute_python:5': {'status': 'setup_complete', 'tickers_count': 86, 'examples': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.query_db:7': [{'days_with_high_volatility': '13'}], 'var_functions.query_db:8': [{'days_with_high_volatility': '0'}], 'var_functions.query_db:12': [{'ticker': 'AMHC', 'days_with_high_volatility': '0'}, {'ticker': 'ANDA', 'days_with_high_volatility': '0'}, {'ticker': 'APEX', 'days_with_high_volatility': '15'}, {'ticker': 'BCLI', 'days_with_high_volatility': '0'}, {'ticker': 'BHAT', 'days_with_high_volatility': '10'}]}

exec(code, env_args)
