counts <- c(1, 6.8, 12.7, 23.4)
png("warcsizeComparision5.png")
barplot(counts, main="size comparision", xlab="(warc tools )",ylab="size in MB",
        names.arg=c("wget", "webrecorder.io", "warcreate","wail"))
