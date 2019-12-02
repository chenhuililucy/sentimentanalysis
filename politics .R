rm(list = ls())

install.packages("neuralnet")
library(neuralnet)

response = rev(read.csv("~/R/excel/politics.csv",header = TRUE)$Incum.vic)
pred1 = rev(read.csv("~/R/excel/politics.csv",header = TRUE)$house) # worst
pred2 = rev(read.csv("~/R/excel/politics.csv",header = TRUE)$Incum.Pres)
pred3 = rev(read.csv("~/R/excel/politics.csv",header = TRUE)$GDP.election.year)
pred4 = rev(read.csv("~/R/excel/politics.csv",header = TRUE)$Inflation.elec.year) # best


len = length(pred1)


trainLen = length(pred1) - floor(0.6*(length(pred1)))

responsetr = response[(length(pred1) - trainLen):length(pred1)]
pred1tr = pred1[(length(pred1) - trainLen):length(pred1)]
pred2tr = pred2[(length(pred1) - trainLen):length(pred1)]
pred3tr = pred3[(length(pred1) - trainLen):length(pred1)]
pred4tr = pred4[(length(pred1) - trainLen):length(pred1)]

traindata = as.data.frame(cbind(pred1tr, pred2tr, pred3tr, pred4tr, responsetr))

smart = neuralnet(formula = responsetr ~ pred1tr + pred2tr + pred3tr + pred4tr,
                  data = traindata,
                  hidden = c(10,2),
                  stepmax = 10^5,
                  threshold = 0.001,
                  lifesign = "full",
                  lifesign.step = 10)
plot(smart)

testlen = length(pred1) - trainLen

responsets = response[(length(pred1) + 1 - testlen):length(pred1)]
pred1ts = pred1[(length(pred1) + 1 - testlen):length(pred1)]
pred2ts = pred2[(length(pred1) + 1 - testlen):length(pred1)]
pred3ts = pred3[(length(pred1) + 1 - testlen):length(pred1)]
pred4ts = pred4[(length(pred1) + 1 - testlen):length(pred1)]

testdata = as.data.frame(cbind(pred1ts, pred2ts, pred3ts, pred3ts, responsets))

predictedresponse = compute(smart,testdata[c("pred1ts","pred2ts","pred3ts","pred3ts")])
predictedresponse = predictedresponse[["net.result"]]

predictedresponse = ifelse(predictedresponse >= 0.5,1,0)

l = length(predictedresponse)
test = seq(1, l,by = 1)
for(ii in 1:length(predictedresponse)){
  if(predictedresponse[ii] == responsets[ii]){
    test[ii] = 1
  }
  else{
    test[ii] = 0
  }
}

mean(test)

trump = matrix(c(0.55,1,3,2),nrow = 1)


