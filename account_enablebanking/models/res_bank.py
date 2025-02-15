from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class ResBank(models.Model):
    _inherit = "res.bank"

    def action_authorize_bank(self):
        if not self.country:
            raise ValidationError("Set a country for the bank")
        company_id = self.env.user.company_id
        auth_url = company_id.action_sync_transactions_with_enable_banking(self)
        return {
            'type': 'ir.actions.act_url',
            'url': auth_url.get("url"),
            'target': 'self'
        }


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    account_uuid = fields.Char(string="Account UUID")

