from datetime import datetime
import sched
import time


def timedTask():
    # 初始化 sched 模块的 scheduler 类,传入(time.time, time.sleep)这两个参数
    scheduler = sched.scheduler(time.time, time.sleep)
    # 增加调度任务，enter(睡眠时间，执行级别，执行函数)
    scheduler.enter(5, 1, task)
    # 运行任务
    scheduler.run()

# 定时任务
def task():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    while True:
        timedTask()

# import schedule
# import time
#
# def hellow():
#     print('hellow')
#
# def Timer():
#     schedule.every().day.at("09:00").do(hellow)
#     schedule.every().day.at("18:00").do(hellow)
#
#     while True:
#         schedule.run_pending()
#
#         time.sleep('需要睡眠的周期')
#
#
# Timer()