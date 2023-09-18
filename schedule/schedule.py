from schedule.schedule_ctx import ScheduleCtx

from schedule.schedule_job_monitor import ScheduleJobMonitor


jobs=[]
schedule_ctx = None

def check_ctx(func):
    def wrapper(*args):
        if schedule_ctx == None:
            raise(Exception("ScheduleCtx is None.({func})"))
        return func(*args)
    return wrapper

def init(is_daemon: bool):
    global jobs, schedule_ctx
    jobs = [ScheduleJobMonitor()]

    schedule_ctx = ScheduleCtx(is_daemon=is_daemon, jobs=jobs)

@check_ctx
def run():
    schedule_ctx.start()

@check_ctx
def stop():
    global schedule_ctx
    schedule_ctx.stop()
    schedule_ctx = None
