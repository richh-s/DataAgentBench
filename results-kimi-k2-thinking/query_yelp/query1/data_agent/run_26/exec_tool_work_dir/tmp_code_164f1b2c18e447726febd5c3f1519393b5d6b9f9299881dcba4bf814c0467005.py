code = """import json
import pandas as pd

# Access the file path from the previous query result
file_path = locals()['var_functions.query_db:4']

# Read the full results from the file
with open(file_path, 'r') as f:
    businesses = json.load(f)

# Convert to DataFrame for easier processing
df = pd.DataFrame(businesses)

# Filter businesses in Indianapolis, IN
# Look for "Indianapolis, IN" in the description
indianapolis_businesses = df[df['description'].str.contains('Indianapolis, IN', case=False, na=False)]

# Extract the business IDs and convert to business_ref format (businessid_X -> businessref_X)
indianapolis_business_ids = indianapolis_businesses['business_id'].tolist()
indianapolis_business_refs = [bid.replace('businessid_', 'businessref_') for bid in indianapolis_business_ids]

result = {
    'business_ids': indianapolis_business_ids,
    'business_refs': indianapolis_business_refs,
    'count': len(indianapolis_business_ids)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
