# -*- coding:utf-8 -*-

import json
from jsonpath2 import Path


class PathQuery(object):
    # noinspection PyMethodMayBeStatic
    def on_get(self, req, resp):
        print(req)
        resp.body = '''{"service_status_is": "OK","please_request_send_method": "POST"}'''

    # noinspection PyMethodMayBeStatic
    def on_post(self, req, resp):

        json_request = {}
        if req.content_length:
            json_request = json.load(req.stream)

        json_data = json_request['set_json_data']
        json_path = str(json_request['set_json_path'])

        path_query_result = []

        try:
            json_path_expression = Path.parse_str(json_path)

            for match_data in json_path_expression.match(json_data):
                path_query_result.append(match_data.current_value)

        except Exception as exc:
            path_query_result = exc.args

        resp.body = json.dumps({"Path-Query-Result": path_query_result},
                               sort_keys=True, indent=4)
