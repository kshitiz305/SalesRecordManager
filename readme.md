## **Pandas Tasks:**

Write a code showing how to read a file using pandas Convert multiple JSON files to CSV using Python Problem: If all the
columns match, we will load the two json files, concatenate one to another and convert to a CSV file.

The json files used for this are:

**_File1.json_**

`{
"ID":{
"0":23,
"1":43,
"2":12,
"3":13,
"4":67,
"5":89 },
"Name":{
"0":"Ram",
"1":"Deep",
"2":"Yash",
"3":"Aman",
"4":"Arjun",
"5":"Aditya"
},
"Marks":{
"0":89,
"1":97,
"2":45,
"3":78,
"4":56,
"5":76 },
"Grade":{
"0":"B",
"1":"A",
"2":"F",
"3":"C",
"4":"E",
"5":"C"
} }`

**_File2.json_**

`{
"ID":{
"0":90,
"1":56,
"2":34,
"3":96,
"4":45 },
"Name":{
"0":"Akash",
"1":"Chalsea",
"2":"Divya",
"3":"Sajal",
"4":"Shubham"
},
"Marks":{
"0":81,
"1":87,
"2":100,
"3":89,
"4":78 },
"Grade":{
"0":"B",
"1":"B",
"2":"A",
"3":"B",
"4":"C"
} }`

Merge multiple CSV files in a unique dataset making it into 5 million rows using python.

**Problem**: You have been given a folder that contains 5 CSV files having 1 million sales records each. Using pandas
and python merge all the csv files in the given folder into one CSV file having 5 million records. You may choose to
reset the index. (You may write the code assuming you have a folder named sales_records in your project directory which
would contain the 5 csv files)