code = """import json
import re
from datetime import datetime

# Load the business data from the file which is stored as a path
business_file_path = locals()['var_functions.query_db:6']
if isinstance(business_file_path, str) and business_file_path.endswith('.json'):
    with open(business_file_path, 'r') as f:
        business_data = json.load(f)
else:
    business_data = locals()['var_functions.query_db:6']

# Load the review data from the file which is stored as a path
review_file_path = locals()['var_functions.query_db:8']
if isinstance(review_file_path, str) and review_file_path.endswith('.json'):
    with open(review_file_path, 'r') as f:
        review_data = json.load(f)
else:
    review_data = locals()['var_functions.query_db:8']

# Function to parse time string and check if it's after 6 PM (18:00)
def is_after_6pm(time_str):
    """Check if a closing time is after 6:00 PM"""
    if not time_str or time_str in ['Closed', 'None']:
        return False
    
    if 'Open 24 hours' in str(time_str):
        return True
    
    # Extract the closing time (after the dash/en-dash)
    if '–' in str(time_str):
        closing_time = time_str.split('–')[1].strip()
    elif '-' in str(time_str):
        closing_time = time_str.split('-')[1].strip()
    else:
        return False
    
    # Parse the time
    closing_time = str(closing_time).upper().strip()
    
    try:
        if ':' in closing_time:
            # Format: "9:30PM"
            time_part = closing_time.replace('PM', '').replace('AM', '').strip()
            hours, minutes = map(int, time_part.split(':'))
            
            if 'PM' in closing_time and hours != 12:
                hours += 12
            elif 'AM' in closing_time and hours == 12:
                hours = 0
        else:
            # Format: "6PM" or "12PM"
            time_part = closing_time.replace('PM', '').replace('AM', '').strip()
            hours = int(time_part)
            minutes = 0
            
            if 'PM' in closing_time and hours != 12:
                hours += 12
            elif 'AM' in closing_time and hours == 12:
                hours = 0
        
        # Check if time is after 18:00 (6 PM)
        return hours > 18 or (hours == 18 and minutes > 0)
    except:
        return False

# Function to check if a business is open after 6 PM on any weekday
def is_open_after_6pm_weekday(hours_str):
    """Check if business is open after 6 PM on Monday-Friday"""
    if not hours_str or hours_str == 'None' or hours_str == 'null':
        return False
    
    try:
        # Parse the string representation of list
        hours_list = eval(hours_str)
        
        if not isinstance(hours_list, list):
            return False
        
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_hours in hours_list:
            if isinstance(day_hours, list) and len(day_hours) >= 2:
                day = day_hours[0]
                hours = day_hours[1]
                if day in weekdays and is_after_6pm(str(hours)):
                    return True
        
        return False
    except Exception as e:
        return False

# Calculate average rating per business
from collections import defaultdict

# Group ratings by gmap_id
ratings_by_business = defaultdict(list)
for review in review_data:
    gmap_id = review.get('gmap_id')
    rating = review.get('rating')
    if gmap_id and rating is not None:
        try:
            ratings_by_business[gmap_id].append(int(rating))
        except:
            try:
                ratings_by_business[gmap_id].append(float(rating))
            except:
                continue

# Calculate average ratings
avg_ratings = {}
for gmap_id, ratings in ratings_by_business.items():
    if ratings:
        avg_ratings[gmap_id] = sum(ratings) / len(ratings)

# Process businesses and filter those open after 6 PM on weekdays
eligible_businesses = []

for business in business_data:
    gmap_id = business.get('gmap_id')
    name = business.get('name')
    hours = business.get('hours')
    
    # Check if business has hours and is open after 6 PM on weekdays
    if gmap_id and name and hours and is_open_after_6pm_weekday(hours):
        avg_rating = avg_ratings.get(gmap_id)
        if avg_rating is not None and avg_rating > 0:  # Only include businesses with reviews
            eligible_businesses.append({
                'name': name,
                'gmap_id': gmap_id,
                'hours': hours,
                'avg_rating': round(avg_rating, 2),
                'review_count': len(ratings_by_business.get(gmap_id, []))
            })

# Sort by average rating (descending) and get top 5, excluding any with fewer than 2 reviews
top_businesses = []
for business in sorted(eligible_businesses, key=lambda x: x['avg_rating'], reverse=True):
    if business['review_count'] >= 2:
        top_businesses.append(business)
    if len(top_businesses) == 5:
        break

# Prepare the result
result = []
for business in top_businesses:
    result.append({
        'name': business['name'],
        'operating_hours': business['hours'],
        'average_rating': business['avg_rating'],
        'review_count': business['review_count']
    })

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.list_db:5': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
