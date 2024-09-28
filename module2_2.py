first = input("Ведите первое число: ")
second = input("Ведите второе число: ")
fhird = input("Ведите третье число: ")
Set1 = {first,second,fhird}
if len(Set1)==3:
    print(0)
elif len(Set1)==2:
    print(2)
elif len(Set1)==1:
    print(3)