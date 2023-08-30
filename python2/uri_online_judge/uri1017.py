distence_fuel=12
time=int(input())
speed=int(input())
total_distance=time*speed
total_fuel=(total_distance)/distence_fuel
print('{:.3f}'.format(total_fuel))