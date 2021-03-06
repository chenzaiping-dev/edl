# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from ..utils import common_pb2 as pb


class EdlException(Exception):
    pass


class EdlStopIteration(EdlException):
    pass


class EdlRegisterError(EdlException):
    pass


class EdlBarrierError(EdlException):
    pass


class EdlUnkownError(EdlException):
    pass


class EdlRankError(EdlException):
    pass


class EdlInternalError(EdlException):
    pass


def deserialize_exception(s):
    thismodule = sys.modules[__name__]
    cls = getattr(thismodule, s.type)(s.detail)
    raise cls


def serialize_exception(e):
    s = pb.Status()
    s.type = e.__class__.__name__
    s.detail = str(e)
    return s
