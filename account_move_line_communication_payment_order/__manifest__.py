# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2021- Vertel AB (<https://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Account: Move Line Communtication Payment Order',
    'version': '14.0.0.0.1',
    # Version ledger: 14.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary':'Sets payment. Lines communication field to the name of the account. Move as a last resort.',
    'category': 'Accounting',
    #'sequence': '1'
    'author': 'Vertel AB',
    'website': 'https://vertel.se/apps/odoo-account/account_move_line_communication_payment_order',
    'images': ['/static/description/banner.png'], # 560x280 px.
    'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-account',
    'description': """
        This module makes it possible to make account.payment.lines out of account.move.lines whos "res" field is blank.
        The account.payment.lines set their \"communication\" field to account.moves \"res\" field which is a required 
        field and is always blank. When I know what I should fill the account.move res field with then I will change this module.
        """,
    'depends': ['account_payment_order'],
    'data': [
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
