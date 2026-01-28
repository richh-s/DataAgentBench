code = """import json
import pandas as pd

# Load tickers and company data
with open(locals()['var_functions.execute_python:6'], 'r') as f:
    data = json.load(f)

tickers = data['existing_tickers']
company_names = data['company_names']

# Store results
results = []

# For each ticker, we need to query the 2019 data
# We'll build a query that calculates the intraday range percentage
# and counts days where (High-Low)/Low*100 > 20

for ticker in tickers[:10]:  # Process only first 10 for testing to check performance
    query = f"""
    SELECT 
        COUNT(*) as high_volatility_days
    FROM "{ticker}" 
    WHERE 
        Date >= '2019-01-01' 
        AND Date <= '2019-12-31'
        AND Low > 0  -- Avoid division by zero
        AND ((High - Low) / Low * 100) > 20
    """
    
    # We'll use query_db tool for each ticker
    # But since we can't call tools from inside execute_python, we need to collect queries
    results.append({
        'ticker': ticker,
        'company_name': company_names.get(ticker, ''),
        'query': query
    })

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json'}

exec(code, env_args)
