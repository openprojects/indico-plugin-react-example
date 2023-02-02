# This file is part of Indico.UN.
# Copyright (C) 2019 - 2023 United Nations. All rights reserved.

from marshmallow import fields

from indico.core.marshmallow import mm
from indico.modules.search.base import SearchTarget
from indico.modules.search.result_schemas import ResultItemSchema
from indico.modules.users import User
from aenum import extend_enum

extend_enum(SearchTarget, 'user', 7)


class UserSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ('id', 'type', 'first_name', 'last_name', 'email', 'avatar_url')

    type = fields.Constant(SearchTarget.user)


class UserResultSchema(mm.Schema):
    class Meta:
        model = User

    id = fields.Int(attribute='id')
    first_name = fields.Str(attribute='first_name')
    last_name = fields.Str(attribute='last_name')
    email = fields.Str(attribute='email')
    avatar_url = fields.Str(attribute='avatar_url')
    type = fields.Constant(SearchTarget.user)


# Add new result type schema for User
ResultItemSchema.type_schemas[SearchTarget.user.name] = UserResultSchema
