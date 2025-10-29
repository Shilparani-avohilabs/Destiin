# Copyright (c) 2025, shilpa@avohilabs.com and contributors
# For license information, please see license.txt

# import frappe
#from frappe.model.document import Document


#class EmployeePolicyData(Document):
#	pass



mport frappe
import json
from frappe.model.document import Document

class EmployeeActivity(Document):
    pass


@frappe.whitelist(allow_guest=False)
def get_all_activities():
    """Fetch all Employee Activities"""
    activities = frappe.get_all(
        "Employee Activity",
        fields=["name", "employee", "employee_name", "company", "booking_stage"]
    )
    return activities


@frappe.whitelist(allow_guest=False)
def create_activity():
    """Create a new Employee Activity from raw JSON body"""
    try:
        # Handle both raw JSON and x-www-form-urlencoded inputs
        if frappe.form_dict.get("data"):
            data = json.loads(frappe.form_dict.data)
        elif frappe.request.data:
            data = json.loads(frappe.request.data)
        else:
            frappe.throw("Missing request body")

        doc = frappe.get_doc({
            "doctype": "Employee Activity",
            **data
        })
        doc.insert(ignore_permissions=True)
        frappe.db.commit()

        return {
            "success": True,
            "message": "Employee Activity created successfully",
            "name": doc.name
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "create_activity API Error")
        return {"success": False, "error": str(e)}