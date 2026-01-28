code = """import json
import pandas as pd
from datetime import datetime

# Read the full result from file
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Print key statistics
print('Total records:', len(df))
print('Columns:', df.columns.tolist())
print('First few rows:', df.head())
print('Sample dates:', df[['CompanySignedDate', 'CreatedDate']].head())"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
