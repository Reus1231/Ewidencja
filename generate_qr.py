import qrcode
img = qrcode.make('https://ewidencja-borowek.onrender.com/harvest_overview')
img.save('harvest_overview_qr.png')