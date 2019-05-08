import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '\\'
LOGS_DIR = ROOT_DIR + 'logs\\'
CONF_FILE = ROOT_DIR + 'config.json'


def does_file_exist(path):
	return os.path.isfile(path)


def write_to_file(path, data):
	file = open(file=path, mode='w')
	file.write(str(data))
	file.close()


def read_from_file(path):
	file = open(file=path, mode='r')
	data = file.read()
	file.close()

	return data


def add_to_file(path, data):
	file = open(file=path, mode='a+')
	file.write(str(data))
	file.close()
