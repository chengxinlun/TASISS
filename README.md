# TASISS
Tsinghua Astronomy Society Internal Service System

# Purpose and Aim
* WeChat official platform auto response
* Additional user login and logout
* Observatory opening reservation through WeChat official plarform API ```(partially finished)```
* Observatory reservation checking-in ```(web portal completed, mobile plantform under dev)```
* Database including basic information about every member in TAS ```(planned)```
* Localization for every non-admin webpage ```(planned)```
* Weekly-meeting checking-in ```(planned)```

# Help
## Dependency
* Python 3 (Python 2 will NOT be supported)
* pycrypt (available at pip)
* wechat (since its incompatibality with Python 3, a modified version is needed)
* django 1.10 (available at pip)

## Start service
Open up a terminal and execute
```shell
./launch_service.sh
```

This service is currently hosted at ```http://45.33.62.211/``` with no index, so directly accessing ```/``` will result in HttpError.

## Admin account
Username: ```admin```
Password: ```chengxinlun```
Usable while still in development phase.

## Observatory opening reservation and checking-in
### Creating a observatory opening event
Currently only admin could create new opening. Permission of user creating new opening event is under development.

### Reservation Checking-in
#### Web Portal
Visit ```45.33.62.211/checkin/``` on your browser and a list of currently stored opening event will be displayed. Click on the one you want to check people in. Login is required to do any of the step. A user (observatory admin) has been created for this functionality (if not please add it using admin):

Username: ```obcheckin```
Passowrd: ```observatory```

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
Visit ```45.33.62.211/contact/``` on your browser and a list of currently available contact will show up with hyper-link to each individual's profile. A user (contact admin) and a UI is planned.

# Developer Guide
## Prerequisites (sequence of items is not important)
* A well-enough Python skill (I am a physics student, yet I finished most part of the service system without other's help)
* Be able to understand the document of this porject, ```django``` and ```wechat``` (Most of them are in English)
* Enthusiasm

## User login and logout
For any <a href="https://docs.djangoproject.com/en/1.10/topics/http/views/">django view</a> that needs a user login in order to continue, please add the annotation
```python
@login_required()
````
before the function.

Hyperlink to <a href="https://docs.djangoproject.com/en/1.10/topics/http/urls/#naming-url-patterns">named url</a>
```python
userauth:logout
```
will logout current user on click.

## Adding more functionality to WeChat platform
Please notice that it is NOT my duty to provide document for ```django``` or ```wechat```. For a developer, you should be able to read the documents by yourself. However, since ```wechat``` does not have a good-quality module, I will provide necessary help about the usage of it.

Please also notice that all functionality will only be added as a separate module for clarity and ```wxmanager.wxapp.WxApp``` will only include filtering the request.

According to the <a href="https://github.com/jeffkit/wechat">document</a> of ```wechat```, the following table represents the commonly-used responding functions for different types of messages.

Function Name | Type of messages responded
on_text       | Text sent by user, including unicode expressions
on_link       | Link sent by user
on_image      | Image sent by user
on_voice      | Voice sent by user
on_video      | Video sent by user
on_location   | Location sent by user
on_subscribe  | Subscription event
on_unsubscribe| Unsubscription event
on_click      | Clicking on custom menus
on_view       | Clicking on custom menus linking to an url

Inside each function, a quasi-switch-case funtion (sadly, there is no ```switch case``` funtion in Python) will redirect the incoming request according to its content. Due to the support of regular expression and versatility of selection criteria, it should be much much better than the auto-respond interface provided defaultly.

Please note that when overloading the funtions above, ```DO NOT``` delete the default situation where an ```unsupported``` text message will be returned if the incoming message does not match any of the pattern.
