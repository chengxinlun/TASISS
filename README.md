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
## Prerequisite Skills
* A well-enough Python skill (I major in physics, but still I am very accustomed to Python)
* Ability to understand the document of this porject, ```django``` and ```wechat``` (Most of them are in English)
* Enthusiasm and determinism

## Start development service testing
Open up a terminal and execute
```shell
./launch_service.sh
```
This service is currently hosted at ```http://45.33.62.211/``` with no index, so directly accessing ```/``` will result in HttpError.

For production use, it is triggered as an Apache service and much of the details have been concealed. Therefore, it is recommended only sticking to the development running if you want to debug this program.

## User login and logout
For any <a href="https://docs.djangoproject.com/en/1.10/topics/http/views/">django view</a> that needs a user login in order to continue, please add the annotation
```python
@login_required()
````
before the function.

Hyperlink to <a href="https://docs.djangoproject.com/en/1.10/topics/http/urls/#naming-url-patterns">named url</a>
```userauth:logout``` will logout and redirect current user to ```userauth:login``` on click.

## Adding more functionality to WeChat platform
Please note that it is NOT my duty to provide document for ```django``` or ```wechat```. For a developer, you should be able to read the documents by yourself. However, since ```wechat``` does not have a good-quality module, I will provide necessary help in this document.

Please also note that all functionality will only be added as a separate module for clarity and ```wxmanager.wxapp.WxApp``` will only include filtering the request.

According to the <a href="https://github.com/jeffkit/wechat">document</a> of ```wechat```, the following table represents the commonly-used responding functions for different types of messages.

Function Name | Type of Messages Responded to
--- | ---
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

All the ```on_xxx``` funtions have similar argument lists, ```on_xxx(self, request)```, whereas ```request``` is an instance of ```WxRequest```. Properties of ```WxRequest``` are the same with the ones in xml. A detailed walkthrough of xml data sent from WeChat could be found <a href="https://mp.weixin.qq.com/wiki/17/f298879f8fb29ab98b2f2971d42552fd.html">here</a>.

Inside each function, a quasi-switch-case funtion (sadly, there is no ```switch case``` funtion in Python) will redirect the incoming request according to its content. Due to the support of regular expression and versatility of selection criteria, it should be much much better than the auto-respond interface in the official platform.

The return of these ```on_xxx``` functions must be a derived class of ```WxResponse```. Built-in derived class of ```WxResponse``` is listed <a href="https://github.com/jeffkit/wechat#wxresponse">here</a>.

Please note that when overloading the funtions above, ```DO NOT``` delete the default situation where an ```unsupported``` text message will be returned if the incoming message does not match any of the pattern.
