code = """import json
import pandas as pd

with open(locals()['var_function-call-12471544107158936253'], 'r') as f:
    nasdaq_capital_market_stocks = json.load(f)

company_day_counts = []

for stock_info in nasdaq_capital_market_stocks:
    symbol = stock_info['Symbol']
    company_description = stock_info['Company Description']

    count = 0 # Initialize count for each symbol

    try:
        # Construct the SQL query string
        sql_query = "SELECT Date, High, Low FROM \"" + symbol + "\" WHERE strftime('%Y', Date) = '2019';"
        daily_data_response = default_api.query_db(db_name='stocktrade_database', query=sql_query)

        # Check if the result is a successful query with 'results' key
        if isinstance(daily_data_response, dict) and 'query_db_response' in daily_data_response and 'results' in daily_data_response['query_db_response']:
            daily_data_list = daily_data_response['query_db_response']['results']
            for day in daily_data_list:
                high = day['High']
                low = day['Low']
                if (high - low) > 0.20 * low:
                    count += 1
        # If the query failed or returned an unexpected structure, count remains 0

    except Exception as e:
        # If any other error occurs during query or processing, count remains 0.
        pass # The count is already 0, and we'll append it below.

    company_day_counts.append({'Symbol': symbol, 'Company Description': company_description, 'Count': count})

df = pd.DataFrame(company_day_counts)
sorted_df = df.sort_values(by='Count', ascending=False).head(5)

result = sorted_df[['Company Description']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-1407024033300719416': ['stockinfo'], 'var_function-call-7881696344376959420': 'file_storage/function-call-7881696344376959420.json', 'var_function-call-12471544107158936253': 'file_storage/function-call-12471544107158936253.json'}

exec(code, env_args)
