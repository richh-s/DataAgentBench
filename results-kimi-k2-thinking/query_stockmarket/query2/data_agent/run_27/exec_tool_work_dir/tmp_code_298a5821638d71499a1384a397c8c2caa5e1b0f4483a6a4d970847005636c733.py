code = """import json

# Query stocktrade_database for each ETF to check if adjusted close exceeded $200 in 2015
nyse_arca_etfs = locals()['var_functions.execute_python:14']

# Create a list of queries for the first 10 ETFs
queries = []
for i, symbol in enumerate(nyse_arca_etfs[:10]):
    query = f"""
    SELECT '{symbol}' as Symbol, 
           MAX("Adj Close") as max_adj_close,
           MIN(Date) as first_date,
           MAX(Date) as last_date,
           COUNT(*) as record_count
    FROM "{symbol}"
    WHERE Date BETWEEN '2015-01-01' AND '2015-12-31'
    """
    queries.append(query)

# Join queries with UNION ALL
union_query = " UNION ALL ".join(queries)

print('__RESULT__:')
print(json.dumps({'query': union_query}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.list_db:11': 'file_storage/functions.list_db:11.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:14': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}

exec(code, env_args)
