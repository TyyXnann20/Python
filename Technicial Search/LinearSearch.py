def linearSearch(item, search):
    count = 0
    for i in item:
        if search == i:
            count += 1
            print(f"We need {count} times to found {search}")
        else:
            count += 1
            
list1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
search = "E"
linearSearch(list1, search)