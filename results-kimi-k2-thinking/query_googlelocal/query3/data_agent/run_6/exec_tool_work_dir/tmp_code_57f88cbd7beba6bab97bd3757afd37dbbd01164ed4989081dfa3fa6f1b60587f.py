code = """import json
import re
import ast
import pandas as pd

# Load business hours data
business_data_path = locals()['var_functions.query_db:6']
with open(business_data_path, 'r') as f:
    business_hours_data = json.load(f)

# Load review ratings data
review_data_path = locals()['var_functions.query_db:18']
with open(review_data_path, 'r') as f:
    review_data = json.load(f)

# Create DataFrame for reviews
reviews_df = pd.DataFrame(review_data)
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'])

# Calculate average rating for each business
avg_ratings = reviews_df.groupby('gmap_id')['rating'].agg(['mean', 'count']).reset_index()
avg_ratings.columns = ['gmap_id', 'avg_rating', 'num_reviews']

# Filter businesses with at least 3 reviews to ensure meaningful average
avg_ratings_filtered = avg_ratings[avg_ratings['num_reviews'] >= 3]

print(f"Total businesses with reviews: {len(avg_ratings)}")
print(f"Businesses with >= 3 reviews: {len(avg_ratings_filtered)}")

# Function to parse closing time
def parse_closing_time(time_str):
    try:
        if '–' in time_str:
            parts = time_str.split('–')
            close_time = parts[1].strip()
        elif '-' in time_str:
            parts = time_str.split('-')
            close_time = parts[1].strip()
        else:
            return None
            
        if close_time == 'Open 24 hours' or close_time == 'Closed':
            return None
            
        time_match = re.match(r'(\d{1,2})(?::(\d{2}))?([AP]M)', close_time, re.IGNORECASE)
        if time_match:
            hour = int(time_match.group(1))
            minute = int(time_match.group(2)) if time_match.group(2) else 0
            am_pm = time_match.group(3).upper()
            
            if am_pm == 'PM' and hour != 12:
                hour += 12
            elif am_pm == 'AM' and hour == 12:
                hour = 0
                
            return hour + minute/60
        
        return None
    except:
        return None

# Function to check if business is open after 6 PM on any weekday
def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None' or hours_str == '[[], []]':
        return False
    
    try:
        hours_list = ast.literal_eval(hours_str)
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_entry in hours_list:
            if not day_entry or len(day_entry) < 2:
                continue
            day = day_entry[0]
            hours_range = day_entry[1]
            
            if day not in weekdays:
                continue
            if hours_range == 'Closed':
                continue
                
            close_hour = parse_closing_time(hours_range)
            if close_hour is not None and close_hour > 18:
                return True
        return False
    except:
        return False

# Identify businesses open after 6 PM
businesses_open_late = []
for biz in business_hours_data:
    if is_open_after_6pm(biz.get('hours')):
        businesses_open_late.append(biz)

print(f"Businesses open after 6 PM: {len(businesses_open_late)}")

# Create DataFrame for businesses
business_df = pd.DataFrame(businesses_open_late)

# Merge with average ratings
merged_df = business_df.merge(avg_ratings_filtered, on='gmap_id', how='inner')
print(f"Businesses open after 6 PM with >= 3 reviews: {len(merged_df)}")

# Sort by average rating descending
merged_df = merged_df.sort_values('avg_rating', ascending=False)

# Get top 5
top_5 = merged_df.head(5)

print(f"\\nTop 5 businesses:")
print(top_5[['name', 'hours', 'avg_rating', 'num_reviews']])

# Format hours for display
def format_hours(hours_str):
    if not hours_str or hours_str == 'None':
        return 'N/A'
    try:
        hours_list = ast.literal_eval(hours_str)
        return str(hours_list)
    except:
        return hours_str

top_5_results = []
for _, row in top_5.iterrows():
    top_5_results.append({
        'name': row['name'],
        'hours': format_hours(row['hours']),
        'avg_rating': round(row['avg_rating'], 2),
        'num_reviews': int(row['num_reviews'])
    })

print('__RESULT__:')
print(json.dumps(top_5_results, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.query_db:4': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'count': 22, 'gmap_ids': ['gmap_74', 'gmap_22', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_32', 'gmap_21', 'gmap_28', 'gmap_30', 'gmap_53', 'gmap_65', 'gmap_51', 'gmap_36', 'gmap_12', 'gmap_7', 'gmap_8', 'gmap_11', 'gmap_61', 'gmap_68', 'gmap_67', 'gmap_40', 'gmap_60']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
