score =0
for scores in range(0,100):
    if scores %3 ==0 and scores %5==0:
        print("fizzbuzz")
    elif scores % 3==0:
        print("fizz")
    elif scores % 5==0 :
        print("buzz")
    else:
        print(scores)
print(score)