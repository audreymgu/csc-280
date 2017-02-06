# Project One - Fractions
# NAME: George Gu
# DUE DATE: 09/16/16
# OTHER COMMENTS: Tuples are for squares :P

def gcf(a,b): #6-25 lines
# Take the absolute values of a and b, and reassign the resulting results to a and b, respectively.
  a = abs(a)
  b = abs(b)
# Switch a and b if a is smaller than b.
  if a < b:
      a,b = b,a
# Continue to take the modulus of a by b while the result of the calculation continues to be greater than zero, with the divisor from the prior modulus operation becoming the dividend and the result of the prior modulus operation becoming the divisor. 
  while a%b>0:
      a,b = b,a%b
# Store b.
  return b
    
def reduce(t): #16-25 lines
# Return (0,1) for tuples that have a zero in the numerator.
  if t[0] == 0:
      return (0,1)
# Find the greatest common factor using gcf() and assign the value to variable g.
  g = gcf(t[0],t[1])
# Divide both the numerator and denominator by the greatest common factor, stored as g.
  frac = (t[0]/g,t[1]/g)
# Handle cases where the fraction is negative.
  if frac[1] < 0:
      frac = (-1*frac[0],-1*frac[1])
  else:
      pass
# Store frac.
  return frac

def add(ta, tb): #3-6 lines
# Multiply the numerators of ta and tb by the denominators of tb and ta respectively, multiply the denominators together, and store the resulting two values in frac. 
  frac = ((ta[0]*tb[1])+(tb[0]*ta[1]),(ta[1]*tb[1]))
# Reduce frac.
  frac = reduce(frac)
# Store frac.
  return frac

def subtract(ta, tb): #2 lines
# Use add() to find the sum of fractions ta and -tb.
  frac = add(ta,(-1*tb[0],tb[1]))
# Use reduce() to simplify the resulting fraction.
  frac = reduce(frac)
# Store frac.
  return frac

def multiply(ta, tb): #3-6 lines
# Multiply the numerators of ta and tb together, as well as the denominators. Store the resulting two values in frac.
  frac = (ta[0]*tb[0], ta[1]*tb[1])
# Reduce frac.
  frac = reduce(frac)
# Store frac.
  return frac

def square(t): #2 lines
# Multiply t with itself. reduce() is already included in multiply().
  frac = multiply(t,t)
  return frac

def invert(t): #2 lines
# Create a new variable, frac, that assigns in the 0 spot the 1 value from t, and in the 1 spot the 0 value from t.
  frac = (t[1],t[0])
# Reduce frac.
  frac = reduce(frac)
# Store frac.
  return frac

def divide(ta, tb): #2 lines
# Invert tb.
  tb = invert(tb)
# Multiply ta and tb (inverted). Reduction is already included.
  frac = multiply(ta,tb)
# Store frac.
  return frac

def toFloat(t): # 2lines
# Create a new variable, float, which multiplies t with 1. in order to store t as a float.
  float = 1.*t[0]/t[1]
# Store float.
  return(float)
