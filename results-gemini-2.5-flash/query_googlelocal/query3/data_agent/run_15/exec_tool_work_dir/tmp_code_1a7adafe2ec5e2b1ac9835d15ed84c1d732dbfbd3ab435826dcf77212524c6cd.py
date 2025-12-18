code = """import pandas as pd
import json

business_data_path = locals()['var_function-call-10971755212049758279']
with open(business_data_path, 'r') as f:
    business_data = json.load(f)

df_business = pd.DataFrame(business_data)

def is_open_after_6pm_on_weekday(hours_str):
    if hours_str is None:
        return False
    try:
        hours_list = json.loads(hours_str)
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for day_schedule in hours_list:
            day = day_schedule[0]
            schedule = day_schedule[1]
            if day in weekdays and "Closed" not in schedule:
                if "Open 24 hours" in schedule:
                    return True
                parts = schedule.split('–')
                if len(parts) == 2:
                    end_time_str = parts[1].strip()
                    if "PM" in end_time_str:
                        time_val_str = end_time_str.replace("PM", "").replace("AM", "").strip()
                        if ":" in time_val_str:
                            hour_str = time_val_str.split(":")[0]
                        else:
                            hour_str = time_val_str
                        
                        try:
                            hour = int(hour_str)
                            if "AM" in end_time_str and hour == 12: # 12 AM is midnight, so it's technically open past 6 PM the previous day.
                                return True
                            elif "PM" in end_time_str and hour >= 6:
                                return True
                            elif "AM" in end_time_str and hour < 6:
                                # For cases like "3AM-2AM" which means it's open overnight
                                start_time_str = parts[0].strip()
                                start_hour_str = start_time_str.replace("PM", "").replace("AM", "").strip().split(":")[0]
                                if "PM" in start_time_str or int(start_hour_str) < hour: # if it starts in PM or the start hour is before the end hour (e.g. 10PM-2AM)
                                    return True
                        except ValueError:
                            pass
    except json.JSONDecodeError:
        pass
    return False

df_business['open_after_6pm_weekday'] = df_business['hours'].apply(is_open_after_6pm_on_weekday)
filtered_businesses = df_business[df_business['open_after_6pm_weekday']]
result = filtered_businesses[['gmap_id', 'name', 'hours']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-10971755212049758279': 'file_storage/function-call-10971755212049758279.json'}

exec(code, env_args)
