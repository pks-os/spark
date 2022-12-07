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
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spark/connect/expressions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyspark.sql.connect.proto import types_pb2 as spark_dot_connect_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1fspark/connect/expressions.proto\x12\rspark.connect\x1a\x19spark/connect/types.proto"\xd2\x14\n\nExpression\x12=\n\x07literal\x18\x01 \x01(\x0b\x32!.spark.connect.Expression.LiteralH\x00R\x07literal\x12\x62\n\x14unresolved_attribute\x18\x02 \x01(\x0b\x32-.spark.connect.Expression.UnresolvedAttributeH\x00R\x13unresolvedAttribute\x12_\n\x13unresolved_function\x18\x03 \x01(\x0b\x32,.spark.connect.Expression.UnresolvedFunctionH\x00R\x12unresolvedFunction\x12Y\n\x11\x65xpression_string\x18\x04 \x01(\x0b\x32*.spark.connect.Expression.ExpressionStringH\x00R\x10\x65xpressionString\x12S\n\x0funresolved_star\x18\x05 \x01(\x0b\x32(.spark.connect.Expression.UnresolvedStarH\x00R\x0eunresolvedStar\x12\x37\n\x05\x61lias\x18\x06 \x01(\x0b\x32\x1f.spark.connect.Expression.AliasH\x00R\x05\x61lias\x12\x34\n\x04\x63\x61st\x18\x07 \x01(\x0b\x32\x1e.spark.connect.Expression.CastH\x00R\x04\x63\x61st\x1ap\n\x04\x43\x61st\x12-\n\x04\x65xpr\x18\x01 \x01(\x0b\x32\x19.spark.connect.ExpressionR\x04\x65xpr\x12\x39\n\x0c\x63\x61st_to_type\x18\x02 \x01(\x0b\x32\x17.spark.connect.DataTypeR\ncastToType\x1a\xb2\x0b\n\x07Literal\x12\x14\n\x04null\x18\x01 \x01(\x08H\x00R\x04null\x12\x18\n\x06\x62inary\x18\x02 \x01(\x0cH\x00R\x06\x62inary\x12\x1a\n\x07\x62oolean\x18\x03 \x01(\x08H\x00R\x07\x62oolean\x12\x14\n\x04\x62yte\x18\x04 \x01(\x05H\x00R\x04\x62yte\x12\x16\n\x05short\x18\x05 \x01(\x05H\x00R\x05short\x12\x1a\n\x07integer\x18\x06 \x01(\x05H\x00R\x07integer\x12\x14\n\x04long\x18\x07 \x01(\x03H\x00R\x04long\x12\x16\n\x05\x66loat\x18\n \x01(\x02H\x00R\x05\x66loat\x12\x18\n\x06\x64ouble\x18\x0b \x01(\x01H\x00R\x06\x64ouble\x12\x45\n\x07\x64\x65\x63imal\x18\x0c \x01(\x0b\x32).spark.connect.Expression.Literal.DecimalH\x00R\x07\x64\x65\x63imal\x12\x18\n\x06string\x18\r \x01(\tH\x00R\x06string\x12\x14\n\x04\x64\x61te\x18\x10 \x01(\x05H\x00R\x04\x64\x61te\x12\x1e\n\ttimestamp\x18\x11 \x01(\x03H\x00R\ttimestamp\x12%\n\rtimestamp_ntz\x18\x12 \x01(\x03H\x00R\x0ctimestampNtz\x12\x61\n\x11\x63\x61lendar_interval\x18\x13 \x01(\x0b\x32\x32.spark.connect.Expression.Literal.CalendarIntervalH\x00R\x10\x63\x61lendarInterval\x12\x30\n\x13year_month_interval\x18\x14 \x01(\x05H\x00R\x11yearMonthInterval\x12,\n\x11\x64\x61y_time_interval\x18\x15 \x01(\x03H\x00R\x0f\x64\x61yTimeInterval\x12?\n\x05\x61rray\x18\x16 \x01(\x0b\x32\'.spark.connect.Expression.Literal.ArrayH\x00R\x05\x61rray\x12\x42\n\x06struct\x18\x17 \x01(\x0b\x32(.spark.connect.Expression.Literal.StructH\x00R\x06struct\x12\x39\n\x03map\x18\x18 \x01(\x0b\x32%.spark.connect.Expression.Literal.MapH\x00R\x03map\x12\x1a\n\x08nullable\x18\x32 \x01(\x08R\x08nullable\x12\x38\n\x18type_variation_reference\x18\x33 \x01(\rR\x16typeVariationReference\x1au\n\x07\x44\x65\x63imal\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x12!\n\tprecision\x18\x02 \x01(\x05H\x00R\tprecision\x88\x01\x01\x12\x19\n\x05scale\x18\x03 \x01(\x05H\x01R\x05scale\x88\x01\x01\x42\x0c\n\n_precisionB\x08\n\x06_scale\x1a\x62\n\x10\x43\x61lendarInterval\x12\x16\n\x06months\x18\x01 \x01(\x05R\x06months\x12\x12\n\x04\x64\x61ys\x18\x02 \x01(\x05R\x04\x64\x61ys\x12"\n\x0cmicroseconds\x18\x03 \x01(\x03R\x0cmicroseconds\x1a\x43\n\x06Struct\x12\x39\n\x06\x66ields\x18\x01 \x03(\x0b\x32!.spark.connect.Expression.LiteralR\x06\x66ields\x1a\x42\n\x05\x41rray\x12\x39\n\x06values\x18\x01 \x03(\x0b\x32!.spark.connect.Expression.LiteralR\x06values\x1a\xbd\x01\n\x03Map\x12@\n\x05pairs\x18\x01 \x03(\x0b\x32*.spark.connect.Expression.Literal.Map.PairR\x05pairs\x1at\n\x04Pair\x12\x33\n\x03key\x18\x01 \x01(\x0b\x32!.spark.connect.Expression.LiteralR\x03key\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32!.spark.connect.Expression.LiteralR\x05valueB\x0e\n\x0cliteral_type\x1a\x46\n\x13UnresolvedAttribute\x12/\n\x13unparsed_identifier\x18\x01 \x01(\tR\x12unparsedIdentifier\x1a\xcc\x01\n\x12UnresolvedFunction\x12#\n\rfunction_name\x18\x01 \x01(\tR\x0c\x66unctionName\x12\x37\n\targuments\x18\x02 \x03(\x0b\x32\x19.spark.connect.ExpressionR\targuments\x12\x1f\n\x0bis_distinct\x18\x03 \x01(\x08R\nisDistinct\x12\x37\n\x18is_user_defined_function\x18\x04 \x01(\x08R\x15isUserDefinedFunction\x1a\x32\n\x10\x45xpressionString\x12\x1e\n\nexpression\x18\x01 \x01(\tR\nexpression\x1a(\n\x0eUnresolvedStar\x12\x16\n\x06target\x18\x01 \x03(\tR\x06target\x1ax\n\x05\x41lias\x12-\n\x04\x65xpr\x18\x01 \x01(\x0b\x32\x19.spark.connect.ExpressionR\x04\x65xpr\x12\x12\n\x04name\x18\x02 \x03(\tR\x04name\x12\x1f\n\x08metadata\x18\x03 \x01(\tH\x00R\x08metadata\x88\x01\x01\x42\x0b\n\t_metadataB\x0b\n\texpr_typeB"\n\x1eorg.apache.spark.connect.protoP\x01\x62\x06proto3'
)


_EXPRESSION = DESCRIPTOR.message_types_by_name["Expression"]
_EXPRESSION_CAST = _EXPRESSION.nested_types_by_name["Cast"]
_EXPRESSION_LITERAL = _EXPRESSION.nested_types_by_name["Literal"]
_EXPRESSION_LITERAL_DECIMAL = _EXPRESSION_LITERAL.nested_types_by_name["Decimal"]
_EXPRESSION_LITERAL_CALENDARINTERVAL = _EXPRESSION_LITERAL.nested_types_by_name["CalendarInterval"]
_EXPRESSION_LITERAL_STRUCT = _EXPRESSION_LITERAL.nested_types_by_name["Struct"]
_EXPRESSION_LITERAL_ARRAY = _EXPRESSION_LITERAL.nested_types_by_name["Array"]
_EXPRESSION_LITERAL_MAP = _EXPRESSION_LITERAL.nested_types_by_name["Map"]
_EXPRESSION_LITERAL_MAP_PAIR = _EXPRESSION_LITERAL_MAP.nested_types_by_name["Pair"]
_EXPRESSION_UNRESOLVEDATTRIBUTE = _EXPRESSION.nested_types_by_name["UnresolvedAttribute"]
_EXPRESSION_UNRESOLVEDFUNCTION = _EXPRESSION.nested_types_by_name["UnresolvedFunction"]
_EXPRESSION_EXPRESSIONSTRING = _EXPRESSION.nested_types_by_name["ExpressionString"]
_EXPRESSION_UNRESOLVEDSTAR = _EXPRESSION.nested_types_by_name["UnresolvedStar"]
_EXPRESSION_ALIAS = _EXPRESSION.nested_types_by_name["Alias"]
Expression = _reflection.GeneratedProtocolMessageType(
    "Expression",
    (_message.Message,),
    {
        "Cast": _reflection.GeneratedProtocolMessageType(
            "Cast",
            (_message.Message,),
            {
                "DESCRIPTOR": _EXPRESSION_CAST,
                "__module__": "spark.connect.expressions_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Expression.Cast)
            },
        ),
        "Literal": _reflection.GeneratedProtocolMessageType(
            "Literal",
            (_message.Message,),
            {
                "Decimal": _reflection.GeneratedProtocolMessageType(
                    "Decimal",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _EXPRESSION_LITERAL_DECIMAL,
                        "__module__": "spark.connect.expressions_pb2"
                        # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal.Decimal)
                    },
                ),
                "CalendarInterval": _reflection.GeneratedProtocolMessageType(
                    "CalendarInterval",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _EXPRESSION_LITERAL_CALENDARINTERVAL,
                        "__module__": "spark.connect.expressions_pb2"
                        # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal.CalendarInterval)
                    },
                ),
                "Struct": _reflection.GeneratedProtocolMessageType(
                    "Struct",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _EXPRESSION_LITERAL_STRUCT,
                        "__module__": "spark.connect.expressions_pb2"
                        # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal.Struct)
                    },
                ),
                "Array": _reflection.GeneratedProtocolMessageType(
                    "Array",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _EXPRESSION_LITERAL_ARRAY,
                        "__module__": "spark.connect.expressions_pb2"
                        # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal.Array)
                    },
                ),
                "Map": _reflection.GeneratedProtocolMessageType(
                    "Map",
                    (_message.Message,),
                    {
                        "Pair": _reflection.GeneratedProtocolMessageType(
                            "Pair",
                            (_message.Message,),
                            {
                                "DESCRIPTOR": _EXPRESSION_LITERAL_MAP_PAIR,
                                "__module__": "spark.connect.expressions_pb2"
                                # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal.Map.Pair)
                            },
                        ),
                        "DESCRIPTOR": _EXPRESSION_LITERAL_MAP,
                        "__module__": "spark.connect.expressions_pb2"
                        # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal.Map)
                    },
                ),
                "DESCRIPTOR": _EXPRESSION_LITERAL,
                "__module__": "spark.connect.expressions_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal)
            },
        ),
        "UnresolvedAttribute": _reflection.GeneratedProtocolMessageType(
            "UnresolvedAttribute",
            (_message.Message,),
            {
                "DESCRIPTOR": _EXPRESSION_UNRESOLVEDATTRIBUTE,
                "__module__": "spark.connect.expressions_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Expression.UnresolvedAttribute)
            },
        ),
        "UnresolvedFunction": _reflection.GeneratedProtocolMessageType(
            "UnresolvedFunction",
            (_message.Message,),
            {
                "DESCRIPTOR": _EXPRESSION_UNRESOLVEDFUNCTION,
                "__module__": "spark.connect.expressions_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Expression.UnresolvedFunction)
            },
        ),
        "ExpressionString": _reflection.GeneratedProtocolMessageType(
            "ExpressionString",
            (_message.Message,),
            {
                "DESCRIPTOR": _EXPRESSION_EXPRESSIONSTRING,
                "__module__": "spark.connect.expressions_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Expression.ExpressionString)
            },
        ),
        "UnresolvedStar": _reflection.GeneratedProtocolMessageType(
            "UnresolvedStar",
            (_message.Message,),
            {
                "DESCRIPTOR": _EXPRESSION_UNRESOLVEDSTAR,
                "__module__": "spark.connect.expressions_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Expression.UnresolvedStar)
            },
        ),
        "Alias": _reflection.GeneratedProtocolMessageType(
            "Alias",
            (_message.Message,),
            {
                "DESCRIPTOR": _EXPRESSION_ALIAS,
                "__module__": "spark.connect.expressions_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Expression.Alias)
            },
        ),
        "DESCRIPTOR": _EXPRESSION,
        "__module__": "spark.connect.expressions_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Expression)
    },
)
_sym_db.RegisterMessage(Expression)
_sym_db.RegisterMessage(Expression.Cast)
_sym_db.RegisterMessage(Expression.Literal)
_sym_db.RegisterMessage(Expression.Literal.Decimal)
_sym_db.RegisterMessage(Expression.Literal.CalendarInterval)
_sym_db.RegisterMessage(Expression.Literal.Struct)
_sym_db.RegisterMessage(Expression.Literal.Array)
_sym_db.RegisterMessage(Expression.Literal.Map)
_sym_db.RegisterMessage(Expression.Literal.Map.Pair)
_sym_db.RegisterMessage(Expression.UnresolvedAttribute)
_sym_db.RegisterMessage(Expression.UnresolvedFunction)
_sym_db.RegisterMessage(Expression.ExpressionString)
_sym_db.RegisterMessage(Expression.UnresolvedStar)
_sym_db.RegisterMessage(Expression.Alias)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\036org.apache.spark.connect.protoP\001"
    _EXPRESSION._serialized_start = 78
    _EXPRESSION._serialized_end = 2720
    _EXPRESSION_CAST._serialized_start = 639
    _EXPRESSION_CAST._serialized_end = 751
    _EXPRESSION_LITERAL._serialized_start = 754
    _EXPRESSION_LITERAL._serialized_end = 2212
    _EXPRESSION_LITERAL_DECIMAL._serialized_start = 1650
    _EXPRESSION_LITERAL_DECIMAL._serialized_end = 1767
    _EXPRESSION_LITERAL_CALENDARINTERVAL._serialized_start = 1769
    _EXPRESSION_LITERAL_CALENDARINTERVAL._serialized_end = 1867
    _EXPRESSION_LITERAL_STRUCT._serialized_start = 1869
    _EXPRESSION_LITERAL_STRUCT._serialized_end = 1936
    _EXPRESSION_LITERAL_ARRAY._serialized_start = 1938
    _EXPRESSION_LITERAL_ARRAY._serialized_end = 2004
    _EXPRESSION_LITERAL_MAP._serialized_start = 2007
    _EXPRESSION_LITERAL_MAP._serialized_end = 2196
    _EXPRESSION_LITERAL_MAP_PAIR._serialized_start = 2080
    _EXPRESSION_LITERAL_MAP_PAIR._serialized_end = 2196
    _EXPRESSION_UNRESOLVEDATTRIBUTE._serialized_start = 2214
    _EXPRESSION_UNRESOLVEDATTRIBUTE._serialized_end = 2284
    _EXPRESSION_UNRESOLVEDFUNCTION._serialized_start = 2287
    _EXPRESSION_UNRESOLVEDFUNCTION._serialized_end = 2491
    _EXPRESSION_EXPRESSIONSTRING._serialized_start = 2493
    _EXPRESSION_EXPRESSIONSTRING._serialized_end = 2543
    _EXPRESSION_UNRESOLVEDSTAR._serialized_start = 2545
    _EXPRESSION_UNRESOLVEDSTAR._serialized_end = 2585
    _EXPRESSION_ALIAS._serialized_start = 2587
    _EXPRESSION_ALIAS._serialized_end = 2707
# @@protoc_insertion_point(module_scope)
