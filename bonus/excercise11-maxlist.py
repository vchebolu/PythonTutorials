def get_max():
    list=[]
    grades = [9.6, 9.2, 9.7]
    max_grade = max(grades)
    min_grade = min(grades)
    list.append(max_grade)
    list.append(min_grade)
    return list


list = get_max()
print(f"Max: {list[0]}, Min: {list[1]}")