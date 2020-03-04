from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class CompletionForm(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""
        
        return "completion_form"
        
## 1- slot mapping: check for: noun, verb, split point
## 2- validate values of noun, verb, split point
## 3- match sentence with completion


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
##        return ["noun", "verb", "splitpoint"]
        return ["verb", "splitpoint"]

    def slot_mappings(self) -> Dict[Text, Any]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
##            "noun": self.from_entity(entity="noun", intent=["affirm", "deny"),
            "verb": self.from_entity(entity="verb", intent="incomplete"),
            "splitpoint": self.from_entity(entity="splitpoint", intent="incomplete"),
        }
        
        
##    @staticmethod
##    def noun_db() -> List[Text]:
##        """Database of supported devices"""

##        return [
##            "heating",
##            "oven",
##            "light",
##        ]
        
##    def validate_noun(
##        self,
##        value: Text,
##        dispatcher: CollectingDispatcher,
##        tracker: Tracker,
##        domain: Dict[Text, Any],
##    ) -> Dict[Text, Any]:
##        """Validate noun value."""

##        if value.lower() in self.noun_db():
##            # validation succeeded, set the value of the "noun" slot to value
##            return {"noun": value}
##        else:
##            dispatcher.utter_message(template="utter_wrong_noun")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
##            return {"noun": None}     
        
##        def validate_verb(
##        self,
##        value: Text,
##        dispatcher: CollectingDispatcher,
##        tracker: Tracker,
##        domain: Dict[Text, Any],
##    ) -> Dict[Text, Any]:
       ## """Validate verb value."""
##            return {"verb": value}
##            
##        def validate_splitpoint(
##        self,
##        value: Text,
##        dispatcher: CollectingDispatcher,
##        tracker: Tracker,
##        domain: Dict[Text, Any],
##    ) -> Dict[Text, Any]:
      ##  """Validate splitpoint value."""
##            return {"splitpoint": value}
  
  
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
      ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit")
        return []