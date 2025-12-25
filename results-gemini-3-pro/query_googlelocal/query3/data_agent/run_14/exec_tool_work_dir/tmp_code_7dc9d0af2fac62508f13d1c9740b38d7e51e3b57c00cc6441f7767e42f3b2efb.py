code = """import json
import pandas as pd
import re

# Load business data
with open(locals()['var_function-call-14941970642997851150'], 'r') as f:
    businesses = json.load(f)

# Load ratings data
ratings = locals()['var_function-call-15092265849116477822']
ratings_df = pd.DataFrame(ratings)
ratings_df['avg_rating'] = ratings_df['avg_rating'].astype(float)

# Helper function to check if a time string is after 6:00 PM
def is_open_after_6pm(time_str):
    if not time_str or time_str == 'Closed':
        return False
    if 'Open 24 hours' in time_str:
        return True
    
    # Split start and end time. The separator seems to be \u2013 (en dash)
    # Check what separator is used. In the sample: "6:30AM\u20136PM"
    parts = re.split(r'[\u2013-]', time_str)
    if len(parts) < 2:
        return False
    
    end_time = parts[-1].strip()
    
    # Parse end_time
    # Formats: "6PM", "6:30PM", "12AM", "12PM", "10:30PM"
    match = re.match(r'(\d+)(?::(\d+))?\s*([AP]M)', end_time, re.IGNORECASE)
    if not match:
        return False
    
    hour = int(match.group(1))
    minute = int(match.group(2)) if match.group(2) else 0
    period = match.group(3).upper()
    
    # Convert to 24-hour format (roughly) for comparison
    if period == 'PM':
        if hour != 12:
            hour += 12
    elif period == 'AM':
        if hour == 12:
            hour = 0 # Midnight
        else:
            # 1 AM, etc.
            # If closing time is AM, it usually means it's open past midnight, so definitely after 6PM
            # Unless it's like "11AM" closing, but that's morning.
            # Most businesses closing in AM are late night bars/clubs (e.g. 2 AM).
            # To be safe: if hour < 6 (e.g. 1AM, 2AM, 3AM, 4AM, 5AM), it implies open past 6PM previous day.
            # If hour is e.g. 10AM, 11AM, it closed in morning.
            if hour < 10: 
                return True
            else:
                return False
                
    # Check if > 18:00
    # 6:00 PM is 18:00. We want > 18:00
    if hour > 18:
        return True
    if hour == 18 and minute > 0:
        return True
        
    return False

filtered_businesses = []

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for b in businesses:
    hours_str = b.get('hours')
    if not hours_str or hours_str == 'None':
        continue
    
    # Parse the list from string representation
    # The string is like "[['Thursday', '...'], ...]"
    # It's a Python list string repr, but in JSON it might just be a string.
    # The previous output showed: "hours": "[[\"Thursday\", ...]]"
    try:
        hours_list = json.loads(hours_str)
    except:
        # Fallback if it's single quotes and not valid JSON
        try:
            import ast
            hours_list = ast.literal_eval(hours_str)
        except:
            continue
            
    # Check weekdays
    is_open_late = False
    for day_info in hours_list:
        day_name = day_info[0]
        time_range = day_info[1]
        
        if day_name in weekdays:
            if is_open_after_6pm(time_range):
                is_open_late = True
                break
    
    if is_open_late:
        filtered_businesses.append(b)

filtered_df = pd.DataFrame(filtered_businesses)

# Join with ratings
merged_df = pd.merge(filtered_df, ratings_df, on='gmap_id', how='inner')

# Sort
result_df = merged_df.sort_values(by='avg_rating', ascending=False).head(5)

# Select columns
final_result = result_df[['name', 'hours', 'avg_rating']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(final_result))"""

env_args = {'var_function-call-6551431659011964264': ['business_description'], 'var_function-call-12900961597528651043': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-3407772366185507359': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}], 'var_function-call-8841547116407559933': [{'count': '79'}], 'var_function-call-62047334608425080': [{'COUNT(*)': '2000'}], 'var_function-call-14941970642997851150': 'file_storage/function-call-14941970642997851150.json', 'var_function-call-15092265849116477822': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
