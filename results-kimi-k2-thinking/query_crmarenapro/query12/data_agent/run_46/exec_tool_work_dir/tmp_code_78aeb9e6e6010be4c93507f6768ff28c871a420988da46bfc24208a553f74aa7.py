code = """import json
import pandas as pd
from datetime import datetime

# Access the storage variable containing the file path
file_path_key = 'var_functions.query_db:5'
file_path = locals().get(file_path_key)

# Load the data from JSON file
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Show data info
print('__RESULT__:')
print(f"Data loaded: {len(df)} records, {len(df.columns)} columns")
print(df.head().to_json(orient='records', date_format='iso'))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
