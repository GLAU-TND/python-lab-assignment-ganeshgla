
Attribute Error example
try:
    a='hello'
    a.remove('h')
except AttributeError as e:
    print('error handled',e)
type error example
try:
    a='hello'
    b=5
    c=a+b
except AttributeError as e:
    print('error handled',e)
    
  value error example:
  
  try:
    a=int(input())
except AttributeError as e:
    print('error handled',e)
