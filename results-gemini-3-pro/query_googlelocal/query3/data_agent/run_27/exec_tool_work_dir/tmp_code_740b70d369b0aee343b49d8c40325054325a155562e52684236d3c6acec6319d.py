code = """import json
import pandas as pd
import ast

# Access variables from locals()
business_file_key = 'var_function-call-7899059165738772019'
reviews_file_key = 'var_function-call-13163981481845026653'

business_file_path = locals()[business_file_key]
reviews_file_path = locals()[reviews_file_key]

# Load data
with open(business_file_path, 'r') as f:
    businesses = json.load(f)

with open(reviews_file_path, 'r') as f:
    reviews = json.load(f)

# Convert reviews to DataFrame and calc avg rating
df_reviews = pd.DataFrame(reviews)
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])
avg_ratings = df_reviews.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.rename(columns={'rating': 'average_rating'}, inplace=True)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

filtered_list = []
for b in businesses:
    hours_raw = b.get('hours')
    if not hours_raw or hours_raw == 'None':
        continue
    
    # Parse hours
    try:
        hours_list = json.loads(hours_raw) if isinstance(hours_raw, str) else hours_raw
    except:
        try:
            hours_list = ast.literal_eval(hours_raw)
        except:
            continue
            
    is_open_late = False
    if isinstance(hours_list, list):
        for day_info in hours_list:
            if not isinstance(day_info, list) or len(day_info) != 2:
                continue
            
            day_name = day_info[0]
            time_range = day_info[1]
            
            if day_name in weekdays:
                if 'Open 24 hours' in time_range:
                    is_open_late = True
                    break
                
                if 'Closed' in time_range:
                    continue
                    
                # Split range
                parts = time_range.replace('\u2013', '-').split('-')
                if len(parts) < 2:
                    continue
                
                end_str = parts[1].strip() # e.g. "6PM", "9:30PM", "12AM"
                
                # Analyze end time
                # Check for PM > 6
                if 'PM' in end_str:
                    # Remove PM, split colon
                    t = end_str.replace('PM', '').strip()
                    if ':' in t:
                        h, m = map(int, t.split(':'))
                    else:
                        h = int(t)
                        m = 0
                    
                    # 12PM is noon.
                    if h != 12:
                        if h > 6 or (h == 6 and m > 0):
                            is_open_late = True
                            break
                
                # Check for AM (Midnight or early morning next day)
                elif 'AM' in end_str:
                    t = end_str.replace('AM', '').strip()
                    if ':' in t:
                        h, m = map(int, t.split(':'))
                    else:
                        h = int(t)
                        m = 0
                    
                    # 12AM is Midnight.
                    if h == 12: 
                        is_open_late = True
                        break
                    
                    # 1AM...5AM usually means late night open.
                    if h < 6:
                        is_open_late = True
                        break

    if is_open_late:
        filtered_list.append(b)

# Join with ratings
df_bus = pd.DataFrame(filtered_list)
if not df_bus.empty:
    merged = pd.merge(df_bus, avg_ratings, on='gmap_id', how='inner')
    # Sort
    merged.sort_values(by='average_rating', ascending=False, inplace=True)
    # Top 5
    top5 = merged.head(5)
    result = top5[['name', 'hours', 'average_rating']].to_dict(orient='records')
else:
    result = []

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3046160326493482668': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-7674235243375518328': [{'count': '79'}], 'var_function-call-3542570336395074807': [{'COUNT(*)': '2000'}], 'var_function-call-7899059165738772019': 'file_storage/function-call-7899059165738772019.json', 'var_function-call-13163981481845026653': 'file_storage/function-call-13163981481845026653.json'}

exec(code, env_args)
