library(RColorBrewer)

myData <- read.table('link18data.txt', sep=" ",colClasses=c("POSIXct", "numeric"))

title <- "Jaccard Distance Relative to First Memento through Time"
xlab <- "Date"
ylab <- "Jaccard Distance"

png('link18.png')
par(mar=c(4,4,2.5,2) + 0.1)
set.seed(1)

mp <- plot(myData, type="o", col='red', main=title, xlab=xlab, ylab=ylab, xaxt="n", ylim=c(0,1))

axis.POSIXct(side=1, myData$V1, format="%Y-%m-%d")
