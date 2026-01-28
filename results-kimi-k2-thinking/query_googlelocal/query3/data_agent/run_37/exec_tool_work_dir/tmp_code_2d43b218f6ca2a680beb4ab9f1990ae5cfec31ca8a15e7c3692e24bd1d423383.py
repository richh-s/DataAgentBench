code = """import json
import pandas as pd
import os

# Find all stored file paths by scanning local variables
business_data = None
review_data = None
business_file_path = None
review_file_path = None

# Get all local variables
all_vars = dict(locals())

# List potential variable names that might contain file paths
print("Searching for data files...")

# Check for any variables that might be file paths
for var_name, var_value in all_vars.items():
    if isinstance(var_value, str) and ('/tmp/' in var_value or '.json' in var_value):
        print(f"Found potential file path: {var_name}")
        try:
            with open(var_value, 'r') as f:
                data = json.load(f)
            print(f"  Successfully loaded {len(data)} records from {var_name}")
            
            # Try to identify if this is business or review data
            if any('gmap_id' in str(item) and 'hours' in str(item).lower() for item in data[:3]):
                business_data = data
                business_file_path = var_value
                print(f"  Identified as BUSINESS data")
            elif any('gmap_id' in str(item) and 'rating' in str(item).lower() for item in data[:3]):
                review_data = data
                review_file_path = var_value
                print(f"  Identified as REVIEW data")
        except:
            print(f"  Could not load {var_name}")
            continue

# Check if we found both datasets
if business_data and review_data:
    print(f"\nSuccessfully loaded:")
    print(f"  - {len(business_data)} business records")
    print(f"  - {len(review_data)} review records")
    
    # Continue with analysis
    df_business = pd.DataFrame(business_data)
    df_reviews = pd.DataFrame(review_data)
    
    # Calculate average ratings
    df_avg_rating = df_reviews.groupby('gmap_id')['rating'].agg(['mean', 'count']).reset_index()
    df_avg_rating.columns = ['gmap_id', 'avg_rating', 'review_count']
    
    # Filter businesses with at least 5 reviews
    df_avg_rating = df_avg_rating[df_avg_rating['review_count'] >= 5]
    
    print(f"  - {len(df_avg_rating)} businesses with >=5 reviews")
    
    # Parse hours to find businesses open after 6PM on weekdays
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    def is_open_after_6pm(hours_str):
        """Check if business is open after 6PM on any weekday"""
        if not hours_str or hours_str == 'None':
            return False
        
        try:
            hours_list = eval(hours_str)
            
            for day_schedule in hours_list:
                day = day_schedule[0]
                hours = day_schedule[1]
                
                if day in weekdays:
                    if hours == 'Open 24 hours':
                        return True
                    
                    if hours == 'Closed':
                        continue
                    
                    time_parts = hours.replace('\u2013', '-').split('-')
                    if len(time_parts) != 2:
                        continue
                    
                    end_time = time_parts[1].strip()
                    
                    if 'PM' in end_time:
                        end_hour_str = end_time.replace('PM', '').strip()
                        end_hour = int(end_hour_str.split(':')[0])
                        if end_hour != 12:
                            end_hour += 12
                        
                        if end_hour > 18:
                            return True
                    elif 'AM' in end_time:
                        end_hour_str = end_time.replace('AM', '').strip()
                        end_hour = int(end_hour_str.split(':')[0])
                        if end_hour < 6:
                            return True
            
            return False
        except:
            return False
    
    # Apply function
    df_business['open_after_6pm'] = df_business['hours'].apply(is_open_after_6pm)
    
    # Filter businesses that are open after 6PM
    df_filtered = df_business[df_business['open_after_6pm'] == True]
    print(f"  - {len(df_filtered)} businesses open after 6PM on weekdays")
    
    # Merge with ratings
    df_result = df_filtered.merge(df_avg_rating, on='gmap_id', how='inner')
    print(f"  - {len(df_result)} businesses meeting all criteria")
    
    # Sort by average rating and get top 5
    df_top5 = df_result.sort_values('avg_rating', ascending=False).head(5)
    
    # Prepare final result
    final_result = []
    for _, row in df_top5.iterrows():
        final_result.append({
            'name': row['name'],
            'operating_hours': row['hours'],
            'average_rating': round(float(row['avg_rating']), 2),
            'review_count': int(row['review_count'])
        })
    
    print(f"\nFound top 5 businesses:")
    for i, biz in enumerate(final_result, 1):
        print(f"{i}. {biz['name']} - Rating: {biz['average_rating']} ({biz['review_count']} reviews)")
    
    print("\n__RESULT__:")
    print(json.dumps(final_result, indent=2))
else:
    print("ERROR: Could not find both business and review data")
    print("Available variables:", list(all_vars.keys()))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}, {'name': 'Vons Chicken', 'gmap_id': 'gmap_74', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Black Tie Ski Rental Delivery of Mammoth', 'gmap_id': 'gmap_17', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Dunn-Edwards Paints', 'gmap_id': 'gmap_29', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'hours': 'None', 'state': 'None'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'status': 'success', 'business_count': 66, 'review_count': 2000}, 'var_functions.execute_python:20': {'status': 'loaded', 'business_count': 66, 'review_count': 2000}, 'var_functions.execute_python:22': {'status': 'success', 'business_count': 66, 'review_count': 2000}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}, {'gmap_id': 'gmap_44', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}]}

exec(code, env_args)
