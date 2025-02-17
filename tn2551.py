def WhoAmI():
  return("tn2551")
print(WhoAmI())

"""getBondPrice ppy = 1 and 2"""

def getBondPrice(y, face, couponRate, m, ppy = 1):
  periods = m * ppy
  couponPayment = (couponRate * face) / ppy
  period_ytm = y / ppy
  bondPrice = sum((couponPayment)/(1 +period_ytm)**(t) for t in range (1, periods+1)) + face / (1 + period_ytm) ** (periods)
  return(bondPrice)

y = 0.03
couponRate = 0.04
face = 2000000
m = 10

annualBondValue = getBondPrice(y, face, couponRate, m, ppy = 1)

semiBondValue = getBondPrice(y, face, couponRate, m, ppy = 2)
print(f"Bond Price (Annual): ${annualBondValue:.2f}")
print(f"Bond Price (SemiAnnual): ${semiBondValue:.2f}")

"""getBondDuration"""

def getBondDuration(y, face, couponRate, bondValue, m, ppy):
    couponPayment = (couponRate * face) / ppy
    periods = m * ppy
    period_ytm = y / ppy

    weightedPV = sum([(t * couponPayment) / ((1 + period_ytm)**(t)) for t in range(1, int(m) * int(ppy) + 1)])
    weightedPV = weightedPV + (periods * face) / (1 + period_ytm)**periods

    bondDuration = weightedPV / bondValue

    return bondDuration

y = 0.03
couponRate = 0.04
face = 2000000
m = 10
ppy = 1

bondValue = getBondPrice(y, face, couponRate, m, ppy)
Duration = getBondDuration(y, face, couponRate, bondValue, m, ppy)


print(f"Bond Price: ${bondValue:.2f}")
print(f"Bond Duration: {Duration:.2f}")

"""BOND Price E"""

def getBondPrice_E(face, couponRate, m, yc):

    couponPayment = couponRate * face
    bondPrice = sum((couponPayment) / (1 + yc[t-1]) ** t for t in range(1, m + 1))

    bondPrice += face / (1 + yc[m-1]) ** m

    return bondPrice


yc = [0.010, 0.015, 0.020, 0.025, 0.030]
face = 2000000
couponRate = 0.04
m = 5

bondValue_E = getBondPrice_E(face, couponRate, m, yc)

print(f"Bond Price (E): ${bondValue_E:,.2f}")

"""Bond Price Z"""

def getBondPrice_Z(face, couponRate, m, yc):

    couponPayment = couponRate * face

    bondPrice = sum((couponPayment) / (1 + yc[i]) ** m[i] for i in range(len(m)))

    bondPrice += face / (1 + yc[-1]) ** m[-1]

    return bondPrice


yc = [0.010, 0.015, 0.020, 0.025, 0.030]
face = 2000000
couponRate = 0.04
m = [1,1.5,3,4,7]

bondValue_Z = getBondPrice_Z(face, couponRate, m, yc)

print(f"Bond Price (Z): ${bondValue_Z:,.2f}")

"""FizzBuzz"""

def FizzBuzz(start, finish):
  outlist =[]
  for i in range(start, finish+1):
    if i % 3 == 0 and i % 5 == 0:
      outlist.append("fizzbuzz")
    elif i % 3 == 0 and i % 5 != 0 :
      outlist.append("fizz")
    elif i % 5 == 0 and i%3!=0:
      outlist.append("buzz")
    else:
      outlist.append(i)

  return(outlist)

"""MatMult1"""

def MyMatMult(a,b):
  rows_a = len(a)
  rows_b = len(b)
  cols_b = len(b[0])
  cols_a = len(a[0])

  if cols_a != rows_b:
    return("Matrix Multiplication Not Possible")

  result_c = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
  for i in range(rows_a):
    for j in range(cols_b):
      for k in range(cols_a):
        result_c[i][j] += a[i][k] * b[k][j]

  return result_c

a = [[1, 2, 3]]
b = [[1], [4], [7]]
result_c = MyMatMult(a,b)
for row in result_c:
  print(row)

"""MyMult2"""

def MyMatMult2(a,b):
  rows_a = len(a)
  rows_b = len(b)
  cols_b = len(b[0])
  cols_a = len(a[0])

  if cols_a != rows_b:
    return("Matrix Multiplication Not Possible")

  result_c = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
  for i in range(rows_a):
    for j in range(cols_b):
      for k in range(cols_a):
        result_c[i][j] += a[i][k] * b[k][j]

  return result_c

a = [[1, 2, 3]]
b = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
result_c = MyMatMult(a,b)
for row in result_c:
  print(row)

def test_WhoAmI():
    assert WhoAmI() != 'djr2132'

def test_getBondPrice():
    assert round(getBondPrice(.03, 2000000, .04, 10,  1)) == 2170604
    assert round(getBondPrice(.03, 2000000, .04, 10,  2)) == 2171686


def test_getBondDuration():
    bondValue = getBondPrice(.03, 2000000, .04, 10,  1)
    assert round(getBondDuration(.03, 2000000, .04, bondValue,10, 1),2) == 8.51

def test_GetBondPriceE():
    yc = [.010,.015,.020,.025,.030]
    face = 2000000
    m = 5
    couponRate = .04
    assert round(getBondPrice_E(face, couponRate, m, yc)) == 2098949

def test_GetBondPriceZ():
    yc = [.010,.015,.020,.025,.030]
    times=[1,1.5,3,4,7]
    face = 2000000
    couponRate = .04
    x = getBondPrice_Z(face, couponRate, times, yc)
    assert round(x) == 1996533

def test_FizzBuzz():
    x = FizzBuzz(40,45)
    assert x[0] == "buzz"
    assert x[1] == 41
    assert x[5] == "fizzbuzz"

test_WhoAmI()
test_getBondPrice()
test_getBondDuration()
test_GetBondPriceE()
test_GetBondPriceZ()
test_FizzBuzz()

