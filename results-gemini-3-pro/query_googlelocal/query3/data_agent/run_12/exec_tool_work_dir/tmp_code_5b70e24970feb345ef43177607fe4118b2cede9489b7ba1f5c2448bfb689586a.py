code = """import json
import pandas as pd
import datetime

# Load data
# Use locals() to access variables with hyphens
businesses_path = locals()['var_function-call-5580388133865470968']
reviews_path = locals()['var_function-call-9361860428015302']

with open(businesses_path, 'r') as f:
    businesses = json.load(f)
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

# Convert to DataFrame
df_biz = pd.DataFrame(businesses)
df_rev = pd.DataFrame(reviews)

# Calculate average rating
# Ensure rating is numeric
df_rev['rating'] = pd.to_numeric(df_rev['rating'])
# Group by gmap_id
rating_stats = df_rev.groupby('gmap_id')['rating'].agg(['mean', 'count']).reset_index()
rating_stats.rename(columns={'mean': 'avg_rating', 'count': 'review_count'}, inplace=True)

# Parse hours
# Weekdays set
weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}

def parse_time_to_minutes(time_str):
    # Formats: "6PM", "6:30PM", "12AM", "12:30AM"
    # Returns minutes from start of day.
    # Handle AM/PM
    time_str = time_str.strip().upper()
    if time_str == '12AM': return 0 
    
    is_pm = 'PM' in time_str
    is_am = 'AM' in time_str
    
    # Remove AM/PM
    t = time_str.replace('PM', '').replace('AM', '').strip()
    
    if ':' in t:
        h, m = map(int, t.split(':'))
    else:
        h = int(t)
        m = 0
    
    if is_pm and h != 12:
        h += 12
    if is_am and h == 12:
        h = 0
        
    return h * 60 + m

def is_open_after_6pm(hours_json_str):
    if not hours_json_str or hours_json_str == 'None':
        return False
    try:
        # Check if it's already a list (sometimes JSON load might handle it)
        # But here it's a string
        # Replace python None if any (though stored as string "None")
        if hours_json_str == "None": return False
        
        # Replace single quotes with double quotes for valid JSON
        # The sample showed double quotes, but just in case.
        # Actually, let's look at the sample: "[[\"Thursday\", ...]]"
        # It's valid JSON.
        hours_list = json.loads(hours_json_str)
    except:
        return False
            
    # hours_list is list of [Day, TimeRange]
    # e.g. ["Thursday", "6:30AM–6PM"]
    
    for day, time_range in hours_list:
        if day in weekdays:
            if time_range == "Closed":
                continue
            if time_range == "Open 24 hours":
                return True
            
            # Split time range
            # Separators: \u2013 (en dash), -
            sep = None
            if '\u2013' in time_range: sep = '\u2013'
            elif '-' in time_range: sep = '-'
            
            if sep:
                parts = time_range.split(sep)
                if len(parts) == 2:
                    start_str, end_str = parts
                    end_str = end_str.strip()
                    
                    try:
                        end_minutes = parse_time_to_minutes(end_str)
                        
                        is_am = 'AM' in end_str.upper()
                        is_pm = 'PM' in end_str.upper()
                        
                        # 6PM = 1080 min.
                        if is_pm:
                            if end_minutes > 1080: # Strictly > 18:00
                                return True
                        elif is_am:
                            # AM closing time.
                            # If it's 12AM (0 min) or later, it means it stays open late (after midnight).
                            # If it's early morning like 11AM, it closes before 6PM.
                            
                            # Heuristic: if start time is PM or early AM, and end time is AM (smaller than start or small value), it crossed midnight.
                            start_minutes = parse_time_to_minutes(start_str)
                            
                            if end_minutes < start_minutes:
                                return True # Crossed midnight
                            
                            # Special check for 12AM
                            if '12AM' in end_str.upper() or '12:00AM' in end_str.upper():
                                return True
                            
                            # Case: Open 1AM - 5AM (Night club?) -> Open after 6PM? No.
                            # Case: Open 5PM - 2AM -> Yes.
                            # Case: Open 5AM - 11AM -> No.
                            
                            # If start < end and both AM: 5AM - 11AM. No.
                    except:
                        pass
    return False

# Apply filter
eligible_gmap_ids = []

for index, row in df_biz.iterrows():
    if is_open_after_6pm(row['hours']):
        eligible_gmap_ids.append(row['gmap_id'])

# Filter df_biz
df_eligible = df_biz[df_biz['gmap_id'].isin(eligible_gmap_ids)].copy()

# Join with ratings
df_result = pd.merge(df_eligible, rating_stats, on='gmap_id', how='inner')

# Sort
# Primary: avg_rating (desc)
# Secondary: review_count (desc)
df_result.sort_values(by=['avg_rating', 'review_count'], ascending=[False, False], inplace=True)

# Top 5
top_5 = df_result.head(5)

# Format output
results = []
for index, row in top_5.iterrows():
    results.append({
        "name": row['name'],
        "hours": row['hours'],
        "avg_rating": row['avg_rating'],
        "review_count": int(row['review_count'])
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-9296450689531834642': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_function-call-1537564774235231612': [{'COUNT(*)': '2000'}], 'var_function-call-5258409667665638486': [{'count': '79'}], 'var_function-call-5580388133865470968': 'file_storage/function-call-5580388133865470968.json', 'var_function-call-9361860428015302': 'file_storage/function-call-9361860428015302.json'}

exec(code, env_args)
