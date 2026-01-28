code = """import json
import pandas as pd
from datetime import datetime

# Read the full result from file
result_file = locals()['var_functions.query_db:2']
with open(result_file, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Print key statistics for debugging
print('__RESULT__:')
print(json.dumps({
    'total_records': len(df),
    'columns': df.columns.tolist(),
    'sample_data': df.head().to_dict('records'),
    'sample_dates': df[['CompanySignedDate', 'CreatedDate']].head().to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
