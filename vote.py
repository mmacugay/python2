import csv
import os.path

class Vote: 
    file_output = 'files/data.csv'
    def __init__(self):
        self.candidate = ""
        
        

    def vote(self,id:str, candidate:int) -> bool :
        '''
        collects the current data in the csv file and sends the command to store the new data
        '''
        check = True
        if candidate == 1:
            self.candidate = "John"
        elif candidate == 2:
            self.candidate = "Jane"
        with open(Vote.file_output, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == id:
                    check = False
                    return check

        print(self.candidate)
        self.store_vote(id, self.candidate)
        return check

        

        
        
    def store_vote(self, id:str, candidate:str):
        '''
        Writes changes in Jane and John variables to the data.csv from the session.
        '''
        with open(Vote.file_output, 'a', newline="") as csv_file:
            contents = csv.writer(csv_file)
            contents.writerow([id, candidate])