code = """import json
import pandas as pd
import datetime

# Load data
with open(var_function_call_5580388133865470968, 'r') as f:
    businesses = json.load(f)
with open(var_function_call_9361860428015302, 'r') as f:
    reviews = json.load(f)

# Convert to DataFrame
df_biz = pd.DataFrame(businesses)
df_rev = pd.DataFrame(reviews)

# Calculate average rating
# Ensure rating is numeric
df_rev['rating'] = pd.to_numeric(df_rev['rating'])
# Group by gmap_id
rating_stats = df_rev.groupby('gmap_id')['rating'].agg(['mean', 'count']).reset_index()
rating_stats.rename(columns={'mean': 'avg_rating', 'count': 'review_count'}, inplace=True)

# Parse hours
# Weekdays set
weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}

def parse_time_to_minutes(time_str):
    # Formats: "6PM", "6:30PM", "12AM", "12:30AM"
    # Returns minutes from start of day.
    # Handle AM/PM
    time_str = time_str.strip().upper()
    if time_str == '12AM': return 0 # Start of day, but for closing time usually means end of day 24:00? 
    # Actually, if a shop opens 9AM-12AM, it closes at midnight. That is > 18:00.
    # If it opens 9AM-2AM, it closes at 26:00 relative to start.
    
    is_pm = 'PM' in time_str
    is_am = 'AM' in time_str
    
    # Remove AM/PM
    t = time_str.replace('PM', '').replace('AM', '').strip()
    
    if ':' in t:
        h, m = map(int, t.split(':'))
    else:
        h = int(t)
        m = 0
    
    if is_pm and h != 12:
        h += 12
    if is_am and h == 12:
        h = 0
        
    return h * 60 + m

def is_open_after_6pm(hours_json_str):
    if not hours_json_str or hours_json_str == 'None':
        return False
    try:
        hours_list = json.loads(hours_json_str.replace("'", '"')) # Fix potential single quotes if any, though sample has double quotes
    except:
        try:
            # The sample shows valid JSON string but let's be safe
             hours_list = json.loads(hours_json_str)
        except:
            return False
            
    # hours_list is list of [Day, TimeRange]
    # e.g. ["Thursday", "6:30AM–6PM"]
    
    for day, time_range in hours_list:
        if day in weekdays:
            if time_range == "Closed":
                continue
            if time_range == "Open 24 hours":
                return True
            
            # Split time range
            # Separators: \u2013 (en dash), -
            sep = None
            if '\u2013' in time_range: sep = '\u2013'
            elif '-' in time_range: sep = '-'
            
            if sep:
                parts = time_range.split(sep)
                if len(parts) == 2:
                    start_str, end_str = parts
                    
                    # Parse end time
                    # Logic: 6:00 PM is 18 * 60 = 1080 minutes.
                    # We need closing time > 1080.
                    # Special handling for times past midnight (e.g. 1AM, 2AM).
                    # If closing time is AM (and not 12AM which might be midnight), it's likely next day.
                    # Or 12AM (midnight).
                    
                    # Let's detect AM/PM
                    end_str = end_str.strip()
                    
                    # If it ends with AM, and it's not 12AM (00:00), it is likely next day, so it stays open past 6PM.
                    # E.g. "2AM".
                    # 12AM is midnight. Midnight is > 6PM.
                    
                    # Let's use a robust way.
                    # Calculate minutes.
                    # 6PM = 1080 min.
                    try:
                        end_minutes = parse_time_to_minutes(end_str)
                        
                        # Logic to determine if it is "after 6PM"
                        # If end_minutes > 1080 (18:00), it's open after 6PM.
                        # BUT:
                        # 1PM = 13:00 = 780. Not after 6PM.
                        # 6PM = 18:00 = 1080. Not after 6PM (closes AT 6PM).
                        # 7PM = 19:00 = 1140. Yes.
                        # 12AM = 0:00. This is typically midnight effectively. 24:00.
                        # If parse_time returns 0 for 12AM, we should treat it as 24:00 (1440 min) for closing time logic if it follows a PM open time?
                        # Or simply: if the closing time is AM (00:00 to 11:59), it's almost certainly next day (unless it's a breakfast place closing at 10AM).
                        # Let's look at the open time too?
                        # "6:30AM–6PM" -> Open 6:30, Close 18:00.
                        # "11AM-9:30PM" -> Close 21:30.
                        # "11AM-2AM" -> Close 2:00 (next day).
                        
                        is_am = 'AM' in end_str.upper()
                        is_pm = 'PM' in end_str.upper()
                        
                        # If closing time is PM:
                        # Must be > 6PM.
                        # 12PM is noon.
                        if is_pm:
                            if end_minutes > 1080: # 18:00
                                # Also handle 12PM (noon) correctly. 12PM is 720.
                                # 12:30PM is 750.
                                # 11:59PM is 1439.
                                # 12PM case: parse_time returns 720. 720 < 1080. Correct.
                                # 6PM case: parse_time returns 1080. 1080 is not > 1080. Correct.
                                # 6:01PM: 1081. Correct.
                                # 12AM case check below.
                                return True
                                
                        elif is_am:
                            # If closing time is AM.
                            # It could be morning (closes at 11AM) or night (closes at 1AM).
                            # If it closes at 1AM, it was open at 6PM?
                            # Usually yes.
                            # Check opening time.
                            start_minutes = parse_time_to_minutes(start_str)
                            # If open at 8AM and close at 11AM -> Not open after 6PM.
                            # If open at 5PM and close at 2AM -> Open after 6PM.
                            # If open at 8AM and close at 2AM -> Open after 6PM.
                            
                            # Heuristic: If close is AM and close < open, it crossed midnight.
                            # If close is AM (e.g. 2AM = 120) and open is AM (e.g. 8AM = 480). 120 < 480 -> crossed midnight.
                            # If close is AM (2AM) and open is PM (8PM). Crossed midnight.
                            
                            # However, 12AM needs care.
                            # parse_time(12AM) = 0.
                            # parse_time(12:30AM) = 30.
                            
                            if end_minutes < start_minutes:
                                # Crossed midnight. So it was open during the evening.
                                return True
                            else:
                                # Open and close on same day AM? e.g. 8AM - 11AM.
                                # Not open after 6PM.
                                pass
                                
                            # Special case: 12AM (midnight).
                            # If parsed as 0.
                            if '12AM' in end_str.upper() or '12:00AM' in end_str.upper():
                                # Usually implies midnight closure.
                                # Midnight is > 6PM.
                                return True
                                
                    except:
                        pass
    return False

# Apply filter
eligible_gmap_ids = []
hours_info = {} # Store formatted hours for output

for index, row in df_biz.iterrows():
    if is_open_after_6pm(row['hours']):
        eligible_gmap_ids.append(row['gmap_id'])

# Filter df_biz
df_eligible = df_biz[df_biz['gmap_id'].isin(eligible_gmap_ids)].copy()

# Join with ratings
df_result = pd.merge(df_eligible, rating_stats, on='gmap_id', how='inner')

# Sort
# Primary: avg_rating (desc)
# Secondary: review_count (desc) (optional but good for stability)
df_result.sort_values(by=['avg_rating', 'review_count'], ascending=[False, False], inplace=True)

# Top 5
top_5 = df_result.head(5)

# Format output
results = []
for index, row in top_5.iterrows():
    results.append({
        "name": row['name'],
        "hours": row['hours'],
        "avg_rating": row['avg_rating'],
        "review_count": row['review_count'] # Included for verification
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-9296450689531834642': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_function-call-1537564774235231612': [{'COUNT(*)': '2000'}], 'var_function-call-5258409667665638486': [{'count': '79'}], 'var_function-call-5580388133865470968': 'file_storage/function-call-5580388133865470968.json', 'var_function-call-9361860428015302': 'file_storage/function-call-9361860428015302.json'}

exec(code, env_args)
