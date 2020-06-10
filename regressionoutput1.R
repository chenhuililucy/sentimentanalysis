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

#install.packages("sandwich")

library(sandwich)


#In the most desired regression model, we would ideally like to fomulate as the following: 

#1. Change in ROA= beta1*book to market ratio+beta2*market cap+beta3*industry dummy+beta4*percwrds+beta5*change in ROA in the previous period
#2. Change in ROA= beta1*book to market ratio+beta2*market cap+beta3*industry dummy+beta4*posl+beta5*negl+beta6*negneg+beta7*change in ROA in the previous period

#However, market cap (MKVALT) has too many missing values and this significantly restricts the sample so I removed it. 

################################################################################################


#Preparation

#dat <- `vectorfinal(7)`[!is.na(as.numeric(as.character(`vectorfinal(7)`$roa))),]

dat1 <- transform( `vectorfinal(7)`[grep("^\\d+$",  `vectorfinal(7)`$roa),,drop=T], roa= as.numeric(as.character(roa)))
dat1 <- transform( `vectorfinal(7)`[grep("^\\d+$",  `vectorfinal(7)`$roat.1),,drop=T], roat.1= as.numeric(as.character(roat.1)))
dat1 <- transform( `vectorfinal(7)`[grep("^\\d+$",  `vectorfinal(7)`$roat.1.1),,drop=T], roat.1.1= as.numeric(as.character(roat.1.1)))

`vectorfinal(7)`$BOV=as.double(`vectorfinal(7)`$prcc)*as.double(`vectorfinal(7)`$csho) / as.double(`vectorfinal(7)`$ceq)
`vectorfinal(7)`$gic=as.character(`vectorfinal(7)`$gic)
`vectorfinal(7)`$year=as.character(`vectorfinal(7)`$year)

`vectorfinal(7)`$roac=as.double(`vectorfinal(7)`$roa)-as.double(`vectorfinal(7)`$roat.1)
`vectorfinal(7)`$roac1=as.double(`vectorfinal(7)`$roat.1.1)-as.double(`vectorfinal(7)`$roa)

#results <- fastDummies::dummy_cols(fastDummies_example, select_columns = "cik")

################################################################################################


# First, akin to LM, our data indeed suggests that a high positive:negative performance words percentage in disclosure is correlated with higher future performance (significant at 1 percent level)
# Using the ratio of positive to negative performance (percwrds)  

reg = lm_robust(as.double(roac1) ~ as.double(percwrds)+log(length)+log(as.double(BOV))+gic+as.double(roac), data = subset(`vectorfinal(7)`))
summary(reg)


"""

Call:
lm_robust(formula = as.double(roac1) ~ as.double(percwrds) + 
log(length) + log(as.double(BOV)) + gic + as.double(roac), 
data = subset(`vectorfinal(7)`))

Standard error type:  HC2 

Coefficients:
Estimate Std. Error  t value  Pr(>|t|)   CI Lower   CI Upper    DF
(Intercept)         -3.190e+03  3.322e+02  -9.6032 7.943e-22 -3.841e+03 -2.539e+03 87724
as.double(percwrds)  2.239e-02  6.916e-03   3.2379 1.205e-03  8.838e-03  3.595e-02 87724
log(length)          1.815e+02  2.868e+01   6.3296 2.470e-10  1.253e+02  2.378e+02 87724
log(as.double(BOV))  3.855e+01  2.970e+01   1.2978 1.944e-01 -1.967e+01  9.677e+01 87724
gic101010           -3.520e+03  6.685e+02  -5.2653 1.403e-07 -4.830e+03 -2.209e+03 87724
gic101020           -3.081e+03  5.411e+02  -5.6940 1.245e-08 -4.141e+03 -2.020e+03 87724
gic151010           -2.308e+03  6.413e+02  -3.5992 3.193e-04 -3.565e+03 -1.051e+03 87724
gic151020           -1.845e+03  1.520e+03  -1.2134 2.250e-01 -4.824e+03  1.135e+03 87724
gic151030           -1.480e+03  8.661e+02  -1.7086 8.752e-02 -3.177e+03  2.177e+02 87724
gic151040           -1.578e+03  6.862e+02  -2.2993 2.149e-02 -2.923e+03 -2.329e+02 87724
gic151050           -2.111e+03  1.093e+03  -1.9321 5.335e-02 -4.253e+03  3.051e+01 87724
gic201010           -2.737e+03  7.614e+02  -3.5950 3.245e-04 -4.230e+03 -1.245e+03 87724
gic201020           -1.503e+03  7.740e+02  -1.9416 5.219e-02 -3.020e+03  1.424e+01 87724
gic201030           -2.279e+03  8.380e+02  -2.7198 6.533e-03 -3.922e+03 -6.367e+02 87724
gic201040           -1.603e+03  7.079e+02  -2.2638 2.359e-02 -2.990e+03 -2.151e+02 87724
gic201050           -2.950e+03  1.167e+03  -2.5270 1.151e-02 -5.237e+03 -6.618e+02 87724
gic201060           -2.469e+03  5.857e+02  -4.2145 2.505e-05 -3.617e+03 -1.321e+03 87724
gic201070           -2.677e+03  7.583e+02  -3.5296 4.163e-04 -4.163e+03 -1.190e+03 87724
gic202010           -2.225e+03  5.943e+02  -3.7434 1.816e-04 -3.389e+03 -1.060e+03 87724
gic202020           -2.508e+03  6.766e+02  -3.7070 2.098e-04 -3.835e+03 -1.182e+03 87724
gic203010           -3.237e+03  9.507e+02  -3.4052 6.614e-04 -5.100e+03 -1.374e+03 87724
gic203020           -1.041e+03  1.005e+03  -1.0356 3.004e-01 -3.010e+03  9.289e+02 87724
gic203030           -2.544e+03  1.025e+03  -2.4824 1.305e-02 -4.553e+03 -5.354e+02 87724
gic203040           -1.995e+03  6.429e+02  -3.1030 1.916e-03 -3.255e+03 -7.348e+02 87724
gic203050           -3.900e+03  2.700e+03  -1.4445 1.486e-01 -9.192e+03  1.392e+03 87724
gic251010           -1.658e+03  7.957e+02  -2.0834 3.721e-02 -3.217e+03 -9.822e+01 87724
gic251020           -2.663e+03  1.480e+03  -1.7995 7.194e-02 -5.564e+03  2.375e+02 87724
gic252010           -2.809e+03  6.444e+02  -4.3597 1.304e-05 -4.072e+03 -1.546e+03 87724
gic252020           -1.904e+03  9.048e+02  -2.1041 3.537e-02 -3.677e+03 -1.304e+02 87724
gic252030           -2.830e+03  6.465e+02  -4.3775 1.202e-05 -4.097e+03 -1.563e+03 87724
gic253010           -1.990e+03  5.610e+02  -3.5465 3.905e-04 -3.089e+03 -8.901e+02 87724
gic253020           -2.333e+03  8.056e+02  -2.8960 3.781e-03 -3.912e+03 -7.541e+02 87724
gic254010           -2.296e+03  7.430e+02  -3.0894 2.006e-03 -3.752e+03 -8.392e+02 87724
gic255010           -1.309e+03  9.491e+02  -1.3790 1.679e-01 -3.169e+03  5.514e+02 87724
gic255020           -2.426e+03  8.121e+02  -2.9872 2.816e-03 -4.017e+03 -8.342e+02 87724
gic255030           -4.334e+03  9.147e+02  -4.7380 2.162e-06 -6.127e+03 -2.541e+03 87724
gic255040           -2.936e+03  5.779e+02  -5.0800 3.782e-07 -4.069e+03 -1.803e+03 87724
gic301010           -2.565e+03  8.201e+02  -3.1277 1.762e-03 -4.172e+03 -9.576e+02 87724
gic302010           -1.844e+03  7.677e+02  -2.4019 1.631e-02 -3.349e+03 -3.393e+02 87724
gic302020           -2.942e+03  7.289e+02  -4.0364 5.432e-05 -4.371e+03 -1.514e+03 87724
gic302030           -4.929e+03  1.429e+03  -3.4498 5.613e-04 -7.729e+03 -2.128e+03 87724
gic303010           -1.624e+03  1.540e+03  -1.0546 2.916e-01 -4.643e+03  1.394e+03 87724
gic303020           -3.143e+03  8.608e+02  -3.6508 2.615e-04 -4.830e+03 -1.456e+03 87724
gic351010           -1.452e+03  5.521e+02  -2.6306 8.524e-03 -2.535e+03 -3.703e+02 87724
gic351020           -2.619e+03  5.561e+02  -4.7091 2.492e-06 -3.709e+03 -1.529e+03 87724
gic351030           -2.341e+03  9.371e+02  -2.4984 1.248e-02 -4.178e+03 -5.046e+02 87724
gic352010           -2.508e+02  5.006e+02  -0.5010 6.164e-01 -1.232e+03  7.303e+02 87724
gic352020           -1.055e+03  6.030e+02  -1.7498 8.015e-02 -2.237e+03  1.267e+02 87724
gic352030           -1.876e+03  7.282e+02  -2.5766 9.978e-03 -3.304e+03 -4.491e+02 87724
gic401010           -9.311e+02  4.685e+02  -1.9877 4.685e-02 -1.849e+03 -1.296e+01 87724
gic401020           -1.081e+03  5.303e+02  -2.0386 4.149e-02 -2.120e+03 -4.170e+01 87724
gic402010           -2.708e+03  9.365e+02  -2.8913 3.837e-03 -4.543e+03 -8.722e+02 87724
gic402020           -1.540e+03  8.021e+02  -1.9201 5.485e-02 -3.112e+03  3.202e+01 87724
gic402030           -1.649e+03  5.752e+02  -2.8660 4.158e-03 -2.776e+03 -5.212e+02 87724
gic402040           -2.172e+03  7.698e+02  -2.8218 4.777e-03 -3.681e+03 -6.634e+02 87724
gic403010           -1.902e+03  5.281e+02  -3.6019 3.161e-04 -2.937e+03 -8.671e+02 87724
gic404010           -2.793e+03  8.508e+02  -3.2827 1.028e-03 -4.460e+03 -1.125e+03 87724
gic404020           -1.918e+03  6.886e+02  -2.7858 5.340e-03 -3.268e+03 -5.687e+02 87724
gic404030           -8.621e+02  1.790e+03  -0.4816 6.301e-01 -4.371e+03  2.646e+03 87724
gic451010           -9.398e+02  6.836e+02  -1.3747 1.692e-01 -2.280e+03  4.001e+02 87724
gic451020           -2.041e+03  5.985e+02  -3.4106 6.484e-04 -3.214e+03 -8.682e+02 87724
gic451030           -1.597e+03  5.566e+02  -2.8690 4.118e-03 -2.688e+03 -5.060e+02 87724
gic452010           -2.592e+03  6.309e+02  -4.1089 3.979e-05 -3.829e+03 -1.356e+03 87724
gic452020           -2.449e+03  7.956e+02  -3.0779 2.085e-03 -4.008e+03 -8.894e+02 87724
gic452030           -2.278e+03  5.711e+02  -3.9891 6.636e-05 -3.398e+03 -1.159e+03 87724
gic452040           -2.133e+04  8.536e+03  -2.4984 1.248e-02 -3.806e+04 -4.596e+03 87724
gic452050           -7.211e+03  1.802e+03  -4.0017 6.295e-05 -1.074e+04 -3.679e+03 87724
gic453010           -1.267e+03  6.314e+02  -2.0061 4.485e-02 -2.504e+03 -2.908e+01 87724
gic501010           -1.687e+03  7.320e+02  -2.3041 2.122e-02 -3.121e+03 -2.519e+02 87724
gic501020           -6.147e+02  1.049e+03  -0.5858 5.580e-01 -2.672e+03  1.442e+03 87724
gic502010           -5.807e+02  7.607e+02  -0.7635 4.452e-01 -2.072e+03  9.101e+02 87724
gic502020           -5.938e+02  9.868e+02  -0.6018 5.473e-01 -2.528e+03  1.340e+03 87724
gic502030           -4.577e+02  1.265e+03  -0.3617 7.176e-01 -2.938e+03  2.022e+03 87724
gic551010           -2.123e+03  5.828e+02  -3.6426 2.700e-04 -3.265e+03 -9.806e+02 87724
gic551020           -2.977e+03  7.970e+02  -3.7351 1.878e-04 -4.539e+03 -1.415e+03 87724
gic551030           -2.042e+03  6.040e+02  -3.3807 7.234e-04 -3.226e+03 -8.580e+02 87724
gic551040           -1.725e+03  5.961e+02  -2.8945 3.799e-03 -2.894e+03 -5.570e+02 87724
gic551050           -1.311e+03  1.233e+03  -1.0637 2.875e-01 -3.727e+03  1.105e+03 87724
gic601010           -9.036e+02  5.147e+02  -1.7554 7.919e-02 -1.913e+03  1.053e+02 87724
gic601020           -1.340e+03  1.006e+03  -1.3311 1.832e-01 -3.312e+03  6.329e+02 87724
as.double(roac)     -2.884e-01  4.346e-03 -66.3618 0.000e+00 -2.969e-01 -2.799e-01 87724

Multiple R-squared:  0.1108 ,	Adjusted R-squared:   0.11 
F-statistic: 64.42 on 80 and 87724 DF,  p-value: < 2.2e-16
"""



#However, based on our performance dictionary, we make additional observation that whilst it is indeed true that the disclosure of negative performance is
# correlated with negative performance. To study if companies disclose positive performance as it is, we divided positive performance into 
# negneg, whereby company discloses that it is trying to counteract negative performance (eg. reduce costs, reduce liabilities) and posl, whereby company simply tries 
# discusses positive performance (eg. increase in revenue). It is observed that company's description to counteract negative performance is correlated with performance improvement
# whereby the disclosure of existing positive performance is negatively correlated with performance improvement


reg = lm_robust(as.double(roac1) ~ as.double(posl)+ as.double(negl)+ as.double(negneg)+log(as.double(length))+log(as.double(BOV))+gic+as.double(roac), data = `vectorfinal(7)`)
summary(reg)

"""

Coefficients:
Estimate Std. Error  t value  Pr(>|t|)   CI Lower   CI Upper    DF
(Intercept)             -2880.272  3.327e+02  -8.6561 4.964e-18 -3.532e+03 -2.228e+03 87722
as.double(posl)        -85989.695  1.721e+04  -4.9975 5.819e-07 -1.197e+05 -5.227e+04 87722
as.double(negl)        -15473.569  3.517e+03  -4.3993 1.087e-05 -2.237e+04 -8.580e+03 87722
as.double(negneg)      149260.523  1.666e+04   8.9592 3.332e-19  1.166e+05  1.819e+05 87722
log(as.double(length))    179.507  2.823e+01   6.3591 2.040e-10  1.242e+02  2.348e+02 87722
log(as.double(BOV))        40.185  2.967e+01   1.3542 1.757e-01 -1.797e+01  9.834e+01 87722
gic101010               -3520.543  6.678e+02  -5.2716 1.356e-07 -4.829e+03 -2.212e+03 87722
gic101020               -3097.211  5.408e+02  -5.7272 1.024e-08 -4.157e+03 -2.037e+03 87722
gic151010               -2401.499  6.409e+02  -3.7473 1.788e-04 -3.658e+03 -1.145e+03 87722
gic151020               -1897.118  1.522e+03  -1.2465 2.126e-01 -4.880e+03  1.086e+03 87722
gic151030               -1608.138  8.638e+02  -1.8616 6.266e-02 -3.301e+03  8.499e+01 87722
gic151040               -1655.705  6.855e+02  -2.4155 1.572e-02 -2.999e+03 -3.122e+02 87722
gic151050               -2135.003  1.091e+03  -1.9563 5.044e-02 -4.274e+03  4.064e+00 87722
gic201010               -2787.161  7.606e+02  -3.6643 2.481e-04 -4.278e+03 -1.296e+03 87722
gic201020               -1573.262  7.734e+02  -2.0343 4.193e-02 -3.089e+03 -5.746e+01 87722
gic201030               -2294.453  8.379e+02  -2.7384 6.175e-03 -3.937e+03 -6.522e+02 87722
gic201040               -1694.323  7.073e+02  -2.3955 1.660e-02 -3.081e+03 -3.080e+02 87722
gic201050               -3024.981  1.166e+03  -2.5951 9.458e-03 -5.310e+03 -7.403e+02 87722
gic201060               -2568.519  5.849e+02  -4.3916 1.127e-05 -3.715e+03 -1.422e+03 87722
gic201070               -2713.530  7.566e+02  -3.5865 3.353e-04 -4.196e+03 -1.231e+03 87722
gic202010               -2283.285  5.939e+02  -3.8443 1.210e-04 -3.447e+03 -1.119e+03 87722
gic202020               -2479.667  6.764e+02  -3.6659 2.466e-04 -3.805e+03 -1.154e+03 87722
gic203010               -3250.159  9.502e+02  -3.4203 6.258e-04 -5.113e+03 -1.388e+03 87722
gic203020               -1089.159  1.004e+03  -1.0848 2.780e-01 -3.057e+03  8.788e+02 87722
gic203030               -2581.608  1.026e+03  -2.5160 1.187e-02 -4.593e+03 -5.705e+02 87722
gic203040               -2005.201  6.422e+02  -3.1225 1.794e-03 -3.264e+03 -7.466e+02 87722
gic203050               -3851.675  2.689e+03  -1.4322 1.521e-01 -9.123e+03  1.419e+03 87722
gic251010               -1713.021  7.939e+02  -2.1579 3.094e-02 -3.269e+03 -1.571e+02 87722
gic251020               -2617.768  1.477e+03  -1.7727 7.628e-02 -5.512e+03  2.766e+02 87722
gic252010               -2907.164  6.439e+02  -4.5150 6.340e-06 -4.169e+03 -1.645e+03 87722
gic252020               -2013.518  9.027e+02  -2.2306 2.571e-02 -3.783e+03 -2.443e+02 87722
gic252030               -2890.574  6.457e+02  -4.4766 7.594e-06 -4.156e+03 -1.625e+03 87722
gic253010               -2020.124  5.606e+02  -3.6036 3.140e-04 -3.119e+03 -9.214e+02 87722
gic253020               -2321.083  8.044e+02  -2.8855 3.909e-03 -3.898e+03 -7.445e+02 87722
gic254010               -2347.128  7.420e+02  -3.1631 1.562e-03 -3.802e+03 -8.927e+02 87722
gic255010               -1309.851  9.495e+02  -1.3795 1.677e-01 -3.171e+03  5.511e+02 87722
gic255020               -2414.143  8.112e+02  -2.9759 2.922e-03 -4.004e+03 -8.242e+02 87722
gic255030               -4384.673  9.168e+02  -4.7826 1.733e-06 -6.182e+03 -2.588e+03 87722
gic255040               -2949.817  5.773e+02  -5.1097 3.233e-07 -4.081e+03 -1.818e+03 87722
gic301010               -2591.918  8.207e+02  -3.1582 1.588e-03 -4.200e+03 -9.834e+02 87722
gic302010               -1953.539  7.667e+02  -2.5479 1.084e-02 -3.456e+03 -4.508e+02 87722
gic302020               -3005.846  7.282e+02  -4.1281 3.662e-05 -4.433e+03 -1.579e+03 87722
gic302030               -5012.503  1.427e+03  -3.5138 4.419e-04 -7.808e+03 -2.217e+03 87722
gic303010               -1647.847  1.537e+03  -1.0720 2.837e-01 -4.661e+03  1.365e+03 87722
gic303020               -3220.546  8.606e+02  -3.7422 1.826e-04 -4.907e+03 -1.534e+03 87722
gic351010               -1477.960  5.517e+02  -2.6787 7.392e-03 -2.559e+03 -3.966e+02 87722
gic351020               -2621.640  5.554e+02  -4.7201 2.361e-06 -3.710e+03 -1.533e+03 87722
gic351030               -2307.940  9.359e+02  -2.4659 1.367e-02 -4.142e+03 -4.735e+02 87722
gic352010                -258.404  5.003e+02  -0.5165 6.055e-01 -1.239e+03  7.222e+02 87722
gic352020               -1067.472  6.029e+02  -1.7706 7.663e-02 -2.249e+03  1.142e+02 87722
gic352030               -1882.738  7.274e+02  -2.5884 9.643e-03 -3.308e+03 -4.571e+02 87722
gic401010                -775.622  4.697e+02  -1.6515 9.865e-02 -1.696e+03  1.449e+02 87722
gic401020               -1019.764  5.316e+02  -1.9182 5.509e-02 -2.062e+03  2.221e+01 87722
gic402010               -2644.969  9.340e+02  -2.8319 4.628e-03 -4.476e+03 -8.143e+02 87722
gic402020               -1501.199  8.008e+02  -1.8746 6.085e-02 -3.071e+03  6.836e+01 87722
gic402030               -1588.872  5.747e+02  -2.7647 5.699e-03 -2.715e+03 -4.625e+02 87722
gic402040               -2117.719  7.688e+02  -2.7544 5.881e-03 -3.625e+03 -6.108e+02 87722
gic403010               -1867.086  5.279e+02  -3.5368 4.052e-04 -2.902e+03 -8.324e+02 87722
gic404010               -2716.758  8.525e+02  -3.1870 1.438e-03 -4.388e+03 -1.046e+03 87722
gic404020               -1874.205  6.881e+02  -2.7236 6.458e-03 -3.223e+03 -5.255e+02 87722
gic404030                -857.917  1.786e+03  -0.4802 6.311e-01 -4.359e+03  2.643e+03 87722
gic451010                -934.254  6.831e+02  -1.3676 1.715e-01 -2.273e+03  4.047e+02 87722
gic451020               -2016.016  5.978e+02  -3.3723 7.458e-04 -3.188e+03 -8.443e+02 87722
gic451030               -1590.916  5.560e+02  -2.8613 4.220e-03 -2.681e+03 -5.011e+02 87722
gic452010               -2625.841  6.303e+02  -4.1660 3.103e-05 -3.861e+03 -1.390e+03 87722
gic452020               -2525.166  7.948e+02  -3.1771 1.488e-03 -4.083e+03 -9.673e+02 87722
gic452030               -2329.310  5.704e+02  -4.0835 4.440e-05 -3.447e+03 -1.211e+03 87722
gic452040              -21440.891  8.521e+03  -2.5162 1.186e-02 -3.814e+04 -4.740e+03 87722
gic452050               -7207.859  1.801e+03  -4.0028 6.266e-05 -1.074e+04 -3.678e+03 87722
gic453010               -1335.753  6.305e+02  -2.1184 3.414e-02 -2.572e+03 -9.991e+01 87722
gic501010               -1715.680  7.315e+02  -2.3453 1.902e-02 -3.150e+03 -2.819e+02 87722
gic501020                -644.546  1.050e+03  -0.6139 5.393e-01 -2.702e+03  1.413e+03 87722
gic502010                -635.911  7.600e+02  -0.8368 4.027e-01 -2.125e+03  8.536e+02 87722
gic502020                -628.132  9.866e+02  -0.6366 5.244e-01 -2.562e+03  1.306e+03 87722
gic502030                -456.828  1.265e+03  -0.3612 7.179e-01 -2.936e+03  2.022e+03 87722
gic551010               -2244.347  5.832e+02  -3.8481 1.191e-04 -3.387e+03 -1.101e+03 87722
gic551020               -3130.622  7.994e+02  -3.9161 9.006e-05 -4.697e+03 -1.564e+03 87722
gic551030               -2161.006  6.040e+02  -3.5780 3.465e-04 -3.345e+03 -9.772e+02 87722
gic551040               -1673.655  5.956e+02  -2.8102 4.952e-03 -2.841e+03 -5.064e+02 87722
gic551050               -1357.643  1.233e+03  -1.1013 2.708e-01 -3.774e+03  1.058e+03 87722
gic601010                -845.399  5.144e+02  -1.6436 1.003e-01 -1.854e+03  1.628e+02 87722
gic601020               -1380.683  1.007e+03  -1.3716 1.702e-01 -3.354e+03  5.923e+02 87722
as.double(roac)            -0.289  4.344e-03 -66.5241 0.000e+00 -2.975e-01 -2.805e-01 87722

Multiple R-squared:  0.1117 ,	Adjusted R-squared:  0.1109 
F-statistic: 64.07 on 82 and 87722 DF,  p-value: < 2.2e-16


"""
library(dplyr)

# Struggling to implement fixed effect 

`vectorfinal(7)`$id <- group_indices(`vectorfinal(7)`, cik, year)    
#which would be the same as my.data <- my.data %>% mutate(id = group_indices(st_name, race)), if this function supported mutate. 

rm(large_df, large_list,large_vector,temp_variables) 

plm.reg <- plm(as.double(roac1) ~ as.double(percwrds)+log(length)+log(as.double(BOV))+year+as.double(roac),
               data = `vectorfinal(7)`, index=c("cik"), model = "within")

summary(plm.reg)

#summary(reg)

roac1 = `vectorfinal(7)`$roac1
percwrds = `vectorfinal(7)`$percwrds
length=`vectorfinal(7)`$length
BOV=`vectorfinal(7)`$BOV
roac=`vectorfinal(7)`$roac
gic=`vectorfinal(7)`$gic
cik=`vectorfinal(7)`$cik


plm.reg <- lm(as.double(roac1) ~ as.double(percwrds)+log(length)+log(as.double(BOV))+year+as.double(roac)+gic, data = `vectorfinal(7)`)
               

coeftest(plm.reg , vcov=vcovHC(plm.reg ,type="HC0",cluster="gic"), data = `vectorfinal(7)`)




plm.reg <- plm(as.double(roac1) ~ as.double(percwrds)+log(length)+log(as.double(BOV))+year+as.double(roac),
               data = `vectorfinal(7)`, index=c("gic"), model = "within")

summary(plm.reg)


plm.reg <- lm(as.double(roac1) ~ as.double(percwrds)+log(length)+log(as.double(BOV))+year+as.double(roac)+gic,
               data = `vectorfinal(7)`)

summary(plm.reg)

plm.reg <- plm(as.double(roac1) ~ as.double(percwrds)+log(length)+log(as.double(BOV))+year+as.double(roac),
               data = `vectorfinal(7)`, index=c("cik"), model = "within")

summary(plm.reg)





plm.reg <- plm(as.double(roac1) ~ as.double(percwrds)+log(length)+log(as.double(BOV))+as.double(roac),
               data = `vectorfinal(7)`, index=c("filename","year"), model = "within",
               effect = "twoways")


reg <- lm(as.double(roac1) ~ as.double(percwrds)+log(length)+log(as.double(BOV))+as.double(roac)+as.character(gic), 
                 data = `vectorfinal(7)`)

summary(reg)

roac1 = `vectorfinal(7)`$roac1
percwrds = `vectorfinal(7)`$percwrds
length=`vectorfinal(7)`$length
BOV=`vectorfinal(7)`$BOV
roac=`vectorfinal(7)`$roac
gic=`vectorfinal(7)`$gic
cik=`vectorfinal(7)`$cik


coeftest(reg, vcov=vcovHC(reg,type="HC0",cluster="gic"), data = `vectorfinal(7)`)


fatal_fe_mod <- plm(fatal_rate ~ beertax, 
                    data = Fatalities,
                    index = c("cik", "cikyear"), 
                    model = "within")

table(index(`vectorfinal(7)`), useNA = "ifany")


reg <- plm(as.double(roac1) ~ as.double(percwrds)+log(length)+log(as.double(BOV))+as.double(roac), 
           data = `vectorfinal(7)`,
           model = "within",
           index=c("cik","cikyear"))


`vectorfinal(7)`$cikyear <- paste(`vectorfinal(7)`$cik, `vectorfinal(7)`$year, sep="_")
Produc_plm2 <- pdata.frame(Produc, index = c("region", "year_state"))


Produc_plm2 <- pdata.frame(`vectorfinal(7)`, index = c("cik", "cikyear"))

#reg_plm_2 <- plm(gsp ~ pcap, data = Produc_plm2)

reg <- plm(as.double(roac1) ~ as.double(percwrds)+log(length)+log(as.double(BOV))+as.double(roac), 
           data = `vectorfinal(7)`,
           model = "within",
           index=c("cikyear","year"))

reg <- plm(as.double(roac1) ~ as.double(percwrds)+log(length)+log(as.double(BOV))+as.double(roac), 
                    data = `vectorfinal(7)`,
                    model = "within",
                    index=c("gic","year"))

coeftest(model, vcovHC(model, type = 'HC0', cluster = 'gic'))


reg <- lm_robust(as.double(roac1) ~ as.double(percwrds)+log(length)+log(as.double(BOV))+as.double(roac)+factor(gic), 
           data = `vectorfinal(7)`)

ct.lsdv <- coeftest(reg, vcov. = vcovHC)

summary(ct.lsdv)

reg = lm_robust(as.double(roac1) ~ as.double(percwrds)+log(length)+log(as.double(BOV))+gic+as.double(roac), data = subset(`vectorfinal(7)`))
summary(reg)