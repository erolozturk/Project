Ubuntu ile çalışan bir bilgisayarda bağlanan usb cihazların port isimleri değişebilmektedir.
Bilgisayarlara bağlanan usb cihazlara sabit bir port ismi vermek için port kurallarının düzenlenmesi gerekir.

lsusb komutu ile bilgisayara bağlı cihazlar aşagıdaki şekilde listelenir.
	
	Bus <bus number> Device <device number>: ID <vendor id>:<product id> <Device name>
	Bus 001 Device 010: ID 1b4f:9d0f Logitech, Inc. Cordless RumblePad 2

lsusb komutu ile bilgisayara bağlı ve sabit port ismi verilecek cihaz bulunmalıdır.

	sudo gedit /etc/udev/rules.d/99-usb-serial.rules

Yukarıdaki komut ile açılan dosyanın içerisine aşağıdaki iki satır eklenip kaydedilmelidir.
	
	ATTRS{idVendor}=="1b4f", SYMLINK+="cihaz_1"
	ATTRS{idProduct}=="9d0f", SYMLINK+="cihaz_1"
	
Bu işlemden sonra aynı id adresine sahip cihazlar cihaz_1 port ismi ile görünmeye başlayacaktır.
