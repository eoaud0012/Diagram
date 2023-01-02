import time
from random import randint

from SRT import SRT
srt = SRT("010-4764-3016", "eoaoWkd1!")

dep = '수서'
arr = '부산'
date = '20220907'
time = '180000'
trains = srt.search_train(dep, arr, date, time)
while(1):
    if(len(trains) > 0):
        time.sleep(randint(2,4))  # 2~4초 랜덤으로 기다리기
        trains
        reservation = srt.reserve(trains[1])
        reservation
        print("예매완료했습니다")
        break
    else:
        trains = srt.search_train(dep, arr, date, time)
        print("예매중입니다")
# [[SRT] 09월 30일, 수서~부산(15:00~17:34) 특실 예약가능, 일반실 예약가능,
# [SRT] 09월 30일, 수서~부산(15:30~18:06) 특실 예약가능, 일반실 예약가능,
# [SRT] 09월 30일, 수서~부산(16:00~18:24) 특실 매진, 일반실 예약가능,
# [SRT] 09월 30일, 수서~부산(16:25~18:45) 특실 예약가능, 일반실 예약가능, ...]


# [SRT] 09월 30일, 수서~부산(15:30~18:06) 53700원(1석), 구입기한 09월 20일 23:38