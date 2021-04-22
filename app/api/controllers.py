from flask import Blueprint, jsonify, request
from flask.views import MethodView
import time 
from app import app,q
import asyncio
from app.api.tasks import count_word

api = Blueprint("api", __name__, url_prefix='/api')

class ApiView(MethodView):
    def get(self):
        # time.sleep(5)
        return jsonify({
            "status_code": "200_OK"
        })

    def post(self):
        message = request.json.get('message')
        job = q.enqueue(count_word, message)
        print("Task in job: {} add to queue at {}".format(job.id, job.enqueued_at))
        # print("status: {}".format(job.status))
        print("func_name: {}".format(job.func_name))
        print("args: {}".format(job.args))
        print("kwargs: {}".format(job.kwargs))
        print("result: {}".format(job.result))
        print("started_at: {}".format(job.started_at))
        print("ended_at: {}".format(job.ended_at))
        print("execute_info: {}".format(job.exc_info))
        return jsonify({
            "count": job.result
        })

api_view = ApiView.as_view('api_view')
app.add_url_rule('/api/', view_func=api_view, methods=['GET','POST'])

