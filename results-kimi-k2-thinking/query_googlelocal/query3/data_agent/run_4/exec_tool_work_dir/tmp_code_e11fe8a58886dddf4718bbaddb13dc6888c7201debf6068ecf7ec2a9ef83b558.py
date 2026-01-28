code = """import json
import re
from datetime import datetime
import pandas as pd

# Load business data
business_file = locals()['var_functions.query_db:10']
with open(business_file, 'r') as f:
    businesses = json.load(f)

# Load review data  
review_file = locals()['var_functions.query_db:16']
with open(review_file, 'r') as f:
    reviews = json.load(f)

# Calculate average rating per business
rating_df = pd.DataFrame(reviews)
rating_df['rating'] = pd.to_numeric(rating_df['rating'])
avg_ratings = rating_df.groupby('gmap_id')['rating'].agg(['mean', 'count']).reset_index()
avg_ratings.columns = ['gmap_id', 'avg_rating', 'review_count']

print(f"Average ratings calculated for {len(avg_ratings)} businesses")
print(f"Rating range: {avg_ratings['avg_rating'].min():.2f} to {avg_ratings['avg_rating'].max():.2f}")

print("__RESULT__:")
print(json.dumps({"avg_rating_businesses": len(avg_ratings), "rating_min": avg_ratings['avg_rating'].min(), "rating_max": avg_ratings['avg_rating'].max()}))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'state': 'Open now'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.query_db:6': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'business_count': 66, 'review_count': 5}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'businesses': 66, 'reviews': 2000}, 'var_functions.execute_python:26': {'status': 'data_loaded'}}

exec(code, env_args)
