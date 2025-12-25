code = """import json

key_info = 'var_function-call-6223047370472614305'
key_tables = 'var_function-call-14531105657415532109'

with open(locals()[key_info], 'r') as f:
    stock_info = json.load(f)

with open(locals()[key_tables], 'r') as f:
    tables = json.load(f)

tables_set = set(tables)
valid_stocks = [s for s in stock_info if s['Symbol'] in tables_set]

s = valid_stocks[0]
sym = s['Symbol']
q = f"SELECT '{sym}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"{sym}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"

print("__RESULT__:")
print(json.dumps({"debug_query": q, "count": len(valid_stocks)}))"""

env_args = {'var_function-call-5334989958488010331': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-6223047370472614305': 'file_storage/function-call-6223047370472614305.json', 'var_function-call-14531105657415532109': 'file_storage/function-call-14531105657415532109.json', 'var_function-call-202123142740787655': 'file_storage/function-call-202123142740787655.json', 'var_function-call-8729269538483017222': 'file_storage/function-call-8729269538483017222.json', 'var_function-call-1757640261265007625': 'file_storage/function-call-1757640261265007625.json'}

exec(code, env_args)
