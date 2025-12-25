code = """import json
import pandas as pd

business_hours_data = pd.read_json(locals()['var_function-call-11888193672252761976'])

def is_open_after_6pm_weekday(hours_str):
    if hours_str is None or pd.isna(hours_str):
        return False
    try:
        hours_list = json.loads(hours_str)
        for day, time_range in hours_list:
            day = day.lower()
            if day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
                if '24 hours' in time_range.lower():
                    return True
                if '–' in time_range:
                    end_time_str = time_range.split('–')[1].strip()
                    if 'PM' in end_time_str or 'AM' in end_time_str:
                        # Handle cases like "12PM" or "12AM"
                        if end_time_str == '12AM':
                            end_hour = 0
                        elif end_time_str == '12PM':
                            end_hour = 12
                        else:
                            end_hour = int(end_time_str.replace('AM', '').replace('PM', '').split(':')[0])
                            if 'PM' in end_time_str and end_hour != 12:
                                end_hour += 12
                        
                        if end_hour > 18:  # 18:00 is 6 PM
                            return True
    except json.JSONDecodeError:
        pass
    return False

open_after_6pm_businesses = business_hours_data[business_hours_data['hours'].apply(is_open_after_6pm_weekday)]
result = open_after_6pm_businesses.to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-12578815100984117986': ['business_description'], 'var_function-call-11888193672252761976': 'file_storage/function-call-11888193672252761976.json'}

exec(code, env_args)
