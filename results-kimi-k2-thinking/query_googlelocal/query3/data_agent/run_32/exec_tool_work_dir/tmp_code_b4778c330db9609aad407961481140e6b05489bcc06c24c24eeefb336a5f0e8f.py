code = """import json
import re
from datetime import datetime

# Get the file paths
biz_file = globals()['var_functions.query_db_18']
rev_file = globals()['var_functions.query_db_16']

# Load the data
with open(biz_file, 'r') as f:
    businesses = json.load(f)

with open(rev_file, 'r') as f:
    reviews = json.load(f)

# Debug: Show the structure
print(f"Loaded {len(businesses)} businesses and {len(reviews)} reviews")
print(f"Sample business hours: {businesses[0]['hours'] if businesses else 'None'}")

# First, let's calculate average ratings for each business
ratings_by_biz = {}
for review in reviews:
    gmap_id = review['gmap_id']
    rating = int(review['rating'])  # Convert to integer
    
    if gmap_id not in ratings_by_biz:
        ratings_by_biz[gmap_id] = []
    ratings_by_biz[gmap_id].append(rating)

# Calculate average ratings
avg_ratings = {}
for gmap_id, ratings in ratings_by_biz.items():
    avg_ratings[gmap_id] = sum(ratings) / len(ratings)

print(f"Calculated average ratings for {len(avg_ratings)} businesses")

# Now filter businesses that are open after 6 PM on weekdays
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
qualified_businesses = []

def parse_time_to_minutes(time_str):
    """Convert time like '6PM' or '6:30PM' to minutes since midnight"""
    time_str = time_str.strip().upper()
    
    # Handle special cases
    if time_str == 'CLOSED' or time_str == 'OPEN 24 HOURS':
        return None
    
    # Extract time and am/pm
    match = re.match(r'(\d{1,2})(?::(\d{2}))?\s*(AM|PM)', time_str)
    if not match:
        return None
    
    hour = int(match.group(1))
    minute = int(match.group(2)) if match.group(2) else 0
    period = match.group(3)
    
    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0
    
    return hour * 60 + minute

def is_open_after_6pm(hours_str):
    """Check if business is open after 6 PM (6:01 PM or later) on any weekday"""
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # Parse the hours string which is in format: [["Day", "XAM–YPM"], ...]
        hours_list = eval(hours_str)
        
        for day_entry in hours_list:
            if len(day_entry) != 2:
                continue
                
            day, hours_range = day_entry
            
            # Skip if not a weekday
            if day not in weekdays:
                continue
            
            # Skip if closed
            if hours_range == 'Closed':
                continue
            
            # Handle "Open 24 hours" - this qualifies
            if hours_range == 'Open 24 hours':
                return True
            
            # Parse time range (format: "9AM–9PM" or "9:30AM–10PM")
            if '–' in hours_range:
                times = hours_range.split('–')
                if len(times) == 2:
                    close_time = parse_time_to_minutes(times[1])
                    if close_time is not None:
                        # Check if close time is after 6:00 PM (6:00 PM = 18*60 = 1080 minutes)
                        six_pm_minutes = 18 * 60
                        if close_time > six_pm_minutes:
                            return True
    except:
        # If parsing fails, skip this business
        pass
    
    return False

# Find qualified businesses
qualified = []
for business in businesses:
    gmap_id = business['gmap_id']
    name = business['name']
    hours = business['hours']
    
    if is_open_after_6pm(hours):
        avg_rating = avg_ratings.get(gmap_id, 0)
        review_count = len(ratings_by_biz.get(gmap_id, []))
        
        qualified.append({
            'gmap_id': gmap_id,
            'name': name,
            'hours': hours,
            'avg_rating': avg_rating,
            'review_count': review_count
        })

# Sort by average rating (descending) and take top 5
top_5 = sorted(qualified, key=lambda x: x['avg_rating'], reverse=True)[:5]

print(f"Found {len(qualified)} businesses open after 6 PM")
print(f"Top 5 by rating:")
for i, biz in enumerate(top_5, 1):
    print(f"{i}. {biz['name']}: {biz['avg_rating']:.2f} stars ({biz['review_count']} reviews)")

# Prepare final result
final_result = []
for biz in top_5:
    final_result.append({
        'name': biz['name'],
        'operating_hours': biz['hours'],
        'average_rating': round(biz['avg_rating'], 2),
        'review_count': biz['review_count']
    })

print('__RESULT__:')
print(json.dumps({
    'top_businesses': final_result,
    'total_qualified': len(qualified)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_functions.query_db:6': [{'total': '66'}], 'var_functions.query_db:8': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_functions.query_db:11': [{'name': 'AMMCOR Management Company, Inc.', 'hours': '[["Thursday", "8AM–12PM"], ["Friday", "8AM–12PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8AM–12PM"], ["Tuesday", "8AM–12PM"], ["Wednesday", "8AM–12PM"]]'}, {'name': 'Ace Jewelry & Loan', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "10AM–4PM"], ["Sunday", "10AM–4PM"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Acuity Eye Group, Retina Institute & Acuity 360 Advanced Vision Center - Tustin', 'hours': '[["Thursday", "8AM–4PM"], ["Friday", "8AM–4PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8AM–4PM"], ["Tuesday", "8AM–4PM"], ["Wednesday", "8AM–4PM"]]'}, {'name': 'Advanced Auto Upholstery', 'hours': '[["Thursday", "8AM–7PM"], ["Friday", "8AM–7PM"], ["Saturday", "8AM–5PM"], ["Sunday", "Closed"], ["Monday", "8AM–7PM"], ["Tuesday", "8AM–7PM"], ["Wednesday", "8AM–7PM"]]'}, {'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'name': 'Aurora Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'name': 'Avani Staffing Solutions', 'hours': '[["Thursday", "8–11:30AM"], ["Friday", "8–11:30AM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8–11:30AM"], ["Tuesday", "8–11:30AM"], ["Wednesday", "8–11:30AM"]]'}, {'name': 'B2Sign, Inc.', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8AM–5PM"], ["Tuesday", "8AM–5PM"], ["Wednesday", "8AM–5PM"]]'}, {'name': 'Beads and More', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "9AM–5PM"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Beauty Divine Artistry', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]'}, {'name': 'Birdi Systems, Inc.', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8AM–5PM"], ["Tuesday", "8AM–5PM"], ["Wednesday", "8AM–5PM"]]'}, {'name': 'Black Tie Ski Rental Delivery of Mammoth', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]'}, {'name': 'Colfax Elementary School', 'hours': '[["Thursday", "7:30AM–4PM"], ["Friday", "7:30AM–4PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "7:30AM–4PM"], ["Tuesday", "7:30AM–4PM"], ["Wednesday", "7:30AM–4PM"]]'}, {'name': 'CrossFit to the Core', 'hours': '[["Thursday", "5–11AM"], ["Friday", "5–11AM"], ["Saturday", "8–11AM"], ["Sunday", "Closed"], ["Monday", "5–11AM"], ["Tuesday", "5–11AM"], ["Wednesday", "6:30–11AM"]]'}, {'name': 'Dirk Vermeulen - State Farm Insurance Agent', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–4PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Dr. Syverain Skincare Clinic', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "Closed"], ["Sunday", "8AM–1PM"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]'}, {'name': 'Dunn-Edwards Paints', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]'}, {'name': 'Encino Dermatology & Laser: Alex Khadavi MD', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8AM–5PM"], ["Tuesday", "8AM–5PM"], ["Wednesday", "8AM–5PM"]]'}, {'name': 'Excel Hair & Nails', 'hours': '[["Thursday", "9AM–7PM"], ["Friday", "9AM–7PM"], ["Saturday", "9AM–7PM"], ["Sunday", "10AM–5PM"], ["Monday", "9AM–7PM"], ["Tuesday", "9AM–7PM"], ["Wednesday", "9AM–7PM"]]'}, {'name': 'Fitness Machine Technicians', 'hours': '[["Thursday", "8:30AM–5PM"], ["Friday", "8:30AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5PM"], ["Tuesday", "8:30AM–5PM"], ["Wednesday", "8:30AM–5PM"]]'}, {'name': 'Full Circle Trading Post', 'hours': '[["Thursday", "10AM–5:30PM"], ["Friday", "10AM–5:30PM"], ["Saturday", "10AM–5:30PM"], ["Sunday", "10AM–5:30PM"], ["Monday", "10AM–5:30PM"], ["Tuesday", "10AM–5:30PM"], ["Wednesday", "10AM–5:30PM"]]'}, {'name': 'Good Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'name': 'HAVEN™ Dispensary', 'hours': '[["Thursday", "Closed"], ["Friday", "Closed"], ["Saturday", "4–4:03AM"], ["Sunday", "Closed"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]'}, {'name': 'HDR', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8AM–5PM"], ["Tuesday", "8AM–5PM"], ["Wednesday", "8AM–5PM"]]'}, {'name': 'Hanford Auto Supply', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "9AM–5PM"], ["Sunday", "Closed"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]'}, {'name': 'IBEW 441', 'hours': '[["Thursday", "7:30AM–4:30PM"], ["Friday", "7:30AM–4:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "7:30AM–4:30PM"], ["Tuesday", "7:30AM–4:30PM"], ["Wednesday", "7:30AM–4:30PM"]]'}, {'name': 'IronStep', 'hours': '[["Thursday", "7AM–3:30PM"], ["Friday", "7AM–3:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "7AM–3:30PM"], ["Tuesday", "7AM–3:30PM"], ["Wednesday", "7AM–3:30PM"]]'}, {'name': 'J & T Plumbing Pros', 'hours': '[["Thursday", "7AM–5PM"], ["Friday", "7AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "7AM–5PM"], ["Tuesday", "7AM–5PM"], ["Wednesday", "7AM–5PM"]]'}, {'name': 'J B Oriental Inc', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:40': {'loaded': True, 'num_businesses': 66, 'num_reviews': 2000}}

exec(code, env_args)
