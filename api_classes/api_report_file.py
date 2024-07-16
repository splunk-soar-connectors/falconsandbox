# File: api_report_file.py
#
# Copyright (C) 2018-2024 Hybrid Analysis GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
#
#

from api_classes.api_caller import ApiCaller


class ApiReportFile(ApiCaller):
    endpoint_url = '/report/@id/file/@type'
    request_method_name = ApiCaller.CONST_REQUEST_METHOD_GET
    api_expected_data_type = ApiCaller.CONST_EXPECTED_DATA_TYPE_FILE
    endpoint_auth_level = ApiCaller.CONST_API_AUTH_LEVEL_DEFAULT
