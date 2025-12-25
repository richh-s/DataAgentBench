code = """import json

sym = "ABC"
# q = 'SELECT \'' + sym + '\' AS Symbol FROM "' + sym + '" WHERE "Adj Close" > 200'
# Using tripe quotes? No.
# Use sql dialect that uses single quotes? No, table names in DuckDB need double quotes if case sensitive or unusual, but here they are just tickers.
# Tickers might not need quotes if they are simple.
# But "Adj Close" needs quotes.

# Let's try to construct the string without backslashes if possible?
# q = "SELECT '" + sym + "' AS Symbol FROM " + '"' + sym + '"' + " WHERE " + '"' + "Adj Close" + '"' + " > 200"

q = 'SELECT \'{}\' AS Symbol FROM "{}" WHERE "Adj Close" > 200'.format(sym, sym)

print(q)
print("__RESULT__:")
print(json.dumps([q]))"""

env_args = {'var_function-call-16817766424675427763': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-12499338069894364565': 'file_storage/function-call-12499338069894364565.json', 'var_function-call-9293888739121941435': 'file_storage/function-call-9293888739121941435.json', 'var_function-call-14915668202036031869': 'file_storage/function-call-14915668202036031869.json', 'var_function-call-7434327097366713516': 'file_storage/function-call-7434327097366713516.json', 'var_function-call-2380757378116549886': [{'Date': '2018-08-15'}], 'var_function-call-7107660430946483903': 1435, 'var_function-call-3063757488003502576': 'Hello', 'var_function-call-16536889929438009237': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'var_function-call-18131283317376313178': ['SELECT 1', 'SELECT 1', 'SELECT 1', 'SELECT 1', 'SELECT 1']}

exec(code, env_args)
