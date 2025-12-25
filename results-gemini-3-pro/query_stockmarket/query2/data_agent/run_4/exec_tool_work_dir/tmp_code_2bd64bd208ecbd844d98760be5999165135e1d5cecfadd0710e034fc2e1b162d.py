code = """import json

path = locals()['var_function-call-216321779407504316']
with open(path, 'r') as f:
    queries = json.load(f)

full_query = " UNION ALL ".join(queries)

print('__RESULT__:')
print(json.dumps(full_query))"""

env_args = {'var_function-call-5039856018528113346': 'file_storage/function-call-5039856018528113346.json', 'var_function-call-11443630550213120568': 'file_storage/function-call-11443630550213120568.json', 'var_function-call-15756276779905780223': 'file_storage/function-call-15756276779905780223.json', 'var_function-call-3698771901142726474': [{'Date': '2018-08-15', 'Open': '11.84000015258789', 'High': '11.84000015258789', 'Low': '11.739999771118164', 'Close': '11.739999771118164', 'Adj Close': '11.739999771118164', 'Volume': '27300'}, {'Date': '2018-08-16', 'Open': '11.779999732971191', 'High': '11.800000190734863', 'Low': '11.739999771118164', 'Close': '11.739999771118164', 'Adj Close': '11.739999771118164', 'Volume': '428400'}, {'Date': '2018-08-17', 'Open': '11.800000190734863', 'High': '11.81999969482422', 'Low': '11.770000457763672', 'Close': '11.81999969482422', 'Adj Close': '11.81999969482422', 'Volume': '52400'}, {'Date': '2018-08-20', 'Open': '11.880000114440918', 'High': '11.90999984741211', 'Low': '11.850000381469728', 'Close': '11.899999618530272', 'Adj Close': '11.899999618530272', 'Volume': '28700'}, {'Date': '2018-08-21', 'Open': '11.920000076293944', 'High': '11.949999809265137', 'Low': '11.890000343322754', 'Close': '11.93000030517578', 'Adj Close': '11.93000030517578', 'Volume': '30600'}], 'var_function-call-4723295563071041683': 1435, 'var_function-call-7235647545791382413': 'file_storage/function-call-7235647545791382413.json', 'var_function-call-216321779407504316': 'file_storage/function-call-216321779407504316.json'}

exec(code, env_args)
