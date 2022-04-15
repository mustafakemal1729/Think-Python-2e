# Exercise 2-2.

"""
3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) 
and 1 mile at an easy pace again, what time do I get home for breakfast?

"""

seconds = 1
minutes = 60*seconds
hours = 60*minutes

# Convert run time into seconds
start_time = 6*hours + 52*minutes
easy_pace_per_mile = 8*minutes + 15
tempo_per_mile = 7*minutes + 12

total_run_time = (2*easy_pace_per_mile + 3*tempo_per_mile)
final_time = start_time + total_run_time

# Calculate arrival time
return_home_time_hour = final_time // hours
left_time = final_time % hours
return_home_time_minute = left_time // 60
print(f"You get home at {return_home_time_hour}:{return_home_time_minute}")
