code = """import pandas as pd
import json

def is_open_after_6pm_weekday(hours_str):
    if hours_str is None or hours_str == "None":
        return False
    try:
        hours_list = json.loads(hours_str)
    except json.JSONDecodeError:
        return False

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for day_hours in hours_list:
        day = day_hours[0]
        time_range = day_hours[1]
        if day in weekdays:
            if "Closed" in time_range or "Open 24 hours" in time_range:
                if "Open 24 hours" in time_range:
                    return True
                continue

            try:
                # Handle cases like "3-8PM" or "11AM-9:30PM"
                if "\u2013" in time_range: # unicode for en-dash
                    start_time_str, end_time_str = time_range.split("\u2013")
                elif "-" in time_range:
                    start_time_str, end_time_str = time_range.split("-")
                else:
                    continue

                # Function to convert time string to 24-hour format
                def convert_to_24hr(time_str):
                    time_str = time_str.strip().upper()
                    if "AM" in time_str:
                        t = int(time_str.replace("AM", "").split(":")[0])
                        if t == 12: # 12 AM is 00:00
                            return 0
                        return t
                    elif "PM" in time_str:
                        t = int(time_str.replace("PM", "").split(":")[0])
                        if t == 12: # 12 PM is 12:00
                            return 12
                        return t + 12
                    else: # Handle cases like "6:30" without AM/PM, assume 24-hr format if no AM/PM
                         parts = time_str.split(":")
                         if len(parts) == 2:
                             return int(parts[0])
                         return -1 # Invalid time

                end_hour = convert_to_24hr(end_time_str)

                if end_hour > 18: # 6 PM
                    return True
            except (ValueError, IndexError):
                continue
    return False

# Load the business data from the file
with open(locals()['var_function-call-5424780551342559286'], 'r') as f:
    business_data = json.load(f)

df_business = pd.DataFrame(business_data)

# Filter businesses that are open after 6 PM on at least one weekday
df_filtered_business = df_business[df_business['hours'].apply(is_open_after_6pm_weekday)]

# Select relevant columns
result = df_filtered_business[['gmap_id', 'name', 'hours']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-2775728392946956731': ['business_description'], 'var_function-call-717792320089583401': [{'hours': 'None'}], 'var_function-call-5424780551342559286': 'file_storage/function-call-5424780551342559286.json'}

exec(code, env_args)
