code = """import json
import pandas as pd

business_data = json.loads(open(locals()['var_function-call-12715573400421346162'], 'r').read())
df_business = pd.DataFrame(business_data)

la_businesses = df_business[df_business['description'].str.contains('Los Angeles, CA', na=False)]
la_gmap_ids = la_businesses['gmap_id'].tolist()

print('__RESULT__:')
print(json.dumps(la_gmap_ids))"""

env_args = {'var_function-call-12715573400421346162': 'file_storage/function-call-12715573400421346162.json'}

exec(code, env_args)
