import json
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '\\'
LOGS_DIR = ROOT_DIR + 'logs\\'
CONF_FILE = ROOT_DIR + 'config.json'


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


def get_mutations_from_config():
	data = read_from_file(CONF_FILE)
	conf = json.loads(data)

	return conf['max_num_of_mutations']


def get_bots_number_from_config():
	data = read_from_file(CONF_FILE)
	conf = json.loads(data)

	return conf['number_of_bots']


def get_mutation_chance():
	data = read_from_file(CONF_FILE)
	conf = json.loads(data)

	return conf['mutation_chance_percent']


def add_to_file(path, data):
	file = open(file=path, mode='a+')
	file.write(data)
	file.close()

