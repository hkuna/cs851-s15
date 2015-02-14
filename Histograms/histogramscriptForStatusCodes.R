agedata=read.csv("statusCodeList.txt",stringsAsFactors=F,header=FALSE,sep="\t")
data=agedata[,1]
png("statusCodeHistogram.png")
hist(data,main="Status Codes Frequency Distribution ",freq=T,xlab="status codes",ylab="Frequency",ylim=c(0,20000),xlim=c(200,500))
dev.off()
