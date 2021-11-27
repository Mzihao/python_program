from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def run_spider():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


sched = BlockingScheduler()
sched.add_job(run_spider, 'interval', seconds=5) #分钟 minutes=3
sched.start()

# def run_spider():
#     print("启动爬虫")
#
# # 在每天的10点15分能够准时启动
# sched = BlockingScheduler()
# sched.add_job(run_spider, 'cron', hour=10, minute=15)
# sched.start()