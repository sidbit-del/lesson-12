note1=note5=note10=note20=note50=note100=0
costumer_served=0
total_dispensed=0
serving=True

while serving is True:
    name=input("what is your name")
    amount=int(input("how much money do you want to withdraw"))
    if amount<=0:
        print("you dont have enough money to withdraw")
        continue

    remaining=amount
    id=1
    while id<=6:
        if id==1:
            value=100
        elif id==2:
            value=50
        elif id==3:
            value==20
        elif id==4:
            value==10
        elif id==5:
            value==5
        else:
            value==1

        count=remaining//value
        if count>0:
            print(f"{count}x{value}unit notes={count*value}")
            remaining-=count*value
            if value==100:
                note100+=count
            elif value==50:
                note50+=count
            elif value==20:
                note20+=count
            elif value==10:
                note10+=count
            elif value==5:
                note5+=count
            else:
                note1+=count
        id+=1
    costumer_served+=1
    total_dispensed+=amount
    print(f"transaction complete, {name}")
    again=input("next costumer? yes/no:")
    if again!= "yes":
        serving=False

print("daily denomination report")
for slot in range(1,7):
    if slot==1:
        value,total=100,note100
    elif slot==2:
        value,total=50,note50
    elif slot==3:
        value,total=20,note20
    elif slot==4:
        value,total=10,note10
    elif slot==5:
        value,total=5,note5
    else:
        value,total=1,note1

    if total>0:
        print(f"{value}-unit notes dispensed:{total}",end="")
        for note in range(total):
            print("-",end="")
        print()

print(f"costumers served:{costumer_served}")
print(f"total dispensed:{total_dispensed}units")
print("ATM session ended, bye bye")

