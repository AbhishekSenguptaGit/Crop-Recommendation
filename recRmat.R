t1<-read.csv(file.choose())
t2<-read.csv(file.choose())
install.packages("sqldf")
library(sqldf)
r<-readline(prompt="enter rawmaterial:")
DAP
data<-sqldf("SELECT crop,t1.rawmaterial,AVG(punjab) as p,AVG(madhyapradesh) as m,AVG(himachalpradesh) as h,AVG(mizoram) as z,AVG(ABS(d-distance1)) as pd,AVG(ABS(d-distance2)) as md,AVG(ABS(d-distance3)) as hd,AVG(ABS(d-distance4)) as zd FROM t1,t2 WHERE t1.rawmaterial=t2.rawmaterial GROUP BY crop,t1.rawmaterial
")
data

d<-sqldf("SELECT crop,t1.rawmaterial,MAX(AVG(punjab),AVG(madhyapradesh),AVG(mizoram),AVG(himachalpradesh)) AS MAXPRO,MIN(AVG(ABS(d-distance1)),AVG(ABS(d-distance2)),AVG(ABS(d-distance3)),AVG(ABS(d-distance4))) AS MINDIS FROM t1,t2 WHERE t1.rawmaterial=t2.rawmaterial  GROUP BY crop,t1.rawmaterial
")
d
c<-readline(prompt="enter crop")
Banana
x<-readline(prompt="enter rawmaterial1 for crop")
zinc
y<-readline(prompt="enter rawmaterial2 for crop")
sulphur
c
if(sqldf("SELECT MAXPRO from d where crop='Banana' and rawmaterial='zinc'")==sqldf("SELECT AVG(punjab) FROM t1,t2 where t1.rawmaterial=t2.rawmaterial and crop='Banana' and t1.rawmaterial='zinc'"))
{
  print("for growing banana crop recmmandble state for importing zinc rawmaterial is punjab w.r.t production")  
}else if(sqldf("SELECT MAXPRO from d where crop='Banana' and rawmaterial='zinc'")==sqldf("SELECT AVG(madhyapradesh) FROM t1,t2 where t1.rawmaterial=t2.rawmaterial and crop='Banana' and t1.rawmaterial='zinc'"))
{
print("for growing banana crop recmmandble state for importing zinc rawmaterial is madhyapradesh w.r.t production")  
}else if(sqldf("SELECT MAXPRO from d where crop='Banana' and rawmaterial='zinc'")==sqldf("SELECT AVG(himachalpradesh) FROM t1,t2 where t1.rawmaterial=t2.rawmaterial and crop='Banana' and t1.rawmaterial='zinc'"))
{
print("for growing banana crop recmmandble state for importing zinc rawmaterial is himachalpradesh w.r.t production")
}else{
  print("for growing banana crop recmmandble state for importing zinc rawmaterial is mizoram w.r.t production")
}

if(sqldf("SELECT MINDIS from d where crop='Banana' and rawmaterial='zinc'")==sqldf("SELECT AVG(ABS(d-distance1)) FROM t1,t2 where t1.rawmaterial=t2.rawmaterial and crop='Banana' and t1.rawmaterial='zinc'"))
{
  print("for growing banana crop recmmandble state for importing zinc rawmaterial is punjab w.r.t distance")  
}else if(sqldf("SELECT MINDIS from d where crop='Banana' and rawmaterial='zinc'")==sqldf("SELECT AVG(ABS(d-distance2)) FROM t1,t2 where t1.rawmaterial=t2.rawmaterial and crop='Banana' and t1.rawmaterial='zinc'"))
{
  print("for growing banana crop recmmandble state for importing zinc rawmaterial is madhyapradesh w.r.t production")  
}else if(sqldf("SELECT MINDIS from d where crop='Banana' and rawmaterial='zinc'")==sqldf("SELECT AVG(ABS(d-distance3)) FROM t1,t2 where t1.rawmaterial=t2.rawmaterial and crop='Banana' and t1.rawmaterial='zinc'"))
{
  print("for growing banana crop recmmandble state for importing zinc rawmaterial is himachalpradesh w.r.t distance")
}else{
  print("for growing banana crop recmmandble state for importing zinc rawmaterial is mizoram w.r.t distnace")
}

if(sqldf("SELECT MAXPRO from d where crop='Banana' and rawmaterial='sulphur'")==sqldf("SELECT AVG(punjab) FROM t1,t2 where t1.rawmaterial=t2.rawmaterial and crop='Banana' and t1.rawmaterial='sulphur'"))
{
  print("for growing banana crop recmmandble state for importing sulphur rawmaterial is punjab w.r.t production")  
}else if(sqldf("SELECT MAXPRO from d where crop='Banana' and rawmaterial='sulphur'")==sqldf("SELECT AVG(madhyapradesh) FROM t1,t2 where t1.rawmaterial=t2.rawmaterial and crop='Banana' and t1.rawmaterial='sulphur'"))
{
  print("for growing banana crop recmmandble state for importing sulphur rawmaterial is madhyapradesh w.r.t production")  
}else if(sqldf("SELECT MAXPRO from d where crop='Banana' and rawmaterial='sulphur'")==sqldf("SELECT AVG(himachalpradesh) FROM t1,t2 where t1.rawmaterial=t2.rawmaterial and crop='Banana' and t1.rawmaterial='sulphur'"))
{
  print("for growing banana crop recmmandble state for importing sulphur rawmaterial is himachalpradesh w.r.t production")
}else{
  print("for growing banana crop recmmandble state for importing sulphur rawmaterial is mizoram w.r.t production")
}

if(sqldf("SELECT MINDIS from d where crop='Banana' and rawmaterial='sulphur'")==sqldf("SELECT AVG(ABS(d-distance1)) FROM t1,t2 where t1.rawmaterial=t2.rawmaterial and crop='Banana' and t1.rawmaterial='sulphur'"))
{
  print("for growing banana crop recmmandble state for importing sulphur rawmaterial is punjab w.r.t distance")  
}else if(sqldf("SELECT MINDIS from d where crop='Banana' and rawmaterial='sulphur'")==sqldf("SELECT AVG(ABS(d-distance2)) FROM t1,t2 where t1.rawmaterial=t2.rawmaterial and crop='Banana' and t1.rawmaterial='sulphur'"))
{
  print("for growing banana crop recmmandble state for importing sulphur rawmaterial is madhyapradesh w.r.t production")  
}else if(sqldf("SELECT MINDIS from d where crop='Banana' and rawmaterial='sulphur'")==sqldf("SELECT AVG(ABS(d-distance3)) FROM t1,t2 where t1.rawmaterial=t2.rawmaterial and crop='Banana' and t1.rawmaterial='sulphur'"))
{
  print("for growing banana crop recmmandble state for importing sulphur rawmaterial is himachalpradesh w.r.t distance")
}else{
  print("for growing banana crop recmmandble state for importing sulphur rawmaterial is mizoram w.r.t distnace")
}
