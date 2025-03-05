# Input given -> num_days = 4, daily_temp = [24.7,28.5,25,30.2]

num_days = int(input('Number of days you want to calculate the temperate: '))

daily_temp = []

for i in range(num_days):
    day_temp = float(input(f'Enter peak temperature for day {i}'.format(i)))
    daily_temp.append(day_temp)
avg_temp = sum(daily_temp)/num_days

high_temp_days_count = 0
for i in range(num_days):
    if daily_temp[i] > avg_temp:
        high_temp_days_count+=1

print(f'Average temperature for {num_days} day(s) is {avg_temp}'.format(daily_temp,num_days,avg_temp))
print(f'{high_temp_days_count} out of {num_days} days are above the average temperature'.format(high_temp_days_count,num_days))