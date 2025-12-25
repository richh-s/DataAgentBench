code = """import pandas as pd
import json

business_data_path = locals()['var_function-call-16629413390838551060']
review_data_path = locals()['var_function-call-16629413390838551663']

with open(business_data_path, 'r') as f:
    business_data = json.load(f)

with open(review_data_path, 'r') as f:
    review_data = json.load(f)

business_df = pd.DataFrame(business_data)
review_df = pd.DataFrame(review_data)

# Convert 'rating' to numeric in review_df
review_df['rating'] = pd.to_numeric(review_df['rating'])

# Calculate average rating for each business
avg_ratings = review_df.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.rename(columns={'rating': 'average_rating'}, inplace=True)

# Function to check if a business is open after 6 PM on any weekday
def is_open_after_6pm_weekday(hours_str):
    if hours_str == 'None':
        return False
    try:
        hours_list = json.loads(hours_str)
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for day_hours in hours_list:
            day = day_hours[0]
            time_range = day_hours[1]
            if day in weekdays and '–' in time_range:
                closing_time_str = time_range.split('–')[1]
                closing_time_str = closing_time_str.replace('AM', '').replace('PM', '')
                
                # Handle 'Open 24 hours' case
                if time_range == 'Open 24 hours':
                    return True

                # Parse closing time
                if 'PM' in day_hours[1] and '12' not in closing_time_str:
                    hour_part = int(closing_time_str.split(':')[0])
                    if hour_part < 12: # For 1-11 PM
                        closing_hour = hour_part + 12
                    else: # For 12 PM
                        closing_hour = hour_part
                else:
                    closing_hour = int(closing_time_str.split(':')[0])

                if closing_hour >= 18:  # 6 PM
                    return True
        return False
    except json.JSONDecodeError:
        return False
    except IndexError:
        return False

# Apply the function to filter businesses
business_df['open_after_6pm_weekday'] = business_df['hours'].apply(is_open_after_6pm_weekday)
filtered_businesses = business_df[business_df['open_after_6pm_weekday']]

# Merge with average ratings
merged_df = pd.merge(filtered_businesses, avg_ratings, on='gmap_id')

# Sort by average rating and get top 5
top_5_businesses = merged_df.sort_values(by='average_rating', ascending=False).head(5)

# Select and format the required columns
result = top_5_businesses[['name', 'hours', 'average_rating']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-3383325511704219588': ['review'], 'var_function-call-3383325511704217375': ['business_description'], 'var_function-call-16629413390838551060': 'file_storage/function-call-16629413390838551060.json', 'var_function-call-16629413390838551663': 'file_storage/function-call-16629413390838551663.json'}

exec(code, env_args)
