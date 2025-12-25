code = """import pandas as pd
import json
import ast

# Read file paths from local variables
business_file = locals()['var_function-call-10837374279726124640']
review_file = locals()['var_function-call-10837374279726123413']

with open(business_file, 'r') as f:
    businesses = json.load(f)

with open(review_file, 'r') as f:
    reviews = json.load(f)

df_biz = pd.DataFrame(businesses)
df_rev = pd.DataFrame(reviews)

# Convert rating to numeric
df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')

# Calculate average rating
avg_ratings = df_rev.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.columns = ['gmap_id', 'avg_rating']

# Function to parse time and check condition
def check_hours(hours_data):
    if hours_data is None or hours_data == 'None':
        return False
    
    try:
        if isinstance(hours_data, str):
            hours_list = ast.literal_eval(hours_data)
        else:
            hours_list = hours_data
            
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_info in hours_list:
            day = day_info[0]
            time_range = day_info[1]
            
            if day in weekdays:
                if 'Open 24 hours' in time_range:
                    return True
                if 'Closed' in time_range:
                    continue
                
                # Split time range
                # Use \u2013 for en dash or '-'
                if '\u2013' in time_range:
                    parts = time_range.split('\u2013')
                elif '-' in time_range:
                    parts = time_range.split('-')
                else:
                    continue
                
                if len(parts) < 2:
                    continue
                    
                close_time_str = parts[1].strip()
                
                is_pm = 'PM' in close_time_str
                is_am = 'AM' in close_time_str
                
                time_val = close_time_str.replace('PM', '').replace('AM', '').strip()
                if ':' in time_val:
                    h, m = map(int, time_val.split(':'))
                else:
                    h = int(time_val)
                    m = 0
                
                if is_pm:
                    if h != 12:
                        h += 12
                    # Check > 18:00
                    if h > 18 or (h == 18 and m > 0):
                        return True
                        
                elif is_am:
                    if h == 12: # 12 AM
                        return True
                    if h < 12:
                        if h <= 5: # Closing late night/early morning
                            return True
                    
    except Exception as e:
        return False
        
    return False

# Filter businesses
qualified_indices = []
for idx, row in df_biz.iterrows():
    if check_hours(row['hours']):
        qualified_indices.append(idx)

df_qualified = df_biz.loc[qualified_indices].copy()

# Merge with ratings
df_final = pd.merge(df_qualified, avg_ratings, on='gmap_id', how='left')

# Drop NaN ratings
df_final = df_final.dropna(subset=['avg_rating'])

# Sort by avg_rating desc, then by name (for stability)
df_final = df_final.sort_values(by=['avg_rating', 'name'], ascending=[False, True])

# Select columns
result_df = df_final[['name', 'hours', 'avg_rating']].head(5)

# Format output
result_list = result_df.to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-5790247279488936763': ['business_description'], 'var_function-call-5790247279488934468': ['review'], 'var_function-call-7652929681192300109': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-7652929681192299332': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}], 'var_function-call-13905431827856989603': [{'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}], 'var_function-call-13805068938795481147': [{'count': '79'}], 'var_function-call-13805068938795480982': [{'COUNT(*)': '2000'}], 'var_function-call-10837374279726124640': 'file_storage/function-call-10837374279726124640.json', 'var_function-call-10837374279726123413': 'file_storage/function-call-10837374279726123413.json'}

exec(code, env_args)
