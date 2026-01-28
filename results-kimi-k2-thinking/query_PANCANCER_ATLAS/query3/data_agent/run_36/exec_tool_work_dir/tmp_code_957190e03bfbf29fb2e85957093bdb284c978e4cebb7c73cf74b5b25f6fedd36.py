code = """import json
# First, let's get the available columns in the clinical_info table
query = """
SELECT column_name 
FROM information_schema.columns 
WHERE table_name = 'clinical_info' 
ORDER BY ordinal_position;
"""
print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression']}

exec(code, env_args)
