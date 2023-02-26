mass = float(input("Mass (kg): "))
force = float(input("Force (N): "))
time = float(input("Time (s): "))
initial_velocity = float(input("Initial Velocity (m/s): "))

acceleration = force / mass
final_velocity = initial_velocity + acceleration * time
distance_traveled = initial_velocity * time + 0.5 * acceleration * time ** 2

print("Acceleration:", acceleration, "m/s^2")
print("Final Velocity:", final_velocity, "m/s")
print("Distance Traveled:", distance_traveled, "m")
