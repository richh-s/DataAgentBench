code = """import json
import pandas as pd
import re

# Load data
with open('var_function-call-11667929200820267605.json', 'r') as f:
    businesses = json.load(f)

ratings = locals()['var_function-call-1511148607237023480']

# Create DataFrames
df_biz = pd.DataFrame(businesses)
df_rate = pd.DataFrame(ratings)
df_rate['avg_rating'] = df_rate['avg_rating'].astype(float)

# Merge
df = pd.merge(df_biz, df_rate, on='gmap_id')

def parse_time(t_str):
    # Normalize
    t_str = t_str.strip().upper()
    
    # 24 hours
    if "24 HOURS" in t_str:
        return 2400 # Treat as late
    
    # Check AM/PM
    is_pm = 'PM' in t_str
    is_am = 'AM' in t_str
    
    # Remove AM/PM
    t_clean = t_str.replace('PM', '').replace('AM', '').strip()
    
    if ':' in t_clean:
        parts = t_clean.split(':')
        h = int(parts[0])
        m = int(parts[1])
    else:
        try:
            h = int(t_clean)
            m = 0
        except:
            return None # Parse error
            
    # Convert to 24h
    if is_pm and h != 12:
        h += 12
    if is_am and h == 12:
        h = 0
    # If no AM/PM, it's ambiguous. But in the context of "9AM-5PM" or "3-8PM", the second part usually has the suffix.
    # If the range is "3-8PM", the first part is 3, second is 8PM.
    # We are parsing the closing time, which should have the suffix if the format is standard.
    # However, sometimes it might be "10-2" (implied AM/PM?). 
    # Let's assume the provided format always has AM/PM for closing time if not 24h.
    # If AM/PM is missing but we parsed it, it's risky. But looking at data, e.g. "3-8PM", "8:30AM-5:30PM".
    # Wait, if I parse "8PM", is_pm is True.
    
    return h * 60 + m

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # The string is a JSON representation of a list of lists
        # But it's a string, so we need to parse it.
        # It uses single quotes or double quotes? The previous output showed double quotes in the string representation?
        # Let's look at the sample: "[[\"Thursday\", \"6:30AM\u20136PM\"], ...]"
        # It looks like valid JSON.
        hours_list = json.loads(hours_str)
    except:
        return False
        
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    for day_info in hours_list:
        if len(day_info) != 2:
            continue
        day = day_info[0]
        time_range = day_info[1]
        
        if day in weekdays:
            if time_range == "Open 24 hours":
                return True
            if "Closed" in time_range:
                continue
            
            # Split range
            # Range usually contains en-dash \u2013
            if '\u2013' in time_range:
                parts = time_range.split('\u2013')
            elif '-' in time_range:
                parts = time_range.split('-')
            else:
                continue
            
            if len(parts) >= 2:
                closing_str = parts[1] # The end time
                # Handle cases like "3-8PM" where opening doesn't have suffix but closing does.
                # If closing is "8PM", it works.
                
                closing_minutes = parse_time(closing_str)
                
                if closing_minutes is not None:
                    # 6:00 PM is 18 * 60 = 1080 minutes
                    if closing_minutes > 1080:
                        # Also check for early morning closing times (e.g. 1AM next day)
                        # parse_time returns 0-23h + minutes.
                        # If closing is 1AM, it is 1*60 = 60.
                        # Wait, logic: "remains open after 6:00 PM".
                        # If it closes at 7 PM (19:00), it's > 18:00.
                        # If it closes at 1 AM, it's definitely open after 6 PM (assumed open in evening).
                        # But standard hours "9AM-5PM" -> 17:00 < 18:00.
                        # "5PM-1AM" -> 1AM is 60. 60 < 1080.
                        # So simply `closing_minutes > 1080` is not enough if it spans past midnight.
                        # However, typically "next day" hours are not explicitly marked as next day in this format.
                        # Usually "10AM-2AM".
                        # If opening is PM and closing is AM, it spans midnight.
                        # But I only have closing time here.
                        # Heuristic: If closing time is early morning (e.g. < 10 AM) and opening is likely previous day.
                        # But I am only parsing closing time.
                        # If closing time is 00:00 to 04:00 (say), it's effectively "late".
                        # Let's verify start time? No, let's just use the closing time.
                        # If closing time is 1 AM, it's 60.
                        # If closing time is 12 AM, it's 0 (or 2400?).
                        # My parser: 12 AM -> 0.
                        # 12 PM -> 12 * 60 = 720.
                        # 6 PM -> 18 * 60 = 1080.
                        # So if closing_minutes > 1080, it's open after 6PM.
                        # If closing_minutes < some small number (e.g. 5AM = 300), it's likely late night.
                        # So: if closing_minutes > 1080 or closing_minutes < 360 (6 AM): return True.
                        
                        if closing_minutes > 1080 or closing_minutes < 360:
                            return True
                            
    return False

# Filter
filtered_rows = []
for index, row in df.iterrows():
    if is_open_after_6pm(row['hours']):
        filtered_rows.append(row)

df_filtered = pd.DataFrame(filtered_rows)

if not df_filtered.empty:
    # Sort by avg_rating desc
    df_filtered = df_filtered.sort_values(by='avg_rating', ascending=False)
    
    # Top 5
    top_5 = df_filtered.head(5)
    
    # Select columns
    result = top_5[['name', 'hours', 'avg_rating']].to_dict(orient='records')
else:
    result = []

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-11022338651652732524': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-3525770603734450963': [{'count': '79'}], 'var_function-call-11667929200820267605': 'file_storage/function-call-11667929200820267605.json', 'var_function-call-13730369003664848941': [{'COUNT(DISTINCT gmap_id)': '79'}], 'var_function-call-1511148607237023480': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
