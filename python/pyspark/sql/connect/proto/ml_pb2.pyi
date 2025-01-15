#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import pyspark.sql.connect.proto.ml_common_pb2
import pyspark.sql.connect.proto.relations_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class MlCommand(google.protobuf.message.Message):
    """Command for ML"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class Fit(google.protobuf.message.Message):
        """Command for estimator.fit(dataset)"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ESTIMATOR_FIELD_NUMBER: builtins.int
        PARAMS_FIELD_NUMBER: builtins.int
        DATASET_FIELD_NUMBER: builtins.int
        @property
        def estimator(self) -> pyspark.sql.connect.proto.ml_common_pb2.MlOperator:
            """Estimator information"""
        @property
        def params(self) -> pyspark.sql.connect.proto.ml_common_pb2.MlParams:
            """parameters of the Estimator"""
        @property
        def dataset(self) -> pyspark.sql.connect.proto.relations_pb2.Relation:
            """the training dataset"""
        def __init__(
            self,
            *,
            estimator: pyspark.sql.connect.proto.ml_common_pb2.MlOperator | None = ...,
            params: pyspark.sql.connect.proto.ml_common_pb2.MlParams | None = ...,
            dataset: pyspark.sql.connect.proto.relations_pb2.Relation | None = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "dataset", b"dataset", "estimator", b"estimator", "params", b"params"
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "dataset", b"dataset", "estimator", b"estimator", "params", b"params"
            ],
        ) -> None: ...

    class Delete(google.protobuf.message.Message):
        """Command to delete the cached object which could be a model
        or summary evaluated by a model
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        OBJ_REF_FIELD_NUMBER: builtins.int
        @property
        def obj_ref(self) -> pyspark.sql.connect.proto.ml_common_pb2.ObjectRef: ...
        def __init__(
            self,
            *,
            obj_ref: pyspark.sql.connect.proto.ml_common_pb2.ObjectRef | None = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["obj_ref", b"obj_ref"]
        ) -> builtins.bool: ...
        def ClearField(
            self, field_name: typing_extensions.Literal["obj_ref", b"obj_ref"]
        ) -> None: ...

    class Write(google.protobuf.message.Message):
        """Command to write ML operator"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class OptionsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: builtins.str
            value: builtins.str
            def __init__(
                self,
                *,
                key: builtins.str = ...,
                value: builtins.str = ...,
            ) -> None: ...
            def ClearField(
                self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]
            ) -> None: ...

        OPERATOR_FIELD_NUMBER: builtins.int
        OBJ_REF_FIELD_NUMBER: builtins.int
        PARAMS_FIELD_NUMBER: builtins.int
        PATH_FIELD_NUMBER: builtins.int
        SHOULD_OVERWRITE_FIELD_NUMBER: builtins.int
        OPTIONS_FIELD_NUMBER: builtins.int
        @property
        def operator(self) -> pyspark.sql.connect.proto.ml_common_pb2.MlOperator:
            """Estimator or evaluator"""
        @property
        def obj_ref(self) -> pyspark.sql.connect.proto.ml_common_pb2.ObjectRef:
            """The cached model"""
        @property
        def params(self) -> pyspark.sql.connect.proto.ml_common_pb2.MlParams:
            """The parameters of operator which could be estimator/evaluator or a cached model"""
        path: builtins.str
        """Save the ML instance to the path"""
        should_overwrite: builtins.bool
        """Overwrites if the output path already exists."""
        @property
        def options(
            self,
        ) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
            """The options of the writer"""
        def __init__(
            self,
            *,
            operator: pyspark.sql.connect.proto.ml_common_pb2.MlOperator | None = ...,
            obj_ref: pyspark.sql.connect.proto.ml_common_pb2.ObjectRef | None = ...,
            params: pyspark.sql.connect.proto.ml_common_pb2.MlParams | None = ...,
            path: builtins.str = ...,
            should_overwrite: builtins.bool = ...,
            options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "obj_ref", b"obj_ref", "operator", b"operator", "params", b"params", "type", b"type"
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "obj_ref",
                b"obj_ref",
                "operator",
                b"operator",
                "options",
                b"options",
                "params",
                b"params",
                "path",
                b"path",
                "should_overwrite",
                b"should_overwrite",
                "type",
                b"type",
            ],
        ) -> None: ...
        def WhichOneof(
            self, oneof_group: typing_extensions.Literal["type", b"type"]
        ) -> typing_extensions.Literal["operator", "obj_ref"] | None: ...

    class Read(google.protobuf.message.Message):
        """Command to load ML operator."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        OPERATOR_FIELD_NUMBER: builtins.int
        PATH_FIELD_NUMBER: builtins.int
        @property
        def operator(self) -> pyspark.sql.connect.proto.ml_common_pb2.MlOperator:
            """ML operator information"""
        path: builtins.str
        """Load the ML instance from the input path"""
        def __init__(
            self,
            *,
            operator: pyspark.sql.connect.proto.ml_common_pb2.MlOperator | None = ...,
            path: builtins.str = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["operator", b"operator"]
        ) -> builtins.bool: ...
        def ClearField(
            self, field_name: typing_extensions.Literal["operator", b"operator", "path", b"path"]
        ) -> None: ...

    FIT_FIELD_NUMBER: builtins.int
    FETCH_FIELD_NUMBER: builtins.int
    DELETE_FIELD_NUMBER: builtins.int
    WRITE_FIELD_NUMBER: builtins.int
    READ_FIELD_NUMBER: builtins.int
    @property
    def fit(self) -> global___MlCommand.Fit: ...
    @property
    def fetch(self) -> pyspark.sql.connect.proto.relations_pb2.Fetch: ...
    @property
    def delete(self) -> global___MlCommand.Delete: ...
    @property
    def write(self) -> global___MlCommand.Write: ...
    @property
    def read(self) -> global___MlCommand.Read: ...
    def __init__(
        self,
        *,
        fit: global___MlCommand.Fit | None = ...,
        fetch: pyspark.sql.connect.proto.relations_pb2.Fetch | None = ...,
        delete: global___MlCommand.Delete | None = ...,
        write: global___MlCommand.Write | None = ...,
        read: global___MlCommand.Read | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "command",
            b"command",
            "delete",
            b"delete",
            "fetch",
            b"fetch",
            "fit",
            b"fit",
            "read",
            b"read",
            "write",
            b"write",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "command",
            b"command",
            "delete",
            b"delete",
            "fetch",
            b"fetch",
            "fit",
            b"fit",
            "read",
            b"read",
            "write",
            b"write",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["command", b"command"]
    ) -> typing_extensions.Literal["fit", "fetch", "delete", "write", "read"] | None: ...

global___MlCommand = MlCommand

class MlCommandResult(google.protobuf.message.Message):
    """The result of MlCommand"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class MlOperatorInfo(google.protobuf.message.Message):
        """Represents an operator info"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        OBJ_REF_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        UID_FIELD_NUMBER: builtins.int
        PARAMS_FIELD_NUMBER: builtins.int
        @property
        def obj_ref(self) -> pyspark.sql.connect.proto.ml_common_pb2.ObjectRef:
            """The cached object which could be a model or summary evaluated by a model"""
        name: builtins.str
        """Operator name"""
        uid: builtins.str
        @property
        def params(self) -> pyspark.sql.connect.proto.ml_common_pb2.MlParams: ...
        def __init__(
            self,
            *,
            obj_ref: pyspark.sql.connect.proto.ml_common_pb2.ObjectRef | None = ...,
            name: builtins.str = ...,
            uid: builtins.str = ...,
            params: pyspark.sql.connect.proto.ml_common_pb2.MlParams | None = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "name", b"name", "obj_ref", b"obj_ref", "params", b"params", "type", b"type"
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "name",
                b"name",
                "obj_ref",
                b"obj_ref",
                "params",
                b"params",
                "type",
                b"type",
                "uid",
                b"uid",
            ],
        ) -> None: ...
        def WhichOneof(
            self, oneof_group: typing_extensions.Literal["type", b"type"]
        ) -> typing_extensions.Literal["obj_ref", "name"] | None: ...

    PARAM_FIELD_NUMBER: builtins.int
    SUMMARY_FIELD_NUMBER: builtins.int
    OPERATOR_INFO_FIELD_NUMBER: builtins.int
    @property
    def param(self) -> pyspark.sql.connect.proto.ml_common_pb2.Param:
        """The result of the attribute"""
    summary: builtins.str
    """Evaluate a Dataset in a model and return the cached ID of summary"""
    @property
    def operator_info(self) -> global___MlCommandResult.MlOperatorInfo:
        """Operator information"""
    def __init__(
        self,
        *,
        param: pyspark.sql.connect.proto.ml_common_pb2.Param | None = ...,
        summary: builtins.str = ...,
        operator_info: global___MlCommandResult.MlOperatorInfo | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "operator_info",
            b"operator_info",
            "param",
            b"param",
            "result_type",
            b"result_type",
            "summary",
            b"summary",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "operator_info",
            b"operator_info",
            "param",
            b"param",
            "result_type",
            b"result_type",
            "summary",
            b"summary",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["result_type", b"result_type"]
    ) -> typing_extensions.Literal["param", "summary", "operator_info"] | None: ...

global___MlCommandResult = MlCommandResult
