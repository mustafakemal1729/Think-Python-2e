# Exercise 1-3.

"""

3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? 
   What is your average speed in miles per hour?
"""

mile = 1.609

distance_in_miles = round(10 / mile, 4)
run_time_in_seconds = 42*60 + 42
run_time_in_minutes = 42 + 42/60

print(
    f"Average pace in seconds {round((distance_in_miles/run_time_in_seconds), 4)}")
print(
    f"Average pace in minutes {round((distance_in_miles/run_time_in_minutes), 4)}")
