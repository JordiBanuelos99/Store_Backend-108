def start_tests():
    print("-------- List tests ----------")

    nums = [1,2,3,4,5,6]

    # read from the list
    print( nums[0] )
    print( nums[1] )

    # add elements to a list
    nums.append(9)
    print(nums)

    # for loop from 0 to 20
    for number in range(0, 21):
        print(number)

def test1():
    print("----- Test 1 ------")
    prices = [123, 3, 23, 6475, 58, 89, 45, 34, 87, 34, -12, 23, 123, -23, -123, 0, 123, 0, -29, 10]
    count = 0
    sum = 0
    sum_zero = 0
    count_zero = 0
    for price in prices:
        if price < 50:
            print(f"${price}")
            count = count + 1
        #3 sum of all numbers
        sum = sum + price
        #4 sum of all numbers greater than zero
        if price > 0:
            sum_zero = sum_zero + price
        #5 count of all zeros
        if price == 0:
            count_zero = count_zero + 1
    print(f"There are {count} prices lower than $50")
    print(f"The sum of all numbers is ", sum)
    print(f"The sum of all numbers greater than 0 is ", sum_zero)
    print(f"The number of zeros in this list is ", count_zero)

def test2():
    users =  [
        {
            "gender": "F",
            "name": "Louis",
            "color": "Green"
        },
        {
            "gender": "M",
            "name": "Manuel",
            "color": "Gray"
        },
        {
            "gender": "F",
            "name": "Rossy",
            "color": "Pink"
        },
        {
            "gender": "F",
            "name": "Renny",
            "color": "pink"
        },
        {
            "gender": "M",
            "name": "Roman",
            "color": "Purple"
        },
        {
            "gender": "m",
            "name": "John",
            "color": "Pink"
        },
        {
            "gender": "F",
            "name": "Susan",
            "color": "Black"
        },
    ]
    
    print("------- Test 2 --------")
    user_count = 0
    print("#1 Print user names")
    for user in users:
        #1 Print user names
        print(user["name"])
        #2 Print how many users are in the list
        user_count = user_count + 1
        
    print()
    print("#2 Print how many users are in the list")
    print("User count: ", user_count)
    print() 
    print("#3 Print the name of the users who like pink despite how is typed")
    for user in users:
        #3 Print the name of the users who like pink despite how is typed
        if user["color"].lower() == "pink":
            print(user["name"])

    print() 
    print("#4 If color is equal to 'pink' print user's name")
    for user in users:
        #4 If color is equal to "pink" print user's name
        if user["color"] == "pink":
            print(user["name"])

def test3():
    print("------ Test 3 ------")
    prices = [123, 3, 23, 6475, 58, 89, 45, 34, 87, 34, -12, 23, 123, -23, -123, 0, 123, 0, -29, 10]
    solution = prices [0]
    for number in prices:
        if number > solution:
            solution = number
    print("The highest price found in this list is: " + str(solution))
    # Find the most expensive product
    
# start_tests()
# test1()
# test2()
test3()