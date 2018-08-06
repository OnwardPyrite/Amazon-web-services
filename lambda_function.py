{
    "interactionModel": {
        "languageModel": {
            "invocationName": "phoenix",
            "intents": [
                {
                    "name": "AMAZON.FallbackIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.CancelIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.HelpIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.StopIntent",
                    "samples": []
                },
                {
                    "name": "TechHubExplainedIntent",
                    "slots": [],
                    "samples": [
                        "tell me about this room",
                        "about this place",
                        "about this area",
                        "what can i do here",
                        "what is the tech hub for",
                        "tell me about the tech hub area",
                        "tell me about this area",
                        "what can you do in here",
                        "what can i do in here",
                        "what can you do in the tech hub",
                        "tell me about the tech hub",
                        "tell me about this place",
                        "what is here",
                        "what goes on in this room",
                        "what is this room",
                        "what is this place",
                        "what is the tech hub"
                    ]
                },
                {
                    "name": "FacilitiesIntent",
                    "slots": [],
                    "samples": [
                        "what facilities are there",
                        "what equipment is there for me to use",
                        "what equpment is there to use",
                        "can i use the equipment here",
                        "what is there to use",
                        "what kit is available",
                        "what can i use",
                        "whats available",
                        "explain equipment",
                        "what equipment",
                        "about equipment",
                        "what equipment do you have",
                        "what kit is there",
                        "about kit",
                        "about facilities",
                        "what facilities are available",
                        "available facilities"
                    ]
                },
                {
                    "name": "add_value_to_db",
                    "slots": [
                        {
                            "name": "quan_to_add",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "name",
                            "type": "equipment"
                        }
                    ],
                    "samples": [
                        "add {quan_to_add} {name} to the tech hub",
                        "add {quan_to_add} {name} ",
                        "add {quan_to_add} {name} to the inventory"
                    ]
                },
                {
                    "name": "rem_value_from_db",
                    "slots": [
                        {
                            "name": "quan_to_rem",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "name",
                            "type": "equipment"
                        }
                    ],
                    "samples": [
                        "remove {quan_to_rem} {name} from tech hub",
                        "remove {quan_to_rem} {name} from inventory",
                        "remove {quan_to_rem} {name}"
                    ]
                },
                {
                    "name": "list_items",
                    "slots": [],
                    "samples": [
                        "whats in the inventory",
                        "whats in the tech hub",
                        "whats in there",
                        "what is in the tech hub",
                        "what is there",
                        "what do we have"
                    ]
                },
                {
                    "name": "get_item_quantities",
                    "slots": [
                        {
                            "name": "name",
                            "type": "equipment"
                        }
                    ],
                    "samples": [
                        "how many {name} are there",
                        "how many {name} are in the inventory",
                        "how many {name} are in the tech hub",
                        "how much {name} do we have",
                        "how many {name} do we have"
                    ]
                },
                {
                    "name": "AMAZON.ReadAction<object@Calendar>",
                    "samples": []
                },
                {
                    "name": "AMAZON.SearchAction<object@Calendar>",
                    "samples": []
                },
                {
                    "name": "AMAZON.NoIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.YesIntent",
                    "samples": []
                },
                {
                    "name": "InvIntent",
                    "slots": [],
                    "samples": [
                        "lock the inventory",
                        "shut down the inventory",
                        "close inventory",
                        "i'm finished with the inventory"
                    ]
                },
                {
                    "name": "WhenDoesThisPlaceOpenClose",
                    "slots": [],
                    "samples": [
                        "when does this place open",
                        "what is the closing time",
                        "business hours",
                        "business hour",
                        "closing hours",
                        "opening hours",
                        "opening time",
                        "close time",
                        "closing time",
                        "open time",
                        "what are the opening times",
                        "when does the tech hub",
                        "when does this place close"
                    ]
                },
                {
                    "name": "HowDoIBookThisRoom",
                    "slots": [],
                    "samples": [
                        "how to book room",
                        "can we book this room",
                        "book room",
                        "can i book this room",
                        "how can i book this room",
                        "how do I book this room"
                    ]
                },
                {
                    "name": "CanAnyoneUseThisPlace",
                    "slots": [],
                    "samples": [
                        "use this room",
                        "use this place",
                        "can anyone use this place",
                        "can i use the tech hub",
                        "can i use this room",
                        "who can use the tech hub",
                        "can anyone use the tech hub",
                        "who can use this room"
                    ]
                },
                {
                    "name": "moreOptions",
                    "slots": [],
                    "samples": [
                        "options",
                        "more commands",
                        "give me more options",
                        "more options"
                    ]
                }
            ],
            "types": [
                {
                    "name": "equipment",
                    "values": [
                        {
                            "name": {
                                "value": "laptop",
                                "synonyms": [
                                    "windows machine",
                                    "think pad",
                                    "lenovo",
                                    "computer",
                                    "pc",
                                    "portable computer"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "batteries",
                                "synonyms": [
                                    "battery"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "desks",
                                "synonyms": [
                                    "desk"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "mice",
                                "synonyms": [
                                    "computer mice",
                                    "computer mouse",
                                    "mouse"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "keyboards",
                                "synonyms": [
                                    "keyboard"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "monitors",
                                "synonyms": [
                                    "display",
                                    "screens",
                                    "monitor",
                                    "screen"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "chargers",
                                "synonyms": [
                                    "charging station",
                                    "power supply",
                                    "charging lead",
                                    "charger"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "raspberry pies",
                                "synonyms": [
                                    "raspbian computer",
                                    "raspbian machine",
                                    "raspbian",
                                    "raspberry pie"
                                ]
                            }
                        },
                        {
                            "name": {
                                "value": "mind storms set",
                                "synonyms": [
                                    "mind storms",
                                    "lego",
                                    "mind storm",
                                    "lego set"
                                ]
                            }
                        }
                    ]
                }
            ]
        }
    }
}
