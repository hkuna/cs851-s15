library(RColorBrewer)
data <- read.table("unijackardsorted.txt")
finalDt = rep(data[,1])
title <- "Cumulative Distribution Function"
xlab <- "Uni Jaccard Distance"
ylab <- "Probability"
png("unigram.png")
par(mar=c(4,4,2.5,2) + 0.1)
set.seed(1)
mp <- plot(finalDt, 1:length(finalDt), type="l", col="red", main=title, xlab=xlab, ylab=ylab, yaxt="n")
axis(side=2, at=seq(1,5000,length.out=5), labels=seq(0.2,1,by=0.2))
