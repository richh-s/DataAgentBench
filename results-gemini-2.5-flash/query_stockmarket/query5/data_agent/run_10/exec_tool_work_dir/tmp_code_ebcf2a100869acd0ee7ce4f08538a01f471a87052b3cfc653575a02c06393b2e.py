code = """import json
import pandas as pd

symbols = locals()['var_function-call-16591465081895578054']

companies_high_volatility_days = []
debug_log = [] # To capture debugging messages

for symbol in symbols:
    daily_data = []

    try:
        query_output = default_api.query_db(db_name="stocktrade_database", query=f"SELECT Date, High, Low FROM {symbol} WHERE strftime('%Y', CAST(Date AS DATE)) = '2019';")

        if isinstance(query_output, str):
            debug_log.append(f"Skipping symbol {symbol} due to direct query error: {query_output}")
            continue
        elif isinstance(query_output, dict) and "query_db_response" in query_output:
            response_content = query_output["query_db_response"]
            if "results" in response_content:
                raw_results = response_content["results"]
                if isinstance(raw_results, str) and raw_results.endswith('.json'):
                    try:
                        with open(raw_results, 'r') as f:
                            daily_data = json.load(f)
                    except Exception as file_error:
                        debug_log.append(f"Error loading JSON from file for symbol {symbol}: {file_error}. File: {raw_results}")
                        continue
                elif isinstance(raw_results, list):
                    daily_data = raw_results
                else:
                    debug_log.append(f"Skipping symbol {symbol} due to unexpected raw_results type in response content: {type(raw_results)}")
                    continue
            elif "error" in response_content:
                debug_log.append(f"Skipping symbol {symbol} due to query error within response: {response_content['error']}")
                continue
            else:
                debug_log.append(f"Skipping symbol {symbol} due to missing 'results' or 'error' in query_db_response: {response_content}")
                continue
        else:
            debug_log.append(f"Skipping symbol {symbol} due to unexpected query_output structure: {query_output}")
            continue

        if not isinstance(daily_data, list):
            debug_log.append(f"Skipping symbol {symbol} because daily_data is not a list after processing: {type(daily_data)}")
            continue

        high_volatility_days_count = 0
        for day in daily_data:
            try:
                high_price = float(day.get('High'))
                low_price = float(day.get('Low'))
                if low_price is not None and high_price is not None and low_price > 0 and (high_price - low_price) > (0.2 * low_price):
                    high_volatility_days_count += 1
            except (TypeError, ValueError) as price_error:
                debug_log.append(f"Error parsing High/Low prices for {symbol} on date {day.get('Date')}: {price_error}. Data: {day}")
                continue
        
        if high_volatility_days_count > 0:
            companies_high_volatility_days.append({'symbol': symbol, 'high_volatility_days': high_volatility_days_count})
            debug_log.append(f"Processed symbol {symbol} with {high_volatility_days_count} high volatility days.")
        else:
            debug_log.append(f"Processed symbol {symbol}, but found 0 high volatility days.")

    except Exception as e:
        debug_log.append(f"An unexpected error occurred for symbol {symbol}: {e}")

sorted_companies = sorted(companies_high_volatility_days, key=lambda x: x['high_volatility_days'], reverse=True)
top_5_companies = sorted_companies[:5]

with open(locals()['var_function-call-4277449068954589980'], 'r') as f:
    symbols_and_descriptions = json.load(f)

final_answer_companies = []
for company in top_5_companies:
    symbol = company['symbol']
    company_description = symbols_and_descriptions.get(symbol, "N/A")
    if ' specializes' in company_description:
        company_name = company_description.split(' specializes')[0]
    else:
        company_name = company_description
    final_answer_companies.append(f"{company_name} ({symbol})")

final_output = {
    "top_5_companies": final_answer_companies,
    "debug_log": debug_log,
    "total_companies_with_volatility": len(companies_high_volatility_days)
}

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-17136481753764545298': 'file_storage/function-call-17136481753764545298.json', 'var_function-call-4277449068954589980': 'file_storage/function-call-4277449068954589980.json', 'var_function-call-16591465081895578054': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-5586425546104752979': 'file_storage/function-call-5586425546104752979.json', 'var_function-call-6756011238241088788': [], 'var_function-call-5900565176214233050': [], 'var_function-call-12898007050749787695': [], 'var_function-call-11459846448680200742': [], 'var_function-call-12157875342163066569': [], 'var_function-call-14005437640277379847': 'file_storage/function-call-14005437640277379847.json', 'var_function-call-9447603195851757726': []}

exec(code, env_args)
