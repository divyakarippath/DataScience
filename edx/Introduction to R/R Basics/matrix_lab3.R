# Star Wars box office in millions (!)
box_office_all <- c(461, 314.4, 290.5, 247.9, 309.3, 165.8)
movie_names <- c("A New Hope","The Empire Strikes Back","Return of the Jedi")
col_titles <- c("US","non-US")
star_wars_matrix <- matrix(box_office_all, nrow = 3, byrow = TRUE, dimnames = list(movie_names, col_titles))

# Definition of ticket_prices_matrix
ticket_prices_matrix <- matrix(c(5, 5, 6, 6, 7, 7), nrow = 3, byrow = TRUE, dimnames = list(movie_names, col_titles)) 

# Estimated number of visitors

visitors <- star_wars_matrix/ticket_prices_matrix
# Average number of US visitors
average_us_visitors <- sum(visitors[,1])/3

# Average number of non-US visitors
average_non_us_visitors <- sum(visitors[,2])/3




movie_names1 <- c("A New Hope","The Empire Strikes Back","Return of the Jedi")
col_titles1 <- c("US","non-US")
commission_rates <- matrix(c(0.25,0.28,0.23,0.26,0.20,0.21), nrow = 3, byrow = TRUE, dimnames = list(movie_names1, col_titles1))
commission_rates

budget <- c("A New Hope"=13.0,"The Empire Strikes Back"=18.0,"Return of the Jedi"=2.5)
budget

# Calculate the money that remains after subtracting the commission: remaining

remaining <- star_wars_matrix - (star_wars_matrix*commission_rates)
# Calculate income per film: remaining_tot

remaining_tot <- rowSums(remaining)
# Calculate profit

profit <- remaining_tot-budget