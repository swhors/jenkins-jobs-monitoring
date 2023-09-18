from loguru import logger
from flask.views import View
from service.db.job_status import JobStatus as JobStatusDBService

class MetricView(View):
    methods = ["GET"]

    def dispatch_request(self, job_name: str, interval_sec: int):
        if job_name == "all":
            job_status = JobStatusDBService.get_job_status_all_by_exec_time(interval_sec=interval_sec)
        else:
            job_status = JobStatusDBService.get_job_status_by_exec_time(name=job_name, interval_sec=interval_sec)
        print(f'job_status={job_status}, {type(job_status)}')
        if type(job_status) == list :
            lines = []
            if len(job_status) == 0:
                return "Not Found", 404
            for job in job_status:
                if job != None:
                    print(f'job={job}, {type(job)}')
                    key = "jenkins_job_status{name=\"" + job.name +\
                          "\",execution_id=\"" + str(job.execution_id) +\
                          "\",execution_duration=\"" + str(job.execution_duration) +\
                          "\",status=\"" + job.status + "\"}"
                    lines.append(f"{key} {job.execution_time}")
            return "\n".join(lines), 200
        else:
            if job_status != None:
                key = "jenkins_job_status{name=\"" + job_status.name +\
                      "\",execution_id=\"" + str(job_status.execution_id) +\
                      "\",execution_duration=\"" + str(job_status.execution_duration) +\
                      "\",status=\"" + job_status.status + "\"}"
                return f"{key} {job_status.execution_time}", 200
           
        return "Not Found", 404
