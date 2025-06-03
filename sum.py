# no loop
answer=0      
print(answer)   # 0
answer=answer+1
print(answer)   # 1
answer=answer+2
print(answer)   # 3
answer=answer+3
print(answer)   # 6
answer=answer+4
print(answer)   # 10
# with loop
answer=0
for i in range(5):
    answer=answer+i
    print(answer)   # 0 1 3 6 10 inside the loop 
print(answer)   # 10 outside the loop

