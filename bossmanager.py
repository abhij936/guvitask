ceo =	{
  "emp1": 1975,
  "empname": "abhi",
  "passin":1234,
  "passinm":123
}
search=int(input())
if (search==ceo["emp1"]) :
    print("Found")
    passinw=int(input(""))
    if(passinw==ceo["passin"]):
        print(ceo.items())
        del ceo["emp1"]
        del ceo["empname"]
        print(ceo.items())
    elif(passinw==ceo["passinm"]):
        print(ceo["emp1"])
        print(ceo["empname"])
else:
    print("Not Found")
