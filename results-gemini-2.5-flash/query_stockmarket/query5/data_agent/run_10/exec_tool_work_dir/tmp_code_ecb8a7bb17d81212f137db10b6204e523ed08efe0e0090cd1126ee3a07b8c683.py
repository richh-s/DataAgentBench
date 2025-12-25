code = """import json
import pandas as pd

symbols = locals()['var_function-call-16591465081895578054']

companies_high_volatility_days = []

for symbol in symbols:
    try:
        query_output_raw = default_api.query_db(db_name = "stocktrade_database", query = f"SELECT Date, High, Low FROM {symbol} WHERE strftime('%Y', CAST(Date AS DATE)) = '2019';")
        
        daily_data = []

        if isinstance(query_output_raw, dict) and "query_db_response" in query_output_raw:
            raw_results = query_output_raw["query_db_response"].get("results", [])
            if isinstance(raw_results, str) and raw_results.endswith('.json'):
                with open(raw_results, 'r') as f:
                    daily_data = json.load(f)
            elif isinstance(raw_results, list):
                daily_data = raw_results
        else:
            print(f"Skipping symbol {symbol} due to invalid query output structure: {query_output_raw}")
            continue

        high_volatility_days_count = 0
        for day in daily_data:
            try:
                high_price = float(day.get('High'))
                low_price = float(day.get('Low'))
                if (high_price - low_price) > (0.2 * low_price):
                    high_volatility_days_count += 1
            except (TypeError, ValueError) as price_error:
                print(f"Error parsing High/Low prices for {symbol} on date {day.get('Date')}: {price_error}. Data: {day}")
                continue
        
        companies_high_volatility_days.append({'symbol': symbol, 'high_volatility_days': high_volatility_days_count})
    except Exception as e:
        print(f"An unexpected error occurred for symbol {symbol}: {e}")

sorted_companies = sorted(companies_high_volatility_days, key = lambda x: x['high_volatility_days'], reverse = True)
top_5_companies = sorted_companies[:5]

with open(locals()['var_function-call-4277449068954589980'], 'r') as f:
    symbols_and_descriptions = json.load(f)

final_answer = []
for company in top_5_companies:
    symbol = company['symbol']
    company_description = symbols_and_descriptions.get(symbol, "N/A")
    if ' specializes' in company_description:
        company_name = company_description.split(' specializes')[0]
    else:
        company_name = company_description
    final_answer.append(f"{company_name} ({symbol}): {company['high_volatility_days']} high volatility days")

print("__RESULT__:")
print(json.dumps(final_answer))"""

env_args = {'var_function-call-17136481753764545298': 'file_storage/function-call-17136481753764545298.json', 'var_function-call-4277449068954589980': 'file_storage/function-call-4277449068954589980.json', 'var_function-call-16591465081895578054': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-5586425546104752979': 'file_storage/function-call-5586425546104752979.json'}

exec(code, env_args)
