# Star Wars box office in millions (!)
box <- c(460.998, 314.4, 290.475, 247.900, 309.306, 165.8)

# Create star_wars_matrix
star_wars_matrix <- matrix(box,nrow=3,byrow=TRUE)



# Star Wars box office in millions (!)
new_hope <- c(460.998, 314.4)
empire_strikes <- c(290.475, 247.900)
return_jedi <- c(309.306, 165.8)

# Create star_wars_matrix
star_wars_matrix <- rbind(new_hope,empire_strikes,return_jedi)



# Star Wars box office in millions (!)
new_hope <- c(460.998, 314.4)
empire_strikes <- c(290.475, 247.900)
return_jedi <- c(309.306, 165.8)
star_wars_matrix <- rbind(new_hope, empire_strikes, return_jedi)

# Name the columns and rows of star_wars_matrix
rownames(star_wars_matrix) <- c("A New Hope","The Empire Strikes Back","Return of the Jedi")
colnames(star_wars_matrix) <- c("US","non-US")



# Star Wars box office in millions (!)
new_hope <- c(460.998, 314.4)
empire_strikes <- c(290.475, 247.900)
return_jedi <- c(309.306, 165.8)
star_wars_matrix <- rbind(new_hope, empire_strikes, return_jedi)
colnames(star_wars_matrix) <- c("US", "non-US")
rownames(star_wars_matrix) <- c("A New Hope", "The Empire Strikes Back", "Return of the Jedi")

# Calculate the worldwide box office: worldwide_vector
worldwide_vector = rowSums(star_wars_matrix)
worldwide_vector

# Bind the new variable worldwide_vector as a column to star_wars_matrix: star_wars_ext
star_wars_ext <- cbind(star_wars_matrix,worldwide_vector)
star_wars_ext

# Matrix that contains the first trilogy box office
star_wars_matrix  

# Matrix that contains the second trilogy box office
#star_wars_matrix2 

# Combine both Star Wars trilogies in one matrix: all_wars_matrix
#all_wars_matrix = rbind(star_wars_matrix,star_wars_matrix2)

# Print box office Star Wars
#all_wars_matrix

# Total revenue for US and non-US: total_revenue_vector
total_revenue_vector <- colSums(star_wars_matrix)
total_revenue_vector

first_row <- c(6,8,7,9,9,10)
second_row <- c(6,8,7,5,9,6)
third_row <- c(5,4,6,6,7,8)
fourth_row <- c(4,5,3,4,6,8)


# Create the theater matrix

theater <- rbind(first_row,second_row,third_row,fourth_row)
# Calculate row_scores with rowSums()

row_scores <- rowSums(theater)
# cbind() together theater and row_scores: scores
scores <- cbind(theater,row_scores)
