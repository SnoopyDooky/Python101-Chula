h_in = int(input())
m_in = int(input())
h_out = int(input())
m_out = int(input())
fee = 0  # less than 15 m
interval_time = h_out*60*60 + m_out*60 - (h_in*60*60 + m_in*60)  # in second
interval_time_ceil = -(-interval_time // 3600)  # ceil interval_time (h) without math module
if 15*60 < interval_time <= 3*60*60:  # 15 m - 3 h
    fee = 10 * interval_time_ceil
elif 3*60*60 < interval_time <= 6*60*60:  # 3 h - 6 h
    fee = 30 + 20 * (interval_time_ceil - 3)
elif interval_time > 6*60*60:  # more than 6 h
    fee = 200
print(fee)
