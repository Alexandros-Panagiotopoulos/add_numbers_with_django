# Task

## Software Engineer Python Test

Create a REST endpoint that return the sum of a list of numbers e.g. [1,2,3] => 1+2+3 = 6  
You are free to use any Python 3 framework, however, try and keep the usage of the thirdparty library to a minimum.  
The list of numbers is expected to arrive from a backend service and for this test you can hard code the list using the following line. 
#### Code  
```
numbers_to_add = list(range(10000001))
```

The url of the endpoint and the sample response is as follows:  

#### Request: http://localhost:5000/total  
  
#### Response:  
```
{
"total": 6
}
```

Please provide the source code, tests, documentations and any assumptions you have made.  
Note: We are looking for the candidate's "Software Engineering" ability not just the Python programming skills.


# Solution

The solution was created using Python 3.7 and Django 3.0.3

In order to run the code, the following library should be installed:
jangorestframework

The endpoint can receive a GET request at `/total` or a POST request at `/new_list`

- #### GET request

The GET request is received by `add_numbers/urls.py` and handled by `add_numbers/views` using the function `summing_up`.  
The `summing_up` function retrieves the list of numbers (it is meant to be retrieved from the database but it is hardcoded for this task) and calls the `SumUpNumbers` class at `summing_up` Django app models.  
The logic of adding numbers is implemented at the `get_the_sum` function of the class which returns the sum of the numbers so as the `summing_up` function of the views to respond using the correct foramt.  

- #### POST request

The POST request is received by `add_numbers/urls.py` and handled by `add_numbers/views` using the function `create_list_of_numbers`.  
The POST request is expected to arrive from a backend service as follow:

#### Request
```
POST /new_list

{
"key": "list_of_numbers" 
}
```

The message is analised and validated with the help of `get_list_from_string` and `check_if_list_is_valid` functions to handle possible errors and corfirm that it is an acceptable list of numbers.  
If the request is valid the response is:  

#### Response with status 200:  
```
{
"title": 'list of numbers was successfully stored',  
"status": 200
}
```
while if it is not valid:  
#### Response with status 400:  
```
{
"title": 'Invalid list of numbers. Please post a simple list of numbers for Python 3 to read',  
"status": 400
}
```
The valid list of numbers are meant to be stored on a database but for this test this stage is ommited and the list is hardcoded according to the task.

### Assumptions

The list should only contain integers and float numbers (real numbers) to be considered as valid and any other type like complex numbers are not accepted.
