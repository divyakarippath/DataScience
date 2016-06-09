star_wars_matrix <- matrix(c(460.998,290.475,309.306,314.4,247.9,165.8),nrow=3)
star_wars_matrix

rownames(star_wars_matrix) <- c("A New Hope","The Empire Strikes Back","Return of the Jedi")
colnames(star_wars_matrix) <- c("US","non-US")
star_wars_matrix

# star_wars_matrix is already defined in your workspace
star_wars_matrix
# US box office revenue for "The Empire Strikes Back"
star_wars_matrix[2,1]
# non-US box office revenue for "A New Hope"
star_wars_matrix[1,2]

# star_wars_matrix is already defined in your workspace
star_wars_matrix
# Select all US box office revenue
star_wars_matrix[,1]

# Select revenue for "A New Hope"
star_wars_matrix[1,]

# Average non-US revenue per movie: non_us_all
non_us_all <- sum(star_wars_matrix[,2])/3

# Average non-US revenue of first two movies: non_us_some
non_us_some <- sum(star_wars_matrix[c(1,2),2])/2


# star_wars_matrix is already defined in your workspace
star_wars_matrix
# All figures for "A New Hope" and "Return of the Jedi"
star_wars_matrix[c(1,3),c(1,2)]

# star_wars_matrix is already defined in your workspace
star_wars_matrix
# Select the US revenues for "A New Hope" and "The Empire Strikes Back"
star_wars_matrix[c("A New Hope","The Empire Strikes Back"),"US"]

# Select the last two rows and both columns
star_wars_matrix[c("The Empire Strikes Back","Return of the Jedi"),c("US","non-US")]

# Select the non-US revenue for "The Empire Strikes Back"
star_wars_matrix["The Empire Strikes Back","non-US"]