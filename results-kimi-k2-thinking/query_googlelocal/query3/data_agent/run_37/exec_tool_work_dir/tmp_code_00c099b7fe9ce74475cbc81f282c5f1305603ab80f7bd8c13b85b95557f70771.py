code = """import json
import pandas as pd
import os

# Load data from stored files
biz_key = 'var_functions.query_db:6'
review_key = 'var_functions.query_db:8'

# Get the file paths
result_dir = locals()['var_functions.execute_python:18']
business_file = '/tmp/business_data.json'
review_file = '/tmp/review_data.json'

# Access the file paths from the stored variables
business_file_path = locals()[biz_key]
review_file_path = locals()[review_key]

# Load business data
print("Loading business data...")
with open(business_file_path, 'r') as f:
    business_data = json.load(f)

# Load review data
print("Loading review data...")
with open(review_file_path, 'r') as f:
    review_data = json.load(f)

print(f"Loaded {len(business_data)} businesses and {len(review_data)} reviews")

# Convert to DataFrames
df_business = pd.DataFrame(business_data)
df_reviews = pd.DataFrame(review_data)

print(f"Business columns: {df_business.columns.tolist()}")
print(f"Review columns: {df_reviews.columns.tolist()}")
print(f"Sample business data: {df_business.head(1)}")
print(f"Sample review data: {df_reviews.head(3)}")

# Save for next step
with open(business_file, 'w') as f:
    json.dump(business_data, f)
with open(review_file, 'w') as f:
    json.dump(review_data, f)

print("__RESULT__:")
print(json.dumps({"status": "loaded", "business_count": len(business_data), "review_count": len(review_data)}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}, {'name': 'Vons Chicken', 'gmap_id': 'gmap_74', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Black Tie Ski Rental Delivery of Mammoth', 'gmap_id': 'gmap_17', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Dunn-Edwards Paints', 'gmap_id': 'gmap_29', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'hours': 'None', 'state': 'None'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'status': 'success', 'business_count': 66, 'review_count': 2000}}

exec(code, env_args)
