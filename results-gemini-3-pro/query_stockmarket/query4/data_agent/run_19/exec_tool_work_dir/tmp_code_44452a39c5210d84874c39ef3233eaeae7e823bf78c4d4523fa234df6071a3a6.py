code = """import json

# Load stocks from step 1
with open(locals()['var_function-call-16367055759489104877'], 'r') as f:
    stock_info_list = json.load(f)

# Load tables from step 2
with open(locals()['var_function-call-10823379769543872171'], 'r') as f:
    tables = set(json.load(f))

# Filter stocks that have tables
valid_stocks = []
stock_descs = {}
for s in stock_info_list:
    sym = s['Symbol']
    if sym in tables:
        valid_stocks.append(sym)
        stock_descs[sym] = s['Company Description']

# Generate SQL query
queries = []
for sym in valid_stocks:
    # Construct query string safely
    q = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"" + sym + "\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps({"query": full_query, "descriptions": stock_descs}))"""

env_args = {'var_function-call-16367055759489104877': 'file_storage/function-call-16367055759489104877.json', 'var_function-call-4289538722941154091': 234, 'var_function-call-9869948339806265724': [{'Date': '1987-09-30', 'Open': '14.988152503967283', 'High': '15.701873779296877', 'Low': '14.988152503967283', 'Close': '15.107105255126951', 'Adj Close': '8.918145179748535', 'Volume': '2292200'}, {'Date': '1987-10-01', 'Open': '15.107105255126951', 'High': '15.345012664794922', 'Low': '14.988152503967283', 'Close': '15.345012664794922', 'Adj Close': '9.05859375', 'Volume': '468200'}, {'Date': '1987-10-02', 'Open': '15.345012664794922', 'High': '15.701873779296877', 'Low': '15.107105255126951', 'Close': '15.701873779296877', 'Adj Close': '9.26926040649414', 'Volume': '371600'}, {'Date': '1987-10-05', 'Open': '15.701873779296877', 'High': '15.701873779296877', 'Low': '15.226058959960938', 'Close': '15.701873779296877', 'Adj Close': '9.26926040649414', 'Volume': '121300'}, {'Date': '1987-10-06', 'Open': '15.58292007446289', 'High': '15.58292007446289', 'Low': '15.226058959960938', 'Close': '15.463966369628906', 'Adj Close': '9.128814697265623', 'Volume': '159300'}], 'var_function-call-10823379769543872171': 'file_storage/function-call-10823379769543872171.json'}

exec(code, env_args)
