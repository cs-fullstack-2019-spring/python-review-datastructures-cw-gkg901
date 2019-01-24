def main():






    # ex1()
    ex2()



def getSortName(e):
   return e["name"]

def getSortAge(i):
    return i["age"]


def ex1():
    List = []
    while True:

        ask = input("enter a name")
        List.append(ask)
        if ask.lower() == "q":
            List.pop()
            print(List)
            break




def ex2():

    myDictionaryList = [
        {
            "name": "Kelvin",
            "age": 30
        },
        {
            "name": "Bob",
            "age": 50
        },
        {
            "name": "Alex",
            "age": 21
        }
    ]






    for each in myDictionaryList:
        print(f'{each["name"]} {each["age"]}')




    while True:
        ask = input("sort by age or name")
        if ask.lower() == "q":
            break

        elif ask.lower() == "age":
            myDictionaryList.sort(key=getSortAge)
            print(myDictionaryList)
        elif ask.lower() == "name":
            myDictionaryList.sort(key=getSortName)
            print(myDictionaryList)
        elif ask.lower() != "q" or ask.lower() != "name" or ask.lower() != "age":
            print("INVALID ENTRY. PLEASE TRY AGAIN")
            continue





























if __name__ == '__main__':
    main()