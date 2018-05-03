
import os,csv
import pandas as pd

def path(root_path):

	files_path =[]
	for root, dirs, files in os.walk(root_path):
		files = [f for f in files if not f[0] == '.']
		for name in files:
			files_path.append(os.path.join(root,name))
	print(files_path)
	return files_path

def combinecsv(files_path):

	reader = csv.DictReader(open(files_path))
	header = reader.fieldnames
	print(header)

	for file_path in files_path[1:]:
		with open(file_path,'a') as f:
			writer = csv.DictWriter(f, fieldnames=header)
			writer.writerows(reader)

if __name__ == '__main__':

    combinecsv(path('/Users/*******/Desktop/split/test'))

