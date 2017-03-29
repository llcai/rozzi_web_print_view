# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2012 Agile Business Group sagl (<http://www.agilebg.com>)
#    Copyright (C) 2012 Domsense srl (<http://www.domsense.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Rozzi Web Print View',
    'version': '10.0.1.2.0',
    'category': 'Other',
    'author': "Rozzi(410881525@qq.com)",
    'website': 'http://www.csfinox.cn',
    'depends': [
        'web',
    ],
    'data': [
        'view/web_print_view.xml',
    ],
    'qweb': [
        'static/src/xml/web_print_view_template.xml',
    ],
    'summary':'What you see and what you print',
    'description': """
What you see and what you print
    """,
    'installable': True,
    'auto_install': False,
    'price':99.99,
    'currency': 'EUR',
    'license': 'OPL-1',
    'application': True,
}
