# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import pandas as pd
import csv
from thefuzz import fuzz
from thefuzz import process
import functools
import operator

#
# class ActionHelloWorld(Action):
#
#    def name(self) -> Text:
#         return "action_hello_world"
#
#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#        dispatcher.utter_message(text="Hello World!")
#
#        return []
class GetAnswer(Action):
     def __init__(self):
     #轉檔
         self.faq_d = pd.read_csv('./actions/FAQ.csv')
         qss = list(self.faq_d['question'])
         with open("./data/ygm.yml", "wt", encoding="utf-8") as f:
             f.write('version: "3.1"\n')
             f.write("nlu: \n- intent: question\n  examples: | \n")
             for q in qss:
                 f.write(f"    - {q}\n") 
        
        
     def name(self) -> Text:
        return "action_get_answer"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
            csvfile = open(r"./actions/FAQ.csv",encoding='utf-8')
            reader = csv.reader(csvfile)
            #question
            question = tracker.latest_message['text'] 
            #fuzzywuzzy
            data_list = list(self.faq_d['question'])
            qa = process.extractOne(question,data_list)
            qa1 = functools.reduce(operator.add, str(qa))
            qa_f = qa1[2:-7]
            for row in reader:
                # check
                if qa_f in row[0]:
                    print(row[1])
                    answer = row[1]
                    dispatcher.utter_message(text = str(answer))
                    break;                     
                    return []
     
           
