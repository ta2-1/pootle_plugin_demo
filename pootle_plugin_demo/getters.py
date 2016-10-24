# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from pootle.core.delegate import formats, data_tool
from pootle.core.plugin import getter

from pootle_format.registry import FormatRegistry
from pootle_data.store_data import StoreDataTool
from pootle_store.models import Store


class CustomStoreDataTool(StoreDataTool):
    pass


class CustomFormatRegistry(FormatRegistry):
    pass


@getter(formats)
def formats_getter(**kwargs_):

    return CustomFormatRegistry()


@getter(data_tool, sender=Store)
def store_data_tool_getter(**kwargs_):
    return CustomStoreDataTool

