# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
#class ActionHelloWorld(Action):
#
  #  def name(self) -> Text:
   #     return "action_hello_world"
#
    #def run(self, dispatcher: CollectingDispatcher,
     #       tracker: Tracker,
      #      domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
       # dispatcher.utter_message(text="Hello World!")
#
        #return []
#actions.py


class ActionAskRoomType(Action):
    def name(self) -> Text:
        return "action_ask_room_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("What type of room would you like to book?")
        return []

class ActionConfirmRoomType(Action):
    def name(self) -> Text:
        return "action_confirm_room_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        room_type = tracker.latest_message['entities'][0]['value']
        dispatcher.utter_message(f"You've chosen the {room_type} room.")
        return []

class ActionAskVacationPeriod(Action):
    def name(self) -> Text:
        return "action_ask_vacation_period"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("What dates are you planning for your vacation?")
        return []

class ActionConfirmVacationPeriod(Action):
    def name(self) -> Text:
        return "action_confirm_vacation_period"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        start_date = tracker.get_slot("start_date")
        end_date = tracker.get_slot("end_date")
        dispatcher.utter_message(f"You've chosen the vacation period from {start_date} to {end_date}.")
        return []
    
from rasa_sdk.forms import FormAction
import pandas as pd 
class ActionCheckAvailability(Action):
    #aden_calendre=pd.read_csv
    def name(self) -> Text:
        return "action_check_availability"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("Let me check our availability please.")
        
        return []    
    

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import pandas as pd
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckAvailabilityConfirmation(Action):
    aden_calendre = pd.read_csv("aden_calendre.csv")

    def name(self) -> Text:
        return "action_check_availability_confirmation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        start_date = tracker.get_slot("start_date")
        end_date = tracker.get_slot("end_date")
        room_type = tracker.get_slot("room_type")
        
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        
        
        if any((start_date <= date <= end_date) for date in self.aden_calendre['dates']):
            dispatcher.utter_message("Sorry, there is no available rooms in this date range.")
        else:
            
            if room_type in self.aden_calendre['room'].values:
                dispatcher.utter_message(f"Sorry, there is no available {room_type} rooms in this date range.")
            else:
                dispatcher.utter_message(f"Your reservation for {room_type} rooms in this date range is confirmed.")
        
        return []


    
    
class ActionAskCustomerDetails(Action):
    def name(self) -> Text:
        return "action_ask_customer_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Could you provide with your gendre , name and Location ? ")
        return []

class ActionConfirmCustomerDetails(Action):
    def name(self) -> Text:
        return "action_confirm_customer_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        gendre = tracker.get_slot("gendre")
        
        name = tracker.get_slot("name")
        
        location = tracker.get_slot("location")
        if (gendre== "Male"):
            gn="Mister"
        else :
            gn="Madame"
            
        dispatcher.utter_message(f"welcome {gn} {name} from {location}.")
        return []    




class ActionAskCustomerstatus(Action):
    def name(self) -> Text:
        return "action_ask_customer_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Can you tell me if your married , and if you have children with you ? ")
        return []

class utter_greet(Action):
    def name(self) -> Text:
        return "utter_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        responses = tracker.get_responses("utter_greet")    
        dispatcher.utter_message(responses)
        return []

class ActionConfirmCustomerstatus(Action):
    def name(self) -> Text:
        return "action_confirm_customer_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        number = tracker.get_slot("children_count")
        
        status = tracker.get_slot("marital_status")
        name =tracker.get_slot("name")
        gendre = tracker.get_slot("gendre")
        if (gendre== "Male"):
            gn="Mister"
        else :
            gn="Madame"
          
        dispatcher.utter_message(f"So {gn} {name} {status} with {number} children .")
        return []    
    


import pandas as pd
import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionNearbyRecommendations(Action):
    aden_recommendation = pd.read_csv("aden_recommendation.csv")

    def name(self) -> Text:
        return "action_nearby_recommendations"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("Sure, I can help you with nearby recommendations.")
        
        
        recommendation = random.choice(self.aden_recommendation['column_containing_recommendations'])
        
        dispatcher.utter_message(recommendation)
        
        return []
    
    
class ActionAskCheckInDate(Action):

    def name(self) -> Text:
        return "action_ask_check_in_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("In which date you want to make your reservation ?")
        
        return []    

class ActionAskCheckInDateComfirmation(Action):
    
    def name(self) -> Text:
        return "action_check_in_date_confirmation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("Do you want to comfirm this reservation ?")
        
        return []       
