code = """import pandas as pd
import json
import ast

# Load data
# var_function-call-3278323918064756835 contains businesses
# var_function-call-3278323918064757860 contains reviews

with open(locals()['var_function-call-3278323918064756835'], 'r') as f:
    businesses = json.load(f)

with open(locals()['var_function-call-3278323918064757860'], 'r') as f:
    reviews = json.load(f)

# Process reviews
df_reviews = pd.DataFrame(reviews)
# Ensure rating is numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')
avg_ratings = df_reviews.groupby('gmap_id')['rating'].mean().reset_index()

# Process businesses
relevant_businesses = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def is_open_after_6pm(time_str):
    if not time_str or time_str == 'Closed':
        return False
    if '24 hours' in time_str:
        return True
    
    # Format "6:30AM–6PM" or similar
    try:
        # Split by en-dash or hyphen
        if '\u2013' in time_str:
            parts = time_str.split('\u2013')
        elif '-' in time_str:
            parts = time_str.split('-')
        else:
            return False
            
        if len(parts) < 2:
            return False
            
        # We care about closing time (last part)
        close_str = parts[-1].strip()
        
        # Normalize
        close_str_upper = close_str.upper()
        is_pm = 'PM' in close_str_upper
        is_am = 'AM' in close_str_upper
        
        # Remove AM/PM
        time_clean = close_str_upper.replace('PM', '').replace('AM', '').strip()
        
        if ':' in time_clean:
            h, m = map(int, time_clean.split(':'))
        else:
            h = int(time_clean)
            m = 0
            
        # Convert to 24h
        # 12AM -> 0, 1AM -> 1, ... 11AM -> 11
        # 12PM -> 12, 1PM -> 13, ... 11PM -> 23
        if is_pm:
            if h != 12:
                h += 12
        elif is_am:
            if h == 12:
                h = 0
        # If neither AM nor PM, assume 24h? Unlikely in this dataset, usually strictly formatted.
        # If no AM/PM, it might be parsing error or raw number.
        # But looking at sample: "6PM", "5PM".
        
        # Logic for "after 6 PM" (18:00)
        # Strictly after 18:00
        
        # Check special overnight cases (00:00 to say 10:00)
        if 0 <= h < 10:
            return True
            
        # Check evening cases
        if h > 18:
            return True
        if h == 18 and m > 0:
            return True
            
        return False
    except Exception as e:
        # print(f"Error parsing {time_str}: {e}")
        return False

for b in businesses:
    hours_str = b.get('hours')
    if not hours_str or hours_str == 'None':
        continue
    
    try:
        # Parse list string
        # Sample: [['Thursday', '6:30AM–6PM'], ...]
        if isinstance(hours_str, str):
            hours_list = ast.literal_eval(hours_str)
        else:
            hours_list = hours_str
            
        open_late = False
        if isinstance(hours_list, list):
            for day_info in hours_list:
                if len(day_info) == 2:
                    day, time_range = day_info
                    if day in weekdays:
                        if is_open_after_6pm(time_range):
                            open_late = True
                            break
        
        if open_late:
            relevant_businesses.append(b)
    except Exception as e:
        # print(f"Error processing business {b.get('name')}: {e}")
        pass

df_bus = pd.DataFrame(relevant_businesses)

if not df_bus.empty:
    merged = pd.merge(df_bus, avg_ratings, on='gmap_id')
    # Sort by rating desc, then maybe name
    top5 = merged.sort_values(by='rating', ascending=False).head(5)
    result = top5[['name', 'hours', 'rating']].to_dict(orient='records')
else:
    result = []

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17610577654058034559': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_function-call-15296843030061385698': [{'count': '79'}], 'var_function-call-15296843030061385129': [{'COUNT(*)': '2000'}], 'var_function-call-3278323918064756835': 'file_storage/function-call-3278323918064756835.json', 'var_function-call-3278323918064757860': 'file_storage/function-call-3278323918064757860.json'}

exec(code, env_args)
