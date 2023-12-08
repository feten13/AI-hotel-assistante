# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#from rasa_sdk.events import SlotSet

# class ActionExtractSlots(Action):
#     def name(self) -> Text:
#         return "action_extract_slots"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         extracted_slots = []

#         # Extracting slot from intent 'vacation_period'
#         if tracker.latest_message['intent']['name'] == 'vacation_period':
#             start_date_entity = next((e for e in tracker.latest_message['entities'] if e['entity'] == 'start_date'), None)
#             end_date_entity = next((e for e in tracker.latest_message['entities'] if e['entity'] == 'end_date'), None)

#             if start_date_entity:
#                 extracted_slots.append(SlotSet('start_date', start_date_entity['value']))
#             if end_date_entity:
#                 extracted_slots.append(SlotSet('end_date', end_date_entity['value']))

#         # Extracting slot from intent 'customer_details'
#         elif tracker.latest_message['intent']['name'] == 'customer_details':
#             gender_entity = next((e for e in tracker.latest_message['entities'] if e['entity'] == 'gendre'), None)
#             name_entity = next((e for e in tracker.latest_message['entities'] if e['entity'] == 'name'), None)
#             location_entity = next((e for e in tracker.latest_message['entities'] if e['entity'] == 'location'), None)

#             if gender_entity:
#                 extracted_slots.append(SlotSet('gendre', gender_entity['value']))
#             if name_entity:
#                 extracted_slots.append(SlotSet('name', name_entity['value']))
#             if location_entity:
#                 extracted_slots.append(SlotSet('location', location_entity['value']))

#         # Add more conditions for other intents and slots as needed

#         return extracted_slots

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
    
#from rasa_sdk.forms import FormAction
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

class ActionCheckAvailabilityConfirmation(Action):
    #aden_calendre = pd.read_csv("aden_calendre.csv")
    example_calendre_data = {
        'dates': ['2023-12-10', '2023-12-15', '2023-12-20'],
        'room': ['Single', 'Double', 'Suite']
    }

    aden_calendre = pd.DataFrame(example_calendre_data)
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
        self.aden_calendre['dates'] = pd.to_datetime(self.aden_calendre['dates'])
        available_dates = self.aden_calendre['dates'].astype(str)
        
        if any((start_date <= date <= end_date) for date in available_dates):
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
    

import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher











class ActionNearbyRecommendations(Action):
    # Example structure for the aden_recommendation CSV file
    example_recommendation_data = {
        'column_containing_recommendations': [
            'Visit the local museum.',
            'Explore nearby parks.',
            'Try popular restaurants in the area.'
        ]
    }

    aden_recommendation = pd.DataFrame(example_recommendation_data)

    def name(self) -> Text:
        return "action_nearby_recommendations"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message("Sure, I can help you with nearby recommendations.")
        
        recommendation = random.choice(self.aden_recommendation['column_containing_recommendations'])
        
        dispatcher.utter_message(recommendation)
        
        return []

    