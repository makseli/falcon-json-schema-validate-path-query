# -*- coding:utf-8 -*-

import json
from jsonschema import validate
from jsonschema import ValidationError


class ValidateJson(object):
    # noinspection PyMethodMayBeStatic
    def on_get(self, req, resp):
        print(req)
        resp.body = '''{"service_status_is": "OK","please_request_send_method": "POST"}'''

    # noinspection PyMethodMayBeStatic
    def on_post(self, req, resp):

        json_request = {}
        if req.content_length > 0:
            json_request = json.load(req.bounded_stream)

        if json_request == {}:
            resp.body = json.dumps({"data": "empty"})
            return resp

        json_data = json_request['set_data']
        json_schema = json_request['set_schema']

        validate_result_message = ""

        try:
            validate_result = validate(json_data, json_schema)

            if validate_result is None:
                validate_result_message = "SUCCESS"

        except ValidationError as err:
            validate_result_message = err.message

        except Exception as exc:
            validate_result_message = exc.args

        resp.body = json.dumps({
            "Json-Schema-Validate-Result": validate_result_message
        })
