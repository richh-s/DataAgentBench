code = """import pandas as pd
import json

with open(locals()['var_function-call-11820878449294623413'], 'r') as f:
    nyse_stocks_info = json.load(f)

nyse_stocks_df = pd.DataFrame(nyse_stocks_info)

stock_performance = []
debug_log = [] # To capture errors or info

for index, row in nyse_stocks_df.iterrows():
    symbol = row['Symbol']
    company_description = row['Company Description']

    query_string = "SELECT Date, Open, Close FROM \"" + symbol + "\" WHERE Date LIKE '2017-%';"

    try:
        query_result = default_api.query_db(
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
        elif query_result and 'error' in query_result:
            debug_log.append(f"Error for {symbol}: {query_result['error']}")
        else:
            debug_log.append(f"No results or unexpected format for {symbol}")

    except Exception as e:
        debug_log.append(f"General exception for {symbol}: {str(e)}")


top_5_stocks = sorted(stock_performance, key=lambda x: x['Difference'], reverse=True)[:5]

final_answer = [stock['Company Description'] for stock in top_5_stocks]

print('__RESULT__:')
print(json.dumps(final_answer if final_answer else debug_log))"""

env_args = {'var_function-call-11820878449294623413': 'file_storage/function-call-11820878449294623413.json', 'var_function-call-2353068768197412516': [], 'var_function-call-6386032267884681873': [], 'var_function-call-12109383824988029975': [], 'var_function-call-5615837029812849117': 'file_storage/function-call-5615837029812849117.json', 'var_function-call-4321617129231401927': [{'Date': '1987-09-30', 'Open': '14.988152503967283', 'Close': '15.107105255126951'}], 'var_function-call-7866009266541559027': 'file_storage/function-call-7866009266541559027.json', 'var_function-call-9261700538938387197': [], 'var_function-call-9707489483092941224': 'file_storage/function-call-9707489483092941224.json', 'var_function-call-17299308845485818496': []}

exec(code, env_args)
