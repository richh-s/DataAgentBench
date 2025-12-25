code = """import json

with open(locals()['var_function-call-7905397860107438007'], 'r') as f:
    relevant_stocks = json.load(f)

batch = relevant_stocks[0:30]
queries = []
for stock in batch:
    sym = stock['Symbol']
    q = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"" + sym + "\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    queries.append(q)

final_query = " UNION ALL ".join(queries)
print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-3716719748068765207': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-18147196658339150009': 'file_storage/function-call-18147196658339150009.json', 'var_function-call-7489045623888971666': 'file_storage/function-call-7489045623888971666.json', 'var_function-call-7905397860107438007': 'file_storage/function-call-7905397860107438007.json', 'var_function-call-1245125062215000262': 234, 'var_function-call-7267744829723885900': [{'Date': '2019-10-24', 'Open': '25.399999618530277', 'High': '25.489999771118164', 'Low': '25.290000915527344', 'Close': '25.450000762939453', 'Adj Close': '25.450000762939453', 'Volume': '1422300'}], 'var_function-call-9587358287655727931': 'file_storage/function-call-9587358287655727931.json'}

exec(code, env_args)
