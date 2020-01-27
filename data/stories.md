## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## request advice path
* request_advice
    - advice_form
    - form{"name": "advice_form"}
    - form{"name": null}

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_cheer_up
    - utter_did_that_help

## interactive_story_1
* mood_unhappy
    - utter_cheer_up
    - utter_did_that_help
* mood_unhappy
    - cheer_up

## interactive_story_1
* request_advice{"ingredient": "bananes"}
    - advice_form

## interactive_story_2
* greet
* request_advice{"ingredient": "oranges"}
    - advice_form

## interactive_story_1
* greet
* request_advice{"ingredient": "oranges"}
    - advice_form
* request_advice{"ingredient": "courges"}
    - advice_form

## interactive_story_1
* request_advice{"ingredient": "epinards"}
    - advice_form
    - form{"name": "advice_form"}
    - slot{"ingredient": "epinards"}
    - slot{"event": "slot"}
    - slot{"timestamp": null}
    - slot{"name": "ingredient"}
    - slot{"value": "epinard"}
    - form{"name": null}
    - slot{"requested_slot": null}
* request_advice{"ingredient": "tomates"}
    - advice_form
    - form{"name": "advice_form"}
    - slot{"ingredient": "epinards"}
    - slot{"event": "slot"}
    - slot{"timestamp": null}
    - slot{"name": "ingredient"}
    - slot{"value": "epinard"}
    - slot{"ingredient": "tomates"}
    - slot{"event": "slot"}
    - slot{"timestamp": null}
    - slot{"name": "ingredient"}
    - slot{"value": "tomate"}
    - form{"name": null}
    - slot{"requested_slot": null}
