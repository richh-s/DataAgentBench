code = """clinical_data_file = var_functions.query_db:5
print('__RESULT__:')
print(clinical_data_file)"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
