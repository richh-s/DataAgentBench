code = """import pandas as pd
import json

with open(locals()['var_function-call-11820878449294623413'], 'r') as f:
    nyse_stocks_info = json.load(f)

nyse_stocks_df = pd.DataFrame(nyse_stocks_info)

stock_performance = []

for index, row in nyse_stocks_df.iterrows():
    symbol = row['Symbol']
    company_description = row['Company Description']

    # Construct the query string without f-string to avoid quoting issues
    query_string = "SELECT Date, Open, Close FROM \"" + symbol + "\" WHERE Date LIKE '2017-%';"

    try:
        query_result = default_api.query_db(
            db_name="stocktrade_database",
            query=query_string
        )

        # Check if 'results' key exists and is not empty
        if query_result and 'results' in query_result and query_result['results']:
            stock_data = query_result['results']

            up_days = 0
            down_days = 0

            for day_data in stock_data:
                if day_data['Close'] > day_data['Open']:
                    up_days += 1
                elif day_data['Close'] < day_data['Open']:
                    down_days += 1

            if up_days > down_days:
                stock_performance.append({
                    'Symbol': symbol,
                    'Company Description': company_description,
                    'Up Days': up_days,
                    'Down Days': down_days,
                    'Difference': up_days - down_days
                })
    except Exception as e:
        # print(f"Error processing stock {symbol}: {e}") # Comment out f-string in error message for consistency
        continue

# Sort by difference in descending order and get the top 5
top_5_stocks = sorted(stock_performance, key=lambda x: x['Difference'], reverse=True)[:5]

# Extract only company descriptions for the final answer
final_answer = [stock['Company Description'] for stock in top_5_stocks]

print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_function-call-11820878449294623413': 'file_storage/function-call-11820878449294623413.json', 'var_function-call-2353068768197412516': [], 'var_function-call-6386032267884681873': []}

exec(code, env_args)
