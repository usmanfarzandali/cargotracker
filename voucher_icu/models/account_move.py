# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
from odoo.exceptions import RedirectWarning, UserError, ValidationError
import requests


class AccountMove(models.Model):
    _inherit = "account.move"
    #_inherit = 'mail.thread'


    state = fields.Selection(selection_add = [('icu', 'ICU')])

    @api.multi
    def acion_icu(self):
        self.button_cancel()
        self.state = 'icu'

    
    @api.multi
    def _update_check(self):
        """ Raise Warning to cause rollback if the move is posted, some entries are reconciled or the move is older than the lock date"""
        move_ids = set()
        for line in self:
            err_msg = _('Move name (id): %s (%s)') % (line.move_id.name, str(line.move_id.id))
            if line.move_id.state not in ('draf','icu'):
                raise UserError(_('You cannot do this modification on a posted journal entry, you can just change some non legal fields. You must revert the journal entry to cancel it.\n%s.') % err_msg)
            if line.reconciled and not (line.debit == 0 and line.credit == 0):
                raise UserError(_('You cannot do this modification on a reconciled entry. You can just change some non legal fields or you must unreconcile first.\n%s.') % err_msg)
            if line.move_id.id not in move_ids:
                move_ids.add(line.move_id.id)
        self.env['account.move'].browse(list(move_ids))._check_lock_date()
        return True

    # @api.multi
    # def cancel_voucher(self):
    #     for voucher in self:
    #         voucher.move_id.button_cancel()
    #         voucher.move_id.unlink()
    #     self.write({'state': 'cancel', 'move_id': False})
    