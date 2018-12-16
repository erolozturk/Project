# ZED SDK kurulumu
Zed kamera paketlerini çalıştırabilmek için bilgisayarınızda CUDA kurulu olması gerekir.

	https://www.stereolabs.com/developers/release/
Yukarıdaki linkten CUDA sürümünüze uygun ZED SDK paketi indirilir.

	sudo chmod +x ZED_SDK_Ubuntu16_CUDA9_v2.7.1.run
	
İndirilen paket yukarıdaki örnekteki gibi çalıştırılabilir hale getirilir.

	./ZED_SDK_Ubuntu16_CUDA9_v2.7.1.run

Komutu ile ZED SDK paketi kurulumuna başlanır.

# ZED için Ros çalışma dizini oluşturma
	mkdir ~/zed
	cd ~/zed
	mkdir src
	cd src
	git clone https://github.com/stereolabs/zed-ros-wrapper.git
	cd ..
	catkin_make
	source devel/setup.bash
	
Zed çalışma dizinini her terminal açılışında source yapmamak isterseniz bashrc dosyasına ekleme yapmanız gerekmektedir.

	gedit ~/.bashrc
	
Açılan dosyanın alt satırına aşağıdaki satırın eklenmesi gerekir

	source /home/[kullanıcı ismi]/zed/devel/setup.bash
