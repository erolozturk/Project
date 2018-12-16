Ros ile iki veya daha fazla bilgisayarı birbirine bağlayıp tek bir ros master ile kontrol etmek mümkündür.
Ros ile bilgisayarlara bağlantı kurmak için tüm bilgisayarların aynı ağda olması gerekir ve ip adreslerinin bilinmesi gerekir.

Terminalde ifconfig yazarak bilgisayarların ip adresleri öğrenilebilir.

Yapılacak işlemler için ilk önce master bilgisayar belirlenir. 
Örnek olarak master bilgisayar A diyelim ve ip adresi 192.168.0.105 olsun.
Ros ile bağlanılacak bilgisayara B diyelim ve ip adresi 192.168.0.120 olsun.

A bilgisayarında roscore komutu ile bir master oluşturulur.
B bilgisayarının terminal ekranı açılır.
	
	export ROS_IP=192.168.0.120  #B bilgisayarının kendi ip adresi yazılır
	export ROS_MASTER_URI=http://192.168.0.105:11311 #ros master A bilgisayarının ip adresi yazılır
	
Yukarıdaki iki satır B bilgisayarının terminaline yazılır.
Bu işlemler doğru yapılırsa B bilgisayarında yayınlanan bir topic A bilgisayarında da görünür.

B bilgisayarının devamlı olarak ros master ile A bilgisayarına bağlanmasını istersek, B bilgisayarının bashrc dosyasına ekleme yapılması gerekir.
	
	gedit ~/.bashrc

Açılan dosyanın alt satırlarına aşağıdaki satırlar eklenmelidir.
	
	export ROS_IP=192.168.0.120  #B bilgisayarının kendi ip adresi yazılır
	export ROS_MASTER_URI=http://192.168.0.105:11311 #ros master A bilgisayarının ip adresi yazılır
