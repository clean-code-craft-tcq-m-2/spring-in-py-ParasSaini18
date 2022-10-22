import math
def calculateStats(numbers):
  if len(numbers) == 0:
    return {"avg": math.nan, "max": math.nan, "min": math.nan}
  sum = 0
  for i in numbers:
    sum = sum + i
  sum = sum/len(numbers)
  dic = {"avg": sum, "max": max(numbers), "min": min(numbers)}
  return dic
