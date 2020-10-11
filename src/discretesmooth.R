require("itsmr")

args <- commandArgs(trailingOnly = TRUE)
y <- (read.csv(paste(args[2], "/lpf.csv", sep=""),header=F))[,1]

#y <- smooth.fft(notsmooth, as.numeric(args[2]))
#write.table(y, file = "lowpass-mice-full.csv",row.names = FALSE,col.names = FALSE)
print("low pass done")
y <- y[seq(from = 1, to = length(y), by = 100)]
write.table(y, file = paste(args[2], "/sampled.csv", sep=""),row.names = FALSE,col.names = FALSE)
print("sampling Done")
y <- smooth.rank(y,2)
write.table(y, file = paste(args[2], "/finalsmoothed.csv", sep=""), row.names = FALSE, col.names = FALSE)
print("Rank Filter Done")

print("Input smoothed!")

