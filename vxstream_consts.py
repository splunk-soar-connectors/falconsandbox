# File: vxstream_consts.py
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

PAYLOAD_SECURITY_API_KEY = 'api_key'  # pragma: allowlist secret
PAYLOAD_SECURITY_API_SECRET = 'api_secret'  # pragma: allowlist secret
PAYLOAD_SECURITY_WEBSERVICE_BASE_URL = 'base_url'
PAYLOAD_SECURITY_VERIFY_SERVER_CERT = 'verify_server_cert'

PAYLOAD_SECURITY_MSG_QUERYING = 'Querying Falcon Sandbox'
PAYLOAD_SECURITY_MSG_SUBMITTING_FILE = 'Submitting file/url to Falcon Sandbox'
PAYLOAD_SECURITY_MSG_CHECKED_STATE = (
    'Actual state is \'{}\'. Last check: {}. Done already {} attempts of foreseen {}. The next attempt will be done after {} seconds.'
)
PAYLOAD_SECURITY_MSG_DETONATION_QUERYING_REPORT = 'Querying Falcon Sandbox to get the report'
# When new verdict name will be added, remember about adding it to output in config json file
PAYLOAD_SECURITY_SAMPLE_VERDICT_NAMES = ['no specific threat', 'whitelisted', 'no verdict', 'suspicious', 'malicious', 'unknown']

PAYLOAD_SECURITY_DETONATION_QUEUE_TIME_INTERVAL_SECONDS = 60
PAYLOAD_SECURITY_DETONATION_QUEUE_NUMBER_OF_ATTEMPTS = 1440
PAYLOAD_SECURITY_DETONATION_PROGRESS_TIME_INTERVAL_SECONDS = 30
PAYLOAD_SECURITY_DETONATION_PROGRESS_NUMBER_OF_ATTEMPTS = 30

PAYLOAD_SECURITY_SAMPLE_STATE_IN_QUEUE = 'IN_QUEUE'
PAYLOAD_SECURITY_SAMPLE_STATE_IN_PROGRESS = 'IN_PROGRESS'
PAYLOAD_SECURITY_SAMPLE_STATE_SUCCESS = 'SUCCESS'
PAYLOAD_SECURITY_SAMPLE_STATE_ERROR = 'ERROR'
