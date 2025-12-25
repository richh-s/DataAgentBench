code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-15021409738949519812'], 'r') as f:
    business_data = json.load(f)

with open(locals()['var_function-call-15021409738949518551'], 'r') as f:
    review_data = json.load(f)

# Convert to DataFrame
df_biz = pd.DataFrame(business_data)
df_rev = pd.DataFrame(review_data)

# Convert rating to numeric
df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')

# Calculate average rating per gmap_id
avg_ratings = df_rev.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.rename(columns={'rating': 'average_rating'}, inplace=True)

# Parse hours and filter
def is_open_late_weekday(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # hours_str is a string representation of a list of lists.
        # But it might be valid JSON or python string. 
        # The sample showed: "[['Thursday', '6:30AM–6PM'], ...]" with unicode dash
        # Let's try json.loads first, if fails, use eval (safe enough here as it comes from DB) or ast.literal_eval
        import ast
        try:
            hours_list = json.loads(hours_str)
        except:
            try:
                hours_list = ast.literal_eval(hours_str)
            except:
                return False
        
        if not isinstance(hours_list, list):
            return False

        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_info in hours_list:
            if len(day_info) != 2:
                continue
            day = day_info[0]
            time_range = day_info[1]
            
            if day in weekdays:
                if 'Open 24 hours' in time_range:
                    return True
                if 'Closed' in time_range:
                    continue
                
                # Split time range
                # The dash can be various characters.
                # Common ones: -, –, —
                parts = re.split(r'[–\-\—]', time_range)
                if len(parts) >= 2:
                    close_time_str = parts[-1].strip()
                    
                    # Parse close_time_str
                    # Formats: "6PM", "6:30PM", "12AM", "2:30AM"
                    # We want to know if it's strictly later than 6:00 PM (18:00)
                    
                    # Helper to convert to minutes from midnight
                    def parse_time(t_str):
                        t_str = t_str.upper()
                        is_pm = 'PM' in t_str
                        is_am = 'AM' in t_str
                        
                        t_str = t_str.replace('PM', '').replace('AM', '').strip()
                        if ':' in t_str:
                            h, m = map(int, t_str.split(':'))
                        else:
                            h = int(t_str)
                            m = 0
                        
                        if is_pm and h != 12:
                            h += 12
                        if is_am and h == 12:
                            h = 0
                        
                        return h * 60 + m

                    try:
                        close_min = parse_time(close_time_str)
                        # 6:00 PM is 18 * 60 = 1080 minutes
                        # If closing time is early morning (e.g. 1 AM), it is effectively "after 6 PM" in the context of remaining open.
                        # So if close_min < open_min, it usually means next day.
                        # But simpler:
                        # If close_time is PM and > 6PM -> OK.
                        # If close_time is AM (and not 00:00 midnight which is technically 12AM?), it usually means open late.
                        # 12 AM = 0 mins. 12 PM = 720 mins. 6 PM = 1080 mins.
                        
                        # Logic:
                        # If time is in AM (0 to 11:59 AM) -> It is after 6 PM (next day).
                        # If time is 12 PM to 5:59 PM -> No.
                        # If time is >= 6 PM (18:00) -> Yes (Wait, strictly after? "remains open after 6:00 PM").
                        # If it closes AT 6:00 PM, it does not remain open AFTER 6:00 PM.
                        # So close_min > 1080 OR close_min < 720 (approx, assuming opening is morning).
                        # Let's refine:
                        # 00:00 (12 AM) to 11:59 (11:59 AM) -> Late night / Next morning. Keeps open past 6 PM.
                        # 12:00 (12 PM) to 18:00 (6 PM) -> Closes before or at 6 PM.
                        # 18:01 (6:01 PM) to 23:59 (11:59 PM) -> Closes after 6 PM.
                        
                        if close_min > 1080 or close_min < 720: # < 720 accounts for AM times (next day)
                             return True
                    except:
                        pass
        return False
    except:
        return False

# Apply filter
df_biz['is_open_late'] = df_biz['hours'].apply(is_open_late_weekday)
df_filtered = df_biz[df_biz['is_open_late']]

# Merge with ratings
df_merged = pd.merge(df_filtered, avg_ratings, on='gmap_id', how='left')

# Drop NaN ratings if any (or treat as 0? Usually drop or put at bottom. Prompt asks for top 5 ranked by rating)
df_merged = df_merged.dropna(subset=['average_rating'])

# Sort
df_merged = df_merged.sort_values(by='average_rating', ascending=False)

# Select top 5
top_5 = df_merged.head(5)

# Format result
result_list = []
for _, row in top_5.iterrows():
    result_list.append({
        "name": row['name'],
        "hours": row['hours'],
        "average_rating": row['average_rating']
    })

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-4136843148304252205': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_function-call-4136843148304251200': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_function-call-11332849554563786417': [{'count': '79'}], 'var_function-call-15021409738949519812': 'file_storage/function-call-15021409738949519812.json', 'var_function-call-15021409738949518551': 'file_storage/function-call-15021409738949518551.json'}

exec(code, env_args)
