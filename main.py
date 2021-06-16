import imgpro.image as img

#stack function to stack image data lists together
def stack(data):
  dataset = data[0]
  counter3 = -1
  for a in data:
    counter3 +=1
    if data.index(a) == 0:
      continue
    else:
      counter = -1
      counter2 = -1
      for b in a:
        counter +=1
        counter2 =-1
        for c in b:
          counter2 +=1
          if c == [0, 0, 0]:
            continue
          else:
            dataset[counter+counter3][counter2+counter3] = c
  return dataset

#formatting
def format(data):
  tempstring = ""
  tempstring2 = ""
  counter = -1
  counter2 = 0
  datatemp = []
  info = False
  for f in data:
    counter += 1
    datatemp.append([])
    for a in f:
      if counter2 > 1:
        counter2 = counter2 - 1
        if info:
          counter2 = int(a) + 1
          info = False
          continue
        tempstring2 += a
        if counter2 == 1:
          datatemp[counter].append(tempstring2)
        continue
      if a == "\n":
        continue
      if len(tempstring) > 4:
        datatemp[counter].append(tempstring)
        tempstring = ""
      if len(tempstring) == 0:
        if a == "3":
          counter2 = 3
          info = True
          tempstring2 = a
          continue
        if a == "0" or a == "2":
          datatemp[counter].append(a)
          continue
      tempstring += a
  return datatemp

#decoding
def decode(data):
  letterindx = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

  counter = 0
  counter2 = -1
  datatemp = []
  for g in data:
    counter2 +=1
    counter = 0
    datatemp.append([[]])
    for b in g:
      if b[0] == "3":
        repeatamount = ""
        counter3 = 0
        for l in b:
          counter3 += 1
          if counter3 > 2:
            repeatamount += l
        for p in range(int(repeatamount)):
          if b[1] == "0":
            datatemp[counter2][counter].append([0, 0, 0])
          if b[1] == "2":
            datatemp[counter2].append([])
            counter += 1
      if b[0] == "0":
        datatemp[counter2][counter].append([0, 0, 0])
      if b[0] == "1":
        red = int((letterindx.index(b[1]) / 15)*255)
        green = int((letterindx.index(b[2]) / 15)*255)
        blue = int((letterindx.index(b[3]) / 15)*255)
        datatemp[counter2][counter].append([red, green, blue])
      if b[0] == "2":
        datatemp[counter2].append([])
        counter += 1
  return datatemp

def main():
  #importing file as String
  data = open("data.txt", "r").readlines()

  data = format(data)
  datatemp = decode(data)

  #runs image printer

  #img.main(datatemp[1])
  img.main(stack(datatemp))

main()