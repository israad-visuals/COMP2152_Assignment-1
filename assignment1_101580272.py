#%%
"""
Author: Ismail Abdi
Assignment: #1
"""
#%%
# Creating the 4 variables with their data types
gym_member = "Alex Alliton"  # String
preferred_weight_kg = 20.5  # Float
highest_reps = 25  # Integer
membership_active = True  # Boolean
#%%
# Dictionary with friend names as keys and tuples of workout minutes as values
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 50, 35),
    "Taylor": (25, 30, 40),
    "Jordan": (35, 40, 25),
    "Casey": (20, 35, 30)
}
#%%
# Calculate total workout minutes for each friend and add to dictionary
friend_names = list(workout_stats.keys())
for friend in friend_names:
    total = sum(workout_stats[friend])
    workout_stats[friend + "_Total"] = total

print(workout_stats)
#%%
# 2D list containing workout minutes for each friend as nested list
workout_list = []
for friend in ["Alex", "Jamie", "Taylor", "Jordan", "Casey"]:
    workout_list.append(list(workout_stats[friend]))

print(workout_list)
#%%
# Slicing workout_list to extract yoga and running minutes for all friends
print("Yoga and Running minutes for all friends:")
for row in workout_list:
    print(row[0:2])  # First two columns (yoga and running)
#%%
# Extract weightlifting minutes for the last two friends
print("\nWeightlifting minutes for last two friends:")
for row in workout_list[-2:]:
    print(row[2])  # Third column (weightlifting)
#%%
# Check if any friend has >= 120 total workout minutes
friend_names = ["Alex", "Jamie", "Taylor", "Jordan", "Casey"]
for friend in friend_names:
    total_key = friend + "_Total"
    if workout_stats[total_key] >= 120:
        print(f"Great job staying active, {friend}!")
#%%
# Allow user to input a friend's name and check if exists
name = input("Enter a friend's name: ")

if name in workout_stats and not name.endswith("_Total"):
    yoga, running, weightlifting = workout_stats[name]
    total = workout_stats[name + "_Total"]
    print(f"\n{name}'s workout minutes:")
    print(f"Yoga: {yoga} minutes")
    print(f"Running: {running} minutes")
    print(f"Weightlifting: {weightlifting} minutes")
    print(f"Total: {total} minutes")
else:
    print(f"Friend {name} not found in the records.")
#%%
# Find friend with highest and lowest total workout minutes
friend_names = ["Alex", "Jamie", "Taylor", "Jordan", "Casey"]
max_friend = ""
max_minutes = 0
min_friend = ""
min_minutes = float('inf')

for friend in friend_names:
    total = workout_stats[friend + "_Total"]
    if total > max_minutes:
        max_minutes = total
        max_friend = friend
    if total < min_minutes:
        min_minutes = total
        min_friend = friend

print(f"\nFriend with highest total: {max_friend} with {max_minutes} minutes")
print(f"Friend with lowest total: {min_friend} with {min_minutes} minutes")
#%%

#%%
