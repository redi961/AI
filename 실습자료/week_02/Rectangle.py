class Rectangle :
  # __init__ -> 기본 실행문 // __init__()은 반드시 첫 번째 인수로 self를 지정해야한다.
  # self = 자기 자신에 대한 참조
  # 함수 이름 왼쪽 _는 보안성이 약한 private 의미로 사용하는 경우이다 
  #  언더바 관련 자료 참고 https://doorbw.tistory.com/153 / https://hwanii-with.tistory.com/54
  def __init__ (self, width=1, height=1) :
    self._width = width
    self._height = height
  
  def setWidth(self, width) :
    self._width = width

  def setHeight(self, height) :
    self._height = height

  def getWidth(self) :
    return self._width
  
  def getHeight(self) :
    return self._height
  
  def area(self) :
    return self._width * self._height
  
  def perimeter(self) :
    return 2 * (self._width + self._height)
  
  # 출력문
  def __str__(self) :
    return ("Width : " + str(self._width)
    + "\nHeight : " + str(self._height))