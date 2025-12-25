code = """import json
q_mark = chr(34)
with open(locals()['var_function-call-2230327180537817995'], 'r') as f:
    syms = json.load(f)
syms.sort()
batch = syms[:150]
qs = []
for s in batch:
    query = "SELECT '{0}' as Symbol FROM {1}{0}{1} WHERE {1}Adj Close{1} > 200 AND Date LIKE '2015%' LIMIT 1".format(s, q_mark)
    qs.append(query)
full_q = " UNION ALL ".join(qs)
print('__RESULT__:')
print(json.dumps(full_q))"""

env_args = {'var_function-call-11011174398477336959': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-6298308308672748942': 'file_storage/function-call-6298308308672748942.json', 'var_function-call-7304166957241906547': 'file_storage/function-call-7304166957241906547.json', 'var_function-call-2230327180537817995': 'file_storage/function-call-2230327180537817995.json', 'var_function-call-13724006762451098890': 1435, 'var_function-call-1925036998085644226': [{'Date': '2018-08-15', 'Open': '11.84000015258789', 'High': '11.84000015258789', 'Low': '11.739999771118164', 'Close': '11.739999771118164', 'Adj Close': '11.739999771118164', 'Volume': '27300'}, {'Date': '2018-08-16', 'Open': '11.779999732971191', 'High': '11.800000190734863', 'Low': '11.739999771118164', 'Close': '11.739999771118164', 'Adj Close': '11.739999771118164', 'Volume': '428400'}, {'Date': '2018-08-17', 'Open': '11.800000190734863', 'High': '11.81999969482422', 'Low': '11.770000457763672', 'Close': '11.81999969482422', 'Adj Close': '11.81999969482422', 'Volume': '52400'}, {'Date': '2018-08-20', 'Open': '11.880000114440918', 'High': '11.90999984741211', 'Low': '11.850000381469728', 'Close': '11.899999618530272', 'Adj Close': '11.899999618530272', 'Volume': '28700'}, {'Date': '2018-08-21', 'Open': '11.920000076293944', 'High': '11.949999809265137', 'Low': '11.890000343322754', 'Close': '11.93000030517578', 'Adj Close': '11.93000030517578', 'Volume': '30600'}], 'var_function-call-12941464532178026217': ['var_function-call-11011174398477336959', 'var_function-call-6298308308672748942', 'var_function-call-7304166957241906547', 'var_function-call-2230327180537817995', 'var_function-call-13724006762451098890', 'var_function-call-1925036998085644226', '__builtins__', 'json']}

exec(code, env_args)
