# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waflz.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='waflz.proto',
  package='waflz_pb',
  serialized_pb='\n\x0bwaflz.proto\x12\x08waflz_pb\"\xc8\x12\n\x08\x63onfig_t\x12/\n\x08sec_rule\x18\x01 \x03(\x0b\x32\x1d.waflz_pb.config_t.sec_rule_t\x1a\x8a\x12\n\nsec_rule_t\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12@\n\x0b\x61\x63tion_type\x18\n \x01(\x0e\x32+.waflz_pb.config_t.sec_rule_t.action_type_t\x12\x0f\n\x07\x63\x61pture\x18\x0b \x01(\x08\x12\r\n\x05nolog\x18\x0c \x01(\x08\x12\x0b\n\x03log\x18\r \x01(\x08\x12\x12\n\nmultimatch\x18\x0e \x01(\x08\x12\x12\n\nnoauditlog\x18\x0f \x01(\x08\x12\x10\n\x08\x61uditlog\x18\x10 \x01(\x08\x12\x0f\n\x07initcol\x18\x14 \x01(\t\x12\x0e\n\x06status\x18\x15 \x01(\t\x12\x0c\n\x04skip\x18\x16 \x01(\t\x12\x17\n\x0fsanitisematched\x18\x1f \x01(\x08\x12\x10\n\x08\x61\x63\x63uracy\x18\x64 \x01(\t\x12\x10\n\x08maturity\x18\x65 \x01(\t\x12\r\n\x05phase\x18\x66 \x01(\t\x12\x0b\n\x03rev\x18g \x01(\t\x12\x0b\n\x03ver\x18h \x01(\t\x12\x0c\n\x04\x66ile\x18i \x01(\t\x12\x11\n\x08severity\x18\xc8\x01 \x01(\r\x12\x0c\n\x03tag\x18\xac\x02 \x03(\t\x12\x0f\n\x06setvar\x18\x90\x03 \x03(\t\x12\x10\n\x07logdata\x18\x91\x03 \x01(\t\x12?\n\x01t\x18\xf4\x03 \x03(\x0e\x32\x33.waflz_pb.config_t.sec_rule_t.transformation_type_t\x12\x0c\n\x03\x63tl\x18\xd8\x04 \x03(\t\x12\x12\n\tskipafter\x18\xbc\x05 \x01(\t\x12;\n\x08variable\x18\xe8\x07 \x03(\x0b\x32(.waflz_pb.config_t.sec_rule_t.variable_t\x12;\n\x08operator\x18\xe9\x07 \x01(\x0b\x32(.waflz_pb.config_t.sec_rule_t.operator_t\x12\x34\n\x0c\x63hained_rule\x18\xd0\x0f \x03(\x0b\x32\x1d.waflz_pb.config_t.sec_rule_t\x1a\xce\x06\n\nvariable_t\x12=\n\x04type\x18\x01 \x01(\x0e\x32/.waflz_pb.config_t.sec_rule_t.variable_t.type_t\x12\x12\n\nis_negated\x18\x02 \x01(\x08\x12\x10\n\x08is_count\x18\x03 \x01(\x08\x12\r\n\x05match\x18\x64 \x01(\t\"\xcb\x05\n\x06type_t\x12\x08\n\x04\x41RGS\x10\x01\x12\x16\n\x12\x41RGS_COMBINED_SIZE\x10\x02\x12\x0e\n\nARGS_NAMES\x10\x03\x12\t\n\x05\x46ILES\x10\x04\x12\x17\n\x13\x46ILES_COMBINED_SIZE\x10\x05\x12\x0f\n\x0b\x46ILES_NAMES\x10\x06\x12\n\n\x06GLOBAL\x10\x07\x12\x1a\n\x16MULTIPART_STRICT_ERROR\x10\x08\x12 \n\x1cMULTIPART_UNMATCHED_BOUNDARY\x10\t\x12\x10\n\x0cQUERY_STRING\x10\n\x12\x0f\n\x0bREMOTE_ADDR\x10\x0b\x12\x11\n\rREQBODY_ERROR\x10\x0c\x12\x14\n\x10REQUEST_BASENAME\x10\r\x12\x10\n\x0cREQUEST_BODY\x10\x0e\x12\x13\n\x0fREQUEST_COOKIES\x10\x0f\x12\x19\n\x15REQUEST_COOKIES_NAMES\x10\x10\x12\x14\n\x10REQUEST_FILENAME\x10\x11\x12\x13\n\x0fREQUEST_HEADERS\x10\x12\x12\x19\n\x15REQUEST_HEADERS_NAMES\x10\x13\x12\x10\n\x0cREQUEST_LINE\x10\x14\x12\x12\n\x0eREQUEST_METHOD\x10\x15\x12\x14\n\x10REQUEST_PROTOCOL\x10\x16\x12\x0f\n\x0bREQUEST_URI\x10\x17\x12\x0c\n\x08RESOURCE\x10\x18\x12\x11\n\rRESPONSE_BODY\x10\x19\x12\x13\n\x0fRESPONSE_STATUS\x10\x1a\x12\x06\n\x02TX\x10\x1b\x12\x17\n\x13WEBSERVER_ERROR_LOG\x10\x1c\x12\x07\n\x03XML\x10\x1d\x12\x15\n\x11REQBODY_PROCESSOR\x10\x1e\x12\x0c\n\x08\x41RGS_GET\x10\x1f\x12\x12\n\x0e\x41RGS_GET_NAMES\x10 \x12\r\n\tARGS_POST\x10!\x12\x13\n\x0f\x41RGS_POST_NAMES\x10\"\x12\x0f\n\x0bMATCHED_VAR\x10#\x12\x14\n\x10RESPONSE_HEADERS\x10$\x12\x0b\n\x07SESSION\x10%\x1a\x89\x03\n\noperator_t\x12=\n\x04type\x18\x01 \x01(\x0e\x32/.waflz_pb.config_t.sec_rule_t.operator_t.type_t\x12\r\n\x05match\x18\x02 \x01(\t\x12\x10\n\x08is_regex\x18\x03 \x01(\x08\"\x9a\x02\n\x06type_t\x12\x0f\n\x0b\x42\x45GINS_WITH\x10\x01\x12\x0c\n\x08\x43ONTAINS\x10\x02\x12\x11\n\rCONTAINS_WORD\x10\x03\x12\r\n\tENDS_WITH\x10\x04\x12\x06\n\x02\x45Q\x10\x05\x12\x06\n\x02GE\x10\x06\x12\x06\n\x02GT\x10\x07\x12\x06\n\x02LT\x10\x08\x12\x06\n\x02PM\x10\t\x12\x10\n\x0cPM_FROM_FILE\x10\n\x12\x07\n\x03PMF\x10\x0b\x12\x06\n\x02RX\x10\x0c\x12\n\n\x06STR_EQ\x10\r\x12\r\n\tSTR_MATCH\x10\x0e\x12\x17\n\x13VALIDATE_BYTE_RANGE\x10\x0f\x12\x19\n\x15VALIDATE_URL_ENCODING\x10\x10\x12\x1a\n\x16VALIDATE_UTF8_ENCODING\x10\x11\x12\r\n\tVERIFY_CC\x10\x12\x12\n\n\x06WITHIN\x10\x13\"\xb2\x02\n\x15transformation_type_t\x12\x0c\n\x08\x43MD_LINE\x10\x01\x12\x18\n\x14\x43OMPRESS_WHITE_SPACE\x10\x02\x12\x0e\n\nCSS_DECODE\x10\x03\x12\x0e\n\nHEX_ENCODE\x10\x04\x12\x16\n\x12HTML_ENTITY_DECODE\x10\x05\x12\r\n\tJS_DECODE\x10\x06\x12\n\n\x06LENGTH\x10\x07\x12\x0e\n\nLOWER_CASE\x10\x08\x12\x07\n\x03MD5\x10\t\x12\x08\n\x04NONE\x10\n\x12\x12\n\x0eNORMALISE_PATH\x10\x0b\x12\x10\n\x0cREMOVE_NULLS\x10\x0c\x12\x16\n\x12REMOVE_WHITE_SPACE\x10\r\x12\x14\n\x10REPLACE_COMMENTS\x10\x0e\x12\x12\n\x0eURL_DECODE_UNI\x10\x0f\x12\x13\n\x0fUTF8_TO_UNICODE\x10\x10\".\n\raction_type_t\x12\x08\n\x04PASS\x10\x01\x12\t\n\x05\x42LOCK\x10\x02\x12\x08\n\x04\x44\x45NY\x10\x03')



_CONFIG_T_SEC_RULE_T_VARIABLE_T_TYPE_T = _descriptor.EnumDescriptor(
  name='type_t',
  full_name='waflz_pb.config_t.sec_rule_t.variable_t.type_t',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ARGS', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARGS_COMBINED_SIZE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARGS_NAMES', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILES', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILES_COMBINED_SIZE', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILES_NAMES', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLOBAL', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTIPART_STRICT_ERROR', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTIPART_UNMATCHED_BOUNDARY', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_STRING', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_ADDR', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQBODY_ERROR', index=11, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_BASENAME', index=12, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_BODY', index=13, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_COOKIES', index=14, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_COOKIES_NAMES', index=15, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_FILENAME', index=16, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_HEADERS', index=17, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_HEADERS_NAMES', index=18, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_LINE', index=19, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_METHOD', index=20, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_PROTOCOL', index=21, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_URI', index=22, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESOURCE', index=23, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESPONSE_BODY', index=24, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESPONSE_STATUS', index=25, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TX', index=26, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEBSERVER_ERROR_LOG', index=27, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='XML', index=28, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQBODY_PROCESSOR', index=29, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARGS_GET', index=30, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARGS_GET_NAMES', index=31, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARGS_POST', index=32, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARGS_POST_NAMES', index=33, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MATCHED_VAR', index=34, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESPONSE_HEADERS', index=35, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION', index=36, number=37,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=934,
  serialized_end=1649,
)

_CONFIG_T_SEC_RULE_T_OPERATOR_T_TYPE_T = _descriptor.EnumDescriptor(
  name='type_t',
  full_name='waflz_pb.config_t.sec_rule_t.operator_t.type_t',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BEGINS_WITH', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTAINS', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTAINS_WORD', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENDS_WITH', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EQ', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GE', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GT', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LT', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PM', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PM_FROM_FILE', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PMF', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RX', index=11, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STR_EQ', index=12, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STR_MATCH', index=13, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALIDATE_BYTE_RANGE', index=14, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALIDATE_URL_ENCODING', index=15, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALIDATE_UTF8_ENCODING', index=16, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFY_CC', index=17, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WITHIN', index=18, number=19,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1763,
  serialized_end=2045,
)

_CONFIG_T_SEC_RULE_T_TRANSFORMATION_TYPE_T = _descriptor.EnumDescriptor(
  name='transformation_type_t',
  full_name='waflz_pb.config_t.sec_rule_t.transformation_type_t',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CMD_LINE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPRESS_WHITE_SPACE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CSS_DECODE', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEX_ENCODE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTML_ENTITY_DECODE', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JS_DECODE', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LENGTH', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOWER_CASE', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MD5', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONE', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NORMALISE_PATH', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_NULLS', index=11, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_WHITE_SPACE', index=12, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPLACE_COMMENTS', index=13, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_DECODE_UNI', index=14, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UTF8_TO_UNICODE', index=15, number=16,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2048,
  serialized_end=2354,
)

_CONFIG_T_SEC_RULE_T_ACTION_TYPE_T = _descriptor.EnumDescriptor(
  name='action_type_t',
  full_name='waflz_pb.config_t.sec_rule_t.action_type_t',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PASS', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOCK', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DENY', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2356,
  serialized_end=2402,
)


_CONFIG_T_SEC_RULE_T_VARIABLE_T = _descriptor.Descriptor(
  name='variable_t',
  full_name='waflz_pb.config_t.sec_rule_t.variable_t',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='waflz_pb.config_t.sec_rule_t.variable_t.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_negated', full_name='waflz_pb.config_t.sec_rule_t.variable_t.is_negated', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_count', full_name='waflz_pb.config_t.sec_rule_t.variable_t.is_count', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match', full_name='waflz_pb.config_t.sec_rule_t.variable_t.match', index=3,
      number=100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONFIG_T_SEC_RULE_T_VARIABLE_T_TYPE_T,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=803,
  serialized_end=1649,
)

_CONFIG_T_SEC_RULE_T_OPERATOR_T = _descriptor.Descriptor(
  name='operator_t',
  full_name='waflz_pb.config_t.sec_rule_t.operator_t',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='waflz_pb.config_t.sec_rule_t.operator_t.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match', full_name='waflz_pb.config_t.sec_rule_t.operator_t.match', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_regex', full_name='waflz_pb.config_t.sec_rule_t.operator_t.is_regex', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONFIG_T_SEC_RULE_T_OPERATOR_T_TYPE_T,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1652,
  serialized_end=2045,
)

_CONFIG_T_SEC_RULE_T = _descriptor.Descriptor(
  name='sec_rule_t',
  full_name='waflz_pb.config_t.sec_rule_t',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='waflz_pb.config_t.sec_rule_t.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='waflz_pb.config_t.sec_rule_t.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action_type', full_name='waflz_pb.config_t.sec_rule_t.action_type', index=2,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='capture', full_name='waflz_pb.config_t.sec_rule_t.capture', index=3,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nolog', full_name='waflz_pb.config_t.sec_rule_t.nolog', index=4,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log', full_name='waflz_pb.config_t.sec_rule_t.log', index=5,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multimatch', full_name='waflz_pb.config_t.sec_rule_t.multimatch', index=6,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='noauditlog', full_name='waflz_pb.config_t.sec_rule_t.noauditlog', index=7,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auditlog', full_name='waflz_pb.config_t.sec_rule_t.auditlog', index=8,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initcol', full_name='waflz_pb.config_t.sec_rule_t.initcol', index=9,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='waflz_pb.config_t.sec_rule_t.status', index=10,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skip', full_name='waflz_pb.config_t.sec_rule_t.skip', index=11,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sanitisematched', full_name='waflz_pb.config_t.sec_rule_t.sanitisematched', index=12,
      number=31, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accuracy', full_name='waflz_pb.config_t.sec_rule_t.accuracy', index=13,
      number=100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maturity', full_name='waflz_pb.config_t.sec_rule_t.maturity', index=14,
      number=101, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phase', full_name='waflz_pb.config_t.sec_rule_t.phase', index=15,
      number=102, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rev', full_name='waflz_pb.config_t.sec_rule_t.rev', index=16,
      number=103, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ver', full_name='waflz_pb.config_t.sec_rule_t.ver', index=17,
      number=104, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file', full_name='waflz_pb.config_t.sec_rule_t.file', index=18,
      number=105, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='severity', full_name='waflz_pb.config_t.sec_rule_t.severity', index=19,
      number=200, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag', full_name='waflz_pb.config_t.sec_rule_t.tag', index=20,
      number=300, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='setvar', full_name='waflz_pb.config_t.sec_rule_t.setvar', index=21,
      number=400, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logdata', full_name='waflz_pb.config_t.sec_rule_t.logdata', index=22,
      number=401, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='t', full_name='waflz_pb.config_t.sec_rule_t.t', index=23,
      number=500, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ctl', full_name='waflz_pb.config_t.sec_rule_t.ctl', index=24,
      number=600, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skipafter', full_name='waflz_pb.config_t.sec_rule_t.skipafter', index=25,
      number=700, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variable', full_name='waflz_pb.config_t.sec_rule_t.variable', index=26,
      number=1000, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operator', full_name='waflz_pb.config_t.sec_rule_t.operator', index=27,
      number=1001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chained_rule', full_name='waflz_pb.config_t.sec_rule_t.chained_rule', index=28,
      number=2000, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CONFIG_T_SEC_RULE_T_VARIABLE_T, _CONFIG_T_SEC_RULE_T_OPERATOR_T, ],
  enum_types=[
    _CONFIG_T_SEC_RULE_T_TRANSFORMATION_TYPE_T,
    _CONFIG_T_SEC_RULE_T_ACTION_TYPE_T,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=88,
  serialized_end=2402,
)

_CONFIG_T = _descriptor.Descriptor(
  name='config_t',
  full_name='waflz_pb.config_t',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sec_rule', full_name='waflz_pb.config_t.sec_rule', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CONFIG_T_SEC_RULE_T, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=26,
  serialized_end=2402,
)

_CONFIG_T_SEC_RULE_T_VARIABLE_T.fields_by_name['type'].enum_type = _CONFIG_T_SEC_RULE_T_VARIABLE_T_TYPE_T
_CONFIG_T_SEC_RULE_T_VARIABLE_T.containing_type = _CONFIG_T_SEC_RULE_T;
_CONFIG_T_SEC_RULE_T_VARIABLE_T_TYPE_T.containing_type = _CONFIG_T_SEC_RULE_T_VARIABLE_T;
_CONFIG_T_SEC_RULE_T_OPERATOR_T.fields_by_name['type'].enum_type = _CONFIG_T_SEC_RULE_T_OPERATOR_T_TYPE_T
_CONFIG_T_SEC_RULE_T_OPERATOR_T.containing_type = _CONFIG_T_SEC_RULE_T;
_CONFIG_T_SEC_RULE_T_OPERATOR_T_TYPE_T.containing_type = _CONFIG_T_SEC_RULE_T_OPERATOR_T;
_CONFIG_T_SEC_RULE_T.fields_by_name['action_type'].enum_type = _CONFIG_T_SEC_RULE_T_ACTION_TYPE_T
_CONFIG_T_SEC_RULE_T.fields_by_name['t'].enum_type = _CONFIG_T_SEC_RULE_T_TRANSFORMATION_TYPE_T
_CONFIG_T_SEC_RULE_T.fields_by_name['variable'].message_type = _CONFIG_T_SEC_RULE_T_VARIABLE_T
_CONFIG_T_SEC_RULE_T.fields_by_name['operator'].message_type = _CONFIG_T_SEC_RULE_T_OPERATOR_T
_CONFIG_T_SEC_RULE_T.fields_by_name['chained_rule'].message_type = _CONFIG_T_SEC_RULE_T
_CONFIG_T_SEC_RULE_T.containing_type = _CONFIG_T;
_CONFIG_T_SEC_RULE_T_TRANSFORMATION_TYPE_T.containing_type = _CONFIG_T_SEC_RULE_T;
_CONFIG_T_SEC_RULE_T_ACTION_TYPE_T.containing_type = _CONFIG_T_SEC_RULE_T;
_CONFIG_T.fields_by_name['sec_rule'].message_type = _CONFIG_T_SEC_RULE_T
DESCRIPTOR.message_types_by_name['config_t'] = _CONFIG_T

class config_t(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class sec_rule_t(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType

    class variable_t(_message.Message):
      __metaclass__ = _reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _CONFIG_T_SEC_RULE_T_VARIABLE_T

      # @@protoc_insertion_point(class_scope:waflz_pb.config_t.sec_rule_t.variable_t)

    class operator_t(_message.Message):
      __metaclass__ = _reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _CONFIG_T_SEC_RULE_T_OPERATOR_T

      # @@protoc_insertion_point(class_scope:waflz_pb.config_t.sec_rule_t.operator_t)
    DESCRIPTOR = _CONFIG_T_SEC_RULE_T

    # @@protoc_insertion_point(class_scope:waflz_pb.config_t.sec_rule_t)
  DESCRIPTOR = _CONFIG_T

  # @@protoc_insertion_point(class_scope:waflz_pb.config_t)


# @@protoc_insertion_point(module_scope)
