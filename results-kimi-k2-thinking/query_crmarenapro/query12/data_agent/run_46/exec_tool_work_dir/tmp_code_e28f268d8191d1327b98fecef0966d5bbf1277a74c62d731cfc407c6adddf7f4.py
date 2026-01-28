code = """# Load the list of tables for reference
tables = var_functions.list_db:0
print('__RESULT__:')
print(str(tables))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem']}

exec(code, env_args)
