from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=2)
def timed_job():
    print('This job is run every 2 seconds.')
    
sched.start()