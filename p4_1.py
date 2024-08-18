date = input()  # (mm/dd/yyyy)
months = "JANFEBMARAPRMAYJUNJULAUGSEPOCTNOVDEC"
d = date[3:5]
m = months[3*int(date[:2])-3: 3*int(date[:2])]
y = date[6:]
print(d, m, y)
