import time
tt=time.strftime('%Y-%m-%d', time.localtime(time.time()))
print(f"오늘 날짜는 {tt}입니다.")
schedule=[]
while 1:
    a=input('오늘의 해야할 일을 말해주세요 (멈추려면 1을 입력하세요) : ')
    if a == '1':
        break
    schedule.append(a)
for j in range(len(schedule)):
    print("TODOLIST")
    for i in range(len(schedule)):
        print(f"{i}.{schedule[i]}",end='\n')
    number=int(input('번호를 입력해주세요 : '))
    print(f"{schedule[number]}이(가) 선택되었습니다.\n시간 측정을 시작합니다.")
    start=time.time()
    stop=input("Enter를 누르면 시간 측정을 멈춥니다.")
    end=time.time()
    result=int(end-start)
    H=result//3600
    M=result//60
    s=result-(M*60)-(H*3600)
    print(f"{schedule[number]}을/를 {H}시간 {M}분 {s}초만에 완수했습니다.")
    f=open("TODOLIST.txt",'a')
    if j==0:
        f.write(f"{tt}\n")
    f.write(f"{schedule[number]} [{H}:{M}:{s}]\n")
    f.close()
    del schedule[number]