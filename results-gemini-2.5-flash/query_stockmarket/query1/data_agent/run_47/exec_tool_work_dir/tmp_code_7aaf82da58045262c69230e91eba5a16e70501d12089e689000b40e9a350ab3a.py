code = """print('__RESULT__:')
print(locals()['var_function-call-14991602465526530101'][0]['max("Adj Close")'])"""

env_args = {'var_function-call-16725170421010284692': [{'Symbol': 'REAL'}], 'var_function-call-14991602465526530101': [{'max("Adj Close")': '18.440000534057617'}]}

exec(code, env_args)
