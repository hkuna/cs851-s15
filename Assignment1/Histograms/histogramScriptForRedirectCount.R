agedata=read.csv("redirectCountList.txt",stringsAsFactors=F,header=FALSE,sep="\t")
data=agedata[,1]
png("urlRedirectCount.png")
hist(data,main="Url Redirects Frequency Distribution ",freq=T,xlab="number of redirects",ylab="Frequency",ylim=c(0,5000),xlim=c(1,6))
dev.off()
