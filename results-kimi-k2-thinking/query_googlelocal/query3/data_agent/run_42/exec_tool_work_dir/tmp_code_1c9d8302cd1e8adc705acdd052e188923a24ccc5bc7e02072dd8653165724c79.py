code = """import json
import re
from datetime import datetime

# Load business data from file
business_file_path = var_functions.query_db:8
with open(business_file_path, 'r') as f:
    businesses = json.load(f)

# Load review data
review_data = var_functions.query_db:11

# Dictionary to store businesses that meet criteria
eligible_businesses = []

# Helper function to parse time strings like "6:30AM", "9PM", "12PM", etc.
def parse_time(time_str):
    time_str = time_str.strip()
    
    # Handle special cases like "Open 24 hours"
    if "Open 24 hours" in time_str:
        return None, True  # Always open
    
    try:
        # Remove any extra whitespace and unicode characters
        time_str = time_str.replace('\u2013', '-').replace('\u2019', '')
        
        # Extract AM/PM
        period = 'AM'
        if 'PM' in time_str.upper():
            period = 'PM'
        elif 'AM' in time_str.upper():
            period = 'AM'
            
        # Extract just the time numbers
        time_clean = re.sub(r'[^0-9:]', '', time_str)
        
        if ':' in time_clean:
            hour, minute = map(int, time_clean.split(':'))
        else:
            hour = int(time_clean)
            minute = 0
            
        # Convert to 24-hour format
        if period == 'PM' and hour != 12:
            hour += 12
        elif period == 'AM' and hour == 12:
            hour = 0
            
        return datetime.strptime(f"{hour:02d}:{minute:02d}", "%H:%M").time(), False
    except:
        return None, False

# Check if a business is open after 6 PM on any weekday
def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # Parse hours from string representation
        hours_list = eval(hours_str)  # Convert string representation of list to actual list
        
        weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_info in hours_list:
            if len(day_info) < 2:
                continue
                
            day_name, hours_range = day_info[0], day_info[1]
            
            # Only check weekdays
            if day_name in weekday_names:
                # Check if open 24 hours
                if "Open 24 hours" in str(hours_range):
                    return True
                    
                # Check closing time
                if '\u2013' in str(hours_range) or '-' in str(hours_range):
                    # Split time range
                    time_parts = hours_range.replace('\u2013', '-').split('-')
                    if len(time_parts) >= 2:
                        close_time_str = time_parts[1].strip()
                        close_time, is_24h = parse_time(close_time_str)
                        
                        if is_24h:
                            return True
                            
                        if close_time:
                            # Check if closing after 6 PM (18:00)
                            if close_time >= datetime.strptime("18:00", "%H:%M").time():
                                return True
        
        return False
    except Exception as e:
        return False

# Create a mapping of gmap_id to average rating for quick lookup
rating_map = {item['gmap_id']: float(item['avg_rating']) for item in review_data}
review_count_map = {item['gmap_id']: int(item['review_count']) for item in review_data}

# Process each business
for business in businesses:
    gmap_id = business['gmap_id']
    hours = business['hours']
    
    # Check if business has hours and reviews
    if not hours or hours == 'None':
        continue
        
    if gmap_id not in rating_map:
        continue
        
    # Check if open after 6 PM on weekdays
    if is_open_after_6pm(hours):
        eligible_businesses.append({
            'name': business['name'],
            'gmap_id': gmap_id,
            'hours': hours,
            'avg_rating': rating_map[gmap_id],
            'review_count': review_count_map[gmap_id]
        })

# Sort by average rating (highest first)
eligible_businesses.sort(key=lambda x: x['avg_rating'], reverse=True)

# Get top 5
top_5 = eligible_businesses[:5]

# Format result
result = []
for business in top_5:
    # Parse hours to be more readable
    hours_str = business['hours']
    try:
        hours_list = eval(hours_str)
        formatted_hours = []
        for day_info in hours_list:
            if len(day_info) >= 2:
                formatted_hours.append(f"{day_info[0]}: {day_info[1]}")
        readable_hours = "; ".join(formatted_hours)
    except:
        readable_hours = hours_str
    
    result.append({
        'name': business['name'],
        'average_rating': round(business['avg_rating'], 2),
        'operating_hours': readable_hours,
        'total_reviews': business['review_count']
    })

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'state': 'Open now', 'hours': 'None', 'num_of_reviews': '6'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'state': 'Open ⋅ Closes 6PM', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'num_of_reviews': '18'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'state': 'Open ⋅ Closes 5PM', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'num_of_reviews': '6'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'state': 'Open ⋅ Closes 5PM', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'num_of_reviews': '7'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'state': 'Open ⋅ Closes 5:30PM', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'num_of_reviews': '6'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:11': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'review_count': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'review_count': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'review_count': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'review_count': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'review_count': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'review_count': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'review_count': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'review_count': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'review_count': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'review_count': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'review_count': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'review_count': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'review_count': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'review_count': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'review_count': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'review_count': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'review_count': '3'}]}

exec(code, env_args)
