code = """import json
print(json.dumps({
    "type_of_var": str(type(locals()['var_function-call-16282831282853032359'])),
    "repr_of_var": repr(locals()['var_function-call-16282831282853032359'])
}))"""

env_args = {'var_function-call-3776247780831150037': 'file_storage/function-call-3776247780831150037.json', 'var_function-call-5337988088047697233': [{'cpc_group': 'C04B', 'best_year': 2015, 'max_ema': 45.0}, {'cpc_group': 'F02M', 'best_year': 2014, 'max_ema': 10.0}, {'cpc_group': 'H01J', 'best_year': 2013, 'max_ema': 10.0}, {'cpc_group': 'G02B', 'best_year': 2018, 'max_ema': 8.0}, {'cpc_group': 'F02D', 'best_year': 2017, 'max_ema': 8.0}, {'cpc_group': 'F02N', 'best_year': 2013, 'max_ema': 7.0}, {'cpc_group': 'H01R', 'best_year': 2018, 'max_ema': 6.0}, {'cpc_group': 'H02J', 'best_year': 2009, 'max_ema': 6.0}, {'cpc_group': 'E02F', 'best_year': 2012, 'max_ema': 5.0}, {'cpc_group': 'G01L', 'best_year': 2017, 'max_ema': 4.0}], 'var_function-call-1135313935533368253': [], 'var_function-call-16282831282853032359': 'file_storage/function-call-16282831282853032359.json'}

exec(code, env_args)
