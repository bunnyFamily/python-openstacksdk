# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.messaging.v1 import _proxy
from openstack.messaging.v1 import queue
from openstack.tests.unit import test_proxy_base


class TestMessagingProxy(test_proxy_base.TestProxyBase):
    def setUp(self):
        super(TestMessagingProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_queue_create_attrs(self):
        kwargs = {"x": 1, "y": 2, "z": 3}
        self.verify_create2('openstack.proxy.BaseProxy._create',
                            self.proxy.create_queue,
                            method_kwargs=kwargs,
                            expected_args=[queue.Queue],
                            expected_kwargs=kwargs)