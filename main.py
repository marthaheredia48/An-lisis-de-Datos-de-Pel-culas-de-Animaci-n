#Talking Data Starter Code

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "The Iron Giant"
#check that the movie is written correctly!! with spaces and grammar
print("My favorite movie is " + favMovie)



#Part 3 Investigate the data
#print(movieData["movie_title"])


#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information

#we need the name of the data frame, movie data, and inside square brackets and quotes, the column name movie underscore title.

favMovieBooleanList = movieData["movie_title"] == favMovie

#print(favMovieBooleanList)

#Loc stands for location - this attribute will help us locate the rows we’re looking for. An attribute is used to access more information about an object, or in our case the data frame. To know what to locate, Loc needs to know which rows to access. We can put our fave movie boolean list variable inside the square brackets, and loc will select, or give us, the output of rows where the boolean is true.

favMovieData = movieData.loc[favMovieBooleanList]
print(favMovieData)

print("\n\n")

#Create a new variable to store a new data set with a certain genre
animationMovieBooleanList = movieData["genres"].str.contains("Animation")

animationMovieData = movieData.loc[animationMovieBooleanList]

numOfMovies = animationMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Animation in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Animation.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
#min
min = animationMovieData["audience_rating"].min()

print("The min audience rating of the data set is: " + str(min))


print(favMovie + " is rated " + str(abs(min - 90)) + " points higher than the lowest rated movie.")
print()

#find max
max = animationMovieData["audience_rating"].max()

#Min and max are methods that can help us start to understand where it falls in comparison to the lowest and highest values. we can access the column of the audience ratings from our new genre movie data We need to call the name of the dataframe

print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated " + str(abs(max - 90)) + " points lower than the highest rated movie.")

print()

#find mean
mean = animationMovieData["audience_rating"].mean()

print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is higher than the mean movie rating.")

#find median
median = animationMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is higher than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist(animationMovieData["audience_rating"], range = (0, 100), bins = 20)

#These bars are called bins. In the hist method, we'll type a comma to separate the parameters, range equal parenthesis zero comma one hundred. This is telling the histogram that our values go from zero to one hundred - all the possible audience ratings since it is a percentage. Next, let's tell the histogram how to divide them. type a comma to separate the parameters, and type bins equal 20. Now let's think - what will each bin represent? With 100 values, we just have to divide them by 20.


#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Rating of Animation Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Numbers of Animation Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, most animated movies had an audience rating between 70 and 80. Also you can find that there are 16 bins in total which are located between 20 to 100. "
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = animationMovieData, x = "audience_rating", y = "critic_rating")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating versus Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, we can see that there is a positive correlation, which means that as the audience rating increases, the critic rating also tends to increase."
)
print()

print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")

