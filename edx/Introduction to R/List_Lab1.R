# Numeric vector: 1 up to 10
my_vector <- 1:10 

# Numeric matrix: 1 up to 9
my_matrix <- matrix(1:9, ncol = 3)

# Factor of sizes
my_factor <- factor(c("M","S","L","L","M"), ordered = TRUE, levels = c("S","M","L"))

# Construct my_list with these different elements
my_list <- list(my_vector,my_matrix,my_factor)

# Construct my_super_list with the four data structures above
my_super_list <- list(my_vector, my_matrix, my_factor,my_list)

# Display structure of my_super_list
str(my_super_list)

# Construct my_list with these different elements
my_list1 <- list(vec=my_vector, mat=my_matrix, fac=my_factor)

# Print my_list to the console
my_list1



# Create actors and reviews
actors_vector <- c("Jack Nicholson","Shelley Duvall","Danny Lloyd","Scatman Crothers","Barry Nelson")
reviews_factor <- factor(c("Good", "OK", "Good", "Perfect", "Bad", "Perfect", "Good"), 
                         ordered = TRUE, levels = c("Bad", "OK", "Good", "Perfect"))

# Create shining_list
shining_list <- list(title="The Shining",actors=actors_vector,reviews=reviews_factor)


top <- c("basic data type","vectors","matrices","factors","lists")
top
cont_vector <- c("core","data","data","data","data")
cont <- factor(cont_vector)
cont
prop <- matrix(c(TRUE,FALSE,TRUE,TRUE,FALSE,FALSE,TRUE,TRUE,TRUE,FALSE,TRUE,FALSE,TRUE,TRUE,TRUE,FALSE),nrow=4)
rownames(prop) <- c("ID","heterogeneous","subsetting","arithmetic")
colnames(prop) <- c("vector","matrix","factor","list")
prop

# Create the list lst
lst <- list(top[5],prop[,4])

# Create the list skills
skills <- list(topics=top,context=cont,properties=prop,list_info=lst)

# Display the structure of skills
str(skills)
