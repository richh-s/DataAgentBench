code = """import json

# Read NASDAQ Capital Market data
file_path = 'var_functions.query_db:48.json'
with open(file_path, 'r') as f:
    nasdaq_stocks = json.load(f)

# Create mapping of ticker to company name
ticker_to_company = {}
for stock in nasdaq_stocks:
    symbol = stock['Symbol']
    desc = stock['Company Description']
    # Extract company name (simplified)
    company_name = desc.split('.')[0]
    ticker_to_company[symbol] = company_name

tickers = list(ticker_to_company.keys())
print('Processing', len(tickers), 'tickers...')

# Process each ticker
results = []
processed = 0
errors = 0

for ticker in tickers:
    try:
        # Query 2019 data
        date_filter = "Date >= '2019-01-01' AND Date <= '2019-12-31'"
        query = 'SELECT High, Low FROM "' + ticker + '" WHERE ' + date_filter
        data = query_db('stocktrade_database', query)
        
        if data and len(data) > 0:
            volatile_days = 0
            for row in data:
                high_val = float(row['High'])
                low_val = float(row['Low'])
                if low_val > 0 and (high_val - low_val) > (0.2 * low_val):
                    volatile_days += 1
            
            results.append({
                'ticker': ticker,
                'company': ticker_to_company[ticker],
                'volatile_days': volatile_days
            })
        
        processed += 1
        
    except Exception as e:
        errors += 1
        processed += 1

# Sort by volatile_days
results.sort(key=lambda x: x['volatile_days'], reverse=True)

top_5 = results[:5]

output = {
    'processed': processed,
    'errors': errors,
    'results_with_data': len(results),
    'top_5': top_5
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['stockinfo'], 'var_functions.query_db:6': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}, {'Date': '2019-01-09', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}, {'Date': '2019-01-10', 'Open': '27.690000534057617', 'High': '28.149999618530277', 'Low': '27.690000534057617', 'Close': '28.0', 'Adj Close': '28.0', 'Volume': '900'}, {'Date': '2019-01-11', 'Open': '28.0', 'High': '28.0', 'Low': '28.0', 'Close': '28.0', 'Adj Close': '28.0', 'Volume': '100'}, {'Date': '2019-01-14', 'Open': '28.0', 'High': '28.0', 'Low': '28.0', 'Close': '28.0', 'Adj Close': '28.0', 'Volume': '100'}, {'Date': '2019-01-15', 'Open': '29.149999618530277', 'High': '31.0', 'Low': '29.059999465942383', 'Close': '31.0', 'Adj Close': '31.0', 'Volume': '1800'}], 'var_functions.query_db:12': [{'Symbol': 'AGMH'}, {'Symbol': 'ALACU'}, {'Symbol': 'AMHC'}, {'Symbol': 'ANDA'}, {'Symbol': 'APEX'}, {'Symbol': 'BCLI'}, {'Symbol': 'BHAT'}, {'Symbol': 'BIOC'}, {'Symbol': 'BKYI'}, {'Symbol': 'BLFS'}, {'Symbol': 'BOSC'}, {'Symbol': 'BOTJ'}, {'Symbol': 'BWEN'}, {'Symbol': 'CBAT'}, {'Symbol': 'CCCL'}, {'Symbol': 'CDMOP'}, {'Symbol': 'CEMI'}, {'Symbol': 'CFBK'}, {'Symbol': 'CFFA'}, {'Symbol': 'CLRB'}, {'Symbol': 'CORV'}, {'Symbol': 'CPAAU'}, {'Symbol': 'CPAH'}, {'Symbol': 'CUBA'}, {'Symbol': 'CVV'}, {'Symbol': 'DZSI'}, {'Symbol': 'ELSE'}, {'Symbol': 'EXPC'}, {'Symbol': 'EYEG'}, {'Symbol': 'FAMI'}, {'Symbol': 'FNCB'}, {'Symbol': 'FSBW'}, {'Symbol': 'FTFT'}, {'Symbol': 'GDYN'}, {'Symbol': 'GLG'}, {'Symbol': 'GRNVU'}, {'Symbol': 'GTEC'}, {'Symbol': 'HCCOU'}, {'Symbol': 'HNNA'}, {'Symbol': 'HQI'}, {'Symbol': 'HRTX'}, {'Symbol': 'IDEX'}, {'Symbol': 'IGIC'}, {'Symbol': 'IOTS'}, {'Symbol': 'ISNS'}, {'Symbol': 'ITI'}, {'Symbol': 'LACQ'}, {'Symbol': 'MBCN'}, {'Symbol': 'MBNKP'}, {'Symbol': 'MCEP'}, {'Symbol': 'MLND'}, {'Symbol': 'MMAC'}, {'Symbol': 'MNCLU'}, {'Symbol': 'MNPR'}, {'Symbol': 'NVEE'}, {'Symbol': 'NXTD'}, {'Symbol': 'OPOF'}, {'Symbol': 'OPTT'}, {'Symbol': 'ORGO'}, {'Symbol': 'ORSNU'}, {'Symbol': 'OTEL'}, {'Symbol': 'PBFS'}, {'Symbol': 'PBTS'}, {'Symbol': 'PCSB'}, {'Symbol': 'PECK'}, {'Symbol': 'PEIX'}, {'Symbol': 'PFIE'}, {'Symbol': 'PLIN'}, {'Symbol': 'POPE'}, {'Symbol': 'QRHC'}, {'Symbol': 'SES'}, {'Symbol': 'SHSP'}, {'Symbol': 'SNSS'}, {'Symbol': 'SSNT'}, {'Symbol': 'STKS'}, {'Symbol': 'TGLS'}, {'Symbol': 'TMSR'}, {'Symbol': 'VERB'}, {'Symbol': 'VMD'}, {'Symbol': 'VRRM'}, {'Symbol': 'VTIQW'}, {'Symbol': 'VVPR'}, {'Symbol': 'WHLM'}, {'Symbol': 'WHLR'}, {'Symbol': 'XBIOW'}, {'Symbol': 'XPEL'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': [{'Date': '2019-01-02', 'Open': '3.490000009536743', 'High': '3.509999990463257', 'Low': '3.309999942779541', 'Close': '3.4600000381469727', 'Adj Close': '3.4600000381469727', 'Volume': '92200'}, {'Date': '2019-01-03', 'Open': '3.4600000381469727', 'High': '3.509999990463257', 'Low': '3.3499999046325684', 'Close': '3.400000095367432', 'Adj Close': '3.400000095367432', 'Volume': '66100'}, {'Date': '2019-01-04', 'Open': '3.4800000190734863', 'High': '3.4800000190734863', 'Low': '3.369999885559082', 'Close': '3.369999885559082', 'Adj Close': '3.369999885559082', 'Volume': '36100'}, {'Date': '2019-01-07', 'Open': '3.569999933242798', 'High': '3.569999933242798', 'Low': '3.380000114440918', 'Close': '3.380000114440918', 'Adj Close': '3.380000114440918', 'Volume': '47000'}, {'Date': '2019-01-08', 'Open': '3.4600000381469727', 'High': '3.5199999809265137', 'Low': '3.359999895095825', 'Close': '3.400000095367432', 'Adj Close': '3.400000095367432', 'Volume': '48500'}], 'var_functions.execute_python:28': {'total_tickers': 86, 'sample_tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
