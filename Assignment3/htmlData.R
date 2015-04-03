htmlF <- read.table('top50frequencyhtml.txt', header=T)
htmlData <- rep(htmlF[,1])

textF<- read.table('top50frequencytext.txt', header=T)
textData <- rep(textF[,1])
xlimit <- c(0,50)
ylimit <- c(4000,120000)

plot(htmlData, type='l', col='blue',xlim=xlimit,ylim=ylimit, xlab='Word Rank', ylab='Word Frequency', main='Words Distribution before boilerplate ')
