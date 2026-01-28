code = """import json
import re
from datetime import datetime

# Read business data from file
result_file = locals()['var_functions.query_db:20']
print('Loading business data from file:', str(result_file)[:100])

with open(result_file, 'r') as f:
    business_records = json.load(f)

print('Total businesses with hours:', len(business_records))

# Parse hours and find businesses open after 6 PM on weekdays
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
selected_businesses = []

for business in business_records:
    gmap_id = business.get('gmap_id')
    name = business.get('name')
    hours_str = business.get('hours')
    num_reviews = business.get('num_of_reviews')
    
    if not hours_str or hours_str == 'None':
        continue
    
    try:
        hours_list = json.loads(hours_str.replace('\\\\', '\\'))
        open_late = False
        
        for day, hours in hours_list:
            if day not in weekdays:
                continue
                
            if hours == 'Closed':
                continue
            
            if hours == 'Open 24 hours':
                open_late = True
                break
            
            # Parse closing time
            match = re.search(r'(\d{1,2}(?::\d{2})?)(AM|PM)$', hours.split(u'\u2013')[1])
            if match:
                time_str, ampm = match.groups()
                hour = int(time_str.split(':')[0])
                
                if ampm == 'PM' and hour != 12:
                    hour += 12
                elif ampm == 'AM' and hour == 12:
                    hour = 0
                
                if hour >= 18:  # 6 PM or later
                    open_late = True
                    break
        
        if open_late:
            selected_businesses.append({
                'gmap_id': gmap_id,
                'name': name,
                'hours': hours_str,
                'num_of_reviews': num_reviews
            })
    
    except Exception as e:
        pass
        # print('Error parsing hours for', name, ':', str(e)[:50])

print('Businesses open after 6PM on weekdays:', len(selected_businesses))
print('\nFirst 5 selected:')
for i, b in enumerate(selected_businesses[:5]):
    print(f"{i+1}. {b['name']}")

result = json.dumps(selected_businesses)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_functions.query_db:8': [{'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'num_of_reviews': '18'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'num_of_reviews': '6'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'num_of_reviews': '7'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'num_of_reviews': '6'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]', 'num_of_reviews': '18'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'num_of_reviews': '6'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]', 'num_of_reviews': '8'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'hours': '[["Thursday", "9AM–10PM"], ["Friday", "9AM–10PM"], ["Saturday", "9AM–10PM"], ["Sunday", "9AM–10PM"], ["Monday", "9AM–10PM"], ["Tuesday", "9AM–10PM"], ["Wednesday", "9AM–10PM"]]', 'num_of_reviews': '8'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'num_of_reviews': '56'}, {'gmap_id': 'gmap_32', 'name': 'J B Oriental Inc', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]', 'num_of_reviews': '6'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'hours': '[["Thursday", "10AM–8PM"], ["Friday", "10AM–8PM"], ["Saturday", "10AM–8PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–8PM"], ["Tuesday", "10AM–8PM"], ["Wednesday", "10AM–8PM"]]', 'num_of_reviews': '15'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'num_of_reviews': '8'}, {'gmap_id': 'gmap_63', 'name': 'Regus - California, Irvine - Oracle Tower', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "Open 24 hours"], ["Saturday", "Open 24 hours"], ["Sunday", "Open 24 hours"], ["Monday", "Open 24 hours"], ["Tuesday", "Open 24 hours"], ["Wednesday", "Open 24 hours"]]', 'num_of_reviews': '16'}, {'gmap_id': 'gmap_65', 'name': 'Excel Hair & Nails', 'hours': '[["Thursday", "9AM–7PM"], ["Friday", "9AM–7PM"], ["Saturday", "9AM–7PM"], ["Sunday", "10AM–5PM"], ["Monday", "9AM–7PM"], ["Tuesday", "9AM–7PM"], ["Wednesday", "9AM–7PM"]]', 'num_of_reviews': '52'}, {'gmap_id': 'gmap_51', 'name': 'Taba Rug Gallery', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'num_of_reviews': '18'}], 'var_functions.query_db:18': [{'gmap_id': 'gmap_9', 'average_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_77', 'average_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_76', 'average_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_56', 'average_rating': '5.0', 'review_count': '28'}, {'gmap_id': 'gmap_51', 'average_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_50', 'average_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_5', 'average_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_37', 'average_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_36', 'average_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_31', 'average_rating': '5.0', 'review_count': '8'}, {'gmap_id': 'gmap_27', 'average_rating': '5.0', 'review_count': '5'}, {'gmap_id': 'gmap_16', 'average_rating': '5.0', 'review_count': '6'}, {'gmap_id': 'gmap_1', 'average_rating': '5.0', 'review_count': '3'}, {'gmap_id': 'gmap_17', 'average_rating': '4.970588235294118', 'review_count': '34'}, {'gmap_id': 'gmap_52', 'average_rating': '4.9655172413793105', 'review_count': '58'}, {'gmap_id': 'gmap_11', 'average_rating': '4.9603174603174605', 'review_count': '378'}, {'gmap_id': 'gmap_75', 'average_rating': '4.944055944055944', 'review_count': '143'}, {'gmap_id': 'gmap_15', 'average_rating': '4.911111111111111', 'review_count': '45'}, {'gmap_id': 'gmap_53', 'average_rating': '4.894736842105263', 'review_count': '38'}, {'gmap_id': 'gmap_70', 'average_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_26', 'average_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_0', 'average_rating': '4.888888888888889', 'review_count': '18'}, {'gmap_id': 'gmap_47', 'average_rating': '4.879310344827586', 'review_count': '58'}, {'gmap_id': 'gmap_40', 'average_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_30', 'average_rating': '4.857142857142857', 'review_count': '21'}, {'gmap_id': 'gmap_72', 'average_rating': '4.842105263157895', 'review_count': '38'}, {'gmap_id': 'gmap_7', 'average_rating': '4.837837837837838', 'review_count': '37'}, {'gmap_id': 'gmap_6', 'average_rating': '4.75', 'review_count': '4'}, {'gmap_id': 'gmap_58', 'average_rating': '4.75', 'review_count': '8'}, {'gmap_id': 'gmap_2', 'average_rating': '4.705882352941177', 'review_count': '17'}, {'gmap_id': 'gmap_29', 'average_rating': '4.6923076923076925', 'review_count': '26'}, {'gmap_id': 'gmap_74', 'average_rating': '4.666666666666667', 'review_count': '18'}, {'gmap_id': 'gmap_3', 'average_rating': '4.666666666666667', 'review_count': '27'}, {'gmap_id': 'gmap_59', 'average_rating': '4.631578947368421', 'review_count': '38'}, {'gmap_id': 'gmap_13', 'average_rating': '4.625', 'review_count': '8'}, {'gmap_id': 'gmap_44', 'average_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_34', 'average_rating': '4.5', 'review_count': '8'}, {'gmap_id': 'gmap_67', 'average_rating': '4.451612903225806', 'review_count': '31'}, {'gmap_id': 'gmap_63', 'average_rating': '4.4375', 'review_count': '16'}, {'gmap_id': 'gmap_62', 'average_rating': '4.411764705882353', 'review_count': '68'}, {'gmap_id': 'gmap_48', 'average_rating': '4.4', 'review_count': '5'}, {'gmap_id': 'gmap_69', 'average_rating': '4.395833333333333', 'review_count': '48'}, {'gmap_id': 'gmap_14', 'average_rating': '4.375', 'review_count': '8'}, {'gmap_id': 'gmap_22', 'average_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_38', 'average_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_41', 'average_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_64', 'average_rating': '4.25', 'review_count': '8'}, {'gmap_id': 'gmap_4', 'average_rating': '4.25', 'review_count': '4'}, {'gmap_id': 'gmap_78', 'average_rating': '4.222222222222222', 'review_count': '18'}, {'gmap_id': 'gmap_57', 'average_rating': '4.184210526315789', 'review_count': '38'}, {'gmap_id': 'gmap_20', 'average_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_32', 'average_rating': '4.166666666666667', 'review_count': '6'}, {'gmap_id': 'gmap_35', 'average_rating': '4.142857142857143', 'review_count': '84'}, {'gmap_id': 'gmap_46', 'average_rating': '4.130952380952381', 'review_count': '168'}, {'gmap_id': 'gmap_65', 'average_rating': '4.115384615384615', 'review_count': '52'}, {'gmap_id': 'gmap_68', 'average_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_61', 'average_rating': '4.0', 'review_count': '3'}, {'gmap_id': 'gmap_49', 'average_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_19', 'average_rating': '4.0', 'review_count': '8'}, {'gmap_id': 'gmap_18', 'average_rating': '4.0', 'review_count': '4'}, {'gmap_id': 'gmap_21', 'average_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_54', 'average_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_28', 'average_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_24', 'average_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_45', 'average_rating': '3.5', 'review_count': '6'}, {'gmap_id': 'gmap_43', 'average_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_42', 'average_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'average_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_33', 'average_rating': '2.125', 'review_count': '8'}, {'gmap_id': 'gmap_71', 'average_rating': '2.0625', 'review_count': '16'}, {'gmap_id': 'gmap_60', 'average_rating': '1.8235294117647058', 'review_count': '17'}, {'gmap_id': 'gmap_55', 'average_rating': '1.0', 'review_count': '3'}, {'gmap_id': 'gmap_23', 'average_rating': '1.0', 'review_count': '8'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
