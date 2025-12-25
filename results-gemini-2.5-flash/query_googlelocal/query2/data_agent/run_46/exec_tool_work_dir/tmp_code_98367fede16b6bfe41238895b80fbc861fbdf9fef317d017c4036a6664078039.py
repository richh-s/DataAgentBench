code = """import pandas as pd

business_names = locals()['var_function-call-374750667616518621']
business_df = pd.DataFrame(business_names)
gmap_ids = business_df['gmap_id'].tolist()

# Construct a comma-separated string of gmap_ids for the SQL IN clause
gmap_ids_str = ', '.join(f"'{gmap_id}'" for gmap_id in gmap_ids)

print('__RESULT__:')
print(gmap_ids_str)"""

env_args = {'var_function-call-16730726033356625513': [], 'var_function-call-3138104655230594539': [], 'var_function-call-374750667616518621': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}]}

exec(code, env_args)
