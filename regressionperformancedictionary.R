library(readr)
#install.packages("estimatr")
#install.packages("margins")
#install.packages("car")
library(estimatr)
library(margins)
library(car)
#install.packages("statar")
library(statar)
#install.packages("perry")
library(perry)
#install.packages("robustbase")
library(robustbase)
#install.packages("DescTools")
library(DescTools)
#install.packages("robustHD")
library(robustHD)
#summary(regression1)
#install.packages("plyr")
#install.packages("ggplot2")
#install.packages("lmtest")
library(plyr)
library(ggplot2)
library(lmtest)
library(sandwich)
#install.packages("plm")
library(plm)
#install.packages("sandwich")
library(sandwich)


#In the most desired regression model, we would ideally like to fomulate as the following: 

#1. Change in ROA= beta1*book to market ratio+beta2*market cap+beta3*industry dummy+beta4*percwrds+beta5*change in ROA in the previous period
#2. Change in ROA= beta1*book to market ratio+beta2*market cap+beta3*industry dummy+beta4*posl+beta5*negl+beta6*negneg+beta7*change in ROA in the previous period

#However, market cap (MKVALT) has too many missing values and this significantly restricts the sample so I removed it. 

################################################################################################


#Preparation

#dat <- `vectorfinal(7)`[!is.na(as.numeric(as.character(`vectorfinal(7)`$roa))),]

`vectorfinal(7)`<-`vectorfinal(7)`[!is.na(as.numeric(as.character(`vectorfinal(7)`$roa))),]
`vectorfinal(7)` <- `vectorfinal(7)`[!is.na(as.numeric(as.character(`vectorfinal(7)`$roat.1))),]
`vectorfinal(7)` <- `vectorfinal(7)`[!is.na(as.numeric(as.character(`vectorfinal(7)`$roat.1.1))),]
#`vectorfinal(7)` <- `vectorfinal(7)`[!is.na(as.numeric(as.character(`vectorfinal(7)`$csho))),]
`vectorfinal(7)` <- `vectorfinal(7)`[!is.na(as.numeric(as.character(`vectorfinal(7)`$roat.2))),]
#`vectorfinal(7)` <- `vectorfinal(7)`[!is.na(as.numeric(as.character(`vectorfinal(7)`$shareturnover))),]


#dat1 <- transform( `vectorfinal(7)`[grep("^\\d+$",  `vectorfinal(7)`$roa),,drop=T], roa= as.numeric(as.character(roa)))
#dat1 <- transform( `vectorfinal(7)`[grep("^\\d+$",  `vectorfinal(7)`$roat.1),,drop=T], roat.1= as.numeric(as.character(roat.1)))
#dat1 <- transform( `vectorfinal(7)`[grep("^\\d+$",  `vectorfinal(7)`$roat.1.1),,drop=T], roat.1.1= as.numeric(as.character(roat.1.1)))

#`vectorfinal(7)`$BOV=as.double(`vectorfinal(7)`$prcc)*as.double(`vectorfinal(7)`$csho) / as.double(`vectorfinal(7)`$ceq)
`vectorfinal(7)`$posl=as.double(`vectorfinal(7)`$posl)*100
`vectorfinal(7)`$negl=as.double(`vectorfinal(7)`$negl)*100
`vectorfinal(7)`$negneg=as.double(`vectorfinal(7)`$negneg)*100

`vectorfinal(7)`$gic=as.character(`vectorfinal(7)`$gic)
`vectorfinal(7)`$year=as.character(`vectorfinal(7)`$year)
#`vectorfinal(7)`$percwrds=(as.double(`vectorfinal(7)`$posl)+as.double(`vectorfinal(7)`$negneg))/ as.double(`vectorfinal(7)`$negl)
#`vectorfinal(7)`$percwrds=as.double(`vectorfinal(7)`$percwrds)


#Option 1: Use change in roa as a percentage

`vectorfinal(7)`$roac=(as.numeric(`vectorfinal(7)`$roa)-as.numeric(`vectorfinal(7)`$roat.1)) /as.numeric(`vectorfinal(7)`$roat.1)*100 # year (t)- year (t-1) ROA 
`vectorfinal(7)`$roac1=(as.numeric(`vectorfinal(7)`$roat.1.1)-as.numeric(`vectorfinal(7)`$roa))/as.numeric(`vectorfinal(7)`$roat.1.1)*100 # year (t+1) - year (t) ROA
`vectorfinal(7)`$roacp=(as.numeric(`vectorfinal(7)`$roat.1)-as.numeric(`vectorfinal(7)`$roat.2))/as.numeric(`vectorfinal(7)`$roat.2)*100 # year (t-1) - year (t-2) ROA


#Option 2: Use change in roa

`vectorfinal(7)`$roac=(as.numeric(`vectorfinal(7)`$roa)-as.numeric(`vectorfinal(7)`$roat.1))*100  # year (t)- year (t-1) ROA 
`vectorfinal(7)`$roac1=(as.numeric(`vectorfinal(7)`$roat.1.1)-as.numeric(`vectorfinal(7)`$roa))*100 # year (t+1) - year (t) ROA
`vectorfinal(7)`$roacp=(as.numeric(`vectorfinal(7)`$roat.1)-as.numeric(`vectorfinal(7)`$roat.2))*100 # year (t-1) - year (t-2) ROA


##############################################################################################################################
#`vectorfinal(7)`=subset(`vectorfinal(7)`,`vectorfinal(7)`$roac<0.56)
#`vectorfinal(7)`=subset(`vectorfinal(7)`,`vectorfinal(7)`$roacp<0.56)
#`vectorfinal(7)`=subset(`vectorfinal(7)`,`vectorfinal(7)`$roac1<0.56)
#`vectorfinal(7)`$roacp<-lapply(`vectorfinal(7)`$roacp, Winsorize)
#summary(roac)
#winsorize(roac, probs = c(0.01, 0.99),data=`vectorfinal(7)`)

#winsorize(roac, minval = NULL, maxval = NULL, probs = c(0.01, 0.99),
          #na.rm = FALSE, type = 7,data=`vectorfinal(7)`)

#results <- fastDummies::dummy_cols(fastDummies_example, select_columns = "cik")

#####################################################################################################################


# First, akin to LM, our data indeed suggests that a high positive:negative performance words percentage in disclosure is correlated with higher future performance (significant at 5 percent level)
# Using the ratio of positive to negative performance (percwrds)  

#initial regression 
reg = lm_robust(as.double(roac) ~ as.double(percwrds)+log(as.double(BOV))+gic+year+log(as.double(shareturnover))+as.double(roacp), data = subset(`vectorfinal(7)`))
summary(reg)

reg = lm(as.double(roac) ~ as.double(percwrds)+log(as.double(BOV))+gic+year+log(as.double(shareturnover))+as.double(roacp), data = subset(`vectorfinal(7)`))
summary(reg)

#Clustered error by gic sector 

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`vectorfinal(7)`))


# 


# amended regression on date 27 June



reg = lm_robust(as.double(roac) ~ as.double(percwrds)+as.double(BOV)+gic+year+as.double(roacp)+as.double(roat.1)+as.double(marketval)+log(length)+as.double(lev), data = subset(`vectorfinal(7)`))
summary(reg)

reg = lm(as.double(roac) ~ as.double(percwrds)+as.double(BOV)+gic+year+as.double(roacp)+as.double(roat.1)+log(as.double(marketval))+log(length)+lev, data = subset(`vectorfinal(7)`))
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`vectorfinal(7)`))


# Added new regression on date 27 June

reg = lm_robust(as.double(roac) ~ as.double(posl)+ as.double(negl)+ as.double(negneg)+as.double(BOV)+gic+year+as.double(roacp)+as.double(roat.1)+as.double(marketval)+log(length), data = `vectorfinal(7)`)
summary(reg)



#However, based on our performance dictionary, we make additional observation that whilst it is indeed true that the disclosure of negative performance is
# correlated with negative performance. To study if companies disclose positive performance as it is, we divided positive performance into 
# negneg, whereby company discloses that it is trying to counteract negative performance (eg. reduce costs, reduce liabilities) and posl, whereby company simply tries 
# discusses positive performance (eg. increase in revenue). It is observed that company's description to counteract negative performance is correlated with performance improvement
# whereby the disclosure of existing positive performance is negatively correlated with performance improvement


# initial regression 


reg = lm(as.double(roac1) ~ as.double(posl)+ as.double(negl)+ as.double(negneg)+log(as.double(BOV))+gic+year++as.double(roac)+log(length), data = `vectorfinal(7)`)
summary(reg)

summary(reg)


# amended regression on date 27 June

reg = lm(as.double(roac1) ~ as.double(posl)+ as.double(negl)+ as.double(negneg)+(as.double(BOV))+gic+year+as.double(roac)+as.double(roa)+log(length)+as.double(marketval), data = `vectorfinal(7)`)
summary(reg)

coeftest(reg, vcov=vcovHC(reg, type = 'HC0', cluster = 'gic'), data = subset(`vectorfinal(7)`))
