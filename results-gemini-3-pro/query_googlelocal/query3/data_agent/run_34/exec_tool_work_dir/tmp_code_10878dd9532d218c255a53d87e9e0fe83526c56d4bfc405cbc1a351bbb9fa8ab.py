code = """import json
import pandas as pd
import re

# Access file paths from variables
file_path_businesses = locals()['var_function-call-3565738323903944674']
file_path_reviews = locals()['var_function-call-3806619213573453234']

# Load data
with open(file_path_businesses, 'r') as f:
    businesses = json.load(f)

with open(file_path_reviews, 'r') as f:
    reviews = json.load(f)

# Calculate average ratings
df_reviews = pd.DataFrame(reviews)
# Ensure rating is numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])
avg_ratings = df_reviews.groupby('gmap_id')['rating'].mean().to_dict()

# Helper function to parse time
def parse_time_to_hours(time_str):
    time_str = time_str.strip()
    if not time_str: return 0.0
    
    is_pm = 'PM' in time_str
    is_am = 'AM' in time_str
    
    t = time_str.replace('AM', '').replace('PM', '').strip()
    
    if ':' in t:
        h, m = map(int, t.split(':'))
    else:
        h = int(t)
        m = 0
    
    if is_pm and h != 12:
        h += 12
    if is_am and h == 12:
        h = 0 
        
    val = h + m/60.0
    return val

def is_open_after_6pm(hours_data):
    if not hours_data or hours_data == 'None':
        return False
    
    try:
        if isinstance(hours_data, str):
            try:
                schedule = json.loads(hours_data)
            except:
                return False
        else:
            schedule = hours_data
            
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_entry in schedule:
            day = day_entry[0]
            time_range = day_entry[1]
            
            if day in weekdays:
                if 'Open 24 hours' in time_range:
                    return True
                if 'Closed' in time_range:
                    continue
                
                parts = re.split(r'\u2013|-', time_range)
                if len(parts) == 2:
                    end_time_str = parts[1]
                    start_time_str = parts[0]
                    
                    end_val = parse_time_to_hours(end_time_str)
                    start_val = parse_time_to_hours(start_time_str)
                    
                    # Logic:
                    # If crosses midnight (Start > End), it is open late.
                    if start_val > end_val:
                        return True
                    else:
                        # Same day. Check if End > 18.0
                        if end_val > 18.0:
                            return True
                            
    except Exception as e:
        pass
        
    return False

filtered_businesses = []
for b in businesses:
    if is_open_after_6pm(b['hours']):
        b_id = b['gmap_id']
        if b_id in avg_ratings:
            b['average_rating'] = avg_ratings[b_id]
            filtered_businesses.append(b)

# Rank by rating desc
filtered_businesses.sort(key=lambda x: x['average_rating'], reverse=True)

# Take top 5
top_5 = filtered_businesses[:5]

# Format output
result = []
for b in top_5:
    result.append({
        "name": b['name'],
        "hours": b['hours'],
        "average_rating": b['average_rating']
    })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4970281995441041141': ['business_description'], 'var_function-call-4970281995441039434': ['review'], 'var_function-call-569539876123265185': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_function-call-3945752392740038203': [{'count': '79'}], 'var_function-call-2961703696066761256': [{'COUNT(*)': '2000'}], 'var_function-call-3565738323903944674': 'file_storage/function-call-3565738323903944674.json', 'var_function-call-3806619213573453234': 'file_storage/function-call-3806619213573453234.json'}

exec(code, env_args)
