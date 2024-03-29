import os
from collections import defaultdict
import argparse
import sys
sys.path.append('.../')
##from main import args


snips_map = {
    # =========================================
    'AddToPlaylist': {
        'domain_desc': 'add to playlist',
        'slot_info': {
            # 'music_item', 'playlist_owner', 'entity_name', 'playlist', 'artist'
            'music_item': {
                'slot_type': 'music_item',
                'slot_desc': 'music item',
                'slot_desc2': 'music item',
                'slot_example': {
                    'context': 'funk outta here please add a piece to my playlist',
                    'true_response': 'piece',
                },
                'my_template': 'the music item is %s.',
                'question': 'what is the music item?',
                'before': 'the music item is ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'

            },
            'playlist_owner': {
                'slot_type': 'playlist_owner',
                'slot_desc': 'playlist owner',
                'slot_desc2': 'playlist owner',
                'slot_example': {
                    'context': 'add the album to sebastian s ejercicio playlist',
                    'true_response': 'sebastian s',
                },
                'my_template': 'it is %s playlist, not yours.',# 'not your playlist but %s playlist.',# 'the possessive adjective is %s.',
                'question': 'whose playlist is it?',
                'before': 'it is ',# 'the possessive adjective is ',
                'after': ' playlist, not yours.',# '.',
                'dummy': 'someone\'s', #your
                'dummy2': 'somebody s'

            },
            'entity_name': {
                'slot_type': 'entity_name',
                'slot_desc': 'entity name',
                'slot_desc2': 'entity name',
                'slot_example': {
                    'context': 'i am going to add love letter to my list of parties',
                    'true_response': 'love letter',
                },
                'my_template': 'the song name is %s.', #name
                'question': 'what is the name of the song?', ###
                'before': 'the song name is ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'playlist': {
                'slot_type': 'playlist',
                'slot_desc': 'playlist',
                'slot_desc2': 'playlist',
                'slot_example': {
                    'context': 'add this song to my stay happy playlist',
                    'true_response': 'stay happy',
                },
                'my_template': 'the playlist name is %s.', #'the song is added to %s.',
                'question': 'what is the name of the playlist?',#'which playlist is the song added to?'
                'before': 'the playlist name is ', # 'the song is added to ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'artist': {
                'slot_type': 'artist',
                'slot_desc': 'artist',
                'slot_desc2': 'artist',
                'slot_example': {
                    'context': 'i am going to include the taylor swift track in my bass gaming playlist',
                    'true_response': 'taylor swift',
                },
                'my_template': 'play something by %s.',
                'question': 'what is the name of the artist?',
                'before': 'play something by ',
                'after': '.',
                'dummy': 'someone',
                'dummy2': 'somebody'
            },
        }
    },
    # =========================================
    'BookRestaurant': {
        'domain_desc': 'book restaurant',
        'slot_info': {
            # 'city', 'facility', 'timeRange', 'restaurant_name', 'country', 'cuisine', 'restaurant_type',
            #                        'served_dish', 'party_size_number', 'poi', 'sort', 'spatial_relation', 'state',
            #                        'party_size_description'
            'city': {
                'slot_type': 'city',
                'slot_desc': 'city',
                'slot_desc2': 'city',
                'slot_example': {
                    'context': 'make a reservation at the best pub in shanghai',
                    'true_response': 'shanghai',
                },
                'my_template': 'the city name is %s.',
                'question': 'what is the name of the city?', #name #
                'before': 'the city name is ',
                'after': '.',
                'dummy': 'some city',
                'dummy2': 'something'
            },
            'facility': {
                'slot_type': 'facility',
                'slot_desc': 'facility',
                'slot_desc2': 'facility',
                'slot_example': {
                    'context': 'in washington reserve a tavern with baby chair',
                    'true_response': 'baby chair',
                },
                'my_template': 'the restaurant has %s.',
                'question': 'what is the facility?',
                'before': 'the restaurant has ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'timeRange': {
                'slot_type': 'timeRange',
                'slot_desc': 'time range',
                'slot_desc2': 'time range',
                'slot_example': {
                    'context': 'i need a reservation for the chinese food in cuba in 10 minutes',
                    'true_response': 'in 10 minutes',
                },
                'my_template': 'the time or date is %s.',
                'question': 'when is the time or date?',
                'before': 'the time or date is ',
                'after': '.',
                'dummy': 'sometime',
                'dummy2': 'sometime'
            },
            'restaurant_name': {
                'slot_type': 'restaurant_name',
                'slot_desc': 'restaurant name',
                'slot_desc2': 'restaurant name',
                'slot_example': {
                    'context': 'i am going to kfc together with my friends',
                    'true_response': 'kfc',
                },
                'my_template': 'the restaurant name is %s.', ###
                'question': 'what is the name of the restaurant?',
                'before': 'the restaurant name is ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
                
            },
            'country': {
                'slot_type': 'country',
                'slot_desc': 'country',
                'slot_desc2': 'country',
                'slot_example': {
                    'context': 'at 9 am reserve a restaurant in jerusalem for 8 persons',
                    'true_response': 'jerusalem',
                },
                'my_template': 'the country name is %s.', #name
                'question': 'what is the name of the country?',
                'before': 'the country name is ',
                'after': '.',
                'dummy': 'some country',
                'dummy2': 'something'
                
            },
            'cuisine': {
                'slot_type': 'cuisine',
                'slot_desc': 'cuisine',
                'slot_desc2': 'cuisine',
                'slot_example': {
                    'context': 'i d like to reserve a table for one at a spanish restaurant in wesley',
                    'true_response': 'spanish',
                },
                'my_template': 'it is %s cuisine.',
                'question': 'what is the name of the cuisune?', #
                'before': 'it is ',
                'after': ' cuisine.'
                ,
                'dummy': 'some',
                'dummy2': 'something'
                
            },
            'restaurant_type': {
                'slot_type': 'restaurant_type',
                'slot_desc': 'restaurant type',
                'slot_desc2': 'restaurant type',
                'slot_example': {
                    'context': 'i d like to reserve a buffet for my family',
                    'true_response': 'buffet',
                },
                'my_template': 'book a table at a %s.',
                'question': 'what kind of eatery is reserved?',
                'before': 'book a table at a ',
                'after': '.',
                'dummy': 'eatery',
                'dummy2': 'something'
            },
            'served_dish': {
                'slot_type': 'served_dish',
                'slot_desc': 'served dish',
                'slot_desc2': 'served dish',
                'slot_example': {
                    'context': 'find a restaurant serves hot-pot and make a reservation',
                    'true_response': 'hot-pot',
                },
                'my_template': 'the restaurant serves %s.',
                'question': 'what kind of dish does the restaurant serve?',
                'before': 'the restaurant serves ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'party_size_number': {
                'slot_type': 'party_size_number',
                'slot_desc': 'number',
                'slot_desc2': 'party size number',
                'slot_example': {
                    'context': 'make a six-person reservation at an alpine wine bar',
                    'true_response': 'six-person',
                },
                'my_template': 'the number is %s.',
                'question': 'What is the number of people at the party?',
                'before': 'the number is ',
                'after': '.',
                'dummy': 'some number',
                'dummy2': 'some number'
            },
            'poi': {
                'slot_type': 'poi',
                'slot_desc': 'position',
                'slot_desc2': 'position',
                'slot_example': {
                    'context': 'i d want to reserve a restaurant near my hotel',
                    'true_response': 'near my hotel',
                },
                'my_template': 'the position is %s.',
                'question': 'where is the restaurant?',
                'before': 'the position is ',
                'after': '.',
                'dummy': 'somewhere',
                'dummy2': 'somewhere'
            },
            'sort': {
                'slot_type': 'sort',
                'slot_desc': 'type',
                'slot_desc2': 'sort',
                'slot_example': {
                    'context': 'get a highly regarded sandwich shop in colombia',
                    'true_response': 'highly regarded',
                },
                'my_template': 'the restaurant is %s restaurant.',
                'question': 'How is the restaurant s reputation?',
                'before': 'the restaurant is ',
                'after': ' restaurant.',
                'dummy': 'some',
                'dummy2': 'something'
            },
            'spatial_relation': {
                'slot_type': 'spatial_relation',
                'slot_desc': 'spatial relation',
                'slot_desc2': 'spatial relation',
                'slot_example': {
                    'context': 'book a restaurant for 2 that s 10 minutes walk from here',
                    'true_response': '10 minutes walk',
                },
                'my_template': 'that place is %s.',
                'question': 'How close is it there?',
                'before': 'that place is ',
                'after': '.',
                'dummy': 'somewhat close',
                'dummy2': 'somewhere'
            },
            'state': {
                'slot_type': 'state',
                'slot_desc': 'state',
                'slot_desc2': 'state',
                'slot_example': {
                    'context': 'we d want to go to a brasserie in omaha that serves sicilian cuisine',
                    'true_response': 'omaha',
                },
                'my_template': 'the state name is %s.', #
                'question': 'what is the name of the state?',
                'before': 'the state name is ',
                'after': '.'
                ,
                'dummy': 'some state',
                'dummy2': 'somewhere'
            },
            'party_size_description': {
                'slot_type': 'party_size_description',
                'slot_desc': 'person',
                'slot_desc2': 'party size description',
                'slot_example': {
                    'context': 'book a table for sebastian perez and leclerc',
                    'true_response': 'sebastian perez and leclerc',
                },
                'my_template': 'their names are %s.', ###
                'question': 'What is the name of the people attending the party?',#
                'before': 'their names are ',
                'after': '.'
                ,
                'dummy': 'someone',
                'dummy2': 'somebody'
            },
        }
    },
    # =========================================
    'GetWeather': {
        'domain_desc': 'get weather',
        'slot_info': {
            # 'city', 'state', 'timeRange', 'current_location', 'country', 'spatial_relation', 'geographic_poi',
            #                    'condition_temperature', 'condition_description'
            'city': {
                'slot_type': 'city',
                'slot_desc': 'city',
                'slot_desc2': 'city',
                'slot_example': {
                    'context': 'is the temperature going down to 2 in shanghai',
                    'true_response': 'shanghai',
                },
                'my_template': 'the city name is %s.', #
                'question': 'what is the name of the city?',
                'before': 'the city name is ',
                'after': '.',
                'dummy': 'some city',
                'dummy2': 'somewhere'
            },
            'state': {
                'slot_type': 'state',
                'slot_desc': 'state',
                'slot_desc2': 'state',
                'slot_example': {
                    'context': 'check the weather in omaha',
                    'true_response': 'omaha',
                },
                'my_template': 'the state name is %s.',
                'question': 'what is the name of the state?',#
                'before': 'the state name is ',
                'after': '.',
                'dummy': 'some state',
                'dummy2': 'somewhere'
            },
            'timeRange': {
                'slot_type': 'timeRange',
                'slot_desc': 'time range',
                'slot_desc2': 'time range',
                'slot_example': {
                    'context': 'what is the forecast for haidian in next half an hour',
                    'true_response': 'in next half an hour',
                },
                'my_template': 'the time or date is %s.',
                'question': 'when is the time or date?',
                'before': 'the time or date is ',
                'after': '.',
                'dummy': 'sometime',
                'dummy2': 'sometime'
            },
            'current_location': {
                'slot_type': 'current_location',
                'slot_desc': 'current location',
                'slot_desc2': 'current location',
                'slot_example': {
                    'context': 'will it rain in my present local street on 11/10/2023',
                    'true_response': 'present local street',
                },
                'my_template': 'the current location is %s.',
                'question': 'where is the current location?',
                'before': 'the current location is ',
                'after': '.',
                'dummy': 'somewhere',
                'dummy2': 'somewhere'
            },
            'country': {
                'slot_type': 'country',
                'slot_desc': 'country',
                'slot_desc2': 'country',
                'slot_example': {
                    'context': 'what s the weather like in jerusalem right now',
                    'true_response': 'jerusalem',
                },
                'my_template': 'the country name is %s.',#
                'question': 'what is the name of the country?',
                'before': 'the country name is ',
                'after': '.',
                'dummy': 'some country',
                'dummy2': 'somewhere'
            },
            'spatial_relation': {
                'slot_type': 'spatial_relation',
                'slot_desc': 'spatial relation',
                'slot_desc2': 'spatial relation',
                'slot_example': {
                    'context': 'is it going to rain within 10 minutes bus distance',
                    'true_response': 'within 10 minutes bus distance',
                },
                'my_template': 'that place is %s.',
                'question': 'How close is it there?',
                'before': 'that place is ',
                'after': '.',
                'dummy': 'somewhat close',
                'dummy2': 'somewhere'
            },
            'geographic_poi': {
                'slot_type': 'geographic_poi',
                'slot_desc': 'geographic position',
                'slot_desc2': 'geographic position',
                'slot_example': {
                    'context': 'in west lake park, how cold will it be tomorrow',
                    'true_response': 'west lake park',
                },
                'my_template': 'that place is called %s.',
                'question': 'what is the name of the place?',
                'before': 'that place is called ',
                'after': '.',
                'dummy': 'some area',
                'dummy2': 'somewhere'
            },
            'condition_temperature': {
                'slot_type': 'condition_temperature',
                'slot_desc': 'temperature',
                'slot_desc2': 'condition temperature',
                'slot_example': {
                    'context': 'will it get hotter in 2 hours',
                    'true_response': 'hotter',
                },
                'my_template': 'temperatures are %s.',
                'question': 'How are the temperatures?',
                'before': 'temperatures are ',
                'after': '.',
                'dummy': 'somewhat hot',
                'dummy2': 'something'
            },
            'condition_description': {
                'slot_type': 'condition_description',
                'slot_desc': 'weather',
                'slot_desc2': 'condition description',
                'slot_example': {
                    'context': 'will israel be hit by a snow storm',
                    'true_response': 'snow storm',
                },
                'my_template': 'there is %s.',
                'question': 'How is the weather?',
                'before': 'there is ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
        }
    },
    # =========================================
    'PlayMusic': {
        'domain_desc': 'play music',
        'slot_info': {
            # 'genre', 'music_item', 'service', 'year', 'playlist', 'album', 'sort', 'track', 'artist'
            'genre': {
                'slot_type': 'genre',
                'slot_desc': 'genre',
                'slot_desc2': 'genre',
                'slot_example': {
                    'context': 'find me a lullaby in netease cloud music',
                    'true_response': 'lullaby',
                },
                'my_template': 'the music genre is %s.',
                'question': 'what kind of music do yuo listen to?',
                'before': 'the music genre is ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'music_item': {
                'slot_type': 'music_item',
                'slot_desc': 'music item',
                'slot_desc2': 'music item',
                'slot_example': {
                    'context': 'funk outta here please add a piece to my playlist',
                    'true_response': 'piece',
                },
                'my_template': 'the music item is %s.',
                'question': 'what is the music item?',
                'before': 'the music item is ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'service': {
                'slot_type': 'service',
                'slot_desc': 'service',
                'slot_desc2': 'service',
                'slot_example': {
                    'context': 'find me a lullaby in netease cloud music',
                    'true_response': 'netease cloud music',
                },
                'my_template': 'play the music on %s.',
                'question': 'what is the name of the service?',
                'before': 'play the music on ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'year': {
                'slot_type': 'year',
                'slot_desc': 'year',
                'slot_desc2': 'year',
                'slot_example': {
                    'context': 'play the most popular song in 2021',
                    'true_response': '2021',
                },
                'my_template': 'the year or decade is %s.',
                'question': 'what year or decade is it?',
                'before': 'the year or decade is ',
                'after': '.',
                'dummy': 'sometime',
                'dummy2': 'sometime'
            },
            'playlist': {
                'slot_type': 'playlist',
                'slot_desc': 'playlist',
                'slot_desc2': 'playlist',
                'slot_example': {
                    'context': 'add this song to my stay happy playlist',
                    'true_response': 'stay happy',
                },
                'my_template': 'the playlist name is %s.', ###
                'question': 'what is the name of the playlist?',
                'before': 'the playlist name is ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'album': {
                'slot_type': 'album',
                'slot_desc': 'album',
                'slot_desc2': 'album',
                'slot_example': {
                    'context': 'play the album getting ready by eason chan',
                    'true_response': 'getting ready',
                },
                'my_template': 'the album name is %s.', ###
                'question': 'what is the name of the album?',
                'before': 'the album name is ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'sort': {
                'slot_type': 'sort',
                'slot_desc': 'type',
                'slot_desc2': 'sort',
                'slot_example': {
                    'context': 'play the most popular song in 2021',
                    'true_response': 'the most popular',
                },
                'my_template': 'the song is %s song.',
                'question': 'what is that song about?',
                'before': 'the song is ',
                'after': ' song.',
                'dummy': 'some',
                'dummy2': 'something'
            },
            'track': {
                'slot_type': 'track',
                'slot_desc': 'track',
                'slot_desc2': 'track',
                'slot_example': {
                    'context': 'play shall we talk by eason chan',
                    'true_response': 'shall we talk',
                },
                'my_template': 'the track is called %s.',
                'question': 'what is the name of the sound track?',
                'before': 'the track is called ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'artist': {
                'slot_type': 'artist',
                'slot_desc': 'artist',
                'slot_desc2': 'artist',
                'slot_example': {
                    'context': 'i am going to include the taylor swift track in my bass gaming playlist',
                    'true_response': 'taylor swift',
                },
                'my_template': 'play something by %s.',
                'question': 'what is the name of the artist?',
                'before': 'play something by ',
                'after': '.',
                'dummy': 'someone',
                'dummy2': 'somebody'
            },
        }
    },
    # =========================================
    'RateBook': {
        'domain_desc': 'rate book',
        'slot_info': {
            # 'object_part_of_series_type', 'object_select', 'rating_value', 'object_name', 'object_type',
            #                  'rating_unit', 'best_rating'
            'object_part_of_series_type': {
                'slot_type': 'object_part_of_series_type',
                'slot_desc': 'series',
                'slot_desc2': 'object part of series type',
                'slot_example': {
                    'context': 'i rate the sequel 0 point',
                    'true_response': 'sequel',
                },
                'my_template': 'the series type is %s.', ###
                'question': 'what kind of series is it?',
                'before': 'the series type is ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'object_select': {
                'slot_type': 'object_select',
                'slot_desc': 'this current',
                'slot_desc2': 'object select',
                'slot_example': {
                    'context': 'that book deserves a 5 stars',
                    'true_response': 'that',
                },
                'my_template': 'rate %s book.',
                'question': 'which of the books is rated?',
                'before': 'rate ',
                'after': ' book.',
                'dummy': 'that',
                'dummy2': 'that'
            },
            'rating_value': {
                'slot_type': 'rating_value',
                'slot_desc': 'rating value',
                'slot_desc2': 'rating value',
                'slot_example': {
                    'context': 'the book deserves a 5 stars',
                    'true_response': '5',
                },
                'my_template': 'the score number is %s.', ###
                'question': 'How many points does the book get?',
                'before': 'the score number is ',
                'after': '.',
                'dummy': 'some number',
                'dummy2': 'some number'
            },
            'object_name': {
                'slot_type': 'object_name',
                'slot_desc': 'object name',
                'slot_desc2': 'object name',
                'slot_example': {
                    'context': 'i rate lessons from madame chic 10 stars',
                    'true_response': 'lessons from madame chic',
                },
                #'my_template': 'the book is called %s.',
                #'question': 'what is the name of the rated book?',
                #'before': 'the book is called ',
                #'after': '.',
                'my_template': 'the object name is %s.',
                'question': 'what is the name of the object?', #
                'before': 'the object name is ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'object_type': {
                'slot_type': 'object_type',
                'slot_desc': 'object type',
                'slot_desc2': 'object type',
                'slot_example': {
                    'context': 'this horror literature deserves a 5 stars',
                    'true_response': 'horror',
                },
                #'my_template': 'rate this %s.',
                #'question': 'what kind of book is it?',
                #'before': 'rate this ',
                #'after': '.',
                'my_template': 'the object type is %s.',
                'question': 'what kind of object are you looking for?',
                'before': 'the object type is ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'rating_unit': {
                'slot_type': 'rating_unit',
                'slot_desc': 'rating unit',
                'slot_desc2': 'rating unit',
                'slot_example': {
                    'context': 'this book deserves a 5 stars',
                    'true_response': 'stars',
                },
                'my_template': 'the book deserves a few %s.',
                'question': 'what are you counting?',
                'before': 'the book deserves a few ',
                'after': '.',
                'dummy': 'things',
                'dummy2': 'something'
            },
            'best_rating': {
                'slot_type': 'best_rating',
                'slot_desc': 'best rating',
                'slot_desc2': 'best rating',
                'slot_example': {
                    'context': 'the highest rating for this book is 10',
                    'true_response': '10',
                },
                'my_template': 'the scale number is %s.', ###
                'question': 'what is the rating scale?',
                'before': 'the scale number is ',
                'after': '.',
                'dummy': 'some number',
                'dummy2': 'some number'
            },
        }
    },
    # =========================================
    'SearchCreativeWork': {
        'domain_desc': 'search creative work',
        'slot_info': {
            # 'object_name', 'object_type'
            'object_name': {
                'slot_type': 'object_name',
                'slot_desc': 'object name',
                'slot_desc2': 'object name',
                'slot_example': {
                    'context': 'paris baguette is a bakery chain based in south korea owned by the spc group',
                    'true_response': 'paris baguette',
                },
                #'my_template': 'I found %s.',
                #'question': 'what are you searching?',
                #'before': 'I found ',
                #'after': '.',
                'my_template': 'the object name is %s.',
                'question': 'what is the name of the object?',
                'before': 'the object name is ',
                'after': '.',
                'dummy': 'some work',
                'dummy2': 'something'
            },
            'object_type': {
                'slot_type': 'object_type',
                'slot_desc': 'object type',
                'slot_desc2': 'object type',
                'slot_example': {
                    'context': 'paris baguette is a bakery chain based in south korea owned by the spc group',
                    'true_response': 'bakery',
                },
                #'my_template': 'that %s is great.',
                #'question': 'what kind of works are you searching?',
                #'before': 'that ',
                #'after': ' is great.',
                'my_template': 'the object type is %s.',
                'question': 'what kind of object are you looking for?',
                'before': 'the object type is ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
        }
    },
    # =========================================
    'SearchScreeningEvent': {
        'domain_desc': 'search screening event',
        'slot_info': {
            # 'timeRange', 'movie_type', 'object_location_type', 'object_type', 'location_name',
            #                              'spatial_relation', 'movie_name'
            'timeRange': {
                'slot_type': 'timeRange',
                'slot_desc': 'time range',
                'slot_desc2': 'time range',
                'slot_example': {
                    'context': 'the movie starts at half past eight pm',
                    'true_response': 'half past eight pm',
                },
                'my_template': 'the time or date is %s.',
                'question': 'when is the time or date?',
                'before': 'the time or date is ',
                'after': '.',
                'dummy': 'sometime',
                'dummy2': 'sometime'
            },
            'movie_type': {
                'slot_type': 'movie_type',
                'slot_desc': 'movie type',
                'slot_desc2': 'movie type',
                'slot_example': {
                    'context': 'i want to see a comedy like green book',
                    'true_response': 'comedy',
                },
                'my_template': 'i am looking for the %s.',
                'question': 'what kind of movies are you looking for?',
                'before': 'i am looking for the ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'object_location_type': {
                'slot_type': 'object_location_type',
                'slot_desc': 'location type',
                'slot_desc2': 'object location type',
                'slot_example': {
                    'context': 'the castro theatre is the closest movie house showing green book',
                    'true_response': 'movie house',
                },
                'my_template': 'i will watch the movie at %s.',
                'question': 'what is the location type?',
                'before': 'i will watch the movie at ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'object_type': {
                'slot_type': 'object_type',
                'slot_desc': 'object type',
                'slot_desc2': 'object type',
                'slot_example': {
                    'context': 'show me the movie poster of green book',
                    'true_response': 'movie poster',
                },
                #'my_template': 'show %s.',
                #'question': 'what are you looking for?',
                #'before': 'show ',
                #'after': '.',
                'my_template': 'what i want to know is %s.', ###
                'question': 'what kind of object are you looking for?',
                'before': 'what i want to know is ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'location_name': {
                'slot_type': 'location_name',
                'slot_desc': 'location name',
                'slot_desc2': 'location name',
                'slot_example': {
                    'context': 'the castro theatre is the closest movie house showing green book',
                    'true_response': 'the castro theatre',
                },
                'my_template': 'that place is called %s.',
                'question': 'what is the name of the place?',
                'before': 'that place is called ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
            'spatial_relation': {
                'slot_type': 'spatial_relation',
                'slot_desc': 'spatial relation',
                'slot_desc2': 'spatial relation',
                'slot_example': {
                    'context': 'the castro theatre is the closest movie house showing green book',
                    'true_response': 'closest',
                },
                'my_template': 'that place is %s.',
                'question': 'How close is it there?',
                'before': 'that place is ',
                'after': '.',
                'dummy': 'somewhat close',
                'dummy2': 'somewhere'
            },
            'movie_name': {
                'slot_type': 'movie_name',
                'slot_desc': 'movie name',
                'slot_desc2': 'movie name',
                'slot_example': {
                    'context': 'the castro theatre is the closest movie house showing green book',
                    'true_response': 'green book',
                },
                'my_template': 'the movie is called %s.',
                'question': 'what is the name of the movie?',
                'before': 'the movie is called ',
                'after': '.',
                'dummy': 'something',
                'dummy2': 'something'
            },
        }
    },
}

slot2example_rcsf = {
    # AddToPlaylist
    "music_item": ["song", "track"],
    "playlist_owner": ["my", "donna s"],
    "entity_name": ["the crabfish", "natasha"],
    "playlist": ["quiero playlist", "workday lounge"],
    "artist": ["lady bunny", "lisa dalbello"],
    # BookRestaurant
    "city": ["north lima", "falmouth"],
    "facility": ["smoking room", "indoor"],
    "timeRange": ["9 am", "january the twentieth"],
    "restaurant_name": ["the maisonette", "robinson house"],
    "country": ["dominican republic", "togo"],
    "cuisine": ["ouzeri", "jewish"],
    "restaurant_type": ["tea house", "tavern"],
    "served_dish": ["wings", "cheese fries"],
    "party_size_number": ["seven", "one"],
    "poi": ["east brady", "fairview"],
    "sort": ["top-rated", "highly rated"], 
    "spatial_relation": ["close", "faraway"],
    "state": ["sc", "ut"],
    "party_size_description": ["me and angeline", "my colleague and i"],
    # GetWeather
    "current_location": ["current spot", "here"],
    "geographic_poi": ["bashkirsky nature reserve", "narew national park"],
    "condition_temperature": ["chillier", "hot"],
    "condition_description": ["humidity", "depression"],
    # PlayMusic
    "genre": ["techno", "pop"],
    "service": ["spotify", "groove shark"],
    "year": ["2005", "1993"],
    "album": ["allergic", "secrets on parade"],
    "track": ["in your eyes", "the wizard and i"],
    # RateBook
    "object_part_of_series_type": ["series", "saga"],
    "object_select": ["this", "current"],
    "rating_value": ["1", "four"],
    "object_name": ["american tabloid", "my beloved world"],
    "object_type": ["book", "novel"],
    "rating_unit": ["points", "stars"],
    "best_rating": ["6", "5"],
    # SearchCreativeWork
    # SearchScreeningEvent
    "movie_type": ["animated movies", "films"],
    "object_location_type": ["movie theatre", "cinema"],
    "location_name": ["amc theaters", "wanda group"],
    "movie_name": ["on the beat", "for lovers only"]
}

slot2question_rcsf = {
    'playlist':'What is a playlist?', 
    'music_item':'What is the music project?',
    'geographic_poi':'What is the location?', 
    'facility':'What are the facilities?', 
    'movie_name':'What is the name of the movie?',
    'location_name':'What is the location name?',
    'restaurant_name':'What is the name of the restaurant?',
    'track':'What is the track?',
    'restaurant_type':'What is the type of restaurant?', 
    'object_part_of_series_type':'What is the object part of the series type?',
    'country':'which country?',
    'service':'What is the service?',
    'poi':'What is the position?',
    'party_size_description':'Who are the people attending the party?',
    'served_dish':'What is a dish?',
    'genre':'What is the genre?',
    'current_location':'What is the current location?',
    'object_select':'What is the object to be rated?',
    'album':'What album?',
    'object_name':'What is the object name?',
    'state':'Where is the location?',
    'sort':'What type is it?',
    'object_location_type':'What is the location type?',
    'movie_type':'What type of movie is it?',
    'spatial_relation':'What is the spatial relationship?',
    'artist':'What is an artist?',
    'cuisine':'What dish?',
    'entity_name':'What is the name of the entity?',
    'object_type':'What is an object type?',
    'playlist_owner':'What is the owner of the playlist?',
    'timeRange':'What time frame?',
    'city':'What city?',
    'rating_value':'What is the value of the rating?',
    'best_rating':'What is the best score?',
    'rating_unit':'What is the rating unit?',
    'year':'Which year?',
    'party_size_number':'What is the number of people at the party?',
    'condition_description':'How is the weather?',
    'condition_temperature':'What is the condition temperature?'
}


slot2question_qa = {
    'playlist':'What is the playlist?', 
    'music_item':'What is the music item?',
    'geographic_poi':'Where is the location?', 
    'facility':'What is the facility?', 
    'movie_name':'What is the movie name?',
    'location_name':'Where is the location name?',
    'restaurant_name':'What is the name?',
    'track':'What is the track?',
    'restaurant_type':'What is the restaurant type?', 
    'object_part_of_series_type':'What is the series?',
    'country':'what is the country?',
    'service':'What is the service?',
    'poi':'Where is the location?',
    'party_size_description':'Who are the persons?',
    'served_dish':'What is the served dish?',
    'genre':'What is the genre?',
    'current_location':'What is the current location?',
    'object_select':'Which to select?',
    'album':'What is the album?',
    'object_name':'What is the object name?',
    'state':'What is the state?',
    'sort':'What is the type?',
    'object_location_type':'What is the location type?',
    'movie_type':'What is the movie type?',
    'spatial_relation':'What is the spatial relation?',
    'artist':'Who is the artist?',
    'cuisine':'What is the cuisine?',
    'entity_name':'What is the entity name?',
    'object_type':'What is the object type?',
    'playlist_owner':'What is the owner?',
    'timeRange':'When is the time range?',
    'city':'What is the city?',
    'rating_value':'How many rating value?',
    'best_rating':'How many rating points in total?',
    'rating_unit':'What is the rating unit?',
    'year':'When is the year?',
    'party_size_number':'How many people?',
    'condition_description':'How is the weather?',
    'condition_temperature':'How is the temperature?'
}



snips_domains = []
domain2desc = {'atis': 'airline travel'}
domain2slots = {}

domainslot2desc = {}
domainslot2desc2 = {}

domainslot2example = {}
domainslot2context = {}

domainslot2temp = {}
domainslot2question = {}
domainslot2before = {}
domainslot2after = {}
domainslot2dummy = {}
domainslot2dummy2 = {}

domain2slotsnum = {'AddToPlaylist':5, 'BookRestaurant':14, 'GetWeather':9, 'PlayMusic':8, 'RateBook':7, 'SearchCreativeWork':2, 'SearchScreeningEvent':7, 'atis':83}





for domain_name, domain_item in snips_map.items():
    snips_domains.append(domain_name)
    domain2desc[domain_name] = domain_item['domain_desc']
    domain2slots[domain_name] = list(domain_item['slot_info'].keys())

    domainslot2desc[domain_name] = {}
    domainslot2desc2[domain_name] = {}
    domainslot2example[domain_name] = {}
    domainslot2context[domain_name] = {}

    domainslot2temp[domain_name] = {}
    domainslot2question[domain_name] = {}
    domainslot2before[domain_name] = {}
    domainslot2after[domain_name] = {}
    domainslot2dummy[domain_name] = {}
    domainslot2dummy2[domain_name] = {}



    for slot_name, slot_item in domain_item['slot_info'].items():
        domainslot2desc[domain_name][slot_name] = slot_item['slot_desc']
        domainslot2desc2[domain_name][slot_name] = slot_item['slot_desc2']
        domainslot2example[domain_name][slot_name] = slot_item['slot_example']['true_response']
        domainslot2context[domain_name][slot_name] = slot_item['slot_example']['context']

        domainslot2temp[domain_name][slot_name] = slot_item['my_template']
        domainslot2question[domain_name][slot_name] = slot_item['question']
        domainslot2before[domain_name][slot_name] = slot_item['before']
        domainslot2after[domain_name][slot_name] = slot_item['after']
        domainslot2dummy[domain_name][slot_name] = slot_item['dummy']
        domainslot2dummy2[domain_name][slot_name] = slot_item['dummy2']

domain2slots['atis'] = []
domainslot2desc['atis'] = {}
domainslot2desc2['atis'] = {}
domainslot2example['atis'] = {}
with open('gsl/datasets/atis_slot_info.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        line_strip = line.strip('\n').split('\t')
        slot = line_strip[0]
        domainslot2desc['atis'][slot] = line_strip[1]
        domainslot2desc2['atis'][slot] = line_strip[1]
        domain2slots['atis'].append(slot)
        domainslot2example['atis'][slot] = line_strip[2:]

        if len(line_strip) == 4:
            slot2example_rcsf[slot] = line_strip[2:]
        elif len(line_strip) == 3:
            slot2example_rcsf[slot] = [line_strip[2], line_strip[2]]
        else :
            print('!?!?!?!?!?\n')


with open('data/slot2query.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        line_strip = line.strip('\n').split('\t')
        slot = line_strip[0]
        slot2question_rcsf[slot] = line_strip[1]

#unseen_slot = {
#    'AddToPlaylist': ['playlist_owner', 'entity_name'] , 
#    'BookRestaurant': ['restaurant_type', 'served_dish', 'restaurant_name', 'party_size_description', 'cuisine', 'party_size_description', ], 
#    'GetWeather': [], 
#    'PlayMusic': [], 
#    'RateBook': [], 
#    'SearchCreativeWork': [], 
#    'SearchScreeningEvent': []
#    }


 # 'music_item', 'playlist_owner', 'entity_name', 'playlist', 'artist'

 # 'city', 'facility', 'timeRange', 'restaurant_name', 'country', 'cuisine', 'restaurant_type',
            #                        'served_dish', 'party_size_number', 'poi', 'sort', 'spatial_relation', 'state',
            #                        'party_size_description'

 # 'city', 'state', 'timeRange', 'current_location', 'country', 'spatial_relation', 'geographic_poi',
            #                    'condition_temperature', 'condition_description'

# 'genre', 'music_item', 'service', 'year', 'playlist', 'album', 'sort', 'track', 'artist'

# 'object_part_of_series_type', 'object_select', 'rating_value', 'object_name', 'object_type',
            #                  'rating_unit', 'best_rating'


# 'timeRange', 'movie_type', 'object_location_type', 'object_type', 'location_name',
            # 
if False:
#if args.dir_name == '66':
    domainslot2temp['AddToPlaylist']['playlist_owner'] = 'it is %s playlist.'
    domainslot2before['AddToPlaylist']['playlist_owner'] = 'it is '
    domainslot2after['AddToPlaylist']['playlist_owner'] = ' playlist.'
    domainslot2question['AddToPlaylist']['playlist_owner'] = 'whose playlist is it?'
    









def bio2sl(sentence_bio, domain):
    """
    Args:
        sentence_bio: raw line of file
        domain: domain_name

    Returns:
        [(domain, sentence, entity1, slot1), (domain, sentence, entity2, slot2), ...]
    """
    sentence, bio = sentence_bio.split('\t')
    char_label_list = list(zip(sentence.split(), bio.split()))

    length = len(char_label_list)
    idx = 0
    entities, slot_types = [], []
    while idx < length:
        char, label = char_label_list[idx]
        label_first_char = label[0]

        # merge chars
        if label_first_char == "O":
            idx += 1
            continue
        if label_first_char == "B":
            end = idx + 1
            while end < length and char_label_list[end][1][0] == "I":
                end += 1
            entity = ' '.join(char_label_list[i][0] for i in range(idx, end))
            entities.append(entity)
            slot_type = label[2:]
            slot_types.append(slot_type)
            idx = end
        else:
            raise Exception('Invalid Inputs: %s' % (char_label_list[idx]))

    # one slot map to one response
    # if one slot has multi entities, only return one result
    results = []
    collect_dict = defaultdict(list)
    for entity, slot_type in zip(entities, slot_types):
        collect_dict[slot_type].append(entity)
    for slot_type, entities in collect_dict.items():
        results.append((domain, sentence, entities, slot_type))
    return results


def bio2sl_modified(sentence_bio, domain):
    """
    Args:
        sentence_bio: raw line of file
        domain: domain_name

    Returns:
        [(domain, sentence, entity1, slot1), (domain, sentence, entity2, slot2), ...]
    """
    sentence, bio = sentence_bio.split('\t')
    char_label_list = list(zip(sentence.split(), bio.split()))


    slot2entities = {}
    for slot in domain2slots[domain]:
        slot2entities[slot] = []    

    length = len(char_label_list)
    idx = 0
    #entities, slot_types = [], []
    while idx < length:
        char, label = char_label_list[idx]
        label_first_char = label[0]

        # merge chars
        if label_first_char == "O":
            idx += 1
            continue
        if label_first_char == "B":
            end = idx + 1
            while end < length and char_label_list[end][1][0] == "I":
                end += 1
            entity = ' '.join(char_label_list[i][0] for i in range(idx, end))
            #entities.append(entity)
            slot_type = label[2:]
            #slot_types.append(slot_type)
            slot2entities[slot_type].append(entity)
            idx = end
        else:
            raise Exception('Invalid Inputs: %s' % (char_label_list[idx]))

    # one slot map to one response
    # if one slot has multi entities, only return one result
    results = []
    
    for slot_type, entities in slot2entities.items():
        if len(entities) == 0:
            entities.append("")
        results.append((domain, sentence, entities, slot_type))
    
    return results

'''

    collect_dict = defaultdict(list)
    for entity, slot_type in zip(entities, slot_types):
        collect_dict[slot_type].append(entity)
    

    for k in snips_map[domain]["slot_info"].keys():
        if (collect_dict.get(k) == None):
#            collect_dict[k].append("")
            collect_dict[k].append("")


    for slot_type, entities in collect_dict.items():
        results.append((domain, sentence, entities, slot_type))

    return results
'''




def load_file(file_path, domain):
    content = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            content.extend(bio2sl_modified(line.strip(), domain))  # domain, sentence, entity list, slot
    return content


def load_snips_data(data_dir):
    domain2data = {}
    for domain in snips_domains:
        file_path = os.path.join(data_dir, 'snips', domain, f'{domain}.txt')
        domain2data[domain] = load_file(file_path, domain)
    return domain2data


def load_snips_seen_unseen_data(data_dir):
    domain2data_seen = {}
    domain2data_unseen = {}
    for domain in snips_domains:
        seen_file_path = os.path.join(data_dir, 'snips', domain, f'seen_slots.txt')
        unseen_file_path = os.path.join(data_dir, 'snips', domain, f'unseen_slots.txt')
        domain2data_seen[domain] = load_file(seen_file_path, domain)
        domain2data_unseen[domain] = load_file(unseen_file_path, domain)
    return domain2data_seen, domain2data_unseen


def load_atis_data(data_dir):
    file_path = os.path.join(data_dir, 'atis', 'atis.txt')

#    return {'atis' : []}
    return {'atis': load_file(file_path, 'atis')}
#    intents = ['atis_airfare', 'atis_airline', 'atis_flight', 'atis_ground_service', 'others']
#    content = []

#    for intent in intents:
#        intent_path = os.path.join(data_dir, 'atis', intent, f'{intent}.txt')
#        content.extend(load_file(intent_path, 'atis'))

#    return {'atis': content}

#    airfare_path = os.path.join(data_dir, 'atis', 'atis_airfare', 'atis_airfare.txt')
#    content = load_file(airfare_path, 'atis')





def generate_text_data(data_dir, target_domain, shot_num=0):
    snips_data = load_snips_data(data_dir)
    atis_data = load_atis_data(data_dir)
    all_data = {**snips_data, **atis_data}

    train_data = []
    valid_data = []
    test_data = []
    for domain_name, domain_data in all_data.items():
        if domain_name != target_domain and domain_name != 'atis':
            train_data.extend(domain_data)


    valid_data_num = 500 * domain2slotsnum[target_domain]
    shot_data_num = shot_num * domain2slotsnum[target_domain]
    
    train_data.extend(all_data[target_domain][:shot_data_num])  # [(domain, sentence, entity list, slot), ...]
    valid_data.extend(all_data[target_domain][shot_data_num:(valid_data_num + shot_data_num)])
    test_data.extend(all_data[target_domain][(valid_data_num + shot_data_num):])
    #test_data.extend(all_data[target_domain][500:700])

    #train_data = train_data[:100]

    if target_domain != 'atis':
        domain2data_seen, domain2data_unseen = load_snips_seen_unseen_data(data_dir)
        seen_data = domain2data_seen[target_domain]
        unseen_data = domain2data_unseen[target_domain]
        return train_data, valid_data, test_data, seen_data, unseen_data


    return train_data, valid_data, test_data, None, None


def slot_list(data):
    sl = []

    for domain, sentence, entity, slot in data:
        sl.append(slot)
    
    return sl