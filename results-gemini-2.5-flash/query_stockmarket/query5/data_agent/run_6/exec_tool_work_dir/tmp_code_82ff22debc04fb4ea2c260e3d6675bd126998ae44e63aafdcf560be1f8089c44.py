code = """import json
import pandas as pd

with open(locals()['var_function-call-12471544107158936253'], 'r') as f:
    nasdaq_capital_market_stocks = json.load(f)

company_day_counts = []

for stock_info in nasdaq_capital_market_stocks:
    symbol = stock_info['Symbol']
    company_description = stock_info['Company Description']

    try:
        # Query stocktrade_database for each symbol
        daily_data = default_api.query_db(db_name='stocktrade_database', query=f'SELECT Date, High, Low FROM "{symbol}" WHERE strftime("%%Y", Date) = \'2019\';')
        daily_data_list = daily_data['query_db_response']['results']

        count = 0
        for day in daily_data_list:
            high = day['High']
            low = day['Low']
            if (high - low) > 0.20 * low:
                count += 1
        company_day_counts.append({'Symbol': symbol, 'Company Description': company_description, 'Count': count})
    except Exception as e:
        # Handle cases where a symbol might not have a table in stocktrade_database
        # print(f'Error processing {symbol}: {e}') # Removed print statement to avoid interfering with __RESULT__ printing
        continue

df = pd.DataFrame(company_day_counts)
sorted_df = df.sort_values(by='Count', ascending=False).head(5)

result = sorted_df[['Company Description']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-1407024033300719416': ['stockinfo'], 'var_function-call-7881696344376959420': 'file_storage/function-call-7881696344376959420.json', 'var_function-call-12471544107158936253': 'file_storage/function-call-12471544107158936253.json'}

exec(code, env_args)
