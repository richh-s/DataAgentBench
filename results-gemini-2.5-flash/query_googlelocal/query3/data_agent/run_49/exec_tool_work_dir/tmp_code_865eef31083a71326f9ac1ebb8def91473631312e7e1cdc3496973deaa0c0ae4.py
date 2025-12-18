code = """import pandas as pd
import json

business_data = pd.read_json(locals()['var_function-call-2643583013853214511'])

def is_open_after_6pm_on_weekday(hours_str):
    if hours_str is None:
        return False
    try:
        hours_list = json.loads(hours_str)
        for day, time_range in hours_list:
            if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
                if 'Open 24 hours' in time_range:
                    return True
                if '\u2013' in time_range:
                    start_time_str, end_time_str = time_range.split('\u2013')
                    end_time_str = end_time_str.replace('AM', '').replace('PM', '') # Remove AM/PM for easier parsing
                    if ':' in end_time_str:
                        end_hour = int(end_time_str.split(':')[0])
                        end_minute = int(end_time_str.split(':')[1])
                    else:
                        end_hour = int(end_time_str)
                        end_minute = 0
                    
                    # Adjust for PM hours
                    if 'PM' in time_range and end_hour < 12:
                        end_hour += 12
                    # Handle 12 AM (midnight) as 0, 12 PM (noon) as 12
                    if 'AM' in time_range and end_hour == 12:
                        end_hour = 0

                    if end_hour > 18 or (end_hour == 18 and end_minute > 0):
                        return True
    except json.JSONDecodeError:
        pass
    return False

business_data['open_after_6pm_weekday'] = business_data['hours'].apply(is_open_after_6pm_on_weekday)

filtered_businesses = business_data[business_data['open_after_6pm_weekday']][['gmap_id', 'name', 'hours']]

print('__RESULT__:')
print(filtered_businesses.to_json(orient='records'))"""

env_args = {'var_function-call-2643583013853214511': 'file_storage/function-call-2643583013853214511.json'}

exec(code, env_args)
