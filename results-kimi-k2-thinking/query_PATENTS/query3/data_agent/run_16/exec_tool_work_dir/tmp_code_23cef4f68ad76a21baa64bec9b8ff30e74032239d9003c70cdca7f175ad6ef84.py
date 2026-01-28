code = """import os
import glob
print('Current directory files:')
for f in glob.glob('/tmp/*'):
    print(f)

print('\\nPython variables available:')
for var in sorted(globals().keys()):
    if not var.startswith('__'):
        print(var)

print('\\nLocal variables:')
for var in sorted(locals().keys()):
    if not var.startswith('__'):
        print(var)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
