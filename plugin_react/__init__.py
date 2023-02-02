# This file is part of Indico.UN.
# Copyright (C) 2019 - 2023 United Nations. All rights reserved.

from plugin_react.schemas import UserResultSchema
from plugin_react.schemas import UserSchema

from indico.core import signals
from indico.core.plugins import IndicoPlugin
from indico.modules.search.base import SearchTarget
from indico.modules.search.internal import InternalSearch
from indico.modules.users import User


class IndicoReactPlugin(IndicoPlugin):
    """Example Plugin
    An example plugin that demonstrates the capabilities of the new Indico plugin system.
    """

    configurable = False

    def init(self):
        super(IndicoReactPlugin, self).init()
        self.inject_bundle('search.js')


@signals.core.get_search_providers.connect
def _un_search(*args, **kwargs):
    return UNSearch


class UNSearch(InternalSearch):

    def search(self, query, user=None, page=None, object_types=(), *, admin_override_enabled=False, **params):
        category_id = params.get('category_id')
        event_id = params.get('event_id')
        if object_types == [SearchTarget.user]:
            pagenav, results = self.search_user(query, user, page, category_id, event_id,
                                                admin_override_enabled)
            return {
                'total': -1 if results else 0,
                'pagenav': pagenav,
                'results': results,
            }

        return super(UNSearch, self).search(query, user, page, object_types,
                                            admin_override_enabled=admin_override_enabled, **params)

    def _can_access(self, user, obj, allow_effective_protection_mode=True, admin_override_enabled=False):
        if isinstance(obj, User):
            return True  # TODO: Implement Un PMS

        return super(UNSearch, self)._can_access(user, obj, allow_effective_protection_mode=True,
                                                 admin_override_enabled=False)

    def search_user(self, q, user, page, category_id, event_id, admin_override_enabled):
        query = User.query.filter_by(first_name=q)  # TODO: Implement the serach like it was on V2
        query.filter(~User.is_deleted)
        objs, pagenav = self._paginate(query, page, User.id, user, admin_override_enabled)
        res = UserSchema(many=True).dump(objs)
        return pagenav, UserResultSchema(many=True).load(res)

    def _preload_categories(self, objs, preloaded_categories):
        obj_types = {type(o) for o in objs}
        assert len(obj_types) == 1
        obj_type = obj_types.pop()

        if obj_type == User:
            return

        return super(UNSearch, self)._preload_categories(objs, preloaded_categories)
