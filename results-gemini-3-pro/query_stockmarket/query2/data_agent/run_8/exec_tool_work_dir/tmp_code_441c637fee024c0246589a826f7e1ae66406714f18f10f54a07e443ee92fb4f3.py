code = """import os
import glob

print("Files in current dir:", os.listdir('.'))
try:
    import duckdb
    print("DuckDB imported successfully")
except ImportError:
    print("DuckDB not installed")"""

env_args = {'var_function-call-14532322368764427460': 'file_storage/function-call-14532322368764427460.json', 'var_function-call-8803107773511705717': 'file_storage/function-call-8803107773511705717.json', 'var_function-call-6325032711824725866': 'file_storage/function-call-6325032711824725866.json', 'var_function-call-16713880611030902886': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'var_function-call-16160768990026222278': 'file_storage/function-call-16160768990026222278.json', 'var_function-call-1491270065845566597': 1435, 'var_function-call-17396258014626583881': 'file_storage/function-call-17396258014626583881.json'}

exec(code, env_args)
