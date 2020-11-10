quantity = int(input())
times = []
for q in range(quantity):
  times.append(input().split())

iniciado = 0
tmeArray = []
tmtArray = []
for time in range(len(times)):
  tc = int(times[time][0])
  d = int(times[time][1])
  tmeArray.append(iniciado - tc)
  tmtArray.append(iniciado + d - tc)
  iniciado += d
print('TME:'+ str(round(sum(tmeArray) / quantity, 2)))
print('TMT:'+ str(round(sum(tmtArray) / quantity, 2)))