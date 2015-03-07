agedata=read.csv("AgeExtract.txt",stringsAsFactors=F,header=FALSE,sep="\t")
data=agedata[,1]
png("delta--age.png")
hist(data,main="Delta(Age) ",freq=T,xlab="(tweet age - link age)",ylab="Frequency",ylim=c(0,3500),xlim=c(0,6000))
dev.off()
