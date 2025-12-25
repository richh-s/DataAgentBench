code = """import json

with open(locals()['var_function-call-16488807000991432586'], 'r') as f:
    valid_stocks = json.load(f)

subqueries = []
for stock in valid_stocks:
    symbol = stock['Symbol']
    # Use .format()
    sq = "SELECT '{0}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"{0}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'".format(symbol)
    subqueries.append(sq)

full_query_body = " UNION ALL ".join(subqueries)
final_query = "SELECT Symbol, UpDays, DownDays FROM (" + full_query_body + ") WHERE UpDays > DownDays ORDER BY UpDays DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-17490755573003883636': 'file_storage/function-call-17490755573003883636.json', 'var_function-call-8209134030405193310': 'file_storage/function-call-8209134030405193310.json', 'var_function-call-16488807000991432586': 'file_storage/function-call-16488807000991432586.json', 'var_function-call-8713500348890617850': 'file_storage/function-call-8713500348890617850.json'}

exec(code, env_args)
