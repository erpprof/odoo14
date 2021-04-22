# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError, AccessError
from datetime import datetime
from dateutil import relativedelta
import base64
from random import choice
from string import digits
from werkzeug.urls import url_encode


class AccountTax(models.Model):
    _name = 'account.tax'
    _inherit = ['account.tax', 'mail.thread']