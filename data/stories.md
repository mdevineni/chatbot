## Regular sequential story
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
	- slot{"cuisine": "Mexican"}
    - action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "300 to 700"}
    - slot{"budget": "300 to 700"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
    - slot{"budget": "average cost for two 300 to 700"}
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
    - action_restarted
## User greeted and then only denying
* greet
    - utter_greet
* deny
    - utter_default
* deny
    - utter_default
* deny
    - utter_goodbye
	- action_restarted
## Provided location first time is not tier-1 and tier-2 city
* greet
    - utter_greet
* deny
    - utter_default
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "rishikesh"}
	- slot{"location": "rishikesh"}
    - action_validate_location
	- slot{"location": null}
    - utter_ask_location    
* restaurant_search{"location": "mumbai"}
	- slot{"location": "mumbai"}
    - action_validate_location
	- slot{"location": "mumbai"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
	- slot{"cuisine": "Chinese"}
    - action_validate_cuisine
	- slot{"cuisine": "Chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "between 300 - 700"}
    - slot{"budget": "between 300 to 700"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
    - slot{"budget": "average cost for two between 300 to 700"}
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz.gmail.com"}
	- slot{"email": "xyz.gmail.com"}
	- action_validate_email
	- slot{"email": null}
	- utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
    - action_restarted
## User provided incorrect cuisine
* greet
    - utter_greet
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
	- slot{"location": "hyderabad"}
	- action_validate_location
	- slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Spanish"}
	- slot{"cuisine": "Spanish"}
	- action_validate_cuisine
	- slot{"cuisine": null}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- slot{"cuisine": "North Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "> 300"}
    - slot{"budget": "> 300"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
    - slot{"budget": "average cost for two > 300"}
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
    - action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
    - action_restarted
## User provided budget which bot could not extract or understand
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
	- slot{"location": "pune"}
	- action_validate_location
	- slot{"location": "pune"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
	- slot{"cuisine": "South Indian"}
    - action_validate_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_budget
* out_of_scope
	- utter_default
	- utter_ask_budget
* restaurant_search{"budget": "> 700"}
    - slot{"budget": "> 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
    - slot{"budget": "average cost for two > 700"}
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
 	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
    - action_restarted
## User does not want the email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
	- slot{"location": "bangalore"}
	- action_validate_location
	- slot{"location": "bangalore"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
	- slot{"cuisine": "American"}
    - action_validate_cuisine
	- slot{"cuisine": "American"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 300"}
    - slot{"budget": "more than 300"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
    - slot{"budget": "average cost for two more than 300"}
	- utter_ask_about_emailing
* deny
    - utter_goodbye
	- export
## User provided location could not be extracted or none
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "rishikesh"}
	- slot{"location": "rishikesh"}
    - action_validate_location
	- slot{"location": null}
	- utter_ask_location
* restaurant_search{"location": "pune"}
	- slot{"location": "pune"}
    - action_validate_location
	- slot{"location": "pune"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
	- slot{"cuisine": "Italian"}
	- action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}
    - slot{"budget": "between 300 to 700"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
    - slot{"budget": "average cost for two between 300 to 700"}
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "@test.com"}
	- slot{"email": "@test.com"}
	- action_validate_email
	- slot{"email": null}
	- utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
    - action_restarted
## User is not providing location correctly multiple times or location could not be extracted or is none
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": null}
	- slot{"location": null}
	- action_validate_location
	- slot{"location": null}
	- utter_ask_location
* restaurant_search{"location": null}
	- slot{"location": null}
	- action_validate_location
	- slot{"location": null}
	- utter_goodbye
## User providing location but not providing cuisine or it could not be extracted or is none
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
	- slot{"location": "pune"}
	- action_validate_location
	- slot{"location": "pune"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "brazilian"}
	- slot{"cuisine": "brazilian"}
	- action_validate_cuisine
	- slot{"cuisine": null}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "brazilian"}
	- slot{"cuisine": "brazilian"}
	- action_validate_cuisine
	- slot{"cuisine": null}
    - utter_goodbye
	- action_restarted
## User providing location,cuisine but budget could not be extracted or none
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
	- slot{"location": "pune"}
	- action_validate_location
	- slot{"location": "pune"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
	- slot{"cuisine": "South Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_budget
* out_of_scope
	- utter_default
	- utter_ask_budget
* out_of_scope
	- utter_default
	- utter_ask_budget
* out_of_scope
    - utter_goodbye
	- action_restarted
## User provided location and cuisine during location response
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi","cuisine": "mexican"}
	- slot{"location": "delhi"}
	- slot{"cuisine": "mexican"}
	- action_validate_location
	- slot{"location": "delhi"}
	- action_validate_cuisine
	- slot{"cuisine": "mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "< 300"}
    - slot{"budget": "< 300"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_top_restaurant
	- action_restaurant
    - slot{"budget": "average cost for two < 300"}
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
    - action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
    - action_restarted
## User provided location and budget during location response	
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi","budget": "more than 300"}
	- slot{"location": "delhi"}
	- slot{"budget": "more than 300"}
	- action_validate_location
	- slot{"location": "delhi"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
	- slot{"cuisine": "chinese"}
	- action_validate_cuisine
	- slot{"cuisine": "chinese"}
	- utter_top_restaurant
	- action_restaurant
	- slot{"budget": "average cost for two more than 300"}
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
    - action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
    - action_restarted
## User provided location and cuisine and budget during location response
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi","budget": "more than 300","cuisine": "North Indian"}
	- slot{"location": "delhi"}
	- slot{"cuisine": "North Indian"}
	- slot{"budget": "more than 300"}
	- action_validate_location
	- slot{"location": "delhi"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
	- slot{"budget": "average cost for two more than 300"}
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
    - action_restarted
##  User provided location and cuisine and budget during location response but location is not tier-1 or tier-2 city
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "rishikesh","budget": "more than 300","cuisine": "North Indian"}
	- slot{"location": "rishikesh"}
	- slot{"cuisine": "North Indian"}
	- slot{"budget": "more than 300"}
	- action_validate_location
	- slot{"location": null}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
	- slot{"budget": "average cost for two more than 300"}
	- utter_ask_about_emailing
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
    - action_restarted
## User responded location with greeting
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- slot{"cuisine": "North Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 300"}
    - slot{"budget": "more than 300"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
    - slot{"budget": "average cost for two more than 300"}
	- utter_ask_about_emailing
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
    - action_restarted
## User responded cuisine with greeting
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian"}
	- slot{"cuisine": "North Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 300"}
    - slot{"budget": "more than 300"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
    - slot{"budget": "average cost for two more than 300"}
	- utter_ask_about_emailing
* send_email{"email": "xyz@test.com"}
	- action_validate_email
	- action_email
	- utter_goodbye
    - action_restarted
## User responded budget with greeting
* greet
    - utter_greet
* restaurant_search{"budget": "more than 300"}
    - slot{"budget": "more than 300"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
	- action_validate_location
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- action_validate_cuisine
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* send_email{"email": "xyz@test.com"}
	- action_validate_email
	- action_email
	- utter_goodbye
    - action_restarted
## User responded location and budget with greeting
* greet
    - utter_greet
* restaurant_search{"location": "delhi","budget": "more than 300"}
	- action_validate_location
    - slot{"budget": "more than 300"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- action_validate_cuisine
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* send_email{"email": "xyz@test.com"}
	- action_validate_email
	- action_email
	- utter_goodbye
    - action_restarted
## User responded location and cuisine with greeting
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "North Indian"}
	- action_validate_location
	- action_validate_cuisine
	- utter_ask_budget
* restaurant_search{"budget": "more than 300"}
    - slot{"budget": "more than 300"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
    - action_restarted
## User responded budget and cuisine with greeting
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian","budget": "more than 300"}
	- slot{"cuisine": "North Indian"}
	- slot{"budget": "more than 300"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
	- utter_top_restaurant
	- action_restaurant
	- slot{"budget": "average cost for two more than 300"}
	- utter_ask_about_emailing
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
    - action_restarted
## User responded location and budget and cuisine with greeting
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "North Indian","budget": "more than 300"}
	- slot{"location": "delhi"}
	- slot{"cuisine": "North Indian"}
	- slot{"budget": "more than 300"}
	- action_validate_location
	- slot{"location": "delhi"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
	- slot{"budget": "average cost for two more than 300"}
	- utter_ask_about_emailing
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
    - action_restarted
## User responded location and budget and cuisine with greeting but said no to email
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "North Indian","budget": "more than 300"}
	- slot{"location": "delhi"}
	- slot{"cuisine": "North Indian"}
	- slot{"budget": "more than 300"}
	- action_validate_location
	- slot{"location": "delhi"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
	- slot{"budget": "average cost for two more than 300"}
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
## User responded location and cuisine with greeting but said no to email
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "North Indian"}
	- slot{"location": "delhi"}
	- slot{"cuisine": "North Indian"}
	- action_validate_location
	- slot{"location": "delhi"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 300"}
    - slot{"budget": "more than 300"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
    - slot{"budget": "average cost for two more than 300"}
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
## User is playing and no proper response
* out_of_scope
    - utter_default
* out_of_scope
    - utter_default
* out_of_scope
    - utter_default
	- utter_goodbye
	- action_restarted

	
## 1 stage dialog
* restaurant_search{"location": "agra", "cuisine": "Thai", "budget": "300 - 700 range", "email": "xyz@test.com"}
    - action_validate_location
	- slot{"location": "agra"}
    - action_validate_cuisine
	- slot{"cuisine": "Thai"}
	- slot{"budget": "300 - 700 range"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## greet and 1 stage dialog
* greet
    - utter_greet
* restaurant_search{"location": "agra", "cuisine": "Thai", "budget": "300 - 700 range", "email": "xyz@test.com"}
    - action_validate_location
	- slot{"location": "agra"}
    - action_validate_cuisine
	- slot{"cuisine": "Thai"}
	- slot{"budget": "300 - 700 range"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## 2 stage dialog with email later
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican", "budget": "more than 700"}
    - action_validate_location
	- slot{"location": "Kolkata"}
    - action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- action_validate_email
	- action_email
	- utter_goodbye
    - action_restarted
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## 2 stage dialog without email - budget last
* restaurant_search{"location": "Mumbai", "cuisine": "Italian"}
    - action_validate_location
	- slot{"location": "Mumbai"}
    - action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
	
## 2 stage dialog without email - cuisine last
* restaurant_search{"location": "New Delhi", "budget": "less than 300"}
    - action_validate_location
	- slot{"location": "New Delhi"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
## 2 stage dialog without email - city last
* restaurant_search{"cuisine": "Mexican", "budget": "more than 700"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Bhopal"}
    - action_validate_location
	- slot{"location": "Bhopal"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
	
## 2 stage dialog without email - budget last
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted

## greet and 2 stage dialog with email later
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican", "budget": "more than 700"}
    - action_validate_location
	- slot{"location": "Kolkata"}
    - action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.org"}
	- action_validate_email
	- slot{"email": "xyz@test.org"}
	- action_email
	- utter_goodbye
    - action_restarted

	
## greet and 2 satage dialog without email - budget last
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "Italian"}
    - action_validate_location
	- slot{"location": "Mumbai"}
    - action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
	
## greet and 2 stage dialog without email - cuisine last
* greet
    - utter_greet
* restaurant_search{"location": "New Delhi", "budget": "less than 300"}
    - action_validate_location
	- slot{"location": "New Delhi"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
	
## greet 2 stage dialog without email - city last
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "budget": "more than 700"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Bhopal"}
    - action_validate_location
	- slot{"location": "Bhopal"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
	
## greet and 2 stage dialog without email - budget last
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted

## 3 stage dialog without email - city -> cuisine ->budget
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
	
## 3 stage dialog without email -  cuisine ->city ->budget
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted

## 3 stage dialog without email -  budget->cuisine ->city
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
	- action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_location
* restaurant_search{"location": "Chennai"}
    - action_validate_location
	- slot{"location": "Chennai"}
	- utter_top_restaurant	
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted

## 3 stage dialog without email -  budget ->city->cuisine
* restaurant_search{"budget": "less than 300"}
	- slot{"budget": "less than 300"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_ask_location
* restaurant_search{"location": "Nagpur"}
    - action_validate_location
	- slot{"location": "Nagpur"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
	- action_validate_cuisine
	- slot{"cuisine": "American"}	
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
	
## 3 stage dialog without email - city  ->budget-> cuisine
* restaurant_search{"location": "Mumbai"}
    - action_validate_location
	- slot{"location": "Mumbai"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
	
## 3 stage dialog without email -  cuisine ->budget ->city
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Pune"}
    - action_validate_location
	- slot{"location": "Pune"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
	


## greet and 3 stage dialog without email - city -> cuisine ->budget
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
	
## greet and 3 stage dialog without email -  cuisine ->city ->budget
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted

## greet and 3 stage dialog without email -  budget->cuisine ->city
* greet
    - utter_greet
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
	- action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_location
* restaurant_search{"location": "Chennai"}
    - action_validate_location
	- slot{"location": "Chennai"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted

## greet and 3 stage dialog without email -  budget ->city->cuisine
* greet
    - utter_greet
* restaurant_search{"budget": "less than 300"}
	- slot{"budget": "less than 300"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_ask_location
* restaurant_search{"location": "Nagpur"}
    - action_validate_location
	- slot{"location": "Nagpur"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
	- action_validate_cuisine
	- slot{"cuisine": "American"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
	
## greet and 3 stage dialog without email - city  ->budget-> cuisine
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - action_validate_location
	- slot{"location": "Mumbai"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
	
## greet and 3 stage dialog without email -  cuisine ->budget ->city
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Pune"}
    - action_validate_location
	- slot{"location": "Pune"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* deny
	- utter_goodbye
    - action_restarted
	
	
	
## 2 stage dialog with email - budget last
* restaurant_search{"location": "Mumbai", "cuisine": "Italian"}
    - action_validate_location
	- slot{"location": "Mumbai"}
    - action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.edu"}
	- action_validate_email
	- slot{"email": "xyz@test.edu"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## 2 stage dialog with email - cuisine last
* restaurant_search{"location": "New Delhi", "budget": "less than 700"}
    - action_validate_location
	- slot{"location": "New Delhi"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.in"}
	- action_validate_email
	- slot{"email": "xyz@test.in"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## 2 stage dialog with email - city last
* restaurant_search{"cuisine": "Mexican", "budget": "more than 700"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Bhopal"}
    - action_validate_location
	- slot{"location": "Bhopal"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.jp"}
	- action_validate_email
	- slot{"email": "xyz@test.jp"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## 2 stage dialog with email - budget last
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- utter_goodbye
    - action_restarted

## greet and 2 stage dialog with email later
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican", "budget": "more than 700"}
    - action_validate_location
	- slot{"location": "Kolkata"}
    - action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- utter_goodbye
    - action_restarted

	
## greet and 2 stage dialog with email - budget last
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "Italian"}
    - action_validate_location
	- slot{"location": "Mumbai"}
    - action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.gov"}
	- action_validate_email
	- slot{"email": "xyz@test.gov"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## greet and 2 stage dialog with email - cuisine last
* greet
    - utter_greet
* restaurant_search{"location": "New Delhi", "budget": "less than 700"}
    - action_validate_location
	- slot{"location": "New Delhi"}
	- slot{"budget": "less than 700"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.co.in"}
	- action_validate_email
	- slot{"email": "xyz@test.co.in"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## greet 2 stage dialog with email - city last
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "budget": "more than 700"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Bhopal"}
    - action_validate_location
	- slot{"location": "Bhopal"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## greet and 2 stage dialog with email - budget last
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- utter_goodbye
    - action_restarted

## 3 stage dialog with email - city -> cuisine ->budget
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- action_validate_email
	- action_email
	- utter_goodbye
    - action_restarted
	
## 3 stage dialog with email -  cuisine ->city ->budget
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- utter_goodbye
    - action_restarted

## 3 stage dialog with email -  budget->cuisine ->city
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
	- action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_location
* restaurant_search{"location": "Chennai"}
    - action_validate_location
	- slot{"location": "Chennai"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.org"}
	- action_validate_email
	- slot{"email": "xyz@test.org"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## 3 stage dialog with email -  budget ->city->cuisine
* restaurant_search{"budget": "less than 300"}
	- slot{"budget": "less than 300"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_ask_location
* restaurant_search{"location": "Nagpur"}
    - action_validate_location
	- slot{"location": "Nagpur"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
	- action_validate_cuisine
	- slot{"cuisine": "American"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.edu"}
	- action_validate_email
	- slot{"email": "xyz@test.edu"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## 3 stage dialog with email - city  ->budget-> cuisine
* restaurant_search{"location": "Mumbai"}
    - action_validate_location
	- slot{"location": "Mumbai"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.edu"}
	- action_validate_email
	- slot{"email": "xyz@test.edu"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## 3 stage dialog with email -  cuisine ->budget ->city
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Pune"}
    - action_validate_location
	- slot{"location": "Pune"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.in"}
	- action_validate_email
	- slot{"email": "xyz@test.in"}
	- action_email
	- utter_goodbye
    - action_restarted
	


## greet and 3 stage dialog with email - city -> cuisine ->budget
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.in"}
	- action_validate_email
	- slot{"email": "xyz@test.in"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## greet and 3 stage dialog with email -  cuisine ->city ->budget
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.in"}
	- action_validate_email
	- slot{"email": "xyz@test.in"}
	- action_email
	- utter_goodbye
    - action_restarted

## greet and 3 stage dialog with email -  budget->cuisine ->city
* greet
    - utter_greet
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
	- action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_location
* restaurant_search{"location": "Chennai"}
    - action_validate_location
	- slot{"location": "Chennai"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.in"}
	- action_validate_email
	- slot{"email": "xyz@test.in"}
	- action_email
	- utter_goodbye
    - action_restarted

## greet and 3 stage dialog with email -  budget ->city->cuisine
* greet
    - utter_greet
* restaurant_search{"budget": "less than 300"}
	- slot{"budget": "less than 300"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_ask_location
* restaurant_search{"location": "Nagpur"}
    - action_validate_location
	- slot{"location": "Nagpur"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
	- action_validate_cuisine
	- slot{"cuisine": "American"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.in"}
	- action_validate_email
	- slot{"email": "xyz@test.in"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## greet and 3 stage dialog with email - city  ->budget-> cuisine
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - action_validate_location
	- slot{"location": "Mumbai"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.in"}
	- action_validate_email
	- slot{"email": "xyz@test.in"}
	- action_email
	- utter_goodbye
    - action_restarted
	
## greet and 3 stage dialog with email -  cuisine ->budget ->city
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location	
* restaurant_search{"location": "Pune"}
    - action_validate_location
	- slot{"location": "Pune"}
	- utter_top_restaurant
	- action_restaurant
	- utter_ask_about_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.in"}
	- action_validate_email
	- slot{"email": "xyz@test.in"}
	- action_email
	- utter_goodbye
    - action_restarted	

## Generated Story -2892949591761075718
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_location
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 300"}
    - slot{"budget": "more than 300"}
	- action_validate_budget
	- slot{"budget": "mid"}
    - utter_top_restaurant
    - action_restaurant
    - slot{"budget": "average cost for two more than 300"}
    - utter_ask_about_emailing
* send_email{"email": "@kp.com"}
    - slot{"email": "@kp.com"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_email_id
* send_email{"email": "kaustubh.pargaonkar@gmail.com"}
    - slot{"email": "kaustubh.pargaonkar@gmail.com"}
    - action_validate_email
    - slot{"email": "kaustubh.pargaonkar@gmail.com"}
    - action_email
    - slot{"email": "kaustubh.pargaonkar@gmail.com"}
    - utter_goodbye
    - action_restarted
	
## Generated Story 2182004289715809328
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_validate_location
    - slot{"location": "allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "> 700"}
    - slot{"budget": "> 700"}
	- action_validate_budget
	- slot{"budget": "high"}
    - utter_top_restaurant
    - action_restaurant
    - slot{"budget": "average cost for two > 700"}
    - utter_ask_about_emailing
* send_email{"email": "kaustubh.pargaonkar@gmail.com"}
    - slot{"email": "kaustubh.pargaonkar@gmail.com"}
    - action_validate_email
    - slot{"email": "kaustubh.pargaonkar@gmail.com"}
    - action_email
    - slot{"email": "kaustubh.pargaonkar@gmail.com"}
    - utter_goodbye
    - action_restarted