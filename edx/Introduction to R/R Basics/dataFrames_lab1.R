mpg <- c(21.0,21.0,22.8)
cyl <- c(6,6,4)
disp <- c(160.0,160.0,108.0)
hp <- c(110,110,93)
drat <- c(3.90,3.90,3.85)
wt <- c(2.620,2.875,2.320)
qsec <- c(16.46,17.02,18.61)
vs <- c(0,0,1)
am <- c(1,1,1)
gear <- c(4,4,4)
carb <- c(4,4,1)
mtcars <- data.frame(mpg,cyl,disp,hp,drat,wt,qsec,vs,am,gear,carb,row.names = c("Mazda RX4","Mazda RX4 Wag","Datsun 710"))

# Print the first observations of mtcars
head(mtcars)

# Print the last observations of mtcars
tail(mtcars)

# Print the dimensions of mtcars
dim(mtcars)

# Investigate the structure of the mtcars data set
str(mtcars)


# Definition of vectors
planets <- c("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
type <- c("Terrestrial planet", "Terrestrial planet", "Terrestrial planet", 
          "Terrestrial planet", "Gas giant", "Gas giant", "Gas giant", "Gas giant")
diameter <- c(0.382, 0.949, 1, 0.532, 11.209, 9.449, 4.007, 3.883)
rotation <- c(58.64, -243.02, 1, 1.03, 0.41, 0.43, -0.72, 0.67)
rings <- c(FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE)

# Create a data frame: planets_df
planets_df <- data.frame(planets,type,diameter,rotation,rings)

# Display the structure of planets_df
str(planets_df)


# Encode type as a factor: type_factor

type_factor <- factor(type)
# Construct planets_df: strings are not converted to factors!
planets_df1 <- data.frame(planets,type_factor,diameter,rotation,rings,stringsAsFactors=FALSE)

# Display the structure of planets_df
str(planets_df1)

# Improve the names of planets_df
names(planets_df1) <- c("name","type","diameter","rotation","has_rings")
planets_df1





countries <- c("Canada","United States","France","Belgium","India","China","United Kingdom","Russia")
continents <- c("North-America","North-America","Europe","Europe","Asia","Asia","Europe","Asia")
gdp <- c(44843,54596,44538,47787,1808,8154,45653,8184)
hdi <- c(0.902,0.914,0.884,0.881,0.586,0.719,0.892,0.778)
president <- c(FALSE,TRUE,TRUE,FALSE,TRUE,TRUE,FALSE,TRUE)

# Convert continents to factor: continents_factor

continents_factor <- factor(continents)
# Create countries_df with the appropriate column names
countries_df <- data.frame(countries,continents=continents_factor,gdp,hdi,president,stringsAsFactors=FALSE)

# Display the structure of countries_df
str(countries_df)


