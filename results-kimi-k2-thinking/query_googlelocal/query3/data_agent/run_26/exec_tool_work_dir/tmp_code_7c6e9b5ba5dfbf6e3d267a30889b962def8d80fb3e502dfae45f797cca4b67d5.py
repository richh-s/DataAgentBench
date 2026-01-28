code = """import json
from collections import defaultdict

# Load business data
business_file = locals()['var_functions.query_db:2']
with open(business_file, 'r') as f:
    businesses = json.load(f)

# Load review data  
review_file = locals()['var_functions.query_db:10']
with open(review_file, 'r') as f:
    reviews = json.load(f)

# Only need to recalculate the eligible businesses
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

eligible_businesses = []
businesses_by_id = {}

for business in businesses:
    if business['hours'] and business['hours'] != 'None':
        try:
            hours_data = json.loads(business['hours'])
            
            open_after_6 = False
            for day_entry in hours_data:
                day = day_entry[0]
                hours = day_entry[1]
                
                if day in weekdays and hours != 'Closed' and '–' in hours:
                    closing_time = hours.split('–')[1]
                    if 'PM' in closing_time:
                        # Extract hour number
                        import re
                        hour_match = re.search(r'(\d{1,2}):?\d{0,2}\s*PM', closing_time, re.IGNORECASE)
                        if hour_match:
                            hour = int(hour_match.group(1))
                            if hour == 12:
                                hour = 12  # Noon
                            else:
                                hour += 12  # PM conversion
                            
                            # Must be strictly after 6 PM (18:00)
                            if hour > 18 or (hour == 18 and '30' in closing_time):
                                open_after_6 = True
                                break
                    elif ':' in closing_time and ('AM' not in closing_time):
                        # 24-hour format like 19:30, 20:00
                        hour_str = closing_time.split(':')[0]
                        try:
                            hour = int(hour_str)
                            if hour >= 19:  # 7 PM or later
                                open_after_6 = True
                                break
                        except:
                            pass
            
            if open_after_6:
                eligible_businesses.append(business['gmap_id'])
                businesses_by_id[business['gmap_id']] = {
                    'name': business['name'],
                    'hours': business['hours']
                }
        except:
            pass

# Calculate average ratings for eligible businesses
ratings_by_business = defaultdict(list)

for review in reviews:
    gmap_id = review['gmap_id']
    rating = int(review['rating'])
    
    if gmap_id in eligible_businesses:
        ratings_by_business[gmap_id].append(rating)

business_averages = []
for gmap_id, ratings in ratings_by_business.items():
    if len(ratings) >= 1:
        avg_rating = sum(ratings) / len(ratings)
        business_averages.append({
            'gmap_id': gmap_id,
            'name': businesses_by_id[gmap_id]['name'],
            'hours': businesses_by_id[gmap_id]['hours'],
            'avg_rating': round(avg_rating, 2),
            'num_reviews': len(ratings)
        })

# Sort by average rating descending
business_averages.sort(key=lambda x: x['avg_rating'], reverse=True)

# Get top 5
top_5 = business_averages[:5]

print('__RESULT__:')
print(json.dumps(top_5, indent=2))"""

env_args = {'var_functions.query_db:0': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 66, 'sample': {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}}, 'var_functions.execute_python:8': {'total_businesses': 66, 'eligible_businesses': 28, 'sample_eligible': [{'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'business_count': 66, 'review_count': 665, 'review_sample': [{'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}]}, 'var_functions.execute_python:14': {'eligible_count': 0, 'with_reviews': 0, 'top_5': [], 'all_ranked': []}, 'var_functions.execute_python:16': {'total_businesses': 66, 'eligible_count': 0, 'eligible_sample': []}, 'var_functions.execute_python:18': {'status': 'debug complete'}, 'var_functions.execute_python:24': [{'name': 'Vons Chicken', 'hours_raw': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'name': 'Angel-A Massage', 'hours_raw': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}], 'var_functions.execute_python:26': {'eligible_businesses': 13, 'top_5': [{'gmap_id': 'gmap_36', 'name': 'Beauty Divine Artistry', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]', 'avg_rating': 5.0, 'num_reviews': 8}, {'gmap_id': 'gmap_51', 'name': 'Taba Rug Gallery', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'avg_rating': 5.0, 'num_reviews': 18}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]', 'avg_rating': 4.67, 'num_reviews': 18}, {'gmap_id': 'gmap_34', 'name': "Ruby's Boutique", 'hours': '[["Thursday", "10AM–6PM"], ["Friday", "10AM–6PM"], ["Saturday", "10AM–5PM"], ["Sunday", "11AM–4PM"], ["Monday", "10AM–6PM"], ["Tuesday", "10AM–6PM"], ["Wednesday", "10AM–6PM"]]', 'avg_rating': 4.5, 'num_reviews': 8}, {'gmap_id': 'gmap_67', 'name': 'LuXe Organic Nails Boutique', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "9AM–6PM"], ["Sunday", "10AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "Closed"], ["Wednesday", "10AM–7PM"]]', 'avg_rating': 4.45, 'num_reviews': 31}]}}

exec(code, env_args)
