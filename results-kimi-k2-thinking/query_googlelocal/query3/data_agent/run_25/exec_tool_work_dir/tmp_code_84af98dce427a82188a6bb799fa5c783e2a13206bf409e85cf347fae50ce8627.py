code = """import json
import pandas as pd
import re

# Read the business data from file
with open('/tmp/20250320-091853-json-gbjq.json', 'r') as f:
    business_data = json.load(f)

# Read the review data from file
with open('/tmp/20250320-091920-json-5y9y.json', 'r') as f:
    review_data = json.load(f)

# Create DataFrames
df_business = pd.DataFrame(business_data)
df_reviews = pd.DataFrame(review_data)

# Convert rating to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

# Calculate average rating per business
avg_ratings = df_reviews.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.columns = ['gmap_id', 'average_rating']

# Merge business with average ratings
df_merged = df_business.merge(avg_ratings, on='gmap_id', how='inner')

# Function to check if open after 6 PM
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def open_after_six(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    hours_str_clean = hours_str.replace('\\u2013', '-')
    
    try:
        hours_list = eval(hours_str_clean)
        for day, hours in hours_list:
            if day in weekdays and hours != 'Closed':
                if 'Open 24 hours' in str(hours):
                    return True
                
                parts = str(hours).split('-')
                if len(parts) > 1:
                    closing = parts[1].strip()
                    closing_upper = closing.upper()
                    if 'PM' in closing_upper:
                        hour_num = re.findall(r'\d+', closing_upper)
                        if hour_num:
                            hour_val = int(hour_num[0])
                            if hour_val >= 6 and hour_val != 12:
                                return True
                            elif closing_upper.startswith('12') and 'PM' in closing_upper:
                                return True
        return False
    except:
        return False

# Apply function
df_merged['open_after_6pm'] = df_merged['hours'].apply(open_after_six)
open_businesses = df_merged[df_merged['open_after_6pm'] == True]

# Get top 5
top_5 = open_businesses.nlargest(5, 'average_rating')

result = []
for _, row in top_5.iterrows():
    result.append({
        'name': row['name'],
        'operating_hours': row['hours'],
        'average_rating': round(row['average_rating'], 2)
    })


print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'state': 'Open now'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.query_db:8': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken'}, {'gmap_id': 'gmap_17', 'name': 'Black Tie Ski Rental Delivery of Mammoth'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_29', 'name': 'Dunn-Edwards Paints'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_19', 'name': 'PODS Sacramento Hub'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_32', 'name': 'J B Oriental Inc'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_48', 'name': 'State Street/7th Street'}, {'gmap_id': 'gmap_50', 'name': 'HDR'}, {'gmap_id': 'gmap_18', 'name': 'Porvene Doors'}, {'gmap_id': 'gmap_16', 'name': 'Hanford Auto Supply'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
