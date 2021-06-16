#%% Imports
import pandas as pd
from sys import argv
from datetime import date

#%% Process script arguments
if len(argv) == 1:
    input_path = input("Input file path: ")
    output_path = input("Output file path (empty will override input file instead): ")
    if output_path == "":
        output_path = input_path
if len(argv) == 2:
    input_path = argv[1]
    print("Input file path:", input_path)
    output_path = input("Output file path (empty will override input file instead): ")
    if output_path == "":
        output_path = input_path
if len(argv) == 3:
    input_path = argv[1]
    print("Input file path:", input_path)
    output_path = argv[2]
    print("Output file path:", output_path)
if len(argv) > 3:
    print("Wrong number of arguments, use {} [input_path [output_path]]".format(argv[0]))
    exit(1)

#%% Read data from source file
data = pd.read_csv(input_path, sep="\t")

#%% Add a column with the number of days a given data set is available
days_available_label = "Days Available"
if days_available_label not in data.columns:
    print(days_available_label, "column not found, generating...")
    current_date = str(date.today())
    print("Current date:", current_date)
    data.insert(9, days_available_label,
                (pd.to_datetime(current_date) -
                 data["Date Donated"].astype("datetime64")).dt.days
                )
    print("Generated \"{}\" column".format(days_available_label))

#%% Add a column with the number of web hits a given data set gets per one day of it being available
number_of_web_hits_per_day_label = "Number of Web Hits per Day"
if number_of_web_hits_per_day_label not in data.columns:
    print(number_of_web_hits_per_day_label, "column not found, generating...")
    data.insert(11, number_of_web_hits_per_day_label,
                (pd.to_numeric(data["Number of Web Hits"], downcast="float") /
                 data[days_available_label]).astype(str).replace("nan", "")
                )
    print("Generated \"{}\" column".format(number_of_web_hits_per_day_label))

#%% Write data to target file
data.to_csv(output_path, sep="\t", index=False, float_format='%.f')
