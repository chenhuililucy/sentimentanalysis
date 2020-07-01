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
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$roat.3))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$ROAl3))),]


#`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$roat.5))),]

`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$posint))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$posext))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$negint))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$negext))),]

`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$posint1))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$posext1))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$negint1))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$negext1))),]

`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$posint2))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$posext2))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$negint2))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$negext2))),]

`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$posint3))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$posext3))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$negint3))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$negext3))),]

`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$posint4))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$posext4))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$negint4))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$negext4))),]

`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$posint5))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$posext5))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$negint5))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$negext5))),]


`regposnegvector(11)`$posint=as.double(`regposnegvector(11)`$posint)*100+as.double(`regposnegvector(11)`$posint1)*100+as.double(`regposnegvector(11)`$posint2)*100+as.double(`regposnegvector(11)`$posint3)*100+as.double(`regposnegvector(11)`$posint4)*100+as.double(`regposnegvector(11)`$posint5)*100
`regposnegvector(11)`$posext=as.double(`regposnegvector(11)`$posext)*100+as.double(`regposnegvector(11)`$posext1)*100+as.double(`regposnegvector(11)`$posext2)*100+as.double(`regposnegvector(11)`$posext3)*100+as.double(`regposnegvector(11)`$posext4)*100+as.double(`regposnegvector(11)`$posext5)*100
`regposnegvector(11)`$negint=as.double(`regposnegvector(11)`$negint)*100+as.double(`regposnegvector(11)`$negint1)*100+as.double(`regposnegvector(11)`$negint2)*100+as.double(`regposnegvector(11)`$negint3)*100+as.double(`regposnegvector(11)`$negint4)*100+as.double(`regposnegvector(11)`$negint5)*100
`regposnegvector(11)`$negext=as.double(`regposnegvector(11)`$negext)*100+as.double(`regposnegvector(11)`$negext1)*100+as.double(`regposnegvector(11)`$negext2)*100+as.double(`regposnegvector(11)`$negext3)*100+as.double(`regposnegvector(11)`$negext4)*100+as.double(`regposnegvector(11)`$negext5)*100

`regposnegvector(11)`$posintfin=as.double(`regposnegvector(11)`$posint)*100+as.double(`regposnegvector(11)`$posint1)*100+as.double(`regposnegvector(11)`$posint2)*100+as.double(`regposnegvector(11)`$posint3)*100+as.double(`regposnegvector(11)`$posint4)*100
`regposnegvector(11)`$posextfin=as.double(`regposnegvector(11)`$posext)*100+as.double(`regposnegvector(11)`$posext1)*100+as.double(`regposnegvector(11)`$posext2)*100+as.double(`regposnegvector(11)`$posext3)*100+as.double(`regposnegvector(11)`$posext4)*100
`regposnegvector(11)`$negintfin=as.double(`regposnegvector(11)`$negint)*100+as.double(`regposnegvector(11)`$negint1)*100+as.double(`regposnegvector(11)`$negint2)*100+as.double(`regposnegvector(11)`$negint3)*100+as.double(`regposnegvector(11)`$negint4)*100
`regposnegvector(11)`$negextfin=as.double(`regposnegvector(11)`$negext)*100+as.double(`regposnegvector(11)`$negext1)*100+as.double(`regposnegvector(11)`$negext2)*100+as.double(`regposnegvector(11)`$negext3)*100+as.double(`regposnegvector(11)`$negext4)*100


`regposnegvector(11)`$roac1=(as.double(`regposnegvector(11)`$roat.4)-as.double(`regposnegvector(11)`$roa))

`regposnegvector(11)`$roac=(as.double(`regposnegvector(11)`$roa)-as.double(`regposnegvector(11)`$ROAl4))


`regposnegvector(11)`$posintfin=as.double(`regposnegvector(11)`$posint)*100+as.double(`regposnegvector(11)`$posint1)*100+as.double(`regposnegvector(11)`$posint2)*100+as.double(`regposnegvector(11)`$posint3)*100
`regposnegvector(11)`$posextfin=as.double(`regposnegvector(11)`$posext)*100+as.double(`regposnegvector(11)`$posext1)*100+as.double(`regposnegvector(11)`$posext2)*100+as.double(`regposnegvector(11)`$posext3)*100
`regposnegvector(11)`$negintfin=as.double(`regposnegvector(11)`$negint)*100+as.double(`regposnegvector(11)`$negint1)*100+as.double(`regposnegvector(11)`$negint2)*100+as.double(`regposnegvector(11)`$negint3)*100
`regposnegvector(11)`$negextfin=as.double(`regposnegvector(11)`$negext)*100+as.double(`regposnegvector(11)`$negext1)*100+as.double(`regposnegvector(11)`$negext2)*100+as.double(`regposnegvector(11)`$negext3)*100

`regposnegvector(11)`$roac1=(as.double(`regposnegvector(11)`$roat.3)-as.double(`regposnegvector(11)`$roa))

`regposnegvector(11)`$roac=(as.double(`regposnegvector(11)`$roa)-as.double(`regposnegvector(11)`$ROAl3))


`regposnegvector(11)`$posintfin=as.double(`regposnegvector(11)`$posint)*100+as.double(`regposnegvector(11)`$posint1)*100+as.double(`regposnegvector(11)`$posint2)*100
`regposnegvector(11)`$posextfin=as.double(`regposnegvector(11)`$posext)*100+as.double(`regposnegvector(11)`$posext1)*100+as.double(`regposnegvector(11)`$posext2)*100
`regposnegvector(11)`$negintfin=as.double(`regposnegvector(11)`$negint)*100+as.double(`regposnegvector(11)`$negint1)*100+as.double(`regposnegvector(11)`$negint2)*100
`regposnegvector(11)`$negextfin=as.double(`regposnegvector(11)`$negext)*100+as.double(`regposnegvector(11)`$negext1)*100+as.double(`regposnegvector(11)`$negext2)*100






`regposnegvector(11)`$roac1=(as.double(`regposnegvector(11)`$roat.2.1)-as.double(`regposnegvector(11)`$roa))

`regposnegvector(11)`$roac=(as.double(`regposnegvector(11)`$roa)-as.double(`regposnegvector(11)`$ROAl2))





"""



"""

# 30 June modifications
# Look in to how to do the chi-squared test
# Less profitable firms tend to discuss external causes 



`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$roat.2))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$roa))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$ROAl1))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$ROAl2))),]


`regposnegvector(11)`$posintfin=as.double(`regposnegvector(11)`$posint1)*100+as.double(`regposnegvector(11)`$posint2)*100
`regposnegvector(11)`$posextfin=as.double(`regposnegvector(11)`$posext1)*100+as.double(`regposnegvector(11)`$posext2)*100
`regposnegvector(11)`$negintfin=as.double(`regposnegvector(11)`$negint1)*100+as.double(`regposnegvector(11)`$negint2)*100
`regposnegvector(11)`$negextfin=as.double(`regposnegvector(11)`$negext1)*100+as.double(`regposnegvector(11)`$negext2)*100

`regposnegvector(11)`$roac1=(as.double(`regposnegvector(11)`$roat.2)-as.double(`regposnegvector(11)`$roa))

`regposnegvector(11)`$roac=(as.double(`regposnegvector(11)`$ROAl1)-as.double(`regposnegvector(11)`$ROAl2))



"""

`regposnegvector(11)`$posint1=as.double(`regposnegvector(11)`$posint1)*100
`regposnegvector(11)`$posext1=as.double(`regposnegvector(11)`$posext1)*100
`regposnegvector(11)`$negint1=as.double(`regposnegvector(11)`$negint1)*100
`regposnegvector(11)`$negext1=as.double(`regposnegvector(11)`$negext1)*100

`regposnegvector(11)`$posint2=as.double(`regposnegvector(11)`$posint2)*100
`regposnegvector(11)`$posext2=as.double(`regposnegvector(11)`$posext2)*100
`regposnegvector(11)`$negint2=as.double(`regposnegvector(11)`$negint2)*100
`regposnegvector(11)`$negext2=as.double(`regposnegvector(11)`$negext2)*100

`regposnegvector(11)`$posint3=as.double(`regposnegvector(11)`$posint3)*100
`regposnegvector(11)`$posext3=as.double(`regposnegvector(11)`$posext3)*100
`regposnegvector(11)`$negint3=as.double(`regposnegvector(11)`$negint3)*100
`regposnegvector(11)`$negext3=as.double(`regposnegvector(11)`$negext3)*100

`regposnegvector(11)`$posint=as.double(`regposnegvector(11)`$posint)*100
`regposnegvector(11)`$posext=as.double(`regposnegvector(11)`$posext)*100
`regposnegvector(11)`$negint=as.double(`regposnegvector(11)`$negint)*100
`regposnegvector(11)`$negext=as.double(`regposnegvector(11)`$negext)*100

"""

`regposnegvector(11)`$int=`regposnegvector(11)`$posint+`regposnegvector(11)`$negint
`regposnegvector(11)`$ext=`regposnegvector(11)`$posext+`regposnegvector(11)`$negext

pos <- `regposnegvector(11)`[ which(roac>0),]
neg <- `regposnegvector(11)`[ which(roac<0),]



reg = lm(as.double(roa) ~ as.double(roat.1)+as.double(posint)+as.double(posext)+as.double(negint)+as.double(negext)+as.double(posint1)+as.double(posext1)+as.double(negint1)+as.double(negext1)+as.double(posint2)+as.double(posext2)+as.double(negint2)+as.double(negext2)+as.double(BOV)+gic+year+as.double(roacp)+as.double(marketval)+as.double(lev), data = neg)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))


reg = lm(as.double(roa) ~ log(length)+as.double(posint)+as.double(posext)+as.double(negint)+as.double(negext)+as.double(BOV)+gic+year+as.double(ROAl1)+as.double(marketval)+as.double(lev), data = neg)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))

#Negative ROA firms tends to attribute negative performance to external reasons and positive performance to internal reasons




`regposnegvector(11)`$roac1=(as.double(`regposnegvector(11)`$roat.1)-as.double(`regposnegvector(11)`$roa))

`regposnegvector(11)`$roac=(as.double(`regposnegvector(11)`$roa)-as.double(`regposnegvector(11)`$ROAl1))
`regposnegvector(11)`$roacp=(as.double(`regposnegvector(11)`$ROAl1)-as.double(`regposnegvector(11)`$ROAl2))


#`regposnegvector(11)`$roa=`regposnegvector(11)`$roa

#positive attribution is consistently high and inconsistent to performance change, there is always attribution bias and doesnt change based on performance 



pos <- `regposnegvector(11)`[ which(roac>0),]
neg <- `regposnegvector(11)`[ which(roac<0),]


reg = lm(as.double(roac) ~ log(length)+as.double(posint)+as.double(posext)+as.double(negint)+as.double(negext)+as.double(BOV)+gic+year+as.double(roacp)+as.double(ROAl1)+as.double(marketval)+as.double(lev), data = pos)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))

reg = lm(as.double(roac) ~ log(length)+as.double(posint)+as.double(posext)+as.double(negint)+as.double(negext)+as.double(BOV)+gic+year+as.double(roacp)+as.double(ROAl1)+as.double(marketval)+as.double(lev), data = neg)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))



reg = lm(as.double(roa) ~ log(length)+as.double(posint)+as.double(posext)+as.double(negint)+as.double(negext)+as.double(BOV)+gic+year+as.double(ROAl1)+as.double(marketval)+as.double(lev), data = pos)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))



reg = lm(as.double(roa) ~ log(length)+as.double(int)+as.double(ext)+as.double(BOV)+gic+year+as.double(ROAl1)+as.double(marketval)+as.double(lev), data = pos)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))


#Positive ROA firms tends to do the same but not as strongly Amendment 27 June: no significant relationship found 


reg = lm(as.double(roa) ~ log(length)+as.double(posint)+as.double(posext)+as.double(negint)+as.double(negext)+as.double(BOV)+gic+year+as.double(ROAl1)+as.double(marketval)+as.double(lev), data = `regposnegvector(11)`)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))



reg = lm(as.double(roac1) ~ as.double(posintfin)+as.double(posextfin)+as.double(negintfin)+as.double(negextfin)+as.double(BOV)+gic+year+as.double(marketval)+as.double(lev)+as.double(roa)+as.double(ROAl1)+as.double(ROAl2)+as.double(ROAl3)+as.double(roac), data = `regposnegvector(11)`)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))




reg = lm(as.double(roac1) ~ as.double(posint)+as.double(posext)+as.double(negint)+as.double(negext)+as.double(BOV)+gic+year+as.double(marketval)+as.double(lev)+as.double(roa)+as.double(ROAl1)+as.double(ROAl2)+as.double(ROAl3)+as.double(roac), data = `regposnegvector(11)`)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))


reg = lm(as.double(roac1) ~ as.double(posint)+as.double(posext)+as.double(negint)+as.double(negext)+as.double(posint1)+as.double(posext1)+as.double(negint1)+as.double(negext1)+as.double(posint2)+as.double(posext2)+as.double(negint2)+as.double(BOV)+gic+year+as.double(marketval)+as.double(lev)+as.double(roa)+as.double(ROAl1)+as.double(ROAl2)+as.double(ROAl3)+as.double(roac), data = `regposnegvector(11)`)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))


reg = lm(as.double(roac1) ~ as.double(posint)+as.double(posext)+as.double(negint)+as.double(negext)+as.double(BOV)+gic+year+as.double(marketval)+as.double(lev)+as.double(roa)+as.double(ROAl1)+as.double(ROAl2)+as.double(ROAl3)+as.double(roac), data = `regposnegvector(11)`)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))


reg = lm(as.double(roac1) ~ as.double(posint)+as.double(posext)+as.double(negint)+as.double(negext)+as.double(BOV)+gic+year+as.double(marketval)+as.double(lev)+as.double(roa)+as.double(ROAl1)+as.double(ROAl2)+as.double(ROAl3)+as.double(roac), data = `regposnegvector(11)`)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))




# firms tends to attribute negative performance to external reasons and positive performance to internal reasons
# negative external event may be a short shock, positive external events may be sustained 
# possible reason might be this 

reg = lm(as.double(roac1) ~ as.double(posintfin)+as.double(posextfin)+as.double(negintfin)+as.double(negextfin)+as.double(BOV)+gic+year+as.double(roac)+as.double(marketval)+as.double(lev)+as.double(roa)+as.double(ROAl1)+as.double(ROAl2)+as.double(ROAl3), data = `regposnegvector(11)`)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))



reg = lm(as.double(roac1) ~ as.double(posintfin)+as.double(posextfin)+as.double(negintfin)+as.double(negextfin)+as.double(BOV)+gic+year+as.double(roac)+as.double(marketval)+as.double(lev)+as.double(roa)+as.double(ROAl1)+as.double(ROAl2)+as.double(ROAl3), data = `regposnegvector(11)`)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))


#updated

reg = lm(as.double(roac1) ~ as.double(posintfin)+as.double(posextfin)+as.double(negintfin)+as.double(negextfin)+as.double(BOV)+gic+year+as.double(roac)+as.double(marketval)+as.double(lev)+as.double(ROAl1)+as.double(ROAl2), data = `regposnegvector(11)`)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`regposnegvector(11)`))
