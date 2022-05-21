import requests
import json
import xlsxwriter

workbook = xlsxwriter.Workbook('F:\\斗鱼直播房间信息爬虫.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 10)
worksheet.set_column('C:C', 40)
worksheet.set_column('D:D', 10)
format = {
    'bold': True,  # 字体加粗
    'align': 'center',  # 水平位置设置：居中
    'valign': 'vcenter',  # 垂直位置设置，居中
    'font_size': 16,  # '字体大小设置'
    'color': '#ff5d23'
}
str_format = workbook.add_format(format)
p = 0
urls = ['https://www.douyu.com/gapi/rkc/directory/2_1/{}'.format(page) for page in range(1, 5)]
for url in urls:
    res = requests.get(url)
    j = json.loads(res.text)
    l1 = j['data']
    l2 = l1['rl']
    p = p + 1
    for i in range(len(l2)):
        Anchor = l2[i]['nn']  # 获取主播名字
        RoomNumber = l2[i]['rid']  # 获取房间号
        Heat = l2[i]['ol']  # 获取热度
        RoomName = l2[i]['rn']  # 获取房间名

        worksheet.write("A1", "主播名字", str_format)
        worksheet.write("B1", "房间号", str_format)
        worksheet.write("C1", "房间名", str_format)
        worksheet.write("D1", "热度", str_format)

        worksheet.write(int(i + 120 * (p - 1)), 0, Anchor)
        worksheet.write(int(i + 120 * (p - 1)), 1, RoomNumber)
        worksheet.write(int(i + 120 * (p - 1)), 2, RoomName)
        worksheet.write(int(i + 120 * (p - 1)), 3, Heat)
# i+120*(p-1):120是因为每一页有120个房间，本次爬取了5页房间数据，用了p = p+1来使得Excel表格能连续记录数据
# 当时遇到的问题：在不添加120*（p-1）时，发现只能爬取120个房间数据，再看了遍代码，发现数据是被覆盖了
workbook.close()
print('斗鱼房间数据已保存')
