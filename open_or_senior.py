def open_or_senior(data):
    for datas in data:
        status = "Open"
        if datas[0] >= 55 and datas[1] > 7:
            status = "Senior"
        print(status)

open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])#,['Open', 'Senior', 'Open', 'Senior'])
open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)])#,['Open', 'Open', 'Senior', 'Open'])