code = """import json
import pandas as pd

business_data = pd.read_json(locals()['var_function-call-6212170818969054380'])

def parse_hours(hours_str):
    if hours_str is None or hours_str == "None":
        return []
    try:
        return json.loads(hours_str)
    except json.JSONDecodeError:
        return []

def is_open_after_6pm_on_weekday(hours_list):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for day_info in hours_list:
        if day_info[0] in weekdays:
            time_range = day_info[1]
            if "Open 24 hours" in time_range:
                return True
            if "Closed" in time_range:
                continue

            # Handle cases like "6:30AM–6PM" or "3–8PM"
            try:
                if '–' in time_range:
                    end_time_str = time_range.split('–')[1].strip()
                    if 'AM' in end_time_str:
                        hour = int(end_time_str.replace('AM', '').split(':')[0])
                        if hour < 6: # e.g. 5:30AM
                            continue
                        else: # e.g. 6AM
                            pass
                    elif 'PM' in end_time_str:
                        hour = int(end_time_str.replace('PM', '').split(':')[0])
                        if hour == 12: # 12PM
                            pass
                        elif hour >= 6: # 6PM or later
                            return True
                    else: # no AM/PM, assuming 24-hour format or error
                        if ':' in end_time_str:
                            hour = int(end_time_str.split(':')[0])
                        else:
                            hour = int(end_time_str) # for "8" in "3-8"
                        if hour >= 18:
                            return True
            except ValueError:
                continue
    return False

business_data['parsed_hours'] = business_data['hours'].apply(parse_hours)
open_after_6pm_businesses = business_data[business_data['parsed_hours'].apply(is_open_after_6pm_on_weekday)]

result = open_after_6pm_businesses[['gmap_id', 'name', 'hours']].to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-6305945186231174028': ['review'], 'var_function-call-6305945186231174955': ['business_description'], 'var_function-call-6212170818969054380': 'file_storage/function-call-6212170818969054380.json'}

exec(code, env_args)
