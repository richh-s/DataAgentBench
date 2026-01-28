code = """import json

# Get the list of NASDAQ Capital Market tickers
tickers_data = locals().get('var_functions.query_db:2', [])
if isinstance(tickers_data, str) and tickers_data.endswith('.json'):
    with open(tickers_data, 'r') as f:
        tickers_data = json.load(f)

tickers = [item['Symbol'] for item in tickers_data]
print(f"Found {len(tickers)} tickers in NASDAQ Capital Market")

# Initialize storage for results
results = []
processed_count = 0
errors = []

# Process each ticker
for ticker in tickers:
    try:
        # Query 2019 data for this ticker
        query = f'''
        SELECT COUNT(*) as days_with_high_volatility
        FROM "{ticker}"
        WHERE Date >= '2019-01-01' AND Date <= '2019-12-31'
          AND (High - Low) / Low > 0.20
        '''
        
        # This would need to be done via query_db, but we can't call it from here
        # Instead, I'll need to build queries for all tickers
        # For now, let's just track what we need to query
        results.append({'ticker': ticker, 'query': query})
        processed_count += 1
        
    except Exception as e:
        errors.append(f"Error processing {ticker}: {str(e)}")

print(f"Prepared queries for {processed_count} tickers")
print(f"Errors: {len(errors)}")

# For now, let's just return a placeholder to show the approach
print('__RESULT__:')
print(json.dumps({'status': 'setup_complete', 'tickers_count': len(tickers), 'examples': tickers[:5]}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': [{'Symbol': 'AGMH'}, {'Symbol': 'ALACU'}, {'Symbol': 'AMHC'}, {'Symbol': 'ANDA'}, {'Symbol': 'APEX'}, {'Symbol': 'BCLI'}, {'Symbol': 'BHAT'}, {'Symbol': 'BIOC'}, {'Symbol': 'BKYI'}, {'Symbol': 'BLFS'}, {'Symbol': 'BOSC'}, {'Symbol': 'BOTJ'}, {'Symbol': 'BWEN'}, {'Symbol': 'CBAT'}, {'Symbol': 'CCCL'}, {'Symbol': 'CDMOP'}, {'Symbol': 'CEMI'}, {'Symbol': 'CFBK'}, {'Symbol': 'CFFA'}, {'Symbol': 'CLRB'}, {'Symbol': 'CORV'}, {'Symbol': 'CPAAU'}, {'Symbol': 'CPAH'}, {'Symbol': 'CUBA'}, {'Symbol': 'CVV'}, {'Symbol': 'DZSI'}, {'Symbol': 'ELSE'}, {'Symbol': 'EXPC'}, {'Symbol': 'EYEG'}, {'Symbol': 'FAMI'}, {'Symbol': 'FNCB'}, {'Symbol': 'FSBW'}, {'Symbol': 'FTFT'}, {'Symbol': 'GDYN'}, {'Symbol': 'GLG'}, {'Symbol': 'GRNVU'}, {'Symbol': 'GTEC'}, {'Symbol': 'HCCOU'}, {'Symbol': 'HNNA'}, {'Symbol': 'HQI'}, {'Symbol': 'HRTX'}, {'Symbol': 'IDEX'}, {'Symbol': 'IGIC'}, {'Symbol': 'IOTS'}, {'Symbol': 'ISNS'}, {'Symbol': 'ITI'}, {'Symbol': 'LACQ'}, {'Symbol': 'MBCN'}, {'Symbol': 'MBNKP'}, {'Symbol': 'MCEP'}, {'Symbol': 'MLND'}, {'Symbol': 'MMAC'}, {'Symbol': 'MNCLU'}, {'Symbol': 'MNPR'}, {'Symbol': 'NVEE'}, {'Symbol': 'NXTD'}, {'Symbol': 'OPOF'}, {'Symbol': 'OPTT'}, {'Symbol': 'ORGO'}, {'Symbol': 'ORSNU'}, {'Symbol': 'OTEL'}, {'Symbol': 'PBFS'}, {'Symbol': 'PBTS'}, {'Symbol': 'PCSB'}, {'Symbol': 'PECK'}, {'Symbol': 'PEIX'}, {'Symbol': 'PFIE'}, {'Symbol': 'PLIN'}, {'Symbol': 'POPE'}, {'Symbol': 'QRHC'}, {'Symbol': 'SES'}, {'Symbol': 'SHSP'}, {'Symbol': 'SNSS'}, {'Symbol': 'SSNT'}, {'Symbol': 'STKS'}, {'Symbol': 'TGLS'}, {'Symbol': 'TMSR'}, {'Symbol': 'VERB'}, {'Symbol': 'VMD'}, {'Symbol': 'VRRM'}, {'Symbol': 'VTIQW'}, {'Symbol': 'VVPR'}, {'Symbol': 'WHLM'}, {'Symbol': 'WHLR'}, {'Symbol': 'XBIOW'}, {'Symbol': 'XPEL'}]}

exec(code, env_args)
