# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from collections import OrderedDict

from translate.storage.php import phpfile

from pootle.core.delegate import format_registration, format_classes
from pootle.core.plugin import provider

from .formats import POOTLE_PLUGIN_PHP_FORMATS


@provider(format_registration)
def register_formats(**kwargs_):
    return OrderedDict(POOTLE_PLUGIN_PHP_FORMATS)


@provider(format_classes)
def register_format_classes(**kwargs_):
    return dict(php=phpfile)
