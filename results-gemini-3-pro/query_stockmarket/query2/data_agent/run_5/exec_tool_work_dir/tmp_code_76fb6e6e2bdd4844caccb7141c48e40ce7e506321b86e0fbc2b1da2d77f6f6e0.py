code = """try:
    import duckdb
    print("__RESULT__:")
    print("true")
except ImportError:
    print("__RESULT__:")
    print("false")"""

env_args = {'var_function-call-16341739704993987166': 'file_storage/function-call-16341739704993987166.json', 'var_function-call-17860090179265240781': 'file_storage/function-call-17860090179265240781.json', 'var_function-call-11973061372010644575': 'file_storage/function-call-11973061372010644575.json', 'var_function-call-16861433214838265826': 1435, 'var_function-call-2000411894810468263': 'test', 'var_function-call-12527035195204984051': 1435, 'var_function-call-1928971542841167320': 'file_storage/function-call-1928971542841167320.json'}

exec(code, env_args)
