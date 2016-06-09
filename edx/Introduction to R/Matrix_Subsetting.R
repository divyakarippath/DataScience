m <- matrix(1:12,nrow=3)
m
m[1,3]
m[3,2]

m[3,]
m[,3]

m[4]

m[2,c(2,3)]
m[c(1,2),c(2,3)]
m[c(1,3),c(1,3,4)]

rownames(m) <- c("r1","r2","r3")
colnames(m) <- c("c1","c2","c3","c4")
m["r2","c3"]
m[2,"c3"]
m["r2",3]
m[3,c("c3","c4")]

m[c(FALSE,FALSE,TRUE),c(FALSE,FALSE,TRUE,TRUE)]