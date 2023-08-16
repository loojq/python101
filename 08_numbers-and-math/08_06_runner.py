# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6km)
distance_in_km = 16
runtime_in_hours = 30.5/60
def mile_to_km(mile):
    km = mile*1.6
    return(km)
distance_in_km = mile_to_km(10)
print(distance_in_km)
average_speed = distance_in_km/runtime_in_hours
print(round(average_speed,2))