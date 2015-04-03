htmlF <- read.table('top50frequencyhtml.txt', header=T)
htmlData <- rep(htmlF[,1])

textF<- read.table('top50frequencytext.txt', header=T)
textData <- rep(textF[,1])
xlimit <- c(0,50)
ylimit <- c(150,4000)

plot(textData, type='l', col='red',xlim=xlimit,ylim=ylimit, xlab='Word Rank', ylab='Word Frequency', main='Words Distribution  after boilerplate' )

