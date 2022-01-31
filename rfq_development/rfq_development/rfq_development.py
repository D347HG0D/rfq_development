import frappe



def validate_for_items(self, method):
	for d in self.get('items'):
		altic = {}
		altic = frappe.db.sql_list("""SELECT alternative_item_code FROM `tabItem Alternative` WHERE item_code = %s""",d.item_code)

		for i in range(0, len(altic)):
			item_supplier = frappe.db.get_value('Item Supplier',{"parent":'Item', "parent":altic[i]},'supplier')
			item_manufacturers = frappe.db.sql_list("""SELECT manufacturer FROM `tabItem Manufacturer` WHERE item_code = %s""",altic[i])
			print(item_supplier)
			print(item_manufacturers)
			print('XXXXXXX')
			print(item_supplier)
			for s in self.get('suppliers'):
				for m in range(0, len(item_manufacturers)):
					print(s.supplier)
					print(item_manufacturers[m])
					if s.supplier == item_supplier:
						doc = frappe.get_doc(self)
						row = doc.append('items',{})
						row.item_code = altic[i]
						row.qty = d.qty
						row.description = altic[i]
						row.uom = "Nos"
						row.conversion_factor = 1
						row.warehouse = d.warehouse
						row.schedule_date = d.schedule_date
						row.manufacturer = item_manufacturers[m]
						row.insert()

