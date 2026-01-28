code = """import json
import re
import ast

# Read businesses data
businesses_file = locals()['var_functions.query_db:26']
with open(businesses_file, 'r') as f:
    businesses_data = json.load(f)

# Read reviews data
reviews_file = locals()['var_functions.query_db:30']
with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

print(f'Total businesses: {len(businesses_data)}')
print(f'Total reviews: {len(reviews_data)}')

# Parse hours and find businesses open after 6PM
def parse_hours(hours_str):
    if not hours_str or hours_str == 'None':
        return []
    try:
        return ast.literal_eval(hours_str)
    except:
        return []

def is_open_after_6pm(hours_list):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    for day, time_range in hours_list:
        if day in weekdays:
            if time_range == 'Open 24 hours':
                return True
            
            if '–' in time_range:
                parts = time_range.split('–')
            elif '-' in time_range:
                parts = time_range.split('-')
            else:
                continue
                
            if len(parts) < 2:
                continue
                
            closing = parts[1].strip()
            
            if 'PM' in closing:
                closing = closing.replace('PM', '').strip()
                if ':' in closing:
                    hour_part = closing.split(':')[0]
                    hour = int(hour_part) if hour_part.isdigit() else 0
                    if hour != 12:
                        hour += 12
                else:
                    hour = int(closing) if closing.isdigit() else 0
                    if hour != 12:
                        hour += 12
                if hour >= 18:
                    return True
            elif 'AM' in closing:
                closing = closing.replace('AM', '').strip()
                if ':' in closing:
                    hour_part = closing.split(':')[0]
                    hour = int(hour_part) if hour_part.isdigit() else 0
                else:
                    hour = int(closing) if closing.isdigit() else 0
                if hour == 12:
                    hour = 0
                if hour >= 18:
                    return True
    
    return False

# Find businesses open after 6PM
open_after_6 = []
for business in businesses_data:
    hours_list = parse_hours(business.get('hours', ''))
    if is_open_after_6pm(hours_list):
        open_after_6.append({
            'gmap_id': business.get('gmap_id'),
            'name': business.get('name'),
            'hours': business.get('hours'),
            'state': business.get('state')
        })

print(f'Businesses open after 6PM: {len(open_after_6)}')

# Calculate average ratings for these businesses
from collections import defaultdict

# Group ratings by gmap_id
ratings_by_business = defaultdict(list)
for review in reviews_data:
    gmap_id = review.get('gmap_id')
    rating = review.get('rating')
    if gmap_id and rating is not None:
        try:
            ratings_by_business[gmap_id].append(int(rating))
        except:
            pass

# Calculate averages for our businesses
business_ratings = []
for business in open_after_6:
    gmap_id = business['gmap_id']
    if gmap_id in ratings_by_business:
        ratings = ratings_by_business[gmap_id]
        avg_rating = sum(ratings) / len(ratings) if ratings else 0
        review_count = len(ratings)
        business_ratings.append({
            'gmap_id': gmap_id,
            'name': business['name'],
            'hours': business['hours'],
            'average_rating': round(avg_rating, 2),
            'review_count': review_count,
            'state': business['state']
        })

# Sort by average rating descending and get top 5
top_5 = sorted(business_ratings, key=lambda x: x['average_rating'], reverse=True)[:5]

print(f'Top 5 businesses: {len(top_5)}')

print('__RESULT__:')
print(json.dumps(top_5))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:5': ['business_description'], 'var_functions.query_db:6': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'count': 39}, 'var_functions.execute_python:24': [{'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_32', 'name': 'J B Oriental Inc'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_16', 'name': 'Hanford Auto Supply'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}, {'gmap_id': 'gmap_30', 'name': 'The Beauty Bar'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_63', 'name': 'Regus - California, Irvine - Oracle Tower'}, {'gmap_id': 'gmap_65', 'name': 'Excel Hair & Nails'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}, {'gmap_id': 'gmap_44', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
