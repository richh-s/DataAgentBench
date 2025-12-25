code = """import json
import pandas as pd
import ast

# Load business data
with open(locals()['var_function-call-4901578397320899268'], 'r') as f:
    businesses = json.load(f)

# Load ratings data
ratings = locals()['var_function-call-4901578397320899695']

# Create DataFrames
df_biz = pd.DataFrame(businesses)
df_ratings = pd.DataFrame(ratings)

# Convert avg_rating to float
df_ratings['avg_rating'] = df_ratings['avg_rating'].astype(float)

# Merge
df = pd.merge(df_biz, df_ratings, on='gmap_id', how='inner')

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        hours_list = ast.literal_eval(hours_str)
    except:
        return False
        
    for day_info in hours_list:
        day = day_info[0]
        hours = day_info[1]
        
        if day in weekdays:
            if hours == 'Closed':
                continue
            if hours == 'Open 24 hours':
                return True
            
            # Parse range "Start–End"
            # Note: The dash could be different chars
            # In the sample: "6:30AM–6PM" (u2013 is en dash)
            if '\u2013' in hours:
                parts = hours.split('\u2013')
            elif '-' in hours:
                parts = hours.split('-')
            else:
                continue
            
            if len(parts) < 2:
                continue
                
            end_time_str = parts[1].strip() # e.g. "6PM", "9:30PM", "12AM", "2AM"
            
            # Parse end time
            # Simple parser
            try:
                # Remove 'PM' or 'AM'
                period = end_time_str[-2:].upper()
                if period not in ['AM', 'PM']:
                    continue
                    
                time_val = end_time_str[:-2]
                if ':' in time_val:
                    h, m = map(int, time_val.split(':'))
                else:
                    h = int(time_val)
                    m = 0
                
                # Logic to determine if > 6PM (18:00)
                # 6:00 PM is cutoff.
                
                if period == 'PM':
                    # 12 PM is 12:00 (Noon) -> Not after 6PM
                    # 1 PM to 5 PM -> 13:00 to 17:00 -> Not after
                    # 6 PM -> 18:00 -> Not after (strictly)
                    # 7 PM to 11 PM -> 19:00 to 23:00 -> After
                    if h == 12:
                        pass # Noon
                    elif h > 6 and h != 12:
                        return True
                    elif h == 6 and m > 0:
                        return True
                        
                elif period == 'AM':
                    # 12 AM (Midnight) -> After 6PM
                    # 1 AM to ... -> After 6PM (technically next day, but implies open late)
                    # Exception: closing at 10 AM, 11 AM (Morning business) -> Not after 6PM?
                    # But usually businesses don't go from Day 1 to 10 AM Day 2 without being open at 6PM Day 1?
                    # Wait, if it's "6AM-11AM", closing is 11 AM. 11 < 18. Fails.
                    # If it's "5PM-2AM", closing is 2 AM. 
                    # Heuristic: If closing time is AM and hour is 12, 1, 2, 3, 4, 5 -> Late night.
                    # If closing time is AM and hour is 6, 7, 8, 9, 10, 11 -> Morning shift?
                    if h == 12: # Midnight
                        return True
                    if h <= 5: # 1 AM to 5 AM
                        return True
                    # If h >= 6 (6 AM to 11 AM), assume it's a morning closing time, so NOT after 6PM (of previous day)
                    # Unless it's "Open 24 hours" handled above.
                    # Example: "6AM–2PM" -> Closes 2 PM.
            except:
                continue
                
    return False

# Filter
filtered_rows = []
for index, row in df.iterrows():
    if is_open_after_6pm(row['hours']):
        filtered_rows.append(row)

result_df = pd.DataFrame(filtered_rows)

if not result_df.empty:
    # Rank by rating (desc)
    # If tie, arbitrary (maybe name?)
    top5 = result_df.sort_values(by='avg_rating', ascending=False).head(5)
    
    # Select columns
    final_data = top5[['name', 'hours', 'avg_rating']].to_dict(orient='records')
else:
    final_data = []

print("__RESULT__:")
print(json.dumps(final_data))"""

env_args = {'var_function-call-6756781466245040193': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-6756781466245041404': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_function-call-13686654162312156682': [{'count': '79'}], 'var_function-call-13686654162312159169': [{'COUNT(*)': '2000'}], 'var_function-call-4901578397320899268': 'file_storage/function-call-4901578397320899268.json', 'var_function-call-4901578397320899695': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
