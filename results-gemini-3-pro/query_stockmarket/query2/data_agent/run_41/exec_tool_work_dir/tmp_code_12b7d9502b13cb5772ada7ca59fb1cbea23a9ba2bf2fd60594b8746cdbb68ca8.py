code = """import os
try:
    import duckdb
    print("DuckDB is installed")
except ImportError:
    print("DuckDB is NOT installed")

print("Files in current dir:", os.listdir('.'))"""

env_args = {'var_function-call-14195711220532126717': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-13030058367102200413': 'file_storage/function-call-13030058367102200413.json', 'var_function-call-151626240589154895': 'file_storage/function-call-151626240589154895.json', 'var_function-call-4241544829162874194': 'file_storage/function-call-4241544829162874194.json', 'var_function-call-10903685240376781787': 1435, 'var_function-call-4787797297192363939': 'file_storage/function-call-4787797297192363939.json'}

exec(code, env_args)
