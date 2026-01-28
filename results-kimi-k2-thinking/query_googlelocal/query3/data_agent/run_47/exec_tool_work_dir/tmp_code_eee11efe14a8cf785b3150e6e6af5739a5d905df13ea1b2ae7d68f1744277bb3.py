code = """import json
import pandas as pd

# Load hours data
hours_var = 'var_functions.query_db:4'
hours_path = locals().get(hours_var)

hours_data = []
if hours_path and isinstance(hours_path, str) and hours_path.endswith('.json'):
    with open(hours_path, 'r') as f:
        hours_data = json.load(f)
elif hours_path and isinstance(hours_path, list):
    hours_data = hours_path

# Load review data
reviews_var = 'var_functions.query_db:22'
reviews_path = locals().get(reviews_var)

reviews = []
if reviews_path and isinstance(reviews_path, str) and reviews_path.endswith('.json'):
    with open(reviews_path, 'r') as f:
        reviews = json.load(f)
elif reviews_path and isinstance(reviews_path, list):
    reviews = reviews_path

print(f"Loaded {len(hours_data)} businesses and {len(reviews)} reviews")

# Function to check if truly open AFTER 6PM on weekdays
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # Parse the string representation of a list
        hours_list = eval(hours_str)
        
        for day, hours in hours_list:
            if day in weekdays and hours != 'Closed':
                # Check 24 hours
                if hours == 'Open 24 hours':
                    return True
                
                # Parse closing time (handle both en dash and regular dash)
                if '–' in hours:
                    parts = hours.split('–')
                elif '-' in hours:
                    parts = hours.split('-')
                else:
                    continue
                
                if len(parts) >= 2:
                    close_time = parts[1].strip()
                    if 'PM' in close_time:
                        # Extract hour
                        hour_part = close_time.replace('PM', '').replace(' ', '')
                        if ':' in hour_part:
                            hour = int(hour_part.split(':')[0])
                        else:
                            hour = int(hour_part)
                        
                        # Convert to 24-hour format
                        if hour != 12:
                            hour += 12
                        
                        # Must be AFTER 6PM (hour > 18)
                        if hour > 18:
                            return True
    except Exception as e:
        return False
    return False

# Filter businesses with valid hours
valid_businesses = []
for business in hours_data:
    if open_after_6pm(business['hours']):
        valid_businesses.append({
            'gmap_id': business['gmap_id'],
            'name': business['name'],
            'hours': business['hours']
        })

print(f"Found {len(valid_businesses)} businesses open after 6PM excluding exactly 6PM")

# Calculate average ratings per business
if reviews:
    reviews_df = pd.DataFrame(reviews)
    reviews_df['rating'] = pd.to_numeric(reviews_df['rating'])
    
    avg_ratings = reviews_df.groupby('gmap_id')['rating'].agg(['mean', 'count']).reset_index()
    avg_ratings.columns = ['gmap_id', 'avg_rating', 'review_count']
else:
    avg_ratings = pd.DataFrame(columns=['gmap_id', 'avg_rating', 'review_count'])

# Merge businesses with ratings
businesses_df = pd.DataFrame(valid_businesses)
df_merged = pd.merge(businesses_df, avg_ratings, on='gmap_id', how='left')

# Remove businesses with no ratings
df_merged = df_merged.dropna(subset=['avg_rating'])

# Sort by average rating (desc) and get top 5
df_top5 = df_merged.sort_values('avg_rating', ascending=False).head(10)  # Get top 10 first to filter

print(f"Top 5 by rating (including ties):")
for idx, row in df_top5.iterrows():
    print(f"  {row['name']}: {row['avg_rating']:.2f} stars ({row['review_count']} reviews)")

# Format final result
result = []
for idx, row in df_top5.iterrows():
    result.append({
        'name': str(row['name']),
        'hours': str(row['hours']),
        'avg_rating': round(float(row['avg_rating']), 2),
        'review_count': int(row['review_count'])
    })
    if len(result) >= 5:
        break

final_result = {'top_5_businesses': result}
print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:20': {'businesses': [{'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'hours': '[["Thursday", "9AM–10PM"], ["Friday", "9AM–10PM"], ["Saturday", "9AM–10PM"], ["Sunday", "9AM–10PM"], ["Monday", "9AM–10PM"], ["Tuesday", "9AM–10PM"], ["Wednesday", "9AM–10PM"]]'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_32', 'name': 'J B Oriental Inc', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'hours': '[["Thursday", "10AM–8PM"], ["Friday", "10AM–8PM"], ["Saturday", "10AM–8PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–8PM"], ["Tuesday", "10AM–8PM"], ["Wednesday", "10AM–8PM"]]'}, {'gmap_id': 'gmap_16', 'name': 'Hanford Auto Supply', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "9AM–5PM"], ["Sunday", "Closed"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_30', 'name': 'The Beauty Bar', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "9AM–8PM"], ["Sunday", "Closed"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots', 'hours': '[["Thursday", "3–8PM"], ["Friday", "3–9PM"], ["Saturday", "12–9PM"], ["Sunday", "12–8PM"], ["Monday", "Closed"], ["Tuesday", "3–8PM"], ["Wednesday", "3–8PM"]]'}, {'gmap_id': 'gmap_63', 'name': 'Regus - California, Irvine - Oracle Tower', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "Open 24 hours"], ["Saturday", "Open 24 hours"], ["Sunday", "Open 24 hours"], ["Monday", "Open 24 hours"], ["Tuesday", "Open 24 hours"], ["Wednesday", "Open 24 hours"]]'}, {'gmap_id': 'gmap_65', 'name': 'Excel Hair & Nails', 'hours': '[["Thursday", "9AM–7PM"], ["Friday", "9AM–7PM"], ["Saturday", "9AM–7PM"], ["Sunday", "10AM–5PM"], ["Monday", "9AM–7PM"], ["Tuesday", "9AM–7PM"], ["Wednesday", "9AM–7PM"]]'}, {'gmap_id': 'gmap_51', 'name': 'Taba Rug Gallery', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]'}, {'gmap_id': 'gmap_36', 'name': 'Beauty Divine Artistry', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]'}, {'gmap_id': 'gmap_12', 'name': 'White Barn Candle Co', 'hours': '[["Thursday", "10AM–9PM"], ["Friday", "10AM–9PM"], ["Saturday", "10AM–9PM"], ["Sunday", "11AM–7PM"], ["Monday", "10AM–9PM"], ["Tuesday", "10AM–9PM"], ["Wednesday", "10AM–9PM"]]'}, {'gmap_id': 'gmap_7', 'name': "Rossy's Beauty Salon", 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "9AM–6PM"], ["Sunday", "9AM–3PM"], ["Monday", "Closed"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]'}, {'gmap_id': 'gmap_8', 'name': 'TACOS LA CABANA', 'hours': '[["Thursday", "Closed"], ["Friday", "5–11PM"], ["Saturday", "5–11PM"], ["Sunday", "5–11PM"], ["Monday", "5–11PM"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]'}, {'gmap_id': 'gmap_9', 'name': 'Mariscos el poblano', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "8AM–3:30PM"], ["Saturday", "8AM–3:30PM"], ["Sunday", "8AM–3:30PM"], ["Monday", "9AM–3:30AM"], ["Tuesday", "8AM–3:30PM"], ["Wednesday", "8AM–3:30PM"]]'}, {'gmap_id': 'gmap_5', 'name': 'Dr. Syverain Skincare Clinic', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "Closed"], ["Sunday", "8AM–1PM"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]'}, {'gmap_id': 'gmap_34', 'name': "Ruby's Boutique", 'hours': '[["Thursday", "10AM–6PM"], ["Friday", "10AM–6PM"], ["Saturday", "10AM–5PM"], ["Sunday", "11AM–4PM"], ["Monday", "10AM–6PM"], ["Tuesday", "10AM–6PM"], ["Wednesday", "10AM–6PM"]]'}, {'gmap_id': 'gmap_11', 'name': 'Paradise tattoo', 'hours': '[["Thursday", "12–10PM"], ["Friday", "12PM–12AM"], ["Saturday", "12PM–12AM"], ["Sunday", "12–10PM"], ["Monday", "12–10PM"], ["Tuesday", "12–10PM"], ["Wednesday", "12–10PM"]]'}, {'gmap_id': 'gmap_61', 'name': 'Off The Hoof', 'hours': '[["Thursday", "11AM–10PM"], ["Friday", "11AM–10PM"], ["Saturday", "11AM–10PM"], ["Sunday", "11AM–9PM"], ["Monday", "11AM–9PM"], ["Tuesday", "11AM–9PM"], ["Wednesday", "11AM–9PM"]]'}, {'gmap_id': 'gmap_47', 'name': 'Laptop Masters', 'hours': '[["Thursday", "10AM–6PM"], ["Friday", "10AM–6PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "10AM–6PM"], ["Tuesday", "10AM–6PM"], ["Wednesday", "10AM–6PM"]]'}, {'gmap_id': 'gmap_55', 'name': 'Mobile Moreno Valley Dispensary', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "Open 24 hours"], ["Saturday", "Open 24 hours"], ["Sunday", "Open 24 hours"], ["Monday", "Open 24 hours"], ["Tuesday", "Open 24 hours"], ["Wednesday", "Open 24 hours"]]'}, {'gmap_id': 'gmap_68', 'name': 'Advanced Auto Upholstery', 'hours': '[["Thursday", "8AM–7PM"], ["Friday", "8AM–7PM"], ["Saturday", "8AM–5PM"], ["Sunday", "Closed"], ["Monday", "8AM–7PM"], ["Tuesday", "8AM–7PM"], ["Wednesday", "8AM–7PM"]]'}, {'gmap_id': 'gmap_67', 'name': 'LuXe Organic Nails Boutique', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "9AM–6PM"], ["Sunday", "10AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "Closed"], ["Wednesday", "10AM–7PM"]]'}, {'gmap_id': 'gmap_64', 'name': 'St John Knits International Inc', 'hours': '[["Thursday", "10AM–6PM"], ["Friday", "10AM–6PM"], ["Saturday", "10AM–6PM"], ["Sunday", "12:30–6PM"], ["Monday", "10AM–6PM"], ["Tuesday", "10AM–6PM"], ["Wednesday", "10AM–6PM"]]'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'hours': '[["Thursday", "11AM–8PM"], ["Friday", "11AM–7PM"], ["Saturday", "10AM–6PM"], ["Sunday", "10AM–2PM"], ["Monday", "Closed"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]'}, {'gmap_id': 'gmap_60', 'name': 'The Dream Junction', 'hours': '[["Thursday", "9AM–7PM"], ["Friday", "9AM–7PM"], ["Saturday", "9AM–7PM"], ["Sunday", "9AM–7PM"], ["Monday", "9AM–7PM"], ["Tuesday", "9AM–7PM"], ["Wednesday", "9AM–7PM"]]'}], 'gmap_ids': ['gmap_41', 'gmap_74', 'gmap_22', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_32', 'gmap_21', 'gmap_16', 'gmap_28', 'gmap_30', 'gmap_53', 'gmap_63', 'gmap_65', 'gmap_51', 'gmap_36', 'gmap_12', 'gmap_7', 'gmap_8', 'gmap_9', 'gmap_5', 'gmap_34', 'gmap_11', 'gmap_61', 'gmap_47', 'gmap_55', 'gmap_68', 'gmap_67', 'gmap_64', 'gmap_40', 'gmap_60'], 'count': 31}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'top_5_businesses': [{'name': 'Hanford Auto Supply', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "9AM–5PM"], ["Sunday", "Closed"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]', 'avg_rating': 5.0, 'review_count': 6}, {'name': 'Taba Rug Gallery', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'avg_rating': 5.0, 'review_count': 18}, {'name': 'Dr. Syverain Skincare Clinic', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "Closed"], ["Sunday", "8AM–1PM"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]', 'avg_rating': 5.0, 'review_count': 5}, {'name': 'Mariscos el poblano', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "8AM–3:30PM"], ["Saturday", "8AM–3:30PM"], ["Sunday", "8AM–3:30PM"], ["Monday", "9AM–3:30AM"], ["Tuesday", "8AM–3:30PM"], ["Wednesday", "8AM–3:30PM"]]', 'avg_rating': 5.0, 'review_count': 3}, {'name': 'TACOS LA CABANA', 'hours': '[["Thursday", "Closed"], ["Friday", "5–11PM"], ["Saturday", "5–11PM"], ["Sunday", "5–11PM"], ["Monday", "5–11PM"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'avg_rating': 5.0, 'review_count': 2}]}}

exec(code, env_args)
