code = """import json, pandas as pd, os

attr_file = var_call_UhxUJncFC2GVd9cMLQRhdSY8
with open(attr_file, 'r') as f:
    attr_data = json.load(f)

attr_df = pd.DataFrame(attr_data)

# Filter businesses that offer BusinessParking or BikeParking

has_parking = []
for idx, row in attr_df.iterrows():
    attrs = row.get('attributes') or {}
    bike = attrs.get('BikeParking')
    bpark = attrs.get('BusinessParking')
    offers_bike = isinstance(bike, str) and bike.strip().strip("u").strip("'") == 'True'
    offers_bpark = isinstance(bpark, str) and 'True' in bpark
    if offers_bike or offers_bpark:
        has_parking.append(row['business_id'])

result = json.dumps({"count_parking_businesses_anytime": len(set(has_parking))})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_UhxUJncFC2GVd9cMLQRhdSY8': 'file_storage/call_UhxUJncFC2GVd9cMLQRhdSY8.json', 'var_call_qBxnNCjNPhbRYv3jGL36g6QG': []}

exec(code, env_args)
