code = """import json
import pandas as pd

# Load data
with open('var_function-call-8460312002315954258.json', 'r') as f:
    businesses = json.load(f)

with open('var_function-call-8460312002315952693.json', 'r') as f:
    ratings = json.load(f)

df_bus = pd.DataFrame(businesses)
df_rate = pd.DataFrame(ratings)
df_rate['avg_rating'] = df_rate['avg_rating'].astype(float)

# Function to check if open after 6 PM on a weekday
def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # hours_str is a string representation of a list
        # e.g., "[[\"Thursday\", \"6:30AM\\u20136PM\"], ...]"
        # We can use json.loads if we replace single quotes with double quotes, 
        # but the inner quotes are already double quotes escaped?
        # Actually, the string looks like: '[["Thursday", "6:30AM\u20136PM"], ...]'
        # Let's try json.loads directly.
        hours_list = json.loads(hours_str)
    except:
        return False
        
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    for day_info in hours_list:
        day = day_info[0]
        time_range = day_info[1]
        
        if day in weekdays:
            if time_range == 'Closed':
                continue
            if time_range == 'Open 24 hours':
                return True
                
            # Parse end time
            try:
                # time_range example: "6:30AM–6PM"
                # Split by en-dash or hyphen
                if '–' in time_range:
                    parts = time_range.split('–')
                elif '-' in time_range: # Fallback if standard hyphen is used
                     parts = time_range.split('-')
                else:
                    continue
                
                end_time_str = parts[1].strip() # e.g., "6PM" or "5:30PM" or "12AM"
                
                # Convert to 24h format to compare
                is_pm = 'PM' in end_time_str
                is_am = 'AM' in end_time_str
                
                if not is_pm and not is_am:
                    # Could be 24h format like "18:00" ? Unlikely given examples.
                    # Or noon/midnight?
                    pass
                
                time_val_str = end_time_str.replace('PM', '').replace('AM', '').strip()
                
                if ':' in time_val_str:
                    h, m = map(int, time_val_str.split(':'))
                else:
                    h = int(time_val_str)
                    m = 0
                
                # Convert to 24h
                if is_pm and h != 12:
                    h += 12
                if is_am and h == 12:
                    h = 0
                
                # Check if > 18:00 (6 PM)
                # If closing time is exactly 6 PM (18:00), is it "open after"?
                # "remains open after 6:00 PM" usually implies closing time > 18:00.
                # If it closes AT 6:00 PM, it doesn't remain open *after* 6:00 PM.
                # So strictly > 18:00.
                
                # Special case: closing at 12AM or 1AM, 2AM etc. (next day)
                # These are clearly after 6PM.
                # If h < 12 (AM) and not 0 (midnight can be start of day or end), 
                # usually means late night closing.
                # For standard parsing:
                # 12AM -> 0
                # 1AM -> 1
                # ...
                # 6PM -> 18
                
                # If the business closes in the AM (e.g. 1 AM), h will be 1.
                # We need to handle the "next day" logic.
                # But typically "9AM-5PM" -> 17.
                # "11AM-9:30PM" -> 21.5.
                
                # If h < opening time? No, we don't have opening time easily parsed here.
                # But simplified: if it's PM and > 6 (18:00), or if it's AM (meaning late night/early morning next day).
                
                # "12PM" is noon (12:00).
                # "12AM" is midnight (00:00).
                
                # Open after 6 PM condition:
                # - If PM: h > 6 (so 7PM, 8PM...) or (h == 6 and m > 0)? No, h is 12-based here for comparison logic?
                # Let's use 24h `h`.
                # 6 PM = 18.
                # Condition: `h > 18` or `(h == 18 and m > 0)` or `h < 6` (early morning next day implies open all night?)
                # Wait, `h < 6` (e.g. 1 AM) means it closed after 6 PM.
                # What if it closes at 12 PM (noon)? h=12. Not after 18.
                
                closing_minutes_from_midnight = h * 60 + m
                cutoff_minutes = 18 * 60 # 1080
                
                # If closing time is in the early morning (e.g. 00:00 to 09:00), it implies it stayed open past 6 PM.
                # Unless it's a breakfast place 5AM-9AM.
                # So we need to distinguish "closed early morning next day" vs "closed morning same day".
                # But the format usually puts the end time.
                # 6:30AM-6PM -> 18:00. Not > 18:00.
                # 9:30AM-10PM -> 22:00. Yes.
                # 9:30AM-9:30PM -> 21:30. Yes.
                # 5PM-2AM -> 2AM is next day.
                
                # Heuristic:
                # If closing time is PM:
                #   Must be > 6 PM (18:00).
                # If closing time is AM:
                #   If it's 12AM (0:00) to say 5AM?
                #   Usually "open after 6 PM" matches.
                #   What if it's 11AM? That's before 6 PM.
                
                if is_pm:
                    if closing_minutes_from_midnight > cutoff_minutes:
                        return True
                elif is_am:
                    # AM usually means next day early morning OR morning same day.
                    # If it's 12AM (midnight), it is after 6PM.
                    # If it's 1AM, 2AM... usually after 6PM.
                    # If it's 11AM, it's before 6PM (e.g. 6AM-11AM).
                    # Let's assume if h < 12 (AM) and h < 9 (e.g. up to 9AM closing could be night shift? Or breakfast?).
                    # Context: "remains open after 6:00 PM".
                    # If it closes at 1AM, it was open at 6PM?
                    # "Remains open after 6PM" means the business is open at some point after 6PM.
                    # Actually "remains open" implies it is open *at* 6PM and continues?
                    # Or just that the operating hours include time after 6PM.
                    # "Open after 6PM" -> closing time > 18:00.
                    
                    # If it closes at 1AM, 2AM... it satisfies.
                    # If it closes at 11AM, it doesn't.
                    # Let's say if h < 12 (noon) and h <= 5 (5 AM), it's late night.
                    # If h >= 6 (6 AM) and h < 12, it's morning shift.
                    
                    # Safe bet: if PM > 6 or AM < 9?
                    # Most "night" places close 12AM, 1AM, 2AM.
                    # Most "breakfast" places close 11AM, 12PM, 2PM.
                    
                    if h < 12: # AM
                        # 12 AM is 0. 1 AM is 1.
                        if h <= 5: # Close before 5 AM (next day)
                             return True
                        if h == 0: # Midnight
                             return True
                        # Else (6AM - 11AM) -> No.
                        
            except Exception as e:
                # print(f"Error parsing {time_range}: {e}")
                pass

    return False

# Apply filter
df_bus['is_open_late'] = df_bus['hours'].apply(is_open_after_6pm)
df_late = df_bus[df_bus['is_open_late']]

# Merge with ratings
df_merged = pd.merge(df_late, df_rate, on='gmap_id')

# Sort
df_sorted = df_merged.sort_values(by='avg_rating', ascending=False)

# Top 5
top_5 = df_sorted.head(5)[['name', 'hours', 'avg_rating']]

# Format result
result = top_5.to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-5582005809459928716': ['business_description'], 'var_function-call-5582005809459927563': ['review'], 'var_function-call-10196335900261481356': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-10196335900261481783': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_function-call-7089632061565965824': [{'count': '79'}], 'var_function-call-8460312002315954258': 'file_storage/function-call-8460312002315954258.json', 'var_function-call-8460312002315952693': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
