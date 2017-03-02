# Bangor Savings Charity Rewards


### Current Weekly Objective (By 3/22)
- Jake and Katie research views
- webdev and infra teams code and make PRs 

### Discussion Points for Next Meeting
- Jake and Katie lead View designs
- webdev and infra talk about their PRs
- potentially swap a few roles 


### Team Members
- Nathan Mathis
- Kevin Lewis???
- Jake wuz here
- Katie is here
- Cramer (Isabel Hernandez)
- xxJacksonHeyxx
- Katrina
- Ben Jeffrey
- Mitchell Smith

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


### 3/1 Meeting Notes
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
	views
		- jake
		- katie

	infrastructure 
		- ben
		- jackson
		- katrina

	webdev
		- mitchell
		- nathan
		- cramer
		- kevin