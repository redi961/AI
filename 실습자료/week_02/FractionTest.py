class FractionTest :
  def __init__ (self, numerator = 0, denominator = 1) :
    self._numerator = numerator
    self._denominator = denominator

  def setNumerator(self, numerator) :
    self._numerator = numerator
  
  def getNumerator(self) :
    return self._numerator
  
  def setDenominator(self, denominator) :
    self._denominator = denominator
  
  def getDenominator(self) :
    return self._denominator

  def GCD(self, m, n) :
    while n != 0 :
      t = n
      n = m % n
      m = t
    return m

  def reduce (self) :
    gcd = self.GCD(self._numerator, self._denominator)
    self._numerator = self._numerator // gcd
    self._denominator = self._denominator // gcd

  
