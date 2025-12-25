code = """import pandas as pd
import json

# Load the business descriptions from the file
with open(locals()['var_function-call-3994384311218662169'], 'r') as f:
    business_descriptions = json.load(f)

df_business = pd.DataFrame(business_descriptions)

# Filter for businesses related to 'massage'
massage_businesses = df_business[
    df_business['description'].fillna('').str.contains('massage', case=False) |
    df_business['name'].fillna('').str.contains('massage', case=False)
]

# Get the gmap_ids of these massage businesses
massage_gmap_ids = massage_businesses['gmap_id'].tolist()

# Convert the list of gmap_ids to a JSON string for the next tool call
print('__RESULT__:')
print(json.dumps(massage_gmap_ids))"""

env_args = {'var_function-call-2705248405242993009': [], 'var_function-call-6260699461556202789': [], 'var_function-call-3994384311218662169': 'file_storage/function-call-3994384311218662169.json'}

exec(code, env_args)
