import csv
import os.path

class Vote: 
    file_output = 'files/data.csv'
    def __init__(self):
        self.__john = 0
        self.__jane = 0
        
        
        

    def vote(self, candidate):
        if(os.path.isfile(Vote.file_output)):
            with open(Vote.file_output, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    if row == 0:
                        self.__john = row[1]
                    elif row == 1:
                        self.__jane = row[1]

        if candidate == 1:
            self.__john += 1
        elif candidate == 2:
            self.__jane += 1

        self.store_vote()
        
    def store_vote(self):
        with open(Vote.file_output, 'w', newline="") as csv_file:
            contents = csv.writer(csv_file)
            contents.writerow([("John"), self.__john])
            contents.writerow([("Jane"), self.__jane])