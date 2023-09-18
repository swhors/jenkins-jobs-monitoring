from flask.views import View
from flask import request

from service.db.job_status import JobStatus as JobStatusDBService

class JobStatusView(View):
    methods=["POST"]
    def dispatch_request(self):
        print(f'request.json = {request.json}')
        name=request.json['name']
        execution_id=int(request.json['id'])
        execution_time=int(request.json['time'])
        execution_dur=int(request.json['dur'])
        status=request.json['status']

        JobStatusDBService.add_new_job_status(name=name, execution_id=execution_id, execution_time=execution_time, execution_duration=execution_dur, status=status)
        return "Success", 200

    #def del(self):
    #    name=request.args('name', type=str)
    #    execution_id=request.args('id', type=int)
    #    JobStatusDBService.del_job_status(name=name, execution_id=execution_id)
    #    return "Success", 200
        
