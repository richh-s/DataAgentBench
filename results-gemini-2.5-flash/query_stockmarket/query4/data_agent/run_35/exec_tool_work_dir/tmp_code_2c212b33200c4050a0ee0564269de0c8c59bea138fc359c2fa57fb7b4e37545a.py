code = """import pandas as pd
import json

with open(locals()['var_function-call-15489448046703615035'], 'r') as f:
    nyse_stocks_info = json.load(f)

nyse_stocks_df = pd.DataFrame(nyse_stocks_info)

stock_performance = []

for index, row in nyse_stocks_df.iterrows():
    symbol = row['Symbol']
    company_description = row['Company Description']

    query_string = "SELECT Date, Open, Close FROM \"" + symbol + "\" WHERE Date LIKE '2017-%';"

    try:
        # Call query_db directly as it seems to be available in the execution environment
        query_result = query_db(
            db_name="stocktrade_database",
            query=query_string
        )

        if query_result and 'results' in query_result and query_result['results']:
            stock_data = query_result['results']

            up_days = 0
            down_days = 0

            for day_data in stock_data:
                open_price = float(day_data['Open'])
                close_price = float(day_data['Close'])

                if close_price > open_price:
                    up_days += 1
                elif close_price < open_price:
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
        # Continue to next stock if there's an error (e.g., table not found, or data parsing error)
        continue

# Sort by difference in descending order and get the top 5
top_5_stocks = sorted(stock_performance, key=lambda x: x['Difference'], reverse=True)[:5]

# Extract only company descriptions for the final answer
final_answer = [stock['Company Description'] for stock in top_5_stocks]

print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_function-call-11820878449294623413': 'file_storage/function-call-11820878449294623413.json', 'var_function-call-2353068768197412516': [], 'var_function-call-6386032267884681873': [], 'var_function-call-12109383824988029975': [], 'var_function-call-5615837029812849117': 'file_storage/function-call-5615837029812849117.json', 'var_function-call-4321617129231401927': [{'Date': '1987-09-30', 'Open': '14.988152503967283', 'Close': '15.107105255126951'}], 'var_function-call-7866009266541559027': 'file_storage/function-call-7866009266541559027.json', 'var_function-call-9261700538938387197': [], 'var_function-call-9707489483092941224': 'file_storage/function-call-9707489483092941224.json', 'var_function-call-17299308845485818496': [], 'var_function-call-6396896753408482335': 'file_storage/function-call-6396896753408482335.json', 'var_function-call-15489448046703615035': 'file_storage/function-call-15489448046703615035.json'}

exec(code, env_args)
