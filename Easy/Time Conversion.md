
# Problem Description
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

#### Input Format

A single string _s_ containing a time in 12-hour clock format (i.e.hh:mm:ssAM  or hh:mm:ssPM)

#### Output Format

Convert and print the given time in 24-hour format.

# Solution
```python
def timeConversion(s):
    if s[-2:] == "AM" and s[0:2] == "12":
        h24 = "00"+ s[2:-2]
    elif s[-2:] == "PM" and s[0:2] != "12":
        h24 = str(int(s[0:2])+12)+ s[2:-2]

    else:
        h24 = s[0:-2]
    return h24
    
    
s = input()
result = timeConversion(s)
print(result)
```
