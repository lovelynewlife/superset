# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import logging

from flask_appbuilder import has_access, expose
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import Model

from superset import app
from superset.constants import MODEL_VIEW_RW_METHOD_PERMISSION_MAP, RouteMethod
from superset.superset_typing import FlaskResponse
from superset.views.base import SupersetModelView
from superset.models.dashboard import Dashboard as DashboardModel

metadata = Model.metadata  # pylint: disable=no-member
config = app.config
logger = logging.getLogger(__name__)


class SearchEngineModelView(SupersetModelView):
    route_base = "/searching"
    class_permission_name = "Search"
    method_permission_name = MODEL_VIEW_RW_METHOD_PERMISSION_MAP|{
        "search": "read",
    }
    datamodel = SQLAInterface(DashboardModel)

    include_route_methods = RouteMethod.CRUD_SET | {
        "search"
    }

    default_view = "show"

    @has_access
    @expose("/show")
    def show(self) -> FlaskResponse:
        return super().render_app_template()

    @has_access
    @expose("/search")
    def search(self) -> FlaskResponse:
        return "Hello world"
