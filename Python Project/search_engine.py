import PySimpleGUIWeb as sg
import os
import pickle
from typing import Dict


class Gui:
    def __init__(self):
        self.theme = sg.theme('DarkAmber')
        self.layout = [[sg.Text('Search Term', size=(10,1)), 
                        sg.Input(size=(45,1), focus=True, key="TERM"),
                        sg.Radio('Contains', group_id='choice', key='CONTAINS', default=True),
                        sg.Radio("Starts With", group_id='choice', key="STARTSWITH"),
                        sg.Radio("Ends With", group_id='choice', key="ENDSWITH")],
                        [sg.Text('Root Path', size=(10,1)), 
                        sg.Input('C:/', size=(45,1), key="PATH"), 
                        sg.FolderBrowse('Browse', size=(10,1)), 
                        sg.Button('Re-Index', size=(10,1), key="_INDEX_"), 
                        sg.Button('Search', size=(10,1), bind_return_key=True, key="_SEARCH_")],
                        [sg.Output(size=(50,100))]]
        
        self.window = sg.Window('File Search Engine').Layout(self.layout)


class SearchEngine:
    def __init__(self):
        self.file_index = []
        self.results = []
        self.matches = 0
        self.records = 0

    #Create a new index
    def create_new_index(self, values: Dict[str,str]):
        root_path = values["PATH"]
        self.file_index = [(root, files) for root, dirs, files in os.walk(root_path) if files]

        with open('file_index.pkl', 'wb') as f:
            pickle.dump(self.file_index, f)

    #Load an existing index
    def load_existing_index(self):
        try:
            with open('file.index.pkl', 'rb') as f:
                self.file_index = pickle.load(f)
        except:
            self.file_name = []

    #Search Function
    def search(self, values: Dict[str,str]):

        self.results.clear()
        self.matches = 0
        self.records = 0
        term = values["TERM"]

        for path, files in self.file_index:
            for file in files:
                self.records +=1
                if (values["CONTAINS"] and term.lower() in file.lower() or
                    values["STARTSWITH"] and file.lower().startswith(term.lower()) or
                    values["ENDSWITH"] and file.lower().endswith(term.lower())):

                    result = path.replace('\\','/') + '/' + file
                    self.results.append(result)
                    self.matches += 1
                else:
                    continue

        #Save File
        with open('search_results.txt', 'w') as f:
            for row in self.results:
                f.write(row + '\n')
            

def main():
    g = Gui()
    s = SearchEngine()
    s.load_existing_index()

    while True:
        event, values = g.window.Read()

        if event is None:
            break

        if event == '_INDEX_':
            s.create_new_index(values)
            print()
            print("New Index has been created")
            print()

        
        if event == '_SEARCH_':
            s.search(values)
            print()
            for result in s.results:
                print(result)
            
            print()
            print(f"There were {s.matches} matches out of {s.records} records")
            print()
            print("Results saved in working directory as search_results.txt")
            
if __name__=='__main__':
    print("Starting Program...")
    main()

