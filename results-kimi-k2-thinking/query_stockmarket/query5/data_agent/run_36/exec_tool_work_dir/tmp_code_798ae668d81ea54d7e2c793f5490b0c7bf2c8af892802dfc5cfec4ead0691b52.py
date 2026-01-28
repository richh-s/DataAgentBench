code = """import json

# Check what variables are available
available_vars = [var for var in locals().keys() if var.startswith('var_')]
print(f"Available variables: {available_vars}")

# Direct access to the variables
nasdaq_capital_stocks = var_functions.query_db_0
all_tables = var_functions.list_db_2

print(f"Type of nasdaq_capital_stocks: {type(nasdaq_capital_stocks)}")
print(f"Type of all_tables: {type(all_tables)}")
print(f"First item in nasdaq_capital_stocks: {nasdaq_capital_stocks[0] if nasdaq_capital_stocks else 'Empty'}")
print(f"Length of all_tables: {len(all_tables) if all_tables else 'Empty'}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
