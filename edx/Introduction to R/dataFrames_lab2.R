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



# planets_df is pre-loaded

# The type of Mars: mars_type
mars_type <- planets_df1[4,2]

# Entire rotation column: rotation
rotation <- planets_df1[,4]

# First three planets: closest_planets_df
closest_planets_df <- planets_df1[c(1,2,3),]

# Last three planets: furthest_planets_df

furthest_planets_df <- planets_df1[c(6,7,8),]


# Diameter and rotation for Earth: earth_data 

earth_data <- planets_df1[3,c(3,4)]
# Diameter for the last six rows: furthest_planets_diameter

furthest_planets_diameter <- planets_df1[3:8,3]
# Print furthest_planets_diameter
furthest_planets_diameter

# Create rings_vector
rings_vector <- planets_df1$has_rings

# Print rings_vector
rings_vector

# Create rings_vector
rings_vector <- planets_df$has_rings

# Select the information on planets with rings: planets_with_rings_df
planets_with_rings_df <- planets_df1[rings_vector,]
planets_with_rings_df


# Planets that are smaller than planet Earth: small_planets_df
small_planets_df <- subset(planets_df1,subset=diameter<planets_df1[3,3])
# Planets that rotate slower than planet Earth: slow_planets_df
slow_planets_df <- subset(planets_df1,subset=abs(rotation)>planets_df1[3,4])

# Definition of moons and masses
moons <- c(0, 0, 1, 2, 67, 62, 27, 14)
masses <- c(0.06, 0.82, 1.00, 0.11, 317.8, 95.2, 14.6, 17.2)

# Add moons to planets_df under the name "moon"
planets_df1$moon <- moons

# Add masses to planets_df under the name "mass"
planets_df1$mass <- masses

# Name pluto correctly
pluto <- data.frame(name="Pluto", type="Terrestrial planet", diameter=0.18, rotation=-6.38, has_rings=FALSE)

# Bind planets_df and pluto together: planets_df_ext
planets_df_ext <- rbind(planets_df1d,pluto)

# Print out planets_df_ext
planets_df_ext

# Create a desired ordering for planets_df: positions
positions <- order(planets_df1$diameter,decreasing=TRUE)

# Create a new, ordered data frame: largest_first_df

largest_first_df <- planets_df1[positions,]
# Print largest_first_df
largest_first_df



countries <- c("Canada","United States","France","Belgium","India","China","United Kingdom","Russia")
continents <- c("North-America","North-America","Europe","Europe","Asia","Asia","Europe","Asia")
gdp <- c(44843,54596,44538,47787,1808,8154,45653,8184)
hdi <- c(0.902,0.914,0.884,0.881,0.586,0.719,0.892,0.778)
president <- c(FALSE,TRUE,TRUE,FALSE,TRUE,TRUE,FALSE,TRUE)
population <- c(35749600,321163157,66616416,11239755,1210193422,1357380000,64511000,143975923)
# Convert continents to factor: continents_factor

continents_factor <- factor(continents)
# Create countries_df with the appropriate column names
countries_df <- data.frame(countries,continents=continents_factor,gdp,hdi,president,stringsAsFactors=FALSE)

# Remove economic variables and add population

countries_df_dem <- countries_df[,c(1,2,5)]
countries_df_dem <- cbind(countries_df_dem,population)
# Add brazil
brazil <- data.frame(name="Brazil",continent="South-America",has_president=TRUE,population=202768562)
countries_df2 <- rbind(countries_df_dem,brazil)

# Sort by population
countries_df2[order(countries_df2$population,decreasing=TRUE),]


