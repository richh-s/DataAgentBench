code = """import json
import pandas as pd
import datetime

# Load data
with open(locals()['var_function-call-1044313792227080845'], 'r') as f:
    businesses = json.load(f)
with open(locals()['var_function-call-1044313792227079046'], 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_biz = pd.DataFrame(businesses)
df_rev = pd.DataFrame(reviews)

# Aggregate ratings
df_rev['rating'] = pd.to_numeric(df_rev['rating'])
avg_ratings = df_rev.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.columns = ['gmap_id', 'average_rating']

# Filter businesses
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def parse_time(t_str):
    # Formats: 6:30AM, 6PM, 12PM, 12AM, 9:30PM, 11AM
    # Returns integer minutes from midnight
    if not t_str: return None
    is_pm = 'PM' in t_str
    is_am = 'AM' in t_str
    t_str = t_str.replace('PM', '').replace('AM', '')
    parts = t_str.split(':')
    h = int(parts[0])
    m = int(parts[1]) if len(parts) > 1 else 0
    
    if is_pm and h != 12:
        h += 12
    if is_am and h == 12:
        h = 0
    
    return h * 60 + m

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    try:
        # hours_str is a string representation of a list
        # e.g. "[['Thursday', '6:30AM–6PM'], ...]"
        # We need to parse this string into a list
        hours_list = json.loads(hours_str.replace("'", '"')) # Replace single quotes if any
        
        for day, time_range in hours_list:
            if day in weekdays:
                if time_range == 'Open 24 hours':
                    return True
                if time_range == 'Closed':
                    continue
                
                # Split range: "6:30AM–6PM" or "11AM–9:30PM"
                # The separator can be different dashes.
                # Common ones: \u2013 (en dash), - (hyphen)
                # In the sample: \u2013
                sep = '\u2013'
                if sep not in time_range:
                    sep = '-'
                if sep not in time_range:
                     # Maybe only open time? Unlikely based on sample.
                     continue
                
                start_str, end_str = time_range.split(sep)
                end_minutes = parse_time(end_str.strip())
                
                # 6:00 PM is 18 * 60 = 1080 minutes
                # If end_minutes > 1080, it's open after 6PM.
                # Also handle cases spanning midnight (e.g. closes at 2AM)
                # If closes at 2AM, end_minutes is 120. 
                # Start time needs to be checked to confirm it spans midnight?
                # Usually if end time is small (morning) and start is morning/afternoon, it spans.
                # But simpler heuristic: 
                # If end_minutes > 1080: Open after 6PM.
                # If end_minutes < start_minutes: Spans midnight, so definitely open after 6PM (unless it opens after 6PM and closes in morning, still open after 6PM).
                
                start_minutes = parse_time(start_str.strip())
                
                if end_minutes > 1080: # Closes after 18:00
                    return True
                if end_minutes < start_minutes: # Spans midnight (e.g. 11AM - 2AM)
                    return True
                    
        return False
    except Exception as e:
        # print(f"Error parsing {hours_str}: {e}")
        return False

# Apply filter
filtered_biz = []
for index, row in df_biz.iterrows():
    if is_open_after_6pm(row['hours']):
        filtered_biz.append(row)

df_filtered = pd.DataFrame(filtered_biz)

# Merge
if not df_filtered.empty:
    merged = pd.merge(df_filtered, avg_ratings, on='gmap_id', how='left')
    
    # Sort
    # High rating first.
    merged = merged.sort_values(by=['average_rating'], ascending=False)
    
    # Select columns
    result_df = merged[['name', 'hours', 'average_rating']].head(5)
    
    # Convert result to dict
    final_result = result_df.to_dict(orient='records')
else:
    final_result = []

print("__RESULT__:")
print(json.dumps(final_result))"""

env_args = {'var_function-call-4820621851526419643': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_function-call-6624333439626800419': [{'count': '79'}], 'var_function-call-6624333439626800800': [{'COUNT(*)': '2000'}], 'var_function-call-1044313792227080845': 'file_storage/function-call-1044313792227080845.json', 'var_function-call-1044313792227079046': 'file_storage/function-call-1044313792227079046.json'}

exec(code, env_args)
