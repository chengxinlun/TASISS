# TASISS
Tsinghua Astronomy Society Internal Service System

# Purpose and Aim
* WeChat official platform auto response
* Observatory opening reservation through WeChat official plarform API ```(under dev)```
* Observatory reservation checking-in ```(web portal completed, mobile plantform under dev)```
* Database including basic information about every member in TAS ```(under dev)```
* Localization for every non-admin webpage ```(under dev)```
* Weekly-meeting checking-in ```(planned)```

# Help
## Dependency
* Python 3 (Python 2 will NOT be supported)
* pycrypt (available at pip)
* wechat (available at pip)
* django 1.10 (available at pip)

## Start service
Open up a terminal and execute
```shell
python3 manage.py runserver
```

This service is currently hosted at ```127.0.0.1:8000``` with no index, so directly accessing ```/``` will result in HttpError.

## Admin account
Username: ```admin```
Password: ```chengxinlun```
Usable while still in development phase.

## Observatory opening reservation and checking-in
### Creating a observatory opening event
Currently only admin could create new opening. Permission of user creating new opening event is under development.

### Reservation Checking-in
#### Web Portal
Visit ```checkin/``` on your browser and a list of currently stored opening event will be displayed. Click on the one you want to check people in. (Currently no login is required, but it will be complimentary soon.)

Then a text-input field and a button are displayed in the new webpage. Enter the ```openid``` (the message received by user from our WeChat platform) and press button to authenticate. A list of results will be returned in the field of ```error_message```. (Well, I am too lazy to make a separate gui for it. Leave it to department of propoganda.)

Return Message | Technical Explaination | Interpretation
---|---|---
Successful_checkin	|	All authentication passed										|	User is granted to enter obsservatory.
Not_registered			|	```open_id``` cannot be found in database		|	User is a code that is not issued by TAS.
Repeated_checkin		|	```signed``` is not 0												|	User has used the code more than once.
Malformed_post			|	```POST``` package is malformed							| Possible program bug. Please contact the developer.

#### Mobile platform
* Android: Under development
* Other platform: NO SPECIAL SUPPORT WILL BE OFFERED

## Contact
Visit ```contact/``` on your browser and a list of currently available contact will show up with hyper-link to each individual's profile. The profiles can only be altered by admin
