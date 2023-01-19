import time
from random import randint 
from SRT import SRT

srt = SRT("2281358944", "whqkxk7541!") #
dep = '동탄'
arr = '울산'
date = '20230121' # 날짜 (yyyymmdd)
tr_time = '000000' # 시간 (HHMMSS)

# 기차 검색
trains = srt.search_train(dep, arr, date, tr_time, available_only=False)
print(*trains, sep='\n')
# 결과 :  [[SRT] 11월 06일, 수서~부산(20:00~22:23) 특실 매진, 일반실 .....
train_num = input("몇 번째 기차를 예매하시겠어요?(0번부터 시작)")
train_num = int(train_num)


flag = False
i = 0

# 루프 시작
while flag == False:
    try:
        i += 1
        time.sleep(randint(2, 4))
        
        print(f"{i}번째 시도")
        reservation = srt.reserve(trains[train_num])
        print(reservation)
        flag = True
        
    except:
        pass
        
# 결과 : [SRT] 11월 06일, 수서~부산(22:40~01:07) 52400원(1석), 구입기한 11월 06일 22:36