code = """import json

sym = "ABC"
dq = chr(34)
sq = chr(39)
q = "SELECT {}{}{} AS Symbol FROM {}{}{} WHERE {}Adj Close{} > 200".format(sq, sym, sq, dq, sym, dq, dq, dq)

print(q)
print("__RESULT__:")
print(json.dumps([q]))"""

env_args = {'var_function-call-16817766424675427763': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-12499338069894364565': 'file_storage/function-call-12499338069894364565.json', 'var_function-call-9293888739121941435': 'file_storage/function-call-9293888739121941435.json', 'var_function-call-14915668202036031869': 'file_storage/function-call-14915668202036031869.json', 'var_function-call-7434327097366713516': 'file_storage/function-call-7434327097366713516.json', 'var_function-call-2380757378116549886': [{'Date': '2018-08-15'}], 'var_function-call-7107660430946483903': 1435, 'var_function-call-3063757488003502576': 'Hello', 'var_function-call-16536889929438009237': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'var_function-call-18131283317376313178': ['SELECT 1', 'SELECT 1', 'SELECT 1', 'SELECT 1', 'SELECT 1']}

exec(code, env_args)
