#========================================================================
# End
#========================================================================

## Setup 
rm(list=ls())
#install.packages(c("readxl", "zoo", "lmtest", 
#                   "sandwich", "dynlm", "fUnitRoots"))
library(readxl)
library(zoo)
library(lmtest)
library(sandwich)
library(dynlm)
library(fUnitRoots)
library(car)
setwd("~/Dropbox/Teaching/Oxford/Department/QE/2019/computer class/Rclass")
dataSW = read_excel("StockWatsonUSA.xlsx")
View(dataSW)


## Clean data set
dataSW = dataSW[,c("GDPDEF", "UNRATE", "FEDFUNDS")]
revalue = dataSW$FEDFUNDS == "#N/A"
dataSW$FEDFUNDS[revalue] = NA
dataSW = apply(dataSW, 2, as.double)


## Create zoo object and variables
dataSW = zooreg(data = dataSW, start = as.yearqtr("1948-1"), 
                frequency = 4)
dataSW$INF = 400*diff(log(dataSW$GDPDEF), 1)
dataSW$DINF = diff(dataSW$INF, 1)


## Plot variables
dev.off()
par(mfrow=c(2,2), mar = c(5,3,1,1), yaxs="r", xaxs="i")
plot(dataSW[,"INF"], ylab = "", xlab = "INF", main = "")
plot(dataSW[,"DINF"], ylab = "", xlab = "DINF", main = "")
acf(dataSW[,"INF"], na.action = na.pass, 
    ylab = "", xlab = "ACF-INF", main = "")
acf(dataSW[,"DINF"], na.action = na.pass, 
    ylab = "", xlab = "ACF-DINF", main = "")


## Estimate AR(1) model, plot fitted values and residuals
m1 = dynlm(DINF ~ L(DINF), data = window(dataSW, 
                                         start = as.yearqtr("1959-4"), end = as.yearqtr("2016-4")))

dev.off()
par(mfrow=c(2,1), mar = c(5,3,1,1), yaxs="r", xaxs="i")
ts.plot(as.matrix(cbind(dataSW$DINF, fitted.values(m1))), col = c(1,2),
        ylab = "", xlab = "Fitted vs Actual", main = "")
abline(h = 0)
plot(resid(m1), type = "h", ylab = "", xlab = "Residuals", main = "")
abline(h = 0)


## Testing exclusion restrictions
m2 = dynlm(DINF ~ L(DINF) + L(DINF, 2) + L(DINF, 3) + L(DINF,4),
           data = window(dataSW, start = "1959-1", end = "2016-4"))

m3 = dynlm(DINF ~ L(DINF) + L(DINF, 2) + L(DINF, 3) + L(DINF,4)
           + L(UNRATE) + L(UNRATE, 2) + L(UNRATE, 3) + L(UNRATE, 4),
           data = window(dataSW, start = "1959-1", end = "2016-4"))



## ADF tests user written functions - 
# Generate vector of start dates:
dateVec = function(t1s, # Start value of main units - eg years.
                   t2s, # Start value of secondary units; 
                   p,   # Number of lags
                   t2b = 4) { # Secondary unit base; 
  # default is quarters; 12 for months.
  idx = (t2b - t2s):(p + t2b - t2s)
  y = t1s - idx %/% t2b
  q = t2b - idx %% t2b
  return(paste(y, q, sep = "-"))
}

linearHypothesis(m2, c("L(DINF, 2)=0", "L(DINF, 3)=0", "L(DINF, 4)=0"))

# Run ADF tests over different lag lengths, same sample.
adfOut = function(data, # The variable of interest, should be zoo.
                  p,    # Max number of lags.
                  syear, # The vector of start years
                  tidy = 1) { # Output type; 1 for table, otherwise list.
  if(tidy==1) { 
    out = matrix(0, p+1, 5)
    colnames(out) = c("Lags", "ADF stat", "1 - beta", 
                      "p-Value", "AIC")
    for(i in 0:p) {
      dataSS = window(as.zoo(data), 
                      start = syear[i+1], 
                      end = end(data))
      adfOut = adfTest(dataSS, i, type = "c")
      adfCoef = summary(adfOut@test$lm)$coefficients[2,1]
      adfStat = adfOut@test$statistic
      adfPval = adfOut@test$p.value
      adfAIC = AIC(adfOut@test$lm)
      out[i+1, ] = c(i, adfStat, adfCoef, adfPval, adfAIC)
    }
    out[,c(2,3,5)] = round(out[,c(2,3,5)], 4)
    return(out)
  }
  else {
    out = list(0)
    for(i in 0:p) {
      dataSS = window(as.zoo(data), 
                      start = syear[i+1], 
                      end = end(data))
      out[i+1] = adfTest(dataSS, i, type = "c")
      names(out)[i+1] = paste0("adf",i)
    }
  }
  return(out)
}

## Run ADF tests
periods = dateVec(1959, 4, 6)

adfINF = adfOut(dataSW$INF, 6, periods, 1)
adfINF
adfINF[adfINF[,5] == min(adfINF[,5]), ]

adfDINF = adfOut(dataSW$DINF, 6, periods, 1)
adfDINF


## Test for cointegration
dataIR = as.data.frame(read_excel("./InterestRates.xlsx"))
dataIR = zooreg(data = dataIR[,-1], 
                start = as.yearmon("1960-1"), 
                frequency = 12)

periods = dateVec(1961, 12, 18, 12)

# ADF test
adfR90 = adfOut(dataIR$R90, 18, periods, 1)
adfR90
adfR90[adfR90[,5] == min(adfR90[,5]), ]

# ADF test
adfR1yr = adfOut(dataIR$R1yr, 18, periods, 1)
adfR1yr
adfR1yr[adfR1yr[,5] == min(adfR1yr[,5]), ]

# ADF test
adfspread = adfOut(dataIR$spread, 18, periods, 1)
adfspread
adfspread[adfspread[,5] == min(adfspread[,5]), ]

# Regression for EG unit root test
m7 = lm(R1yr ~ R90, window(dataIR, start = as.yearmon("1960-1"), 
                           end = as.yearmon("2017-5")))
summary(m7)

# Get residuals
resids = zooreg(residuals(m7), start = as.yearmon("1960-1"), 
                frequency = 12)


## EG test for cointegration; ADF test on m7 residuals
periods = dateVec(1961, 7, 18, 12)
adfres = adfOut(resids, 18, periods, 1)
adfres
adfres[adfres[,5] == min(adfres[,5]), ]


## Robust standard errors
dataOJ = as.data.frame(read_excel("./ojdata.xlsx"))
dataOJ = dataOJ[,-c(1,2)]
revalue = dataOJ$ChgP == "#N/A"
dataOJ$ChgP[revalue] = NA
revalue = dataOJ$fdd == "#N/A"
dataOJ$fdd[revalue] = NA
dataOJ = apply(dataOJ, 2, as.double)
dataOJ = zooreg(data = dataOJ, start = as.yearmon("1948-1"), 
                frequency = 12)


m8 = lm(ChgP ~ fdd, window(dataOJ, start = as.yearmon("1950-1"),
                           end = as.yearmon("2000-12")))

coeftest(m8, vcov = vcovHC(m8, type = "const")) # SE
coeftest(m8, vcov = vcovHC(m8, type = "HC"))    # HCSE White
coeftest(m8, vcov = vcovHC(m8, type = "HC1"))   # HCSE
coeftest(m8, vcov = NeweyWest(m8))              # HACSE


f1 = paste0("lag(fdd,", 0:6, ")", collapse = " + ")
f = as.formula(paste0("ChgP ~ ", f1))
m9 = dynlm(f,  window(dataOJ, start = as.yearmon("1949-7"),
                      end = as.yearmon("2000-12")))

coeftest(m9)
coeftest(m9, vcov = vcovHC(m9, type = "HC1")) # HCSE
coeftest(m9, vcov = NeweyWest(m9))            # HACSE

#========================================================================
# End
#==================================