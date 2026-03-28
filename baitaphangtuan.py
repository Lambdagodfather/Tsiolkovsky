# Ex 1.2 - Python as a calculator
minutes = 42
seconds = 42
total_seconds = minutes * 60 + seconds
km = 10
mile = km * 0.621371
distance_km = 10
time_seconds = total_seconds
pace_sec_per_km = time_seconds / distance_km
pace_minutes = int(pace_sec_per_km // 60)
pace_seconds = int(pace_sec_per_km % 60)
speed_kmh = distance_km / time_seconds * 3600
print("=== KẾT QUẢ ===")
print("1. Tổng số giây:", total_seconds, "giây")
print("2. 10 km =", round(mile, 2), "mile")
print("3. Average pace:", pace_minutes, "phút", pace_seconds, "giây/km")
print("   Average speed:", round(speed_kmh, 2), "km/h")