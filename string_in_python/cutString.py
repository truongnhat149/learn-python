# sử dụng dấu hai chấm để cắt từ đầu đến cuối
"""có rất nhiều cách để cắt chuỗi
đây là cách 1: """
strA = "CodeGym"
strB = strA[:]
print(strB)

#cách 2: dùng từ khóa None
# từ khóa None đại diện cho điểm bắt đàu hoặc kết thúc trobng chuỗi
strC = strA[1:None]
print(strC)

#cách 3: dùng bước nhảy ::
strD = strA[None:None:]
print(strD)