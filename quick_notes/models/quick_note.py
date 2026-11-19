from odoo import fields, models


class QuickNote(models.Model):
    _name = "x_custom.quick_note"
    _description = "Quick Note"
    _order = "created_date desc, id desc"

    name = fields.Char(string="Note Title", required=True, index=True)
    description = fields.Text(string="Description")
    created_date = fields.Datetime(
        string="Created Date",
        required=True,
        default=fields.Datetime.now,
        readonly=True,
        index=True,
    )
    status = fields.Selection(
        selection=[
            ("pending", "Pending"),
            ("completed", "Completed"),
        ],
        string="Status",
        required=True,
        default="pending",
        index=True,
    )

    def action_mark_completed(self):
        self.write({"status": "completed"})
        return True
