# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import ActionExecutionRejection
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT

import re

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


class AdviceForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "advice_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["ingredient"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"ingredient": self.from_entity(entity="ingredient",
                                               not_intent="greet")}

    @staticmethod
    def ingredient_db():
        # type: () -> List[Text]
        """Database of supported ingredients"""
        return ["abricot",
                "banane",
                "cassis",
                "cerise",
                "citron",
                "clémentine",
                "coing",
                "fraise",
                "framboise",
                "groseille",
                "mirabelle",
                "mûre",
                "myrtille",
                "nectarine",
                "orange",
                "pamplemousse",
                "pomelo",
                "pêche",
                "poire",
                "pomme",
                "prune",
                "pruneau",
                "raisin",
                "rhubarbe",
                "ananas",
                "figue",
                "fruit de la passion",
                "goyave",
                "grenade",
                "kaki",
                "kiwi",
                "kumquat",
                "litchi",
                "mangue",
                "melon",
                "papaye",
                "pastèque",
                "vanille",
                "amande",
                "datte",
                "noisette",
                "artichaut",
                "aubergine",
                "asperge",
                "avocat",
                "betterave",
                "blette",
                "brocoli",
                "banane plantain",
                "carotte",
                "cardon",
                "céleri rave",
                "céleri branche",
                "champignon",
                "champignon de paris",
                "chou blanc",
                "chou rouge",
                "chou de bruxelles",
                "chou-fleur",
                "citrouille",
                "concombre",
                "courge",
                "courgette",
                "crosne",
                "echalote",
                "epinard",
                "endive",
                "fenouil",
                "haricot vert",
                "haricot",
                "navet",
                "oignon",
                "oseille",
                "panais",
                "pâtisson",
                "petit pois",
                "poireau",
                "poivron",
                "potiron",
                "radis rouge",
                "rutabaga",
                "navet",
                "salade ",
                "salsifis",
                "tomate",
                "topinambour",
                "maïs"]

    def validate_ingredient(self,
                            value: Text,
                            dispatcher: CollectingDispatcher,
                            tracker: Tracker,
                            domain: Dict[Text, Any]) -> Optional[Text]:
        """Validate ingredient value."""

        lemma = re.sub(r's$','', value.lower())
        if lemma in self.ingredient_db():
            # validation succeeded
            return SlotSet('ingredient', lemma)
        else:
            dispatcher.utter_message(template='utter_wrong_ingredient')
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return None

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message("Voici ma réponse pour l'ingrédient: ")
        dispatcher.utter_message(tracker.get_slot("ingredient"))
        return []
