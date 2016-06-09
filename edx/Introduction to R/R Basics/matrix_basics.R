#default column-wise
matrix(1:6,nrow = 2)
matrix(1:6,ncol = 3)
#Row wise
matrix(1:6,nrow = 2,byrow = TRUE)
#recycling
matrix(1:3,nrow = 2,ncol = 3)
#to show warning message incase multiple of vector does not fit in matrix
matrix(1:4,nrow = 2,ncol = 3)
matrix(1:4,nrow = 2,ncol = 3,byrow = TRUE)
#rbind and cbind
rbind(1:3,1:3)
cbind(1:3,1:3)

m <- matrix(1:6,byrow = TRUE,nrow = 2)
rbind(m,7:9)
cbind(m,7:8)
#naming the matrices
rownames(m) <- c("row1","row2")
m
colnames(m) <- c("col1","col2","col3")
m

#dimnames
n <- matrix(1:6,byrow = TRUE, nrow = 2,dimnames = list(c("row1","row2"),c("col1","col2","col3")))
n

#coercion
num <- matrix(1:8,ncol=2)
char <- matrix(LETTERS[1:6],ncol=3,nrow=4)
cbind(num,char)
