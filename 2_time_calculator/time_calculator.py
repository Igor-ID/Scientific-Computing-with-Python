def add_time(start, duration, starting_day=None):
    l_start = start.split()
    apm = l_start[1]
    temp_hm = l_start[0].split(':')
    hours_start = temp_hm[0]
    minutes_start = temp_hm[1]
    l_duration = duration.split(':')
    hours_duration = l_duration[0]
    minutes_duration = l_duration[1]
    minutes_result = int(minutes_start) + int(minutes_duration)
    i = 0
    if minutes_result >= 60:
        i = 1
        minutes_result = minutes_result - 60

    if apm == 'PM':
        hours_start = int(hours_start) + 12 + i
    else:
        hours_start = int(hours_start) + i

    hours_result = hours_start + int(hours_duration)

    if hours_result >= 24:
        n_days = hours_result // 24
        display_hours = hours_result % 24
        if display_hours == 0:
            display_hours = 12
    else:
        n_days = 0
        display_hours = hours_result

    final_day_value = None
    if starting_day is not None:
        starting_day_key = None
        week = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
        for k, v in week.items():
            if v.lower() == starting_day.lower():
                starting_day_key = k
        final_day = n_days + starting_day_key
        if final_day > 7:
            final_day_key = final_day % 7
        else:
            final_day_key = final_day
        final_day_value = week[final_day_key]

    if n_days == 0 and starting_day is None:
        if display_hours > 12:
            new_time = ''.join(str(display_hours - 12) + ':' + str(minutes_result).zfill(2) + ' PM')
            return new_time
        elif display_hours == 12:
            new_time = ''.join(str(display_hours) + ':' + str(minutes_result).zfill(2) + ' PM')
            return new_time
        else:
            new_time = ''.join(str(display_hours) + ':' + str(minutes_result).zfill(2) + ' AM')
            return new_time

    elif n_days == 1 and starting_day is None:
        if display_hours > 12:
            new_time = ''.join(str(display_hours - 12) + ':' + str(minutes_result).zfill(2) + ' PM' + ' (next day)')
            return new_time
        else:
            new_time = ''.join(str(display_hours) + ':' + str(minutes_result).zfill(2) + ' AM' + ' (next day)')
            return new_time

    elif n_days == 0 and starting_day is not None:
        if display_hours > 12:
            new_time = ''.join(str(display_hours - 12) + ':' + str(minutes_result).zfill(2) + ' PM, ' + final_day_value)
            return new_time
        elif display_hours == 12:
            new_time = ''.join(str(display_hours) + ':' + str(minutes_result).zfill(2) + ' PM, ' + final_day_value)
            return new_time
        else:
            new_time = ''.join(str(display_hours) + ':' + str(minutes_result).zfill(2) + ' AM, ' + final_day_value)
            return new_time

    elif n_days == 1 and starting_day is not None:
        if display_hours > 12:
            new_time = ''.join(str(display_hours - 12) + ':' + str(minutes_result).zfill(2) + ' PM, ' +
                               final_day_value + ' (next day)')
            return new_time
        else:
            new_time = ''.join(str(display_hours) + ':' + str(minutes_result).zfill(2) + ' AM, ' +
                               final_day_value + ' (next day)')
            return new_time

    elif n_days > 1 and starting_day is None:
        days_str = f' ({n_days} days later)'
        if display_hours > 12:
            new_time = ''.join(str(display_hours - 12) + ':' + str(minutes_result).zfill(2) + ' PM' + days_str)
            return new_time
        else:
            new_time = ''.join(str(display_hours) + ':' + str(minutes_result).zfill(2) + ' AM' + days_str)
            return new_time

    elif n_days > 1 and starting_day is not None:
        days_str = f' ({n_days} days later)'
        if display_hours > 12:
            new_time = ''.join(str(display_hours - 12) + ':' + str(minutes_result).zfill(2) + ' PM, ' +
                               final_day_value + days_str)
            return new_time
        else:
            new_time = ''.join(str(display_hours) + ':' + str(minutes_result).zfill(2) + ' AM, ' +
                               final_day_value + days_str)
            return new_time