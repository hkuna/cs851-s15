dp1 <- read.table('bijackardsorted.txt', header=FALSE)
cumulative_distribution <- dp1[,1]
title <- "Bigram Data Change Cumulative Distribution Frequency"
xlab <- "Jaccard Distance"
ylab <- "Probability"
P1 = ecdf(cumulative_distribution)
plot(P1, main=title, xlab=xlab, ylab=ylab,col="red", )
