code = """import json
import pandas as pd

symbols = json.loads(locals()['var_function-call-16591465081895578054'])

companies_high_volatility_days = []

for symbol in symbols:
    try:
        query_output = default_api.query_db(db_name = "stocktrade_database", query = f"SELECT Date, High, Low FROM {symbol} WHERE strftime('%Y', CAST(Date AS DATE)) = '2019';")
        
        # The structure is query_output = {"query_db_response": {"results": <data>}}
        # <data> can be a list of records or a file path string
        raw_results = query_output.get("query_db_response", {}).get("results", [])

        if isinstance(raw_results, str) and raw_results.endswith('.json'):
            # If it's a file path (for large results), load from the file
            with open(raw_results, 'r') as f:
                daily_data = json.load(f)
        elif isinstance(raw_results, list):
            # If it's a list of records directly
            daily_data = raw_results
        else:
            daily_data = [] # Fallback for unexpected format
        
        high_volatility_days_count = 0
        for day in daily_data:
            high_price = float(day['High'])
            low_price = float(day['Low'])
            if (high_price - low_price) > (0.2 * low_price):
                high_volatility_days_count += 1
        
        companies_high_volatility_days.append({'symbol': symbol, 'high_volatility_days': high_volatility_days_count})
    except Exception as e:
        # Handle cases where a table for the symbol might not exist or other query errors
        print(f"Error querying data for symbol {symbol}: {e}")

sorted_companies = sorted(companies_high_volatility_days, key = lambda x: x['high_volatility_days'], reverse = True)
top_5_companies = sorted_companies[:5]

# Load the symbols_and_descriptions from the file
with open(locals()['var_function-call-4277449068954589980'], 'r') as f:
    symbols_and_descriptions = json.load(f)

final_answer = []
for company in top_5_companies:
    symbol = company['symbol']
    # Use .get() with a default value to avoid KeyError if ' specializes' is not found
    company_description = symbols_and_descriptions.get(symbol, "N/A")
    # Split only if ' specializes' is in the description
    if ' specializes' in company_description:
        company_name = company_description.split(' specializes')[0]
    else:
        company_name = company_description # Use full description if ' specializes' not found
    final_answer.append(f"{company_name} ({symbol}): {company['high_volatility_days']} high volatility days")

print("__RESULT__:")
print(json.dumps(final_answer))"""

env_args = {'var_function-call-17136481753764545298': 'file_storage/function-call-17136481753764545298.json', 'var_function-call-4277449068954589980': 'file_storage/function-call-4277449068954589980.json', 'var_function-call-16591465081895578054': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-5586425546104752979': 'file_storage/function-call-5586425546104752979.json'}

exec(code, env_args)
