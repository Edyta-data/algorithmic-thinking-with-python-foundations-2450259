<<<<<<< Updated upstream
# doors = [False] * 101
#
# print(doors)
#
# for i in range(1, 101):
#     doors[i] = not doors[i]
#
# print(doors)
#
# for i in range(1, 6):
#     for j in range(1, 4):
#         print("i:", i, "j:", j)

for i in range(1, 11, 2):
    print(i)




=======
door_status = [False]*101

for i in range(1,101):
    for j in range(1, 101, i):
        door_status[j] = not door_status[j]

    
>>>>>>> Stashed changes
