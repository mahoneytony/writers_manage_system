import datetime
def dl_transform(client_val):
	client_val = client_val.strip()
	separator_index = client_val.index(':')
	hours = int(client_val[:separator_index].strip())
	minutes = int(client_val[separator_index+1:-2].strip())
	if client_val[-2:] == 'AM':
		return datetime.time(hours, minutes)
	elif client_val[-2:] == 'PM':
		hours += 12
		return datetime.time(hours, minutes)

print (dl_transform('4:25 AM'))
print (dl_transform('4:25 PM'))
