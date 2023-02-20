

:: type venv.bat in the root directory
::This is the batch file to create virtual environment and install all required packages listed on requirements.txt



python -m venv venv

mkdir data

mkdir attendance

pip install -r requirements.txt