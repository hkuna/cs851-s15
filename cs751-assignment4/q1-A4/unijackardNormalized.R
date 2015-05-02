dp1 <- read.table('uniJackardDistance', header=FALSE)
cumulative_distribution <- dp1[,1]
title <- "uniigram Data Change Normalized Cumulative Distribution Frequency"
xlab <- "Normalized Data"
ylab <- "Probability"
X1 = rnorm(cumulative_distribution)
P1 = ecdf(X1)
plot(P1, main=title, xlab=xlab, ylab=ylab,col="red", )