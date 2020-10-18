# 开发时间：2020-10-14 21:24
# 开发者：星河主炮
import requests
import csv
import re
import time
import tkinter as tk
from tkinter import messagebox
import random
from os.path import exists
from os import remove
import matplotlib.pyplot as plt
import threading
from PIL import Image, ImageTk

# 前言：此程序用于检测微博动态的转发数、评论数以及点赞数，可根据趋势判断某人是否请了水军
# 程序附带说明文档（没有英文版，抱歉）
# 代码使用python编写，在设计gui时没有使用类方法，因而稍显繁琐，不过没有重构计划
# 此检测程序仅能用于微博。如果失效，请联系我(872324454@qq.com)，我会想办法更新修复
# 此程序严格遵守中国法律编写
# 如果喜欢的话，请点个赞吧

# introduction:this programme is designed for detecting number of forward,commend and like of message
# you can judge whether he employs online ghostwriters
# i prepared a instruction-document(no English version, sorry)
# it's written with Python, GUI was designed without object-oriented so a little complex
# it can only be used for weibo.If it can't work, please connect me, I'll try to solve it as soon as i can.
# this programme obey chinese laws strictly
# if you like it, give a like, please

# 爬取模块


class Spider:

    numbers_list = [1, 1, 1]
    img_name = 'testfig.jpg'
    record_time = 10
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    # 预定义了url和文件名
    def __init__(self, url='https://weibo.com/6643123988/JnKDsEvko?type=comment#_rnd1602772968078'
                 , record_name='example'):
        self.url = url
        self.record_name = record_name

    def crawl(self):

        global store_name
        session = requests.session()
        real_headers = random.choice(self.user_agent_list)
        headers = {'User-Agent': real_headers,
                   'cookie':cookie_text.get()}
        store_name = self.record_name + '.txt'
        page_text = session.get(url=self.url, headers=headers).text
        with open(store_name, 'w', encoding='utf-8')as fp:
            fp.write(page_text)
            # print('ok')
            # 爬取数据，写入文件

    def prase(self):
        global store_name
        with open(store_name, 'r', encoding='utf-8')as fp:
            content = str(fp.readlines())
            self.numbers_list = re.findall(r'<em>(\d+)<', content)
            # 读取网页数据


    def creatcsv(self):
        csv_name = self.record_name + '.csv'
        if not exists('./' + csv_name):
            with open(csv_name, 'w', encoding='utf-8', newline='')as fp:
                record_time = time.strftime('%H.%M',time.localtime(time.time()))
                f_csv = csv.writer(fp)
                f_csv.writerow(['时间', '转发数', '评论数', '点赞数'])
                f_csv.writerow([record_time, self.numbers_list[0], self.numbers_list[1], self.numbers_list[2]])
                # 如果目录下没有此名称的文件，则创建csv文件
        else:
            pass
            # 否则不执行任何操作

    def writeCsv(self):
        csv_name = self.record_name + '.csv'
        with open(csv_name, 'a', encoding='utf-8', newline='')as fp:
            record_time = time.strftime('%H.%M', time.localtime(time.time()))
            f_csv = csv.writer(fp)
            f_csv.writerow([record_time, self.numbers_list[0], self.numbers_list[1], self.numbers_list[2]])
            # 数据写入csv

    def delete_useless_file(self):
        # 移除发生错误时的文件，防止干扰下次运行
        # 实际上没用
        if exists(self.record_name + '.csv'):
            remove('./' + self.record_name + '.csv')
        if exists(self.record_name + '.jpg'):
            remove('./' + self.record_name + '.jpg')
        if exists(self.record_name + '.txt'):
            remove('./' + self.record_name + '.txt')


# 交互界面
# 主界面
win = tk.Tk()
# 标题
win.title('微博流量监控程序 ver 0.2')
# 设定窗口大小，且不可更改窗口大小
win.geometry('640x480')
win.resizable(0, 0)

# 绘制参数设置区
# 输入url
# 绑定url变量
url_text = tk.StringVar()
url_tip_text = tk.Label(win, text='输入url', font=('宋体', 14), ).place(x=40, y=20, anchor='nw')
url_entry = tk.Entry(win, show=None, textvariable=url_text,
                     font=('宋体', 14)).place(x=160, y=20, anchor='nw')
# 输入cookie
# 绑定cookie变量
cookie_text = tk.StringVar()
cookie_tip_text = tk.Label(win, text='输入cookie', font=('宋体', 14), ).place(x=40, y=50, anchor='nw')
cookie_entry = tk.Entry(win, show=None, textvariable=cookie_text,
                        font=('宋体', 14)).place(x=160, y=50, anchor='nw')
# 输入被检测名称
# 绑定name变量
name_text = tk.StringVar()
name_tip_text = tk.Label(win, text='输入名字', font=('宋体', 14), ).place(x=40, y=80, anchor='nw')
name_entry = tk.Entry(win, show=None, textvariable=name_text,
                      font=('宋体', 14)).place(x=160, y=80, anchor='nw')

# 设置功能函数
# 设置预置变量
# 此预设防止乱点的人玩崩
sleep_time = 60 + random.randint(-5, 5)
# 默认不触发爬取
trigger = 0
# 开始时间
start_time = 0
# 结束时间
end_time = 0
# 显示图像记号
note = 0


def start_spider():
    global trigger
    global start_time
    start_time = time.time()
    # 主函数段
    i = 1
    trigger = 1
    if url_text.get() and name_text.get():
        try:
            while trigger == 1 and i <= 1000:
                real_spider = Spider(url=url_text.get(), record_name=name_text.get())
                real_spider.crawl()
                real_spider.prase()
                real_spider.creatcsv()
                real_spider.writeCsv()
                # print('第', i, '次爬取成功')
                i = i + 1
                time.sleep(sleep_time)
        except:
            state_text.set('运行\n异常')
            time.sleep(60)
            while trigger == 1 and i <= 1000:
                real_spider = Spider(url=url_text.get(), record_name=name_text.get())
                real_spider.crawl()
                real_spider.prase()
                real_spider.creatcsv()
                real_spider.writeCsv()
                # print('第', i, '次爬取成功')
                i = i + 1
                time.sleep(sleep_time)
                continue
    else:
        messagebox.showwarning('警告！', '尚未输入url或名称！')
    # 判定url,cookie,name是否为空,messagebox提示
    # 测试代码
    # print(trigger)


def complete_spider():
    global trigger
    global end_time
    if trigger == 1:
        messagebox.showinfo('提示', '已停止检测')
        trigger = 0
    else:
        messagebox.showwarning('提示', '尚未开始检测')
    end_time = time.time()
    # 测试代码
    # print(trigger)


def get_help():
    messagebox.showinfo('使用帮助：',
                        '1.输入url(详情页面)，项目名\n'
                        '2.选择监测间隔\n'
                        '3.开始检测(自动检测1,000次)\n'
                        '4.默认间隔为一分钟\n'
                        '5.结束后显示图像')


def set_ten_second():
    global sleep_time
    sleep_time = 10 + random.randint(-5, 5)
    # 测试代码
    # print(sleep_time)


def set_one_minute():
    global sleep_time
    sleep_time = 60 + random.randint(-10, 10)
    # 测试代码
    # print(sleep_time)


def set_five_minutes():
    global sleep_time
    sleep_time = 300 + random.randint(-10, 10)
    # 测试代码
    # print(sleep_time)


def exit_sub(judge):
    if judge == 'yes':
        win.quit()
    else:
        pass


def exit_win():
    judge = messagebox.askquestion('提示信息', '确定要退出吗？')
    time.sleep(0.5)
    exit_sub(judge)



def thread_it(funcs, *args):
    t = threading.Thread(target=funcs, args=args)
    t.setDaemon(True)
    t.start()


def paintfig():
    global note
    note = not note
    if note:
        img_name = name_text.get() + '.png'
        csv_name = name_text.get() + '.csv'
        file = open(csv_name, encoding='utf-8')
        content = csv.reader(file)
        data = list(content)
        length_zu = len(data)
        length_yuan = len(data[0])

        x = list()
        y = list()
        z = list()
        m = list()
        for item in range(1, length_zu):
            x.append(data[item][0])
            y.append(data[item][1])
            z.append(data[item][2])
            m.append(data[item][3])

        a1 = plt.subplot(2, 2, 1)
        a1.plot(x, y, marker='o', label='forward')
        plt.legend()
        a2 = plt.subplot(2, 2, 2)
        a2.plot(x, z, marker='*', label='comment')
        plt.legend()
        a3 = plt.subplot(2, 2, 3)
        a3.plot(x, m, marker='v', label='like')
        plt.legend()
        plt.savefig('./' + img_name)
        label_img.update()
        plt.show()


def show_state():

    global trigger
    if trigger:
        state_text.set('正在\n运行')
    else:
        state_text.set('未\n运行')
'''global img_open
img_open = Image.open('色图.png')
def show_picture():
    global note
    note = not note
    if note:
        img_open = Image.open('色图.png')
        out = img_open.resize((280,210))
        img_png = ImageTk.PhotoImage(out)
        label_img = tk.Label(win, image=img_png)
        label_img.place(x=40, y=180, anchor='nw')'''
# 显示图片模块
img_open = Image.open('example.png')
out = img_open.resize((400, 300))
img_png = ImageTk.PhotoImage(out)
label_img = tk.Label(win, image=img_png)
label_img.place(x=40, y=140, anchor='nw')
# 设置功能按钮
# 开始检测的按钮
start_spider_button = tk.Button(win, text="开始检测", font=('宋体', 14), width=10,
                                command=lambda: thread_it(start_spider, )).place(x=460, y=20, anchor='nw')
# 结束检测的按钮
complete_spider_button = tk.Button(win, text="结束检测", font=('宋体', 14), width=10,
                                   command=complete_spider).place(x=460, y=60, anchor='nw')
# 获取帮助的按钮
get_help_button = tk.Button(win, text="获取帮助", font=('宋体', 14), width=10,
                            command=get_help).place(x=460, y=100, anchor='nw')
# 绘制图像的按钮
paint_picture_button = tk.Button(win, text='绘制折线图', font=('宋体', 14), width=10,
                                 command=paintfig).place(x=460, y=140, anchor='nw')
'''# 显示图像(由于python的垃圾清理机制，这一功能无法实现)
show_fig_button = tk.Button(win, text='显示图像', font=('宋体', 14), width=10,
                            command=show_picture).place(x=460, y=180, anchor='nw')'''
# 退出程序的按钮
exit_button = tk.Button(win, text="退出程序", font=('宋体', 14), width=10,
                        command=exit_win).place(x=460, y=380, anchor='nw')
# 设置检测时长,最后附加随机数
choice = tk.IntVar()
one_minute_radiobutton = tk.Radiobutton(win, text='间隔一分钟', font=('宋体', 14), variable=choice,
                                        value=2, command=set_one_minute).place(x=450, y=260, anchor='nw')
ten_minutes_radiobutton = tk.Radiobutton(win, text='间隔五分钟', font=('宋体', 14), variable=choice,
                                         value=3, command=set_five_minutes).place(x=450, y=300, anchor='nw')
# 显示运行状态
show_state_button = tk.Button(win, text='运行\n状态', font=('宋体', 14), width=5,command=show_state
                               ).place(x=460, y=180, anchor='nw')
state_text = tk.StringVar()
state_text_label = tk.Label(win, textvariable=state_text, font=('宋体', 14), bg='silver', borderwidth=2
                            ).place(x=530, y=185, anchor='nw')

# 绘制动态图像
# 不会做嘤嘤嘤

# 程序图标
win.iconbitmap(default='./medal.ico')

win.mainloop()
