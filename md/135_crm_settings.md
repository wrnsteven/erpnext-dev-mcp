---
original_url: https://docs.frappe.io/erpnext/crm_settings
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# CRM Settings

> Introduced in Version 14.

CRM Settings allow you to configure your leads, opportunities, quotations and communication as per the business tules..

To access CRM Settings, go to:

> Home > CRM > Settings > CRM Settings

## Lead

![](/files/Screenshot%202024-06-03%20at%2012.48.00%20PM.png)

### 1. Campaign Naming By

It ensures consistency in the naming convention used by the organisation by automatically generating names for new campaigns based on predefined rules or patterns. It helps users create and maintain unique campaigns and track their effectiveness.

### 2. Allow Lead Duplication based on Emails

If this is enabled, the system will allow users to create multiple leads with the same email address at the same time.

### 3. Auto Creation of Contact

The system will automatically create a new Contact on creation of a Lead.

## Opportunity

![](/files/Screenshot%202024-06-03%20at%2012.54.38%20PM.png)

### 1. Close Replied Opportunity After Days

If there are many Opportunities having a status other than Open, then they will be auto-closed after the no. of days mentioned in this field if there is no action.

## Quotation

![](/files/Screenshot%202024-06-03%20at%2012.56.40%20PM.png)

### 1. Default Quotation Validity Days

You can configure quotations to the customer to be valid only for certain days. In the Quotation, you can update Valid Till Date manually. By default, the Valid Till date is auto-set as 30 days from the Quotation's Posting Date. You can change the no. of days in this field as per your business case.

## Other Settings

![](/files/Screenshot%202024-06-03%20at%2012.58.09%20PM.png)

### 1. Carry Forward Communication and Comments

If this is enabled, When converting a Lead into Opportunity and Opportunity to Quotation, the system will auto copy the emails and comments from the source document.
