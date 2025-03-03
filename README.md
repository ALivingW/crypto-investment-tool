CRYPTO-INVESTMENT-TOOL

This is one of my favourite projects.

When a user opens the app, they can add the name of any coins that they would. This will allow them to to get the prices of the coins at the appropriate time that it should be recorded. 
When they input the name of a coin, a json file is created for that coin, and will initially be empty. As each day passes, the closing price of each coin will be stored in the file. 
Within this repository, are a lot of text files of the coins that have thier own files that store their closing prices for each day.

You may be thinking, why is there a threading module? The reason for this is so that the program to automatically run with the windows task manager at the appropriate time.
For any parts that require user input, those parts will be timed out due to the threading module. Then the prices of the coins can be updated automatically.
