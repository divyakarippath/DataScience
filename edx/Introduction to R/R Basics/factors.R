blood <- c("B","AB","O","A","O","O","A","B")
blood_factor <- factor(blood)
blood_factor
str(blood_factor)

blood_factor2 <- factor(blood,levels=c("O","A","B","AB"))
str(blood_factor2)

levels(blood_factor) <- c("BT_A","BT_AB","BT_B","BT-O")
blood_factor

blood_factor3 <- factor(blood,levels=c("O","A","B","AB"), labels=c("BT_O","BT_A","BT_B","BT_AB"))
blood_factor3

tshirts <- c("M","L","S","S","L","M","L","M")
tshirts_factor <- factor(tshirts,ordered = TRUE, levels = c("S","M","L"))
tshirts_factor
length(tshirts_factor)
tshirts_factor[8]
tshirts_factor[1]<tshirts_factor[2]