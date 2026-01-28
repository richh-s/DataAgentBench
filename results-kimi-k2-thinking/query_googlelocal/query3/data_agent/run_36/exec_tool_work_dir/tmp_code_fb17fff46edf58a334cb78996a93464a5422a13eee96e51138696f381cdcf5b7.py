code = """import json
import pandas as pd
import re
from datetime import datetime

business_file = locals()['var_functions.query_db:6']
review_file = locals()['var_functions.query_db:8']

with open(business_file, 'r') as f:
    businesses = json.load(f)

with open(review_file, 'r') as f:
    reviews = json.load(f)

df_business = pd.DataFrame(businesses)
df_reviews = pd.DataFrame(reviews)

df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

df_avg_rating = df_reviews.groupby('gmap_id')['rating'].agg(['mean', 'count']).reset_index()
df_avg_rating.columns = ['gmap_id', 'avg_rating', 'review_count']

def is_after_6pm(time_str):
    if time_str in ['Closed', 'Open 24 hours']:
        return False
    
    time_str = time_str.strip()
    time_str = time_str.replace('\u2013', '-').replace('\u2014', '-').replace('\u2212', '-')
    
    if '-' in time_str:
        time_str = time_str.split('-')[1].strip()
    
    try:
        if ':' in time_str:
            time_obj = datetime.strptime(time_str, '%I:%M%p')
        else:
            time_obj = datetime.strptime(time_str, '%I%p')
        
        # Check if after 6:00 PM (hour > 18 or hour == 18 with minutes > 0)
        if time_obj.hour > 18 or (time_obj.hour == 18 and time_obj.minute > 0):
            return True
        elif time_obj.hour < 12 and 'PM' in time_str.upper() and time_obj.hour != 6:
            return True
        return False
    except:
        return False

def check_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        hours_list = eval(hours_str)
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day, hours in hours_list:
            if day in weekdays:
                if is_after_6pm(hours):
                    return True
        return False
    except:
        return False

df_business['open_after_6pm'] = df_business['hours'].apply(check_open_after_6pm)

open_businesses = df_business[df_business['open_after_6pm'] == True]

df_merged = open_businesses.merge(df_avg_rating, on='gmap_id', how='inner')

df_merged = df_merged[df_merged['review_count'] >= 2]

top_5 = df_merged.sort_values(['avg_rating', 'review_count'], ascending=[False, False]).head(5)

result = []
for _, row in top_5.iterrows():
    result.append({
        'name': row['name'],
        'hours': row['hours'],
        'avg_rating': round(row['avg_rating'], 2),
        'review_count': row['review_count']
    })

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.list_db:5': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': 'Total businesses: 66, Total reviews: 2000', 'var_functions.execute_python:18': [{'name': 'Hanford Auto Supply', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "9AM–5PM"], ["Sunday", "Closed"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]', 'avg_rating': 5.0, 'review_count': 6}, {'name': 'White Barn Candle Co', 'hours': '[["Thursday", "10AM–9PM"], ["Friday", "10AM–9PM"], ["Saturday", "10AM–9PM"], ["Sunday", "11AM–7PM"], ["Monday", "10AM–9PM"], ["Tuesday", "10AM–9PM"], ["Wednesday", "10AM–9PM"]]', 'avg_rating': 5.0, 'review_count': 2}, {'name': 'Beauty Divine Artistry', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]', 'avg_rating': 5.0, 'review_count': 8}, {'name': 'Taba Rug Gallery', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'avg_rating': 5.0, 'review_count': 18}, {'name': 'TACOS LA CABANA', 'hours': '[["Thursday", "Closed"], ["Friday", "5–11PM"], ["Saturday", "5–11PM"], ["Sunday", "5–11PM"], ["Monday", "5–11PM"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'avg_rating': 5.0, 'review_count': 2}]}

exec(code, env_args)
