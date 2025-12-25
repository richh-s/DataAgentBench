code = """import json
target_stocks_file = locals()['var_function-call-4127219778048163343']
with open(target_stocks_file, 'r') as f:
    target_stocks = json.load(f)

# Get first 50
batch = target_stocks[0:50]
queries = []
for item in batch:
    sym = item['Symbol']
    q = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as Up, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as Down FROM \"" + sym + "\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    queries.append(q)

final_query = " UNION ALL ".join(queries)
print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-16810398710687085223': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-1631025954943238764': 'file_storage/function-call-1631025954943238764.json', 'var_function-call-4060108603261474737': 'file_storage/function-call-4060108603261474737.json', 'var_function-call-4127219778048163343': 'file_storage/function-call-4127219778048163343.json', 'var_function-call-2579092286742790265': 234, 'var_function-call-8724790248565907862': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG'], 'var_function-call-11822337928771739869': [{'Symbol': 'AEFC', 'Up': 'nan', 'Down': 'nan'}], 'var_function-call-18156010135136407125': [{'Date': '2019-10-24', 'Open': '25.399999618530277', 'High': '25.489999771118164', 'Low': '25.290000915527344', 'Close': '25.450000762939453', 'Adj Close': '25.450000762939453', 'Volume': '1422300'}, {'Date': '2019-10-25', 'Open': '25.61000061035156', 'High': '25.68000030517578', 'Low': '25.559999465942383', 'Close': '25.670000076293945', 'Adj Close': '25.670000076293945', 'Volume': '1088300'}, {'Date': '2019-10-28', 'Open': '25.68000030517578', 'High': '25.68000030517578', 'Low': '25.549999237060547', 'Close': '25.59000015258789', 'Adj Close': '25.59000015258789', 'Volume': '1128400'}, {'Date': '2019-10-29', 'Open': '25.61000061035156', 'High': '25.61000061035156', 'Low': '25.5', 'Close': '25.56999969482422', 'Adj Close': '25.56999969482422', 'Volume': '497700'}, {'Date': '2019-10-30', 'Open': '25.530000686645508', 'High': '25.670000076293945', 'Low': '25.5', 'Close': '25.65999984741211', 'Adj Close': '25.65999984741211', 'Volume': '1517600'}], 'var_function-call-1763765436576342550': [{'min(Date)': '2019-10-24', 'max(Date)': '2020-04-01'}]}

exec(code, env_args)
