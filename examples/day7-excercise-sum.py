# user_entries = ['10', '19.1', '20']
#
# user_entries = [float(user_entry) for user_entry in user_entries]
#
# print(sum(user_entries))

temperatures = [10, 12, 14]

file = open("file.txt", 'w')

temperatures = [str(temperature) + "\n" for temperature in temperatures]

file.writelines(temperatures)

