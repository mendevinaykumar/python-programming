p=int(input("enter principlae"))
r=int(input("enter rate "))
t=int(input("enter time"))
amount=p*(1+r/100)**t
ci=amount-p
print(round(ci,2))
