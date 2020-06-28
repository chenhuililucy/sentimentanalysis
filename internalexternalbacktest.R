library(readr)
library(estimatr)
library(margins)
library(car)
library(plyr)
library(ggplot2)
library(lmtest)
library(sandwich)
library(plm)


# Data preparation 

`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$roa))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$roat.1))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$roat.1.1))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$roat.1.1))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$roat.5))),]

`regposnegvector(11)`$roac=(as.double(`regposnegvector(11)`$roa)-as.double(`regposnegvector(11)`$roat.1))*100
`regposnegvector(11)`$roac1=(as.double(`regposnegvector(11)`$roat.1.1)-as.double(`regposnegvector(11)`$roa))*100
`regposnegvector(11)`$roacp=(as.double(`regposnegvector(11)`$roat.1)-as.double(`regposnegvector(11)`$roat.2))*100
`regposnegvector(11)`$posint1=as.double(`regposnegvector(11)`$posint)/as.double(`regposnegvector(11)`$sentlist)*100
`regposnegvector(11)`$posext1=as.double(`regposnegvector(11)`$posext)/as.double(`regposnegvector(11)`$sentlist)*100
`regposnegvector(11)`$negint1=as.double(`regposnegvector(11)`$negint)/as.double(`regposnegvector(11)`$sentlist)*100
`regposnegvector(11)`$negext1=as.double(`regposnegvector(11)`$negext)/as.double(`regposnegvector(11)`$sentlist)*100
`regposnegvector(11)`$int=`regposnegvector(11)`$posint1+`regposnegvector(11)`$negint1
`regposnegvector(11)`$ext=`regposnegvector(11)`$posext1+`regposnegvector(11)`$negext1

pos <- `regposnegvector(11)`[ which(roac>0),]
neg <- `regposnegvector(11)`[ which(roac<0),]



reg = lm(as.double(roa) ~ log(sentlist)+as.double(posint1)+as.double(posext1)+as.double(negint1)+as.double(negext1)+as.double(BOV)+gic+year+as.double(roat.1)+as.double(marketval), data = neg)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))


#Negative ROA firms tends to attribute negative performance to external reasons and positive performance to internal reasons


reg = lm(as.double(roa) ~ log(sentlist)+as.double(posint1)+as.double(posext1)+as.double(negint1)+as.double(negext1)+as.double(BOV)+gic+year+as.double(roat.1)+as.double(marketval), data = pos)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))


#Positive ROA firms tends to do the same but not as strongly Amendment 27 June: no significant relationship found 


reg = lm(as.double(roa) ~ log(sentlist)+as.double(posint1)+as.double(posext1)+as.double(negint1)+as.double(negext1)+as.double(BOV)+gic+year+as.double(roat.1)+as.double(marketval), data = `regposnegvector(11)`)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))


# firms tends to attribute negative performance to external reasons and positive performance to internal reasons


