	mkdir ~/rplidar
	cd ~/rplidar
	mkdir src
	cd src
	git clone -b slam https://github.com/robopeak/rplidar_ros.git
	cd ..
	catkin_make
	source devel/setup.bash

rplidar çalışma dizinini her terminal açılışında source yapmamak isterseniz bashrc dosyasına ekleme yapmanız gerekmektedir.

	gedit ~/.bashrc
	
Açılan dosyanın alt satırına aşağıdaki satırın eklenmesi gerekir

	source /home/[kullanıcı ismi]/rplidar/devel/setup.bash
