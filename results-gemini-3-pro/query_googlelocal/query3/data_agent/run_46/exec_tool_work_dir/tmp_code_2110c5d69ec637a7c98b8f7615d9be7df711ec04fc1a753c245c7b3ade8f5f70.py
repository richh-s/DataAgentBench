code = """import json
import pandas as pd
import re

# Load ratings
ratings_data = locals()['var_function-call-13036595038697070502']
df_ratings = pd.DataFrame(ratings_data)
df_ratings['avg_rating'] = df_ratings['avg_rating'].astype(float)

# Load business data
# The business data is in a file
file_path = locals()['var_function-call-15887600376055994397']
with open(file_path, 'r') as f:
    business_data = json.load(f)
df_business = pd.DataFrame(business_data)

# Merge
df = pd.merge(df_business, df_ratings, on='gmap_id', how='inner')

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    try:
        # hours_str is a string representation of a list, e.g. "[['Monday', '...'], ...]"
        # But wait, looking at the preview: "hours": "[[\"Thursday\", \"6:30AM\u20136PM\"], ...]"
        # It's a JSON string.
        try:
            hours_list = json.loads(hours_str)
        except:
            # Maybe it's a string repr of a python list?
            # The preview shows double quotes inside, so it looks like JSON.
            # But let's handle potential errors.
            return False
        
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_schedule in hours_list:
            day = day_schedule[0]
            time_range = day_schedule[1]
            
            if day in weekdays:
                if time_range == 'Closed':
                    continue
                if time_range == 'Open 24 hours':
                    return True
                
                # Split time range
                # The separator might be en-dash \u2013 or hyphen
                # Example: "6:30AM–6PM"
                parts = re.split(r'[\u2013-]', time_range)
                if len(parts) == 2:
                    end_time_str = parts[1].strip()
                    
                    # Parse end time
                    # Logic: Convert to 24h integer minutes or hours
                    # 6PM -> 18 * 60 = 1080
                    # 6:30PM -> 18.5 * 60
                    # 12AM -> 0 or 24? usually closing at 12AM means midnight.
                    # 12PM -> 12:00
                    
                    # Helper to parse time
                    def parse_time(t_str):
                        t_str = t_str.upper()
                        is_pm = 'PM' in t_str
                        is_am = 'AM' in t_str
                        time_val = t_str.replace('PM', '').replace('AM', '').strip()
                        
                        if ':' in time_val:
                            h, m = map(int, time_val.split(':'))
                        else:
                            h = int(time_val)
                            m = 0
                            
                        if is_pm and h != 12:
                            h += 12
                        if is_am and h == 12:
                            h = 0
                        return h * 60 + m

                    end_minutes = parse_time(end_time_str)
                    
                    # 6:00 PM is 18:00 -> 18 * 60 = 1080 minutes
                    # We want open AFTER 6 PM. So closing time > 1080.
                    # If closing time is 12AM (0), it usually means late night (24:00).
                    # If a place closes at 2AM, that's after 6PM.
                    # So if h < start_h (e.g. opens at 9AM, closes 2AM), we treat 2AM as next day.
                    # But simpler logic: if end_minutes > 1080 (18:00) OR end_minutes < opening_time (next day)
                    # Actually, if end_minutes is, say, 1 AM (60 mins), is it > 18:00? No.
                    # But effectively it stays open past 6 PM.
                    # Let's assume if end_time is between 00:00 and, say, 10:00 AM, it's next day closing, so it implies open through evening.
                    # But the simplest check for "remains open after 6:00 PM" is:
                    # closing_time > 18:00 OR closing_time < 06:00 (next day)
                    
                    if end_minutes > 1080: # later than 18:00
                        return True
                    if end_minutes < 360: # closes after midnight but before 6 AM (arbitrary cutoff for "late night")
                        return True
                        
    except Exception as e:
        return False
        
    return False

df['open_late'] = df['hours'].apply(is_open_after_6pm)

df_filtered = df[df['open_late']].copy()

# Sort by rating
# If ratings are equal, maybe secondary sort? Name? Not specified.
df_sorted = df_filtered.sort_values(by='avg_rating', ascending=False)

top_5 = df_sorted.head(5)

result = top_5[['name', 'hours', 'avg_rating']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8658414070301868830': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-13036595038697070502': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}], 'var_function-call-15887600376055994397': 'file_storage/function-call-15887600376055994397.json'}

exec(code, env_args)
