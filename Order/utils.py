
def Processor1(collect,start,end):
   _count = collect.find({"clickTime":{"$gte":start,"$lte":end}}).count()
   return _count

