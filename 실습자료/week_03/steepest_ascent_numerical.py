import random
import math

DELTA = 0.01   # Mutation step size
NumEval = 0    # Total number of evaluations

def main():
    # Create an instance of numerical optimization problem
    # 입력 txt 파일에서 수식과 변수의 범위를 읽어와 반환
    p = createProblem()   # 'p': (expr, domain)

    # Call the search algorithm
    # SteepestAscent 알고리즘을 실행하여 solution을 구하기
    solution, minimum = gradientDesent(p)

    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()

    # Report results
    displayResult(solution, minimum)


def createProblem():
    ## Read in an expression and its domain from a file.
    ## Then, return a problem 'p'.
    ## 'p' is a tuple of 'expression' and 'domain'

    # input function을 이용해 읽어올 txt 파일의 경로를 얻어옴
    filePath = input("Enter the path of a file :: ")
    f = open(filePath,'r')

    # readline()을 이용해 각 줄의 정보를 읽어옴 (readline은 사용할떄마다 한줄씩 나아감)
    # expression -> 수식 
    expression = f.readline().rstrip()
    varNames = []
    low = []
    up = []

    # domain source
    while True :
        d = f.readline().split(',')
        if d == [''] : break
        varNames.append(d[0])
        low.append(eval(d[1]))
        up.append(eval(d[2]))

    # domain = []
    # domain.append(varNames)
    # domain.append(low)
    # domain.append(up)
    # or
    domain = [varNames, low, up]

    #return expression, domain
    return expression, domain

def randomInit(p):
    # Return a random initial point
    # as a list of values
    # 초기 값을 만들기 위해 랜덤한 값들을 만들기
    domain = p[1]
    low, up = domain[1], domain[2]
    init = []
    # domain의 low, up 정보를 이용해
    # low <= value <= up 범위에 해당하는 값을 random.uniform을 통해 생성
    # list 형태로 각 변수의 초기 값을 반환
    for i in range(len(up)) :
     a = random.uniform(low[i], up[i])
     init.append(a)

    return init    

def steepestAscent(p):
    # Random한 초기값을 생성
    current = randomInit(p)
    # 초기값에 대한 함수값을 계산
    valueC = evaluate(current, p)

    # 계산을 반복하며 mutant를 생성후 더 나은 solution을 탐색
    while True :
        # mutant를 생성
        neighbors = mutants(current, p)
        # mutant 중 가장 좋은 solution을 선택
        # 각각의 neighbor에 대하여 함수값을 계산후
        # 더 좋은값이 보일시 그것으로 이동
        successor, valueS = bestOf(neighbors, p)
        # best solution 업데이트
        if valueS >= valueC :
            break
        else :
            current = successor
            valueC = valueS
    #        print("ValueC :: ", valueC)
    # Best solution과 그때의 Cost를 반환
    return current, valueC

def gradient(x, v, dx, p) :
    # x : 현재값 list
    # v : 현재 값에서의 함수 값
    # dx : x의 증분
    grad = []
    # x_new => x[i]에 dx만큼 더한 x
    # y_new = evaluate를 이용한 계산
    # grad[i]는 (y_ney - v) / dx
    # for ~~ 각 x 마다
    for i in range(len(x)) :
        x_new = x[:]
        x_new[i] += dx
        v_new = evaluate(x_new, p)
        g = ((v_new - v) / dx)
        grad.append(g)

    return grad

def gradientDesent(p) :
    # Random한 초기값을 생성
    current = randomInit(p)
    # 초기값에 대한 함수값을 계산
    valueC = evaluate(current, p)
    # 계산을 반복하며 mutant를 생성후 더 나은 solution을 탐색
    while True :
        # 다음에 Gradient를 따라 이동할 위치를 판단
        nextP = takeStep(current, valueC, 0.1, 1e-4, p)
        #그 위치에서의 함수값 계산
        valueN = evaluate(nextP, p)
        if valueN < valueC :
            #업데이트 하는 부분
            current = nextP
            valueC = valueN
        else :
            break

def takeStep(x, v, alpha, dx, p) :
    #Gradient를 얻는다
    grad = gradient(x, v, dx, p)
    domain = p[1]
    low = domain[1]
    up = domain[2]
    # x를 복사하여 x_new를 만든 뒤
    x_new = x[:]
    # alpha값과 grad를 이용하여 업데이트 진행
    for i in range(len(x)) :
        x_new[i] -= (alpha  * grad[i])
    # 업데이트 된 x_new 값이 domain (low, up) 범위 안에 있는지
    # 확인 후, vaild 한 경우에는 x_new를 그대로 return
    # 범위에 해당하지 않는 경우 x를 그대로 return
        if low[i] <= x_new[i] < up[i] :
            pass
        else : 
            return x

    return x_new

def evaluate(current, p):
    # Number of evaluation을 기록하기 위해 global 변수 이용
    # 글로벌 변수는 사용하기전에 global 입력
    global NumEval
    NumEval += 1

    # expression과 variable name을 읽어오고
    # 이를 이용해 x=value 형태의 string을 만든 뒤,
    # exec 를 이용해 실제로 실행하여 값을 할당 후
    # expression에 eval을 이용해 함수 값을 계산

    #x1, x2, x3, x4, x5 <- 현재값 저장
    #expression을 eval 하여 현재 함수 값을 계산
    # -> x1 = 0.5 같은 형태로 string을 만들어서 eval 함수 이용
    ## 왜냐하면 'x1', 'x2' 같은 변수 명을 저장해 두었기 때문
    ### exec('x1' + '=' + str(CURRENT_VALUE)) -> 결과적으로 X1에 CURRENT VALUE가 할당됨
    ### expression을 eval하여 혐재 함수 값을 계산한다. eval(expression)
    domain = p[1]
    varName = domain[0] # 여기에서 변수명을 참조
    expression = p[0]

    ## eval -> 계산"식" 만을 처리 가능함
    ## exec -> 계산"문" 만을 처리 가능함 + eval과 다르게 별도의 값을 리턴시키지 않음 (문자열 그 자체만으로 계산함)
    for i in range(len(varName)) :
     exec(varName[i] + '=' + str(current[i]))
     # case -- 2
     # cmd = varName[i] + '=' str(current[i])
     # exec(cmd)
    valueC = eval(expression)

    # 함수를 current 를 이용하여 계산했을때의 값
    return valueC

def mutants(current, p):
    # mutate 함수를 사용해 +DELTA, -DELTA 두가지 경우에 대한 mutant 생성
    # 모든 변수에 대해 mutation 실시하여 list 형태로 저장하여 반환
    neighbors = []
    #m = mutate(current, 2, DELTA, p)

    #모든 x값들에 대하여
    # +Delta, -Delta로 mutate 실시
    for i in range(len(current)) :
        mu = mutate(current, i, DELTA, p)
        neighbors.append(mu)
        mu = mutate(current, i, -DELTA, p)
        neighbors.append(mu)
    
    return neighbors     


def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    # 현재 값에대한 복사본을 slicing을 이용해 생성
    # neighbor = current를 복사한다
    neighbor = current[:]

    # 복사 된 값에 mutation을 실시하며, 이 때 domain 정보를 이용해
    # low <= value <= up 사이의 유효한 값이 얻어지도록 확인
    domain = p[1]
    low, up = domain[1], domain[2]

    #if (low[i] <= neighbor[i] + d and neighbor[i] + d <= up[i]) :
    #    neighbor[i] = neighbor[i] + d
    #else : 
    #    neighbor[i] = neighbor[i]

    ## 파이썬만이 가능한 문법
    if low[i] <= neighbor[i] <= up[i] :
        neighbor[i] += d

# neighbor : 값이 5개 들어있는 list (current와 동일한 형태)
    return neighbor

def bestOf(neighbors, p):
    # mutant 중 가장 좋은 solution을 선택
    # neighbors 각각에 대한 evaluation을 실시하여
    # 가장 좋은 solution을 best로 선정 후 반환

    # 1. 가장 처음 sample을 best라고 가정
    best = neighbors[0]
    bestValue = evaluate(best, p)
    # 2. 두번째 부터 계속 비교후 , 더 좋은것이 있으면 best로 저장
    for i in range(1, len(neighbors)) :
        newValue = evaluate(neighbors[i], p)
        if newValue < bestValue :
            best = neighbors[i]
            bestValue = newValue

    # 3. 모두 다 비교가 끝난 후 best를 반환
    return best, bestValue

def describeProblem(p):
    print()
    print("Objective function:")
    # expression 출력
    print(p[0])   # Expression
    print("Search space:")
    # Domain 정보 출력
    varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i])) 

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple

main()
