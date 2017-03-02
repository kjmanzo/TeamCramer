# Bangor Savings Charity Rewards


### Current Weekly Objective (By 3/1)
- Get everyone to add their name to the team members section of the readme
- Get everyone up to part 2 on the django tutorial


### Discussion Points for Next Week
- Assign roles with new django understanding
- Decide what to do over break
- Discuss Model and View designs


### Team Members
- Nathan Mathis
- Kevin Lewis???
- Jake wuz here
- Katie is here
- Cramer (Isabel Hernandez)
- xxJacksonHeyxx
- Katrina
- Ben Jeffrey
-Mitchell Smith

### References
- [Django Tutorial](https://docs.djangoproject.com/en/1.10/intro/tutorial01/)


### Useful Terminal Commands
```
mkvirtualenv <name_of_env> 	-- virtualenvwrapper - makes virtual environment
workon <name_of_env>		-- virtualenvwrapper - changes to selected virtual environment
python bootstrap.py 		-- pip installs requirements.txt on your virtual environment
``` 


### Guide To Changing Models:
- Change your models (in models.py).
- Run `python manage.py makemigrations` to create migrations for those changes.
- Run `python manage.py migrate` to apply those changes to the database.


### March 1st Meeting Notes
##### Model Additions
	charity 
		- url
		- picture

	
	user
		- friendslist - foriegnkey for other users
		- list of dicts with charity and points given
		- total points given
		- picture


	activity / interaction
		- user id for guy who did
		- charity key
		- english description (points given and charity)
		- timestamp


##### New Roles / Teams
views - GETTING POSTING
	- jake
	- katie


models / urls 
	- ben
	- jackson
	- katrina


web stuff
	- mitchell
	- nathan
	- cramer
	- kevin