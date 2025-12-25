code = """import json
import pandas as pd

business_data_path = locals()['var_function-call-17531646216573112097']
with open(business_data_path, 'r') as f:
    business_data = json.load(f)

df_business = pd.DataFrame(business_data)

def is_open_after_6pm_weekday(hours_str):
    if hours_str is None:
        return False
    try:
        hours_list = json.loads(hours_str)
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for day_schedule in hours_list:
            day = day_schedule[0]
            if day in weekdays:
                time_range = day_schedule[1]
                if "Open 24 hours" in time_range:
                    return True
                if "–" in time_range:
                    end_time_str = time_range.split('–')[1].strip()
                    if "PM" in end_time_str:
                        end_hour = int(end_time_str.split('PM')[0].split(':')[-1])
                        if end_hour == 12: # 12PM is noon, 12AM is midnight
                            end_hour = 0
                        if end_hour >= 6 or "Open 24 hours" in time_range:
                            return True
                    elif "AM" in end_time_str:
                        end_hour = int(end_time_str.split('AM')[0].split(':')[-1])
                        if end_hour >= 6 and end_hour < 12: # this covers cases like 6:30AM but not 12AM
                            pass
                        else:
                            return True # If it is after 12AM means it is open after 6pm previous day
    except json.JSONDecodeError:
        return False
    return False

df_business['open_after_6pm_weekday'] = df_business['hours'].apply(is_open_after_6pm_weekday)
filtered_businesses = df_business[df_business['open_after_6pm_weekday'] == True]

print("__RESULT__:")
print(filtered_businesses.to_json(orient='records'))"""

env_args = {'var_function-call-17531646216573112097': 'file_storage/function-call-17531646216573112097.json'}

exec(code, env_args)
