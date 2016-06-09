drawn_suites = c("hearts","spades","diamonds","diamonds","spades")
drawn_suites
is.vector(drawn_suites)
# remaining cards 11 spades,12 hearts, 11 diamonds, 13 clubs
#remain <- c(11,12,11,13)
#suits <- c("spades","hearts","diamonds","clubs")
#names(remain) <- suits
#combining line 5,6,7 using named vector
remain <- c(spades=11,hearts=12,diamonds=11,clubs=13)
remain
str(remain)
#single value = vector
my_apples<-5
my_oranges<-"six"
is.vector(my_apples)
is.vector(my_oranges)
length(my_apples)
length(my_oranges)
length(drawn_suites)

#vector coercion
drawn_ranks <- c(7,4,"A",10,"K",3,2,"Q")
drawn_ranks
class(drawn_ranks)

# Different ways to name and create vectors
poker_vector1 <- c(140, -50, 20, -120, 240)
names(poker_vector1) <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
poker_vector1

poker_vector2 <- c(Monday = 140, -50, 20, -120, 240)

roulette_vector1 <- c(-24, -50, 100, -350, 10)

days_vector <- names(poker_vector1)
days_vector
names(roulette_vector1) <- days_vector

roulette_vector2 <- c(-24, -50, 100, -350, 10)
names(roulette_vector2) <- "Monday"
roulette_vector2