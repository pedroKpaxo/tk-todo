run:
	python main.py

build:
	pyinstaller --onefile --windowed --icon=icon.png --add-data "icon.png;." main.py
	bash build.sh