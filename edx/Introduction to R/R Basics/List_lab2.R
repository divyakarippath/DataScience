# Create actors and reviews
actors_vector <- c("Jack Nicholson","Shelley Duvall","Danny Lloyd","Scatman Crothers","Barry Nelson")
reviews_factor <- factor(c("Good", "OK", "Good", "Perfect", "Bad", "Perfect", "Good"), 
                         ordered = TRUE, levels = c("Bad", "OK", "Good", "Perfect"))

# Create shining_list
shining_list <- list(title="The Shining",actors=actors_vector,reviews=reviews_factor)

# Actors from shining_list: act
act <- shining_list[["actors"]]

# List containing title and reviews from shining_list: sublist
sublist <- shining_list[c(1,3)]

# Display structure of sublist
str(sublist)

# Select the last actor: last_actor

last_actor <- shining_list[[2]][5]
# Select the second review: second_review
second_review <- shining_list[[3]][2]

# Add the release year to shining_list
shining_list$year <- 1980

# Add the director to shining_list

shining_list$director <- "Stanley Kubrick"
# Inspect the structure of shining_list
str(shining_list)

c(shining_list,
  opinions = c("Love it!", "Hate it!")) #wrong

c(shining_list,
  opinions = list(c("Love it!", "Hate it!")))

# Add both the year and director to shining_list: shining_list_ext
shining_list_ext <- c(shining_list,year=1980,director="Stanley Kubrick")

# Have a look at the structure of shining_list_ext
str(shining_list_ext)


top <- c("basic data type","vectors","matrices","factors","lists")
cont_vector <- c("core","data","data","data","data")
cont <- factor(cont_vector)
prop <- matrix(c(TRUE,FALSE,TRUE,TRUE,FALSE,FALSE,TRUE,TRUE,TRUE,FALSE,TRUE,FALSE,TRUE,TRUE,TRUE,FALSE),nrow=4)
rownames(prop) <- c("ID","heterogeneous","subsetting","arithmetic")
colnames(prop) <- c("vector","matrix","factor","list")
# Create the list lst
lst <- list(top[5],prop[,4])
lst
# Create the list skills
skills <- list(topics=top,context=cont,properties=prop,list_info=lst)

# Create the list key_skills
key_skills <- list(skills$topics[2],skills$context[2],skills$list_info[[2]][4])