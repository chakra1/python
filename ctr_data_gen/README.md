# CTR Data generator 
## CTR -- click-through rate

This project is meant to generate click-through rate or CTR data which is a very common dataset needed for any sort of clickstream analysis. 

# Project structure
The project consists of three components  
* **src** - Containing `CTRDataGenerator.py` + `DatetimeClass.py`  
          1.  `CTRDataGenerator.py` - Takes below optional parameters  
                `<schemafile>` - Name with location of the JSON schema file. It can be any location of user-input schema file with the                                      format as specified by jsonschema. In case of no user input, the default schema will be loaded from   `schema\CTR_Schema.json`  
                `<size>`       - Size of the dataset to be generated  
                `<startdate>`  - Start date of the date range from which click times are to be generated  
                `<enddate>`    - End date of the date range from which click times are to be generated  
                `<timeformat>` - Format in which the click time is to be generated  
                `<outputfile>` - Name with location    


# Schema of the data
The schema of the data is provided 

