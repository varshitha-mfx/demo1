from odoo import fields, models


class Visitor(models.Model):
    _name = "x_custom.visitor"
    _description = "Visitor"
    _order = "check_in_date desc, id desc"

    name = fields.Char(string="Visitor Name", required=True, index=True)
    phone = fields.Char(string="Phone Number")
    company = fields.Char(string="Company")
    visit_purpose = fields.Text(string="Visit Purpose")
    check_in_date = fields.Datetime(
        string="Check-in Date",
        required=True,
        default=fields.Datetime.now,
        index=True,
    )
    status = fields.Selection(
        selection=[
            ("expected", "Expected"),
            ("checked_in", "Checked In"),
            ("checked_out", "Checked Out"),
            ("cancelled", "Cancelled"),
        ],
        string="Visitor Status",
        required=True,
        default="expected",
        index=True,
    )
