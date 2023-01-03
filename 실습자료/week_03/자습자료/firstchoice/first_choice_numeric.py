from problem_skeleton import Numeric

LIMIT_STUCK = 100

def main():
    # Numeric class instance를 생성한다.
    p = Numeric()
    # setVariable을 이용해 문제를 읽어온다.
    p.setVariables()
    # steepestAscent를 실행한다.
    firstChoice(p)
    # describe, report를 이용해 결과를 출력한다.
    p.describe()
    displaySetting(p)
    p.report()

def firstChoice(p) :
  current = p.randomInit()
  valueC = p.evaluate(current)
  i = 0
  # 지정한 한계값 까지의 계산
  while i < LIMIT_STUCK :
       successor = p.randomMutant(current)
       valueS = p.evaluate(successor)
       # best solution 업데이트
       if valueS <= valueC :
         current = successor
         valueC = valueS
         i = 0 # 갱신에 성공하였을때 LIMIT 수치를 0으로 초기화함
       else :
         i += 1 # 갱신이 없을때 LIMIT수치를 1 상승시킴
     # Best solution과 그때의 Cost를 반환
  p.storeResult(current, valueC)
  return current, valueC    

def displaySetting(p):
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", p.getDelta)

main ()