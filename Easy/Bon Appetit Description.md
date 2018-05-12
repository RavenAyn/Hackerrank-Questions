# Problem Description 

Anna and Brian are sharing a meal at a restuarant and they agree to split the bill equally. Brian wants to order something that Anna is allergic to though, and they agree that Anna won't pay for that item. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: _bill = [2,4,6]_ . Anna declines to eat item _k = bill[2]_ which costs _6_. If Brian calculates the bill correctly, Anna will pay _(2 + 4)/2 = 3_. If he includes the cost of _bill[2]_, he will calculate _(2+4+6)/2 = 6_. In the second case, he should refund 3 to Anna.

You are given an array of prices, , the cost of each of the  items, , the item Anna doesn't eat, and , the total amount of money that Brian charged Anna for her portion of the bill. If the bill is fairly split, print Bon Appetit. Otherwise, print the integer amount of money that Brian must refund to Anna.

##### Input Format

The first line contains two space-separated integers _n_ and _k_, the number of items ordered and the 0-based index of the item that Anna did not eat. 
The second line contains _n_ space-separated integers _bill[i]_ where _i < n_. 
The third line contains an integer,_b_ , the amount of money that Brian charged Anna for her share of the bill.

# Solution 
```python
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
```
