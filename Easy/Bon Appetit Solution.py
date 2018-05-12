def isthisfair(bill,charge,n,k):
    bill.remove(bill[k])
    supposed_charge = sum(bill)/2
    if charge != supposed_charge:
        print(int(charge - supposed_charge))
    elif charge == supposed_charge:
        print('Bon Appetit')
    


first = input().strip().split(' ')
bill = list(map(int, input().strip().split(' ')))
charge = int(input())
n = int(first[0])
k = int(first[1])

isthisfair(bill,charge,n,k)
