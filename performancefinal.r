library(readr)
library(estimatr)
library(margins)
library(car)
library(statar)
library(perry)
library(robustbase)
library(DescTools)
library(robustHD)
library(plyr)
library(ggplot2)
library(lmtest)
library(sandwich)
library(plm)
library(sandwich)


`vectorfinal(7)`<-`vectorfinal(7)`[!is.na(as.numeric(as.character(`vectorfinal(7)`$roa))),]
`vectorfinal(7)` <- `vectorfinal(7)`[!is.na(as.numeric(as.character(`vectorfinal(7)`$roat.1))),]
`vectorfinal(7)` <- `vectorfinal(7)`[!is.na(as.numeric(as.character(`vectorfinal(7)`$roat.1.1))),]
`vectorfinal(7)` <- `vectorfinal(7)`[!is.na(as.numeric(as.character(`vectorfinal(7)`$roat.2))),]

`vectorfinal(7)`$posl=as.double(`vectorfinal(7)`$poscount)/as.double(`vectorfinal(7)`$sentences) #Our metric
`vectorfinal(7)`$negl=as.double(`vectorfinal(7)`$negcount)/as.double(`vectorfinal(7)`$sentences) #Our metric
`vectorfinal(7)`$poslm=as.double(`vectorfinal(7)`$lmpositive)/as.double(`vectorfinal(7)`$l) #LM metric
`vectorfinal(7)`$neglm=as.double(`vectorfinal(7)`$lmnegative)/as.double(`vectorfinal(7)`$l) #LM metric

#creating sector dummy and year dummy
`vectorfinal(7)`$gic=as.character(`vectorfinal(7)`$gic)
`vectorfinal(7)`$year=as.character(`vectorfinal(7)`$year)

#creating ROA lags
`vectorfinal(7)`$roac=(as.numeric(`vectorfinal(7)`$roa)-as.numeric(`vectorfinal(7)`$roat.1)) /as.numeric(`vectorfinal(7)`$roat.1)*100 # year (t)- year (t-1) ROA 
`vectorfinal(7)`$roac1=(as.numeric(`vectorfinal(7)`$roat.1.1)-as.numeric(`vectorfinal(7)`$roa))/as.numeric(`vectorfinal(7)`$roat.1.1)*100 # year (t+1) - year (t) ROA
`vectorfinal(7)`$roacp=(as.numeric(`vectorfinal(7)`$roat.1)-as.numeric(`vectorfinal(7)`$roat.2))/as.numeric(`vectorfinal(7)`$roat.2)*100 # year (t-1) - year (t-2) ROA





#abnormal return (current)##############################################################################################################################

#Only LM
reg = lm(buy_and_hold_abnormal_return~ as.double(poslm)+as.double(neglm)+as.double(BOV)+gic+year+log(l)+log(as.double(marketval))+as.double(lev)+log(numseg)+as.double(roa)+as.double(roacp), data = `vectorfinal(7)`)
summary(reg)
coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`vectorfinal(7)`))

#Only ours
reg = lm(buy_and_hold_abnormal_return~ as.double(posl)+as.double(negl)+as.double(BOV)+gic+year+log(l)+log(as.double(marketval))+as.double(lev)+log(numseg)+as.double(roa)+as.double(roacp), data = `vectorfinal(7)`)
summary(reg)
coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`vectorfinal(7)`))

#Both
reg = lm(buy_and_hold_abnormal_return~ as.double(posl)+as.double(negl)+as.double(poslm)+as.double(neglm)+as.double(BOV)+gic+year+log(l)+log(as.double(marketval))+as.double(lev)+log(numseg)+as.double(roa)+as.double(roacp), data = `vectorfinal(7)`)
summary(reg)
coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`vectorfinal(7)`))



#fama french return (current)#####################################################################################################################################

#Only LM
reg = lm(car_12_ff~ as.double(poslm)+as.double(neglm)+as.double(BOV)+gic+year+log(l)+log(as.double(marketval))+as.double(lev)+log(numseg)+as.double(roa)+as.double(roacp), data = `vectorfinal(7)`)
summary(reg)
coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`vectorfinal(7)`))

#Only ours
reg = lm(car_12_ff~ as.double(posl)+as.double(negl)+as.double(BOV)+gic+year+log(l)+log(as.double(marketval))+as.double(lev)+log(numseg)+as.double(roa)+as.double(roacp), data = `vectorfinal(7)`)
summary(reg)
coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`vectorfinal(7)`))

#Both
reg = lm(car_12_ff~ as.double(posl)+as.double(negl)+as.double(poslm)+as.double(neglm)+as.double(BOV)+gic+year+log(l)+log(as.double(marketval))+as.double(lev)+log(numseg)+as.double(roa)+as.double(roacp), data = `vectorfinal(7)`)
summary(reg)
coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`vectorfinal(7)`))



#volatility (current) #####################################################################################################################################
reg = lm(rmse250~ as.double(posl)+as.double(negl)+as.double(poslm)+as.double(neglm)+as.double(BOV)+gic+year+log(l)+log(as.double(marketval))+as.double(lev)+log(numseg)+as.double(roa)+as.double(roacp), data = `vectorfinal(7)`)
summary(reg)
coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`vectorfinal(7)`))



#future change in ROA #####################################################################################################################################
reg = lm(as.double(roac1) ~as.double(posl)+as.double(negl)+as.double(poslm)+as.double(neglm)+as.double(BOV)+gic+year+log(l)+log(as.double(marketval))+as.double(lev)+log(numseg)+as.double(roa)+as.double(roacp), data = `vectorfinal(7)`)
summary(reg)
coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`vectorfinal(7)`))


#contemporaneous change in ROA ##############################################################################################################################

reg = lm(as.double(roac) ~  as.double(posl)+as.double(negl)+as.double(poslm)+as.double(neglm)+as.double(BOV)+gic+year+log(l)+log(as.double(marketval))+as.double(lev)+log(numseg)+as.double(roat.1), data = `vectorfinal(7)`)
summary(reg)
coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`vectorfinal(7)`))



