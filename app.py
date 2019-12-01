# -*- coding:utf-8 -*-
import json
import falcon
from info_json import InfoJson
from path_query import PathQuery
from validate_json import ValidateJson


class GeneralResource(object):
    # noinspection PyMethodMayBeStatic
    def on_get(self, req, resp):
        print(req)
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps({"service_status_is": "OK"})


home = GeneralResource()
app = falcon.API()
info_json = InfoJson()
path_query = PathQuery()
validate_json = ValidateJson()

app.add_route('/', home)

app.add_route('/data', info_json)
app.add_route('/data/{which_is}', info_json)

app.add_route('/path-query', path_query)
app.add_route('/validate-json', validate_json)
