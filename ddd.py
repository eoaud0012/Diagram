from SRT import SRT
srt = SRT("010-4764-3016", "eoaoWkd1!")

dep = '수서'
arr = '부산'
date = '20220829'
time = '144000'
trains = srt.search_train(dep, arr, date, time)
trains
# [[SRT] 09월 30일, 수서~부산(15:00~17:34) 특실 예약가능, 일반실 예약가능,
# [SRT] 09월 30일, 수서~부산(15:30~18:06) 특실 예약가능, 일반실 예약가능,
# [SRT] 09월 30일, 수서~부산(16:00~18:24) 특실 매진, 일반실 예약가능,
# [SRT] 09월 30일, 수서~부산(16:25~18:45) 특실 예약가능, 일반실 예약가능, ...]

reservation = srt.reserve(trains[1])
reservation
# [SRT] 09월 30일, 수서~부산(15:30~18:06) 53700원(1석), 구입기한 09월 20일 23:38