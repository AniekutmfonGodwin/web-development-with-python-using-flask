import pdb



count1 = count2 = 0


while True:
    print(count1,"in while one")
    count1 +=1

    while True:
        print(count2,"in while two")
        count2 +=1
        if count2>10:
            print("count two break")
            break

    pdb.set_trace()
    count2 = 0
    if count1>10:
        print("count one breaks")
        break
