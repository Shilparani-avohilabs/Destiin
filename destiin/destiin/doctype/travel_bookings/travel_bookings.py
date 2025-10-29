# Copyright (c) 2025, shilpa@avohilabs.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TravelBookings(Document):
    pass


@frappe.whitelist(allow_guest=False)
def get_all_bookings():
    """Fetch all travel bookings"""
    bookings = frappe.get_all(
        "Travel Bookings",
        fields=["name", "employee_name", "booking_id", "hotel_name", "check_in_date", "check_out_date", "booking_status"]
    )
    return bookings


@frappe.whitelist(allow_guest=False)
def create_booking(data):
    """Create a new booking"""
    import json
    try:
        data = json.loads(data) if isinstance(data, str) else data
        doc = frappe.get_doc({
            "doctype": "Travel Bookings",
            **data
        })
        doc.insert(ignore_permissions=True)
        frappe.db.commit()
        return {
            "success": True,
            "message": "Booking created successfully",
            "name": doc.name
        }
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "create_booking API Error")
        return {"success": False, "error": str(e)}
