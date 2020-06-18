library(readr)
#install.packages("estimatr")
#install.packages("margins")
#install.packages("car")
library(estimatr)
library(margins)
library(car)
#summary(regression1)



`vectorfinal(8)` <- `vectorfinal(8)`[!is.na(as.numeric(as.character(`vectorfinal(8)`$roa))),]
`vectorfinal(8)` <- `vectorfinal(8)`[!is.na(as.numeric(as.character(`vectorfinal(8)`$roat.1))),]
`vectorfinal(8)` <- `vectorfinal(8)`[!is.na(as.numeric(as.character(`vectorfinal(8)`$roat.1.1))),]
`vectorfinal(8)`<- `vectorfinal(8)`[!is.na(as.numeric(as.character(`vectorfinal(8)`$roat.1.1))),]
`vectorfinal(8)` <- `vectorfinal(8)`[!is.na(as.numeric(as.character(`vectorfinal(8)`$csho))),]


"""
dat1 <- transform( `vectorfinal(7)`[grep("^\\d+$",  `vectorfinal(8)`$roa),,drop=T], roa= as.numeric(as.character(roa)))
dat1 <- transform( `vectorfinal(7)`[grep("^\\d+$",  `vectorfinal(8)`$roat.1),,drop=T], roat.1= as.numeric(as.character(roat.1)))
dat1 <- transform( `vectorfinal(7)`[grep("^\\d+$",  `vectorfinal(8)`$roat.1.1),,drop=T], roat.1.1= as.numeric(as.character(roat.1.1)))

"""

`vectorfinal(8)`$BOV=as.double(`vectorfinal(8)`$prcc)*as.double(`vectorfinal(8)`$csho) / as.double(`vectorfinal(8)`$ceq)
`vectorfinal(8)`$gic=as.character(`vectorfinal(8)`$gic)
`vectorfinal(8)`$roac=as.double(`vectorfinal(8)`$roa)-as.double(`vectorfinal(8)`$roat.1)
`vectorfinal(8)`$roac1=as.double(`vectorfinal(8)`$roat.1.1)-as.double(`vectorfinal(8)`$roa)
`vectorfinal(8)`$intext=as.double(`vectorfinal(8)`$internal)/as.double(`vectorfinal(8)`$external)
`vectorfinal(8)`$year=as.character(`vectorfinal(8)`$year)


reg = lm_robust(as.double(roac1) ~ as.double(internal)+as.double(external)+log(length)+log(as.double(BOV))+gic+as.double(roac)+year, data = subset(`vectorfinal(8)`))
summary(reg)

reg = lm_robust(as.double(roac1) ~ log(as.double(intext))+log(length)+log(as.double(BOV))+gic+as.double(roac)+year, data = subset(`vectorfinal(8)`))
summary(reg) #???

