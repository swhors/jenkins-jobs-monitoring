class Config:
    class ScheduleJobMonitor:
        job_list_file = "job_list.txt"
    
    class Web:
        port = 5054

    class Db:
        db_file = "monitoring.db"
    
    class Http:
        addr = "localhost"
        port = 5054

    class Log:
        size = "20Mb"
        retention = "5 days"
