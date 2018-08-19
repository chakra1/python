# CTR Data generator 
## CTR -- click-through rate

This project is meant to generate click-through rate or CTR data which is a very common dataset needed for any sort of clickstream analysis. 

# Project structure
The project consists of three components  

***src*** - Containing **CTRDataGenerator.py** and **DatetimeClass.py**  

*  *CTRDataGenerator.py* - This is the Python **main** module generating the CTR data based on certain input parameters as described below. Takes below optional parameters  

    * &lt;schemafile&gt; - Name with location of the JSON schema file. It can be any location of user-input schema file with the format as specified by jsonschema. In case of no user input, the default schema will be loaded from `schema\CTR_Schema.json`  
    * &lt;size&gt;       - Size of the dataset to be generated  
    * &lt;startdate&gt;  - Start date of the date range from which click times are to be generated  
    * &lt;enddate&gt;    - End date of the date range from which click times are to be generated  
    * &lt;timeformat&gt; - Format in which the click time is to be generated  
    * &lt;outputfile&gt; - Name with location of the JSON data file to be generated. In case of no user input, the default data file will be under `data\gen_data.json`   

*  *DatetimeClass.py* - This is the Python class which is initialized using constructor parameters -  
    * start  - start date,
    * end    - end date, 
    * format - format of the datetime generated, validated against DatetimeFormat  

The format in the constructor parameter is validated against an internal DatetimeFormat class which contains a list of supported format enum values. 

***NOTE:*** Please note that an user who intend to incorporate new format for datetimes, need to add that new format in this list of enum values  

There are two methods in the *DatetimeClass*

    * DatetimeClass.generate_random_datetime(x) - Returns a random datetime generated between start  
    * DatetimeClass.generate_N_datetimes(n)       - Size of the dataset to be generated  
    





# Schema of the data
The schema of the data is provided 

