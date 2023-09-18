import os
from loguru import logger

from model.job_status import JobStatus as JobStatusModel
from service.db.job_status import JobStatus as JobStatusDBService
from service.http.job_status import JobStatus as JobStatusHTTPService
from config import Config
from schedule.schedule_job import ScheduleJob


job_hour = 0
job_minutes = 1
job_seconds = 0

BASE_PATH="/jenkins/jobs"


class ScheduleJobMonitor(ScheduleJob):

    def __init__(self):
        super().__init__(name="ScheduleJobMonitor", hour=job_hour, minutes=job_minutes, seconds=job_seconds, job_type="interval")

    def _status(self, job_name: str):
        with open(f'{BASE_PATH}/{job_name}/all_builds.mr', 'rb') as f:
            cnt = 0
            try:
                f.seek(-2, os.SEEK_END)
                while f.read(1) != b'\n':
                    cnt += 1
                    f.seek(-2, os.SEEK_CUR)
            except OSError:
                f.seek(0)
            last_line = f.readline().decode()
            if last_line != None and len(last_line) > 0:
                JobStatusHTTPService.add_line_to_job_status(name=job_name, line=last_line)
            f.close()

    def _monitor(self, jenkins_jobs=[]):
        for job in jenkins_jobs:
            try:
                job = job.replace('\n', '')
                self._status(job)
            except Exception as e:
                logger.error(f"Exception: ScheduleJobMonitor._monitor.{job}\n\t{e}")
                pass
    
    def __operate__(self):
        with open(Config.ScheduleJobMonitor.job_list_file, "rt") as fp:
            jenkins_jobs = fp.readlines()
            fp.close()
            self._monitor(jenkins_jobs = jenkins_jobs)

