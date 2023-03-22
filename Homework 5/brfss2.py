
import numpy as np

try:

  # Load data from a CSV file into numpy array

  my_data = np.genfromtxt('brfss.csv', dtype="int", delimiter=',', skip_header=1)
  
  # Make sure the data is succesfully loaded by printing it and the shape
  print("\nFirst Five Rows of the Data:\n")
  print(my_data[:5])
  print(my_data.shape)

  print("\n")

  # Create a new column and concatenate it based on the difference between the weight of last year and the current weight

  new_column = my_data[:,2] - my_data[:, 3]
  my_data = np.column_stack((my_data, new_column))

  print("First Five Rows of the Data with Weight Changes:\n")
  print(my_data[:5])
  print(my_data.shape)

  # Calculate descriptive statistics variables for data related to weight change

  my_mean = np.mean(my_data[:, 6])
  my_median = np.median(my_data[:, 6])
  my_standard_deviation = np.std(my_data[:, 6])
  my_interquartile_range = np.percentile(my_data[:, 6], 75) - np.percentile(my_data[:, 6], 25)

  print("\nDescriptive Statistics for Weight Change Data:")
  print(f"\nMean: {round(my_mean, 2)} ")
  print(f"Median: {round(my_median, 2)} ")
  print(f"Standard Deviation: {round(my_standard_deviation, 2)} ")
  print(f"Interquartile Range: {round(my_interquartile_range, 2)} ")

  print("\n")

  # Create a list of arrays based on number of unique genders, whose subarrays will only display rows of a specific gender

  gender_arrays = [my_data[my_data[:,5]==gender] for gender in np.unique(my_data[:,5])]

  # Counter to keep track of gender being displayed

  i = 0

  # For each gender array created, we will print the first five rows, and other expected information about the data
 
  for gender_array in gender_arrays:

    # Protect against bad data

    if (i > 2):
      break;

    # Which gender is it

    if (i==0):
      print("First Five Rows of the Data Relevant to Males\n")
    elif (i==1):
      print("First Five Rows of the Data relevant to Females:\n")
    else:
      print("First Five Rows of the Data relevant to Other:\n") 
    
    # Print the rows and shape of the data

    print(gender_array[:5])
    print(gender_array.shape)

    # Calculate the descriptive statistics data variables regarding the weight

    my_mean = np.mean(gender_array)
    my_median = np.median(gender_array)
    my_standard_deviation = np.std(gender_array)
    my_interquartile_range = np.percentile(gender_array, 75) - np.percentile(gender_array, 25)

    print("\n")

    # Which gender is it

    if (i==0):
      print("Descriptive Statistics of the Data Relevant to Males")
    elif (i==1):
      print("Descriptive Statistics of the Data relevant to Females:")

    # Display the descriptive statistics of each data relevant to each gender

    print(f"\nMean: {round(my_mean, 2)} ")
    print(f"Median: {round(my_median, 2)} ")
    print(f"Standard Deviation: {round(my_standard_deviation, 2)} ")
    print(f"Interquartile Range: {round(my_interquartile_range, 2)} \n")

    # Keep track of the gender

    i = i + 1

# Let the user know the file was not found

except FileNotFoundError:
  print("The file does not exist or is in the wrong location") 


# Another error was encountered, print exception information to help troubleshoot

except Exception as e: 
  print(f"An error occurred while loading the file: {e}")