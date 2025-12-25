code = """import json
import pandas as pd

business_data_path = locals()['var_function-call-16727833252366307240']
with open(business_data_path, 'r') as f:
    business_data = json.load(f)

df_business = pd.DataFrame(business_data)

# Filter for businesses that are "Open" or "Open now"
df_business = df_business[df_business['state'].str.contains('Open', na=False)]

# Define weekdays
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def is_open_after_6pm_weekday(hours_str):
    if pd.isna(hours_str) or hours_str == "None":
        return False
    try:
        hours_list = json.loads(hours_str)
        for day, time_range in hours_list:
            if day in weekdays:
                if 'Open 24 hours' in time_range:
                    return True
                elif 'PM' in time_range:
                    parts = time_range.split('–')
                    if len(parts) == 2:
                        end_time_str = parts[1].strip()
                        if 'PM' in end_time_str:
                            end_hour_str = end_time_str.replace('PM', '').replace('AM', '').strip()
                            if ':' in end_hour_str:
                                hour, minute = map(int, end_hour_str.split(':'))
                            else:
                                hour = int(end_hour_str)
                                minute = 0
                            if hour < 12: # For 1-11 PM
                                hour += 12
                            if hour >= 18:  # 18:00 is 6 PM
                                return True
    except json.JSONDecodeError:
        pass
    return False

df_business['open_after_6pm_weekday'] = df_business['hours'].apply(is_open_after_6pm_weekday)
filtered_businesses = df_business[df_business['open_after_6pm_weekday']][['gmap_id', 'name', 'hours']]

print("__RESULT__:")
print(filtered_businesses.to_json(orient='records'))"""

env_args = {'var_function-call-16727833252366307240': 'file_storage/function-call-16727833252366307240.json'}

exec(code, env_args)
