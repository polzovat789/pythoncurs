n = 808
hours = (n // 60) % 24
minutes = n % 60
time_str = f"{hours:02d}{minutes:02d}"
total_sum = sum(int(digit) for digit in time_str)
print(total_sum)

experience = 10
threshold = 15
reward = 5
if (experience + reward) >= threshold:
    print(True)
else:
    print(False)

time = '00:00'
hours_t, minutes_t = time.split(':')
if int(hours_t) < 12:
    if int(hours_t) == 0:
        print(f"12:{minutes_t} a.m.")
    else:
        print(f"{int(hours_t)}:{minutes_t} a.m.")
elif int(hours_t) == 12:
    print(f"12:{minutes_t} p.m.")
else:
    print(f"{int(hours_t)-12}:{minutes_t} p.m.")
