# Defintion of survey_vector and survey_factor
survey_vector <- c("R", "L", "L", "R", "R")
survey_factor <- factor(survey_vector, levels = c("R", "L"), labels = c("Right", "Left"))

# Summarize survey_vector
summary(survey_vector)

# Summarize survey_factor
summary(survey_factor)

# Definition of animal_vector and temperature_vector
animal_vector <- c("Elephant", "Giraffe", "Donkey", "Horse")
temperature_vector <- c("High", "Low", "High", "Low", "Medium")

# Convert animal_vector to a factor: animal_factor
animal_factor <- factor(animal_vector)

# Encode temperature_vector as a factor: temperature_factor
temperature_factor <- factor(temperature_vector,ordered=TRUE,levels=c("Low","Medium","High"))

# Print out animal_factor and temperature_factor
animal_factor
temperature_factor

# Definition of survey_vector and survey_factor
survey_vector <- c("R", "L", "L", "R", "R")
survey_factor <- factor(survey_vector, levels = c("R", "L"), labels = c("Right", "Left"))

# First element from survey_factor: right

survey_factor[1]
# Second element from survey_factor: left

survey_factor[2]
# Right 'greater than' left?
survey_factor[1]>survey_factor[2]


# Create speed_vector
speed_vector <- c("OK", "Slow", "Slow", "OK", "Fast") 

# Convert speed_vector to ordered speed_factor
speed_factor <- factor(speed_vector,ordered=TRUE,levels=c("Slow","OK","Fast"))

# Print speed_factor

speed_factor
# Summarize speed_factor
summary(speed_factor)



# Definition of speed_vector and speed_factor
speed_vector1 <- c("Fast", "Slow", "Slow", "Fast", "Ultra-fast")
factor_speed_vector <- factor(speed_vector1, ordered = TRUE, levels = c("Slow", "Fast", "Ultra-fast"))

# Compare DA2 with DA5: compare_them
compare_them <- factor_speed_vector[2] > factor_speed_vector[5]

# Print compare_them: Is DA2 faster than DA5?
compare_them