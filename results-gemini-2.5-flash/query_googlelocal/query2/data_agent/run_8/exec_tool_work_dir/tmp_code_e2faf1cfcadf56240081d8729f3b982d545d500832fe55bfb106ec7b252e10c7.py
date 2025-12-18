code = """import json
import pandas as pd

# Load the business data from the JSON file
with open(locals()['var_function-call-14314757006796023637'], 'r') as f:
    business_data = json.load(f)

df_business = pd.DataFrame(business_data)

# Filter for massage therapy businesses based on keywords in the description
keywords = ['massage', 'bodywork', 'relaxation', 'spa', 'therapy']

def contains_keyword(description, keywords):
    if description is None:
        return False
    return any(keyword in description.lower() for keyword in keywords)

massage_businesses = df_business[df_business['description'].apply(lambda x: contains_keyword(x, keywords))]

# Prepare gmap_ids for the next query
massage_gmap_ids = massage_businesses['gmap_id'].tolist()

print('__RESULT__:')
print(json.dumps(massage_gmap_ids))"""

env_args = {'var_function-call-6067984615539136177': ['business_description'], 'var_function-call-7919125553463431119': [], 'var_function-call-14038103750081746633': ['review'], 'var_function-call-14314757006796023637': 'file_storage/function-call-14314757006796023637.json'}

exec(code, env_args)
