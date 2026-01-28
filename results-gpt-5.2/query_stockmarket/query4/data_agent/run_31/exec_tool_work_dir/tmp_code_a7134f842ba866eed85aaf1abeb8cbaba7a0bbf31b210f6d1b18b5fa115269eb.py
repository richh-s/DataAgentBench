code = """import json
import pandas as pd

nyse = var_call_OnB6fCK9Z9sc0oRJT1v3w7fS
if isinstance(nyse, str):
    with open(nyse, 'r') as f:
        nyse = json.load(f)
nyse_df = pd.DataFrame(nyse)

# Keep symbols that are tables in trade DB
tables = var_call_MW2L0mKITaFAwthgkJuiG1GZ
if isinstance(tables, str):
    with open(tables, 'r') as f:
        tables = json.load(f)
tables_set = set(tables)

nyse_df = nyse_df[nyse_df['Symbol'].astype(str).isin(tables_set)].copy()

# Determine which symbols actually have data in 2017 by probing min/max date for each symbol is too expensive.
# We'll instead select symbols known to have long histories by filtering out symbols whose tables start after 2017 based on a small heuristic: table exists and has > 3000 rows.
# We can't query row counts for all here in python; prepare a sample of first 200 symbols for querying counts+date range in parallel later.
syms = nyse_df['Symbol'].astype(str).tolist()

out = {
    'n_nyse_nonetf_with_table': len(syms),
    'symbols_first_200': syms[:200]
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_KX5UnkAb3MmDwt33HLN1ZTMv': ['stockinfo'], 'var_call_OnB6fCK9Z9sc0oRJT1v3w7fS': 'file_storage/call_OnB6fCK9Z9sc0oRJT1v3w7fS.json', 'var_call_MW2L0mKITaFAwthgkJuiG1GZ': 'file_storage/call_MW2L0mKITaFAwthgkJuiG1GZ.json', 'var_call_QNUieHkFgdGOcvBQKw3zkWZ5': [{'Symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_xfxgMp1dHq9vTQ3j9T4Tz4Vh': [{'n': '0', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_zJalEMWRBTGpxtLnWzfRh3US': [{'min_date': '2019-10-24', 'max_date': '2020-04-01', 'n': '110'}], 'var_call_PgasBnre9KCGvZLGEHKYsqcN': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS'], 'var_call_791IFmIwLkeNYw5lnXP6G9ct': [{'Symbol': 'AIN', 'min_date': '1987-09-30', 'max_date': '2020-04-01', 'n': '8192'}], 'var_call_WILST3EJZpFGq40nbzt6vIUJ': [{'Symbol': 'AIV', 'min_date': '1994-07-22', 'max_date': '2020-04-01', 'n': '6470'}], 'var_call_CaI09hrFkvMHnvJbVeJCs7Wk': [{'Symbol': 'AMP', 'min_date': '2005-09-15', 'max_date': '2020-04-01', 'n': '3661'}], 'var_call_8LkKTix4LlKR55fdaSmbONyF': [{'Symbol': 'AMT', 'min_date': '1998-02-27', 'max_date': '2020-04-01', 'n': '5560'}], 'var_call_i8e7q67A0JtLwNupMq9Lj4iE': [{'Symbol': 'CMI', 'min_date': '1973-02-21', 'max_date': '2020-04-01', 'n': '11885'}], 'var_call_TaZhoQgxdrsoQjoIoHyMIdRT': [{'Symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_P9vP7AG30ouvrygSd0gKzb95': [{'Symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}], 'var_call_2J5Z7SymGRlcOUj0eWyqHfZ2': [{'Symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}], 'var_call_umG8vblZDeyTF92KBqGz8kr6': [{'Symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_sZV1QGGsndMUXsOjVfCLGCM5': [{'Symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}]}

exec(code, env_args)
