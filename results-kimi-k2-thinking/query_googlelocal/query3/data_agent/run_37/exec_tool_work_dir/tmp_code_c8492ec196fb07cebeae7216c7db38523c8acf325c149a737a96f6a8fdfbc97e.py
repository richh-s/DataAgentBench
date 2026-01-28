code = """import json
import pandas as pd

# Get file paths
business_file = locals()['var_functions.query_db:30']
review_file = locals()['var_functions.query_db:44']

# Load data
with open(business_file, 'r') as f:
    business_data = json.load(f)

with open(review_file, 'r') as f:
    review_data = json.load(f)

# Convert to DataFrames
df_business = pd.DataFrame(business_data)
df_reviews = pd.DataFrame(review_data)

# Convert rating to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

# Calculate average ratings
df_avg_rating = df_reviews.groupby('gmap_id')['rating'].agg(['mean', 'count']).reset_index()
df_avg_rating.columns = ['gmap_id', 'avg_rating', 'review_count']
df_avg_rating = df_avg_rating[df_avg_rating['review_count'] >= 5]

# Check for businesses open after 6PM on weekdays
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def check_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        hours_list = eval(hours_str)
        for day, time_range in hours_list:
            if day in weekdays:
                if time_range == 'Open 24 hours':
                    return True
                if time_range == 'Closed':
                    continue
                
                parts = time_range.replace('\u2013', '-').split('-')
                if len(parts) == 2:
                    end_time = parts[1].strip()
                    if 'PM' in end_time:
                        hour_str = end_time.replace('PM', '').strip()
                        hour = int(hour_str.split(':')[0])
                        if hour != 12:
                            hour += 12
                        if hour > 18:
                            return True
                    elif 'AM' in end_time:
                        hour_str = end_time.replace('AM', '').strip()
                        hour = int(hour_str.split(':')[0])
                        if hour < 6:
                            return True
        return False
    except:
        return False

df_business['open_after_6pm'] = df_business['hours'].apply(check_open_after_6pm)
df_filtered = df_business[df_business['open_after_6pm'] == True]

# Merge and get top 5
df_result = df_filtered.merge(df_avg_rating, on='gmap_id', how='inner')
df_top5 = df_result.sort_values('avg_rating', ascending=False).head(5)

# Prepare result
final_result = []
for _, row in df_top5.iterrows():
    final_result.append({
        'name': str(row['name']),
        'operating_hours': str(row['hours']),
        'average_rating': round(float(row['avg_rating']), 2),
        'review_count': int(row['review_count'])
    })

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}, {'name': 'Vons Chicken', 'gmap_id': 'gmap_74', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Black Tie Ski Rental Delivery of Mammoth', 'gmap_id': 'gmap_17', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Dunn-Edwards Paints', 'gmap_id': 'gmap_29', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'hours': 'None', 'state': 'None'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'status': 'success', 'business_count': 66, 'review_count': 2000}, 'var_functions.execute_python:20': {'status': 'loaded', 'business_count': 66, 'review_count': 2000}, 'var_functions.execute_python:22': {'status': 'success', 'business_count': 66, 'review_count': 2000}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}, {'gmap_id': 'gmap_44', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
