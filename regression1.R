library(readr)
#install.packages("estimatr")
#install.packages("margins")
#install.packages("car")
library(estimatr)
library(margins)
library(car)
summary(regression1)
reg = lm_robust(as.double(spreturns) ~ as.double(posl)+ as.double(negl), data = regression1)
summary(reg)
linearHypothesis(reg, c("as.double(posl)"), test = "F")

reg1 = lm_robust(as.double(negl) ~ as.double(spreturns), data = regression1)
summary(reg1)
linearHypothesis(reg1, c("as.double(spreturns)"), test = "F")

"""
filename         year           cik      
/Users/lucy/Desktop/others/newdictestn/newdic/1000180-2006mda.txt:   1   2012   : 550   832480 :   4  
/Users/lucy/Desktop/others/newdictestn/newdic/1000180-2014mda.txt:   1   2011   : 549   1000228:   3  
/Users/lucy/Desktop/others/newdictestn/newdic/1000209-2009mda.txt:   1   2001   : 545   1000232:   3  
/Users/lucy/Desktop/others/newdictestn/newdic/1000209-2017mda.txt:   1   2009   : 535   1000753:   3  
/Users/lucy/Desktop/others/newdictestn/newdic/1000227-2005mda.txt:   1   1998   : 534   1001082:   3  
/Users/lucy/Desktop/others/newdictestn/newdic/1000228-1997mda.txt:   1   2015   : 521   1001606:   3  
(Other)                                                          :9992   (Other):6764   (Other):9979  
pos               neg             l            spreturns         posl               negl         
Min.   :   0.00   Min.   :   0   Min.   :    28   16     : 550   Min.   :0.000000   Min.   :0.000000  
1st Qu.:  25.00   1st Qu.:  36   1st Qu.:  3208   2.11   : 549   1st Qu.:0.006506   1st Qu.:0.008448  
Median :  57.00   Median :  77   Median :  6430   -11.89 : 545   Median :0.009032   Median :0.011894  
Mean   :  85.59   Mean   : 103   Mean   :  8634   26.46  : 535   Mean   :0.009686   Mean   :0.012624  
3rd Qu.: 112.00   3rd Qu.: 139   3rd Qu.: 10786   28.58  : 534   3rd Qu.:0.011924   3rd Qu.:0.015861  
Max.   :1903.00   Max.   :1839   Max.   :121176   1.38   : 521   Max.   :0.134831   Max.   :0.056471  
(Other):6764                                        
> reg = lm_robust(as.double(spreturns) ~ as.double(posl)+ as.double(negl), data = regression1)
> summary(reg)

Call:
  lm_robust(formula = as.double(spreturns) ~ as.double(posl) + 
              as.double(negl), data = regression1)

Standard error type:  HC2 

Coefficients:
  Estimate Std. Error t value  Pr(>|t|) CI Lower CI Upper   DF
(Intercept)        12.52     0.1652  75.782 0.000e+00    12.19   12.839 9995
as.double(posl)   -30.19    14.5762  -2.071 3.835e-02   -58.77   -1.621 9995
as.double(negl)    49.48    11.6222   4.257 2.086e-05    26.70   72.264 9995

Multiple R-squared:  0.002076 ,	Adjusted R-squared:  0.001876 
F-statistic: 9.094 on 2 and 9995 DF,  p-value: 0.0001133
> linearHypothesis(reg, c("as.double(posl)"), test = "F")
Linear hypothesis test

Hypothesis:
  as.double(posl) = 0

Model 1: restricted model
Model 2: as.double(spreturns) ~ as.double(posl) + as.double(negl)

Res.Df Df      F  Pr(>F)  
1   9996                    
2   9995  1 4.2907 0.03835 *
  ---
  Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
> 
  > reg1 = lm_robust(as.double(negl) ~ as.double(spreturns), data = regression1)
> summary(reg1)

Call:
  lm_robust(formula = as.double(negl) ~ as.double(spreturns), data = regression1)

Standard error type:  HC2 

Coefficients:
  Estimate Std. Error t value  Pr(>|t|)  CI Lower  CI Upper   DF
(Intercept)          1.214e-02  1.370e-04  88.644 0.0000000 1.187e-02 1.241e-02 9996
as.double(spreturns) 3.753e-05  9.843e-06   3.813 0.0001381 1.824e-05 5.682e-05 9996

Multiple R-squared:  0.001509 ,	Adjusted R-squared:  0.001409 
F-statistic: 14.54 on 1 and 9996 DF,  p-value: 0.0001381
# linearHypothesis(reg1, c("as.double(spreturns)"), test = "F")
Linear hypothesis test

Hypothesis:
  as.double(spreturns) = 0

Model 1: restricted model
Model 2: as.double(negl) ~ as.double(spreturns)

Res.Df Df      F    Pr(>F)    
1   9997                        
2   9996  1 14.539 0.0001381 ***
  ---
  Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

"""

