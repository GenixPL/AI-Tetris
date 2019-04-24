import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '\\'
LOGS_DIR = os.path.dirname(os.path.abspath(__file__)) + '\\logs' + '\\'


def does_file_exist(path):
	return os.path.isfile(path)


def write_to_file(path, data):
	file = open(file=path, mode='w')
	file.write(data)
	file.close()


def read_from_file(path):
	file = open(file=path, mode='r')
	data = file.read()
	file.close()

	return data

