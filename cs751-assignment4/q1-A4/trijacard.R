dp1 <- read.table('bijackardExtraSorted.txt', header=FALSE)
cumulative_distribution <- dp1[,1]
title <- "trigram Data Change Cumulative Distribution Frequency"
xlab <- "Jaccard Distance"
ylab <- "Probability"
P1 = ecdf(cumulative_distribution)
plot(P1, main=title, xlab=xlab, ylab=ylab,col="red", )