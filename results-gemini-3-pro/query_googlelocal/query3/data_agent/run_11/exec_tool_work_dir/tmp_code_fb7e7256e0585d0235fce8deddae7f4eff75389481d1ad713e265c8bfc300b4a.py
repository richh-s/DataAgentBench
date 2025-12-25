code = """import pandas as pd
import json
import ast
import re

# Load data
avg_ratings_data = locals()['var_function-call-9640460964494927142']
avg_ratings_df = pd.DataFrame(avg_ratings_data)
avg_ratings_df['avg_rating'] = pd.to_numeric(avg_ratings_df['avg_rating'])

businesses_file = locals()['var_function-call-7787007113202162490']
with open(businesses_file, 'r') as f:
    businesses_data = json.load(f)
businesses_df = pd.DataFrame(businesses_data)

# Helper function to check if open after 6 PM
def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        hours_list = ast.literal_eval(hours_str)
    except:
        return False
        
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    for day_info in hours_list:
        day = day_info[0]
        time_range = day_info[1]
        
        if day in weekdays:
            if 'Open 24 hours' in time_range:
                return True
            if time_range == 'Closed':
                continue
            
            # Normalize split character
            # The char is \u2013 (EN DASH)
            time_range = time_range.replace('\u2013', '-')
            
            if '-' in time_range:
                parts = time_range.split('-')
            else:
                continue
            
            if len(parts) < 2:
                continue
                
            end_time_str = parts[1].strip()
            
            # Parse closing time
            match = re.match(r'(\d+)(?::(\d+))?\s*(AM|PM)', end_time_str, re.IGNORECASE)
            if match:
                hour = int(match.group(1))
                minute = int(match.group(2) or 0)
                period = match.group(3).upper()
                
                # Logic:
                # If PM: 12PM is noon (12:00), 1PM is 13:00... 6PM is 18:00.
                # If we want AFTER 18:00, then 6:01PM or 7PM etc.
                # If AM: 12AM is 00:00 (next day), 1AM is 01:00 (next day).
                # Any AM closing time means it closes after midnight, which is definitely after 6 PM of the current day.
                
                # Convert to minutes from start of day (0-24h)
                # But handle AM as next day (>24h) if we consider the shift
                
                # Actually, simpler:
                # If period is AM: it is "late night" / next morning => Yes (unless it closes at, say, 11 AM the next day? usually these are late night spots)
                # But wait, some businesses open at 6 AM and close at 11 AM. That is AM closing.
                # I need to check the START time to see if it's an overnight shift?
                # Or just assume "AM" closing means early morning next day if it corresponds to a standard evening business?
                # The prompt implies "remain open after 6:00 PM".
                # If a business is 7AM-11AM, it closes at 11AM. That is NOT after 6PM.
                # If a business is 6PM-2AM, it closes at 2AM. That IS after 6PM.
                
                # So:
                # PM times: must be > 6 PM (12 PM is noon, < 6 PM). 12 PM = 12, 1 PM = 13 ... 6 PM = 18.
                # AM times:
                # If closing is 12 AM, 1 AM, 2 AM... these are effectively > 6 PM (18:00).
                # But 10 AM, 11 AM? These are before 6 PM.
                # Threshold: 6 PM is 18:00.
                # A closing time X is "after 6 PM" if:
                #   If X is PM: X_24 > 18:00.
                #   If X is AM: Generally implies next day (so yes) OR morning shift (so no).
                #   Let's look at start times? 
                #   Actually, simpler heuristic:
                #   If closing time is AM, is it "early morning" (e.g. 12AM-5AM)? Likely open late.
                #   If closing time is AM, is it "late morning" (e.g. 10AM-11AM)? Likely morning business.
                #   Let's check the examples.
                #   Example: "Thursday", "9AM–5PM" -> Closes 5PM (No)
                #   Example: "Thursday", "9:30AM–9:30PM" -> Closes 9:30PM (Yes)
                #   Example: "Thursday", "9:30AM–10PM" -> Closes 10PM (Yes)
                
                # What if 5PM-2AM? Closes 2AM.
                # What if 6AM-10AM? Closes 10AM (No).
                
                # So for AM closing times:
                # If hour is 12, 1, 2, 3, 4, 5 (AM) -> Probably late night.
                # If hour is 6, 7, 8, 9, 10, 11 (AM) -> Probably morning shift.
                # Let's use < 6 AM as the cutoff for "late night". Or maybe < 9 AM?
                # But usually, "Open after 6 PM" implies it is open during the evening.
                # If it closes at 2 AM, it was open at 6 PM (presumably).
                # If it closes at 10 AM, it was NOT open after 6 PM (it closed way before).
                
                # So:
                # PM: Calculate 24h. If > 18.0 (18:00), then True.
                # AM: If < 12 (noon), we need to distinguish 1am vs 11am.
                #     Assume 12 AM - 4 AM is late night -> True.
                #     Assume 5 AM - 11 AM is morning -> False.
                #     (This is a heuristic, but likely sufficient for business hours).
                
                val = 0
                if period == 'PM':
                    if hour == 12:
                        val = 12
                    else:
                        val = hour + 12
                    # Check if > 18
                    if val > 18:
                        return True
                    if val == 18 and minute > 0:
                        return True
                        
                elif period == 'AM':
                    if hour == 12: # Midnight
                        return True
                    if hour < 6: # 1 AM to 5 AM
                        return True
                    # 6 AM to 11 AM -> False
                    
    return False

# Apply filter
businesses_df['is_open_late'] = businesses_df['hours'].apply(is_open_after_6pm)
filtered_businesses = businesses_df[businesses_df['is_open_late']].copy()

# Merge with ratings
merged_df = pd.merge(filtered_businesses, avg_ratings_df, on='gmap_id', how='inner')

# Sort
merged_df = merged_df.sort_values(by='avg_rating', ascending=False)

# Select top 5
top_5 = merged_df.head(5)

# Format result
result = top_5[['name', 'hours', 'avg_rating']].to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-283690375400797289': ['business_description'], 'var_function-call-15473292039796571328': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-6224501817853066367': [{'count': '79'}], 'var_function-call-10240551998409761322': ['review'], 'var_function-call-9640460964494927142': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}], 'var_function-call-7787007113202162490': 'file_storage/function-call-7787007113202162490.json'}

exec(code, env_args)
