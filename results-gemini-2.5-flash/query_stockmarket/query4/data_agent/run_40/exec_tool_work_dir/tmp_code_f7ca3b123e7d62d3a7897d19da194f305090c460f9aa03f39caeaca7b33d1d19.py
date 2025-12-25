code = """import json

with open(locals()['var_function-call-17729935126212957061'], 'r') as f:
    nyse_non_etf_stocks = json.load(f)

symbols = list(nyse_non_etf_stocks.keys())

all_select_statements = []
for symbol in symbols:
    # Construct each SELECT statement. Double quotes for table name and single quotes for string literals.
    # The table name (symbol) should be enclosed in double quotes for DuckDB.
    select_statement = f"SELECT '{symbol}' AS Symbol, Date, Open, Close FROM \"{symbol}\" WHERE Date BETWEEN '2017-01-01' AND '2017-12-31'"
    all_select_statements.append(select_statement)

# Join all SELECT statements with UNION ALL
union_query = " UNION ALL ".join(all_select_statements)

print("__RESULT__:")
print(json.dumps(union_query))"""

env_args = {'var_function-call-16320646233867090762': 'file_storage/function-call-16320646233867090762.json', 'var_function-call-17729935126212957061': 'file_storage/function-call-17729935126212957061.json'}

exec(code, env_args)
