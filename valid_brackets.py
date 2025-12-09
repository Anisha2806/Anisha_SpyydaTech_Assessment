s=input("enter the brackets:")
bracket=list(s)
stack=[]
dict={'(':')','{':'}','[':']'}
for i in bracket:
    if i in dict.keys():
        stack.append(i)
    else:
        if len(stack)==0:
            print("false")
        else:
            if dict[stack[-1]]==i:
                stack.pop()
            else:
                print("false")
                break
if len(stack)==0:
    print("true")