insert body,name=booboowei weight=54.3,height=57.5,high_waistline=69,waistline=73,low_waistline=86,hipline=93,thigh_circumference=54,low_thigh_circumference=42,calf_circumference=35

cat > /tmp/test01.sh << ENDF
echo 'body,name="booboowei" weight=54.3,height=57.5,high_waistline=69,waistline=73,low_waistline=86,hipline=93,thigh_circumference=54,low_thigh_circumference=42,calf_circumference=35'
ENDF


weight=54.3,
height=57.5,
high_waistline=69,
waistline=73,
low_waistline=86,
hipline=93,
thigh_circumference=54,
low_thigh_circumference=42,
calf_circumference=35

body_dict = {
"weight":"体重",
"height":"身高",
"high_waistline":"上腰围",
"waistline":"腰围",
"low_waistline":"下腰围",
"hipline":"臀围",
"thigh_circumference":"大腿根围",
"low_thigh_circumference":"大腿细围",
"calf_circumference":"小腿围",
}

每天体重变化
SELECT DIFFERENCE("weight") as "体重变化" FROM (select mean(weight) as weight from "telegraf"."autogen"."body" WHERE  "name"='"booboowei"' group by time(1d)) 
每天体围变化
SELECT difference("high_waistline") as "上腰围", 
difference("waistline") as "腰围",
difference("low_waistline") as "下腰围", 
difference("hipline") as "臀围",   
difference("thigh_circumference") as "大腿根围",
difference("low_thigh_circumference") as "大腿细围",
difference("calf_circumference") as "小腿围" 
FROM (select mean(calf_circumference) as calf_circumference, mean(high_waistline) as high_waistline,mean(hipline) as hipline,mean(low_thigh_circumference) as low_thigh_circumference,mean(low_waistline) as low_waistline,mean(thigh_circumference) as thigh_circumference,mean(waistline) as waistline from "telegraf"."autogen"."body" WHERE "name"='"booboowei"' group by time(1d))

SELECT last("high_waistline") as "上腰围", 
last("waistline") as "腰围",
last("low_waistline") as "下腰围", 
last("hipline") as "臀围",   
last("thigh_circumference") as "大腿根围",
last("low_thigh_circumference") as "大腿细围",
last("calf_circumference") as "小腿围" 
FROM "telegraf"."autogen"."body" WHERE time > :dashboardTime: AND "name"='"booboowei"'


