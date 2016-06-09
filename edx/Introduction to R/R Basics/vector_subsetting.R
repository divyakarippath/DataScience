#subsetting using index
remain <- c(spades=11,hearts=12,diamonds=11,clubs=13)
remain[1]
remain[3]

#subsetting using name
remain["spades"]
remain["diamonds"]

#subsetting multiple elements
remain_black <- remain[c(1,4)]
remain_black
remain[c(4,1)]
remain[c("clubs","spades")]

#subset all but some
remain[-1]
remain[-c(1,2)]

#remain[-"spades"] #this will throw error

#subsetting using logical vector

remain[c(FALSE,TRUE,FALSE,TRUE)]

selection_vector <- c(FALSE,TRUE,FALSE,TRUE)
remain[selection_vector]

#shorter logical vectors
remain[c(TRUE,FALSE)] #recycle to TRUE,FALSE,TRUE,FALSE

remain[c(TRUE,FALSE,TRUE)] #recycle to TRUE,FALSE,TRUE,TRUE
