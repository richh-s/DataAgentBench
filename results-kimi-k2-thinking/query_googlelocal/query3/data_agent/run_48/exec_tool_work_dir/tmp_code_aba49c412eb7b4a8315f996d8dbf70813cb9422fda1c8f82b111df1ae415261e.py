code = """import json
import re
import os

# Get the rating data from the query result
rating_records = var_functions_query_db_48

# Build rating dictionary
rating_dict = {}
for rec in rating_records:
    rating_dict[rec['gmap_id']] = {
        'rating': float(rec['avg_rating']),
        'count': int(rec['review_count'])
    }

# Find the business data file
business_file = None
for key in list(locals().keys()):
    if 'query_db' in str(key) and ('54' in str(key) or '46' in str(key)):
        business_file = locals()[key]
        break

# Read business data
business_records = []
if business_file and isinstance(business_file, str) and '.json' in business_file:
    with open(business_file, 'r') as f:
        business_records = json.load(f)
else:
    # Try alternative approach - look for the json file directly
    for fname in os.listdir('.'):
        if 'query_db' in fname and '.json' in fname:
            with open(fname, 'r') as f:
                business_records = json.load(f)
            break

print(f"Loaded {len(business_records)} business records")

# Function to check if open after 6PM on weekdays
def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None' or hours_str == 'None':
        return False
    
    if '24 hours' in str(hours_str):
        return True
    
    try:
        hours_list = eval(hours_str) if isinstance(hours_str, str) else hours_str
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for entry in hours_list:
            if len(entry) >= 2:
                day = entry[0]
                time_range = entry[1]
                
                if day in weekdays and time_range != 'Closed':
                    # Get closing time
                    closing = None
                    if '\u2013' in time_range:
                        parts = time_range.split('\u2013')
                        if len(parts) > 1:
                            closing = parts[1].strip()
                    elif '-' in time_range:
                        parts = time_range.split('-')
                        if len(parts) > 1:
                            closing = parts[1].strip()
                    
                    if closing and 'PM' in closing:
                        hour_part = closing.replace('PM', '').strip()
                        minutes = 0
                        
                        if ':' in hour_part:
                            hour_str = hour_part.split(':')[0]
                            hour = int(hour_str)
                        else:
                            hour = int(hour_part)
                        
                        # Convert to 24 hour format
                        if hour != 12:
                            hour += 12
                        
                        # Check if after 6PM (18:00)
                        if hour > 18:
                            return True
    except Exception as e:
        return False
    
    return False

# Find businesses that match criteria
eligible = []
for biz in business_records:
    gmap_id = biz['gmap_id']
    hours = biz.get('hours', '')
    
    if gmap_id in rating_dict and is_open_after_6pm(hours):
        eligible.append({
            'name': biz['name'],
            'hours': hours,
            'rating': rating_dict[gmap_id]['rating']
        })

# Sort by rating and get top 5
top_5 = sorted(eligible, key=lambda x: x['rating'], reverse=True)[:5]

# Format output
result = []
for b in top_5:
    result.append({
        'name': b['name'],
        'operating_hours': b['hours'],
        'average_rating': round(b['rating'], 2)
    })

print('__RESULT__:')
print(json.dumps(result, indent=2, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_functions.query_db:5': [{'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}, {'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Black Tie Ski Rental Delivery of Mammoth', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Dunn-Edwards Paints', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]', 'state': 'Open ⋅ Closes 10PM'}, {'name': 'SUSY massage', 'hours': '[["Thursday", "9AM–10PM"], ["Friday", "9AM–10PM"], ["Saturday", "9AM–10PM"], ["Sunday", "9AM–10PM"], ["Monday", "9AM–10PM"], ["Tuesday", "9AM–10PM"], ["Wednesday", "9AM–10PM"]]', 'state': 'Open ⋅ Closes 10PM'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'status': 'analysis started'}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.list_db:44': ['review'], 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:48': [{'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'review_count': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'review_count': '38'}], 'var_functions.execute_python:52': [{'name': 'Hanford Veterinary Hospital', 'operating_hours': '[["Thursday", "9AM-6:30PM"], ["Friday", "9AM-6:30PM"], ["Saturday", "9AM-6:30PM"], ["Sunday", "Closed"], ["Monday", "9AM-6:30PM"], ["Tuesday", "9AM-6:30PM"], ["Wednesday", "9AM-6:30PM"]]', 'average_rating': 4.94}, {'name': 'The Beauty Bar', 'operating_hours': '[["Thursday", "9AM-8PM"], ["Friday", "9AM-8PM"], ["Saturday", "9AM-8PM"], ["Sunday", "Closed"], ["Monday", "9AM-8PM"], ["Tuesday", "9AM-8PM"], ["Wednesday", "9AM-8PM"]]', 'average_rating': 4.86}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json'}

exec(code, env_args)
