import time
from taskModel import taskJobModel
from apscheduler.schedulers.blocking import BlockingScheduler
def func():
    ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    taskObj = taskJobModel('husike')
    taskObj.bark()
    # res = taskObj.autoCancelOrder()
    # print('do func  time :',ts)
    # print(res)
    print('自动确认发货定时任务-时间:', ts)
    # time.sleep(2)

def func2():
    # 耗时2S
    ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print('do func2 time：', ts)
    time.sleep(2)
    # 自动取消订单


def dojob():
    # 创建调度器：BlockingScheduler
    scheduler = BlockingScheduler()
    # 添加任务,时间间隔2S
    scheduler.add_job(func, 'interval', seconds=2, id='test_job1')
    # 添加任务,时间间隔5S
    # scheduler.add_job(func2, 'interval', seconds=3, id='test_job2')
    scheduler.start()
dojob()