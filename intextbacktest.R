library(readr)
#install.packages("estimatr")
#install.packages("margins")
#install.packages("car")
library(estimatr)
library(margins)
library(car)
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

#dat<-read.csv(`regposnegvector(11)`)

`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$roa))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$roat.1))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$roat.1.1))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$roat.1.1))),]
`regposnegvector(11)` <- `regposnegvector(11)`[!is.na(as.numeric(as.character(`regposnegvector(11)`$csho))),]


"""

d <- transform(`regposnegvector(11)`[grep("^\\d+$",  `regposnegvector(11)`$roa),,drop=T], roa= as.numeric(as.character(roa)))
d <- transform(`regposnegvector(11)`[grep("^\\d+$",  `regposnegvector(11)`$roat.1),,drop=T], roat.1= as.numeric(as.character(roat.1)))
d <- transform( `regposnegvector(11)`[grep("^\\d+$",  `regposnegvector(11)`$roat.1.1),,drop=T], roat.1.1= as.numeric(as.character(roat.1.1)))

"""


`regposnegvector(11)`$BOV=as.double(`regposnegvector(11)`$prcc)*as.double(`regposnegvector(11)`$csho) / as.double(`regposnegvector(11)`$ceq)
`regposnegvector(11)`$gic=as.character(`regposnegvector(11)`$gic)
`regposnegvector(11)`$year=as.character(`regposnegvector(11)`$year)

"""
`regposnegvector(11)`$roac=as.double(`regposnegvector(11)`$roa)-as.double(`regposnegvector(11)`$roat.1)
`regposnegvector(11)`$roac1=as.double(`regposnegvector(11)`$roat.1.1)-as.double(`regposnegvector(11)`$roa)
"""

`regposnegvector(11)`$posint1=as.double(`regposnegvector(11)`$posint)/as.double(`regposnegvector(11)`$sentlist)
`regposnegvector(11)`$posext1=as.double(`regposnegvector(11)`$posext)/as.double(`regposnegvector(11)`$sentlist)
`regposnegvector(11)`$negint1=as.double(`regposnegvector(11)`$negint)/as.double(`regposnegvector(11)`$sentlist)
`regposnegvector(11)`$negext1=as.double(`regposnegvector(11)`$negext)/as.double(`regposnegvector(11)`$sentlist)
`regposnegvector(11)`$int=`regposnegvector(11)`$posint1+`regposnegvector(11)`$negint1
`regposnegvector(11)`$ext=`regposnegvector(11)`$posext1+`regposnegvector(11)`$negext1




#reg = lm_robust(as.double(roac1) ~ as.double(sentlist)+log(length)+log(as.double(BOV))+gic+as.double(roac), data = dat)
#summary(reg)


pos <- `regposnegvector(11)`[ which(roac>0),]
neg <- `regposnegvector(11)`[ which(roac<0),]

summary(pos)

reg = lm_robust(as.double(roac1) ~ sentlist+as.double(posint1)+as.double(posext1)+as.double(negint1)+as.double(negext1)+log(as.double(BOV))+as.double(roac)+gic+year, data = subset(`regposnegvector(11)`))
summary(reg)


reg = lm_robust(as.double(roac1) ~ sentlist+as.double(posint1)+as.double(posext1)+as.double(negint1)+as.double(negext1)+log(as.double(BOV))+as.double(roac)+gic+year, data = subset(`regposnegvector(11)`))
summary(reg)


reg = lm_robust(as.double(roac1) ~ sentlist+as.double(posint1)+as.double(posext1)+as.double(negint1)+as.double(negext1)+log(as.double(BOV))+as.double(roac)+gic+year, data = pos)
summary(reg)

reg = lm_robust(as.double(roac1) ~ sentlist+as.double(posint1)+as.double(posext1)+as.double(negint1)+as.double(negext1)+log(as.double(BOV))+as.double(roac)+gic+year, data = neg)
summary(reg)




"""

Multiple R-squared:  0.1196 ,	Adjusted R-squared:  0.1186 
F-statistic:    NA on 109 and 87695 DF,  p-value: NA
> reg = lm_robust(as.double(roac1) ~ sentlist+as.double(posint1)+as.double(posext1)+as.double(negint1)+as.double(negext1)+log(as.double(BOV))+as.double(roac)+gic, data = `regposnegvector(11)`)
> summary(reg)

Call:
lm_robust(formula = as.double(roac1) ~ sentlist + as.double(posint1) + 
as.double(posext1) + as.double(negint1) + as.double(negext1) + 
log(as.double(BOV)) + as.double(roac) + gic, data = `regposnegvector(11)`)

Standard error type:  HC2 

Coefficients:
Estimate Std. Error  t value  Pr(>|t|)   CI Lower   CI Upper    DF
(Intercept)         -1.828e+03  2.391e+02  -7.6436 2.134e-14 -2.297e+03 -1359.2198 87721
sentlist             7.453e-01  9.960e-02   7.4834 7.311e-14  5.501e-01     0.9405 87721
as.double(posint1)   3.811e+03  2.160e+03   1.7640 7.773e-02 -4.234e+02  8045.7073 87721
as.double(posext1)   1.198e+04  9.809e+03   1.2217 2.218e-01 -7.242e+03 31208.8384 87721
as.double(negint1)   9.709e+01  8.710e+02   0.1115 9.112e-01 -1.610e+03  1804.2414 87721
as.double(negext1)  -3.991e+03  2.994e+03  -1.3329 1.826e-01 -9.860e+03  1877.7976 87721
log(as.double(BOV))  3.572e+01  2.970e+01   1.2026 2.291e-01 -2.250e+01    93.9285 87721
as.double(roac)     -2.885e-01  4.344e-03 -66.4098 0.000e+00 -2.970e-01    -0.2800 87721
gic101010           -3.446e+03  6.684e+02  -5.1551 2.540e-07 -4.756e+03 -2135.7872 87721
gic101020           -3.035e+03  5.410e+02  -5.6106 2.022e-08 -4.096e+03 -1974.9114 87721
gic151010           -2.256e+03  6.411e+02  -3.5187 4.339e-04 -3.513e+03  -999.3398 87721
gic151020           -1.828e+03  1.520e+03  -1.2023 2.292e-01 -4.808e+03  1151.8963 87721
gic151030           -1.397e+03  8.661e+02  -1.6128 1.068e-01 -3.094e+03   300.6992 87721
gic151040           -1.539e+03  6.857e+02  -2.2451 2.477e-02 -2.883e+03  -195.4782 87721
gic151050           -2.023e+03  1.092e+03  -1.8531 6.388e-02 -4.163e+03   116.7465 87721
gic201010           -2.655e+03  7.609e+02  -3.4889 4.852e-04 -4.146e+03 -1163.3078 87721
gic201020           -1.423e+03  7.740e+02  -1.8386 6.598e-02 -2.940e+03    93.9747 87721
gic201030           -2.233e+03  8.375e+02  -2.6669 7.657e-03 -3.875e+03  -592.0145 87721
gic201040           -1.518e+03  7.077e+02  -2.1455 3.192e-02 -2.905e+03  -131.2718 87721
gic201050           -2.912e+03  1.168e+03  -2.4932 1.266e-02 -5.200e+03  -622.6974 87721
gic201060           -2.389e+03  5.856e+02  -4.0793 4.521e-05 -3.536e+03 -1241.0109 87721
gic201070           -2.582e+03  7.583e+02  -3.4047 6.627e-04 -4.068e+03 -1095.4767 87721
gic202010           -2.146e+03  5.941e+02  -3.6115 3.045e-04 -3.310e+03  -981.2179 87721
gic202020           -2.413e+03  6.763e+02  -3.5677 3.603e-04 -3.738e+03 -1087.2849 87721
gic203010           -3.168e+03  9.502e+02  -3.3335 8.580e-04 -5.030e+03 -1305.1655 87721
gic203020           -9.793e+02  1.004e+03  -0.9755 3.293e-01 -2.947e+03   988.3117 87721
gic203030           -2.460e+03  1.024e+03  -2.4012 1.634e-02 -4.467e+03  -451.9206 87721
gic203040           -1.931e+03  6.426e+02  -3.0050 2.656e-03 -3.190e+03  -671.5236 87721
gic203050           -3.869e+03  2.700e+03  -1.4329 1.519e-01 -9.160e+03  1422.9762 87721
gic251010           -1.587e+03  7.954e+02  -1.9957 4.597e-02 -3.146e+03   -28.3906 87721
gic251020           -2.577e+03  1.480e+03  -1.7412 8.165e-02 -5.479e+03   323.8029 87721
gic252010           -2.726e+03  6.442e+02  -4.2310 2.329e-05 -3.988e+03 -1462.9423 87721
gic252020           -1.827e+03  9.048e+02  -2.0188 4.352e-02 -3.600e+03   -53.1712 87721
gic252030           -2.737e+03  6.463e+02  -4.2347 2.291e-05 -4.003e+03 -1470.0530 87721
gic253010           -1.912e+03  5.610e+02  -3.4083 6.541e-04 -3.012e+03  -812.5132 87721
gic253020           -2.216e+03  8.054e+02  -2.7509 5.944e-03 -3.794e+03  -637.0124 87721
gic254010           -2.214e+03  7.428e+02  -2.9814 2.870e-03 -3.670e+03  -758.6511 87721
gic255010           -1.216e+03  9.507e+02  -1.2790 2.009e-01 -3.079e+03   647.4567 87721
gic255020           -2.343e+03  8.123e+02  -2.8844 3.922e-03 -3.935e+03  -750.8830 87721
gic255030           -4.243e+03  9.138e+02  -4.6427 3.443e-06 -6.034e+03 -2451.5588 87721
gic255040           -2.856e+03  5.777e+02  -4.9428 7.714e-07 -3.988e+03 -1723.2977 87721
gic301010           -2.481e+03  8.189e+02  -3.0295 2.451e-03 -4.086e+03  -875.7844 87721
gic302010           -1.824e+03  7.675e+02  -2.3765 1.748e-02 -3.328e+03  -319.6749 87721
gic302020           -2.861e+03  7.289e+02  -3.9245 8.698e-05 -4.289e+03 -1431.9009 87721
gic302030           -5.040e+03  1.426e+03  -3.5358 4.067e-04 -7.834e+03 -2246.3425 87721
gic303010           -1.529e+03  1.540e+03  -0.9924 3.210e-01 -4.548e+03  1490.4952 87721
gic303020           -3.069e+03  8.607e+02  -3.5662 3.623e-04 -4.756e+03 -1382.4484 87721
gic351010           -1.367e+03  5.525e+02  -2.4741 1.336e-02 -2.450e+03  -284.0501 87721
gic351020           -2.557e+03  5.560e+02  -4.5979 4.274e-06 -3.646e+03 -1466.8018 87721
gic351030           -2.242e+03  9.373e+02  -2.3916 1.678e-02 -4.079e+03  -404.5483 87721
gic352010           -1.577e+02  5.023e+02  -0.3139 7.536e-01 -1.142e+03   826.8318 87721
gic352020           -9.832e+02  6.039e+02  -1.6281 1.035e-01 -2.167e+03   200.3964 87721
gic352030           -1.782e+03  7.281e+02  -2.4475 1.439e-02 -3.209e+03  -354.9607 87721
gic401010           -9.376e+02  4.685e+02  -2.0013 4.536e-02 -1.856e+03   -19.3559 87721
gic401020           -1.137e+03  5.299e+02  -2.1464 3.184e-02 -2.176e+03   -98.7934 87721
gic402010           -2.664e+03  9.351e+02  -2.8489 4.389e-03 -4.497e+03  -831.2108 87721
gic402020           -1.513e+03  8.020e+02  -1.8860 5.930e-02 -3.084e+03    59.3709 87721
gic402030           -1.606e+03  5.748e+02  -2.7936 5.213e-03 -2.732e+03  -479.1808 87721
gic402040           -2.101e+03  7.705e+02  -2.7272 6.388e-03 -3.612e+03  -591.1592 87721
gic403010           -1.978e+03  5.283e+02  -3.7435 1.816e-04 -3.013e+03  -942.1845 87721
gic404010           -2.748e+03  8.504e+02  -3.2317 1.231e-03 -4.415e+03 -1081.3874 87721
gic404020           -1.853e+03  6.884e+02  -2.6914 7.118e-03 -3.202e+03  -503.4674 87721
gic404030           -8.130e+02  1.790e+03  -0.4541 6.497e-01 -4.322e+03  2695.7734 87721
gic451010           -8.401e+02  6.839e+02  -1.2284 2.193e-01 -2.180e+03   500.3534 87721
gic451020           -1.948e+03  5.980e+02  -3.2574 1.125e-03 -3.120e+03  -775.8966 87721
gic451030           -1.496e+03  5.567e+02  -2.6870 7.211e-03 -2.587e+03  -404.7034 87721
gic452010           -2.507e+03  6.305e+02  -3.9761 7.010e-05 -3.743e+03 -1271.1752 87721
gic452020           -2.344e+03  7.956e+02  -2.9466 3.214e-03 -3.904e+03  -784.9509 87721
gic452030           -2.179e+03  5.709e+02  -3.8164 1.355e-04 -3.297e+03 -1059.7527 87721
gic452040           -2.134e+04  8.534e+03  -2.5006 1.240e-02 -3.807e+04 -4613.6415 87721
gic452050           -7.111e+03  1.802e+03  -3.9455 7.971e-05 -1.064e+04 -3578.4726 87721
gic453010           -1.175e+03  6.310e+02  -1.8616 6.266e-02 -2.412e+03    62.0781 87721
gic501010           -1.614e+03  7.317e+02  -2.2058 2.740e-02 -3.048e+03  -179.8300 87721
gic501020           -5.725e+02  1.049e+03  -0.5459 5.851e-01 -2.628e+03  1483.0650 87721
gic502010           -5.160e+02  7.604e+02  -0.6786 4.974e-01 -2.006e+03   974.3774 87721
gic502020           -5.263e+02  9.864e+02  -0.5335 5.937e-01 -2.460e+03  1407.0272 87721
gic502030           -3.665e+02  1.265e+03  -0.2897 7.720e-01 -2.846e+03  2113.0694 87721
gic551010           -2.263e+03  5.833e+02  -3.8789 1.050e-04 -3.406e+03 -1119.2797 87721
gic551020           -2.924e+03  7.979e+02  -3.6644 2.481e-04 -4.487e+03 -1359.8676 87721
gic551030           -2.065e+03  6.041e+02  -3.4189 6.291e-04 -3.249e+03  -881.3132 87721
gic551040           -1.643e+03  5.949e+02  -2.7613 5.758e-03 -2.809e+03  -476.7351 87721
gic551050           -1.372e+03  1.231e+03  -1.1146 2.650e-01 -3.785e+03  1040.5678 87721
gic601010           -8.378e+02  5.146e+02  -1.6281 1.035e-01 -1.846e+03   170.8150 87721
gic601020           -1.270e+03  1.007e+03  -1.2612 2.072e-01 -3.243e+03   703.5195 87721

Multiple R-squared:  0.111 ,	Adjusted R-squared:  0.1102 
F-statistic: 62.29 on 83 and 87721 DF,  p-value: < 2.2e-16

"""


reg = lm_robust(as.double(roac1) ~ as.double(int)+as.double(ext)+log(as.double(BOV))+as.double(roac)+gic+year, data = data = subset(`regposnegvector(11)`))
summary(reg)


reg = lm_robust(as.double(roac1) ~ as.double(int)+as.double(ext)+log(as.double(BOV))+as.double(roac)+gic+year, data = neg)
summary(reg)


reg = lm_robust(as.double(roac1) ~ as.double(int)+as.double(ext)+log(as.double(BOV))+as.double(roac)+gic+year, data = pos)
summary(reg)

