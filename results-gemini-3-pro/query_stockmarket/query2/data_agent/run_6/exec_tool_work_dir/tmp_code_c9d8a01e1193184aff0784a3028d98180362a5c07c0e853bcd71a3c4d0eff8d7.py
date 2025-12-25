code = """import json
filename_tickers = locals()['var_function-call-2250333741242077047']
with open(filename_tickers, 'r') as f:
    tickers = json.load(f)

# Sort tickers to be deterministic
tickers.sort()

batch_size = 40
batch1 = tickers[0:batch_size]
template = '''SELECT '{0}' as Symbol FROM "{0}" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' AND "Adj Close" > 200 LIMIT 1'''
q1 = " UNION ALL ".join([template.format(t) for t in batch1])

print("__RESULT__:")
print(json.dumps(q1))"""

env_args = {'var_function-call-8523386402673308911': ['stockinfo'], 'var_function-call-10504201525486646859': 'file_storage/function-call-10504201525486646859.json', 'var_function-call-11124697286812708806': 'file_storage/function-call-11124697286812708806.json', 'var_function-call-2250333741242077047': 'file_storage/function-call-2250333741242077047.json', 'var_function-call-1568197735561327246': 1435, 'var_function-call-14814690868839741556': ['VTV', 'EWU', 'EIDO', 'GQRE', 'OVB'], 'var_function-call-8022747268740242488': "It's", 'var_function-call-12376444316175167874': 'file_storage/function-call-12376444316175167874.json', 'var_function-call-10093058432098843927': 'file_storage/function-call-10093058432098843927.json', 'var_function-call-13287104706038156252': 9923, 'var_function-call-14108628013096522551': [], 'var_function-call-13596377749751369097': [{'Date': '2015-07-20', 'Open': '212.75', 'High': '213.17999267578125', 'Low': '212.2100067138672', 'Close': '212.58999633789065', 'Adj Close': '193.3121490478516', 'Volume': '70446800'}], 'var_function-call-4436754506683821791': [{'Symbol': 'IVV', 'MaxPrice': '193.5270538330078'}, {'Symbol': 'SSO', 'MaxPrice': '66.95523071289062'}, {'Symbol': 'DIA', 'MaxPrice': '163.6190185546875'}]}

exec(code, env_args)
